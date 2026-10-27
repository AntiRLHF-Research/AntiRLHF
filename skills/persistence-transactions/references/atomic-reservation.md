# 原子预约与一次取消

## 教学场景

两个入口共同预约有限容量。先查询剩余量、在内存判断、再分别保存预约和扣减，会产生竞态或半完成写入。把实际不变量交给同一个事务：容量满足才扣减，扣减成功才保存预约；取消只释放一次。

下面使用 Python 标准库 sqlite3 和 SQLite 条件更新演示。完整应用在进入这些存储操作前完成身份与业务权限判断。持久化失败向调用者传播，由业务边界映射具体错误。

## 存储结构

```sql
CREATE TABLE slots (
    id TEXT PRIMARY KEY,
    remaining INTEGER NOT NULL CHECK (remaining >= 0)
);
CREATE TABLE reservations (
    id TEXT PRIMARY KEY,
    slot_id TEXT NOT NULL REFERENCES slots(id),
    quantity INTEGER NOT NULL CHECK (quantity > 0),
    status TEXT NOT NULL CHECK (status IN ('active', 'cancelled'))
);
```

## 创建与取消操作

```python
import sqlite3
from contextlib import closing
from pathlib import Path

class CapacityUnavailable(Exception):
    pass

def reserve(db: Path, slot_id: str, quantity: int, reservation_id: str) -> None:
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    with closing(sqlite3.connect(db, timeout=5.0)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        with connection:
            changed = connection.execute(
                "UPDATE slots SET remaining = remaining - ? "
                "WHERE id = ? AND remaining >= ?",
                (quantity, slot_id, quantity),
            )
            if changed.rowcount != 1:
                raise CapacityUnavailable(slot_id)
            connection.execute(
                "INSERT INTO reservations(id, slot_id, quantity, status) "
                "VALUES (?, ?, ?, 'active')",
                (reservation_id, slot_id, quantity),
            )

def cancel(db: Path, reservation_id: str) -> bool:
    with closing(sqlite3.connect(db, timeout=5.0)) as connection:
        connection.execute("PRAGMA foreign_keys = ON")
        with connection:
            released = connection.execute(
                "UPDATE reservations SET status = 'cancelled' "
                "WHERE id = ? AND status = 'active' "
                "RETURNING slot_id, quantity",
                (reservation_id,),
            ).fetchone()
            if released is None:
                return False
            slot_id, quantity = released
            connection.execute(
                "UPDATE slots SET remaining = remaining + ? WHERE id = ?",
                (quantity, slot_id),
            )
            return True
```

`RETURNING` 需要 SQLite 3.35 或更新版本，见 [SQLite RETURNING](https://www.sqlite.org/lang_returning.html)。`with connection` 处理提交和回滚，`closing` 负责关闭连接；语义见 [Python sqlite3](https://docs.python.org/3.13/library/sqlite3.html)。已有连接池或 ORM 时采用它们的事务作用域，保持相同的业务原子性。

取消返回 `False` 表示本次没有执行释放。需要区分记录不存在、无权限和已取消时，由正式服务按其公开契约处理，不让这一个布尔返回值承担全部领域错误。

## 观察真正的独立故障

预约记录插入因重复主键失败时，前面的容量扣减应回滚。两个并发请求争最后一个名额时，至多一个成功。连续取消同一预约只增加一次剩余量。这些是值得保护的业务行为。

请求重复提交另有业务语义：同一个请求身份应返回原预约，内容冲突则明确拒绝。可在服务层事务内加入唯一请求键和原请求内容检查。上面代码用于展示容量原子性，完整契约见[预约系统结构](../../system-architecture/references/reservation-system.md)。不要在每个调用者各自捕获数据库错误后猜测请求是否成功。

## 外部效果放在正确边界

成功通知在事务提交后发送。要求可靠发送时，复用现有事务消息或 outbox 机制，把待发送事件与业务状态一起保存。外部服务调用不应长期占住容量事务。一次通知重试也不应重复执行预约扣减。

旧入口完成迁移后，删除各自的容量镜像、补偿扣减和独立提交方法。缓存只保存可重建读模型；正式容量仍由存储事务维护。
