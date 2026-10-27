# 事务边界和并发语义

## 一个工作单元负责提交

业务服务确定一次变化需要一起成立的规则，存储操作使用同一个事务上下文。Helper 可以执行查询与写入，提交留给工作单元。外部模型调用、长时间网络和人工等待通常安排在短事务之外，领域状态说明其进展。

SQLAlchemy 中，项目已有 `Job` 映射和 `JobNotFound`、`JobConflict` 领域异常时，一次完成操作可以直接持有工作单元：

```python
from sqlalchemy import update
from sqlalchemy.orm import Session

# Job、JobNotFound、JobConflict 从项目现有领域定义导入。
def complete_job(engine, job_id: str, output_uri: str) -> None:
    with Session(engine) as session, session.begin():
        result = session.execute(
            update(Job)
            .where(Job.id == job_id, Job.status == "running")
            .values(status="completed", output_uri=output_uri)
        )
        if result.rowcount != 1:
            if session.get(Job, job_id) is None:
                raise JobNotFound(job_id)
            raise JobConflict(job_id)
```

该片段假定当前数据库驱动支持准确的匹配行计数；其它驱动采用其支持的返回行或锁定读取机制。操作只返回业务结果，避免把已关闭 Session 的可变实体泄漏给调用者。异常退出时由既有事务上下文回滚，成功退出时提交。

## 并发需要明确结果

先读再写容易被另一个请求插入。选择已有数据库机制保护业务不变量：唯一约束保护身份，条件更新保护版本或数量，必要的锁保护相关读取与写入。冲突返回领域结果，调用者按产品要求重试或提示重新读取。

例如余额扣减应在约束或条件更新中确保合法，而非 API 和后台任务各读一遍余额再自行写入。跨实体必须同成同败的操作在同一事务内执行。

## 隔离级别的选择

依据实际并发行为采用数据库已有隔离级别。更强隔离可能带来冲突与重试，按任务处理；不要把每个查询自动升级为最强隔离，也不要假设默认设置保护全部跨行规则。

## 对外副作用

邮件、支付或消息投递一旦发生，数据库回滚不会撤销外部效果。定义幂等键、状态查询或可靠投递的真实责任，复用既有组件。只在产品需要时引入 outbox 等机制。

技术参考：[SQLAlchemy 事务管理](https://docs.sqlalchemy.org/en/20/orm/session_transaction.html)、[PostgreSQL 事务隔离](https://www.postgresql.org/docs/current/transaction-iso.html)。
