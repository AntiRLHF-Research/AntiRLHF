# 状态、不变量和修改权

## 区分输入校验与业务规则

入口解析日期、ID 和字段格式，得到有效输入。业务所有者判断操作者是否能执行、实体当前状态是否允许，以及变化需要满足的领域约束。数据库约束保护持久化的结构和并发一致性。把同一业务决策重复写在三个层里，会形成分歧；把所有入口数据都盲信，又会让错误越过真实信任边界。

以任务取消为例，正在排队的任务可以直接转为取消，正在外部执行的任务需要记录取消请求并处理外部调用的实际结果。不要给所有状态都提供公共 `setStatus()`；提供 `cancel()`、`start()`、`complete()` 等对应真实语义的操作。

## 状态机结构示例

```typescript
type Job =
  | { id: string; state: 'queued'; sourceId: string }
  | { id: string; state: 'running'; sourceId: string; runId: string }
  | { id: string; state: 'succeeded'; sourceId: string; resultId: string }
  | { id: string; state: 'failed'; sourceId: string; reason: FailureReason };

type FailureReason = 'source-unreadable' | 'provider-unavailable' | 'invalid-content';
```

按实际业务增加状态。将结果 ID 绑定到成功状态，避免消费者在任意 `status: string` 与 `result?: any` 中猜测合法组合。取消是否成为状态、是否要区分请求取消和确认取消，由真实执行行为决定。

## 并发规则属于写入契约

两个请求同时更新同一记录时，确定版本冲突或顺序语义。使用数据库已有锁、唯一约束或条件更新实现，返回领域冲突。禁止每个调用者各自做一次读后判断再写入，或者靠前端按钮禁用维持一致性。

事务覆盖哪些对象取决于一次必须一起成立的业务变化。例如转移库存需要扣减和增加在同一提交中；耗时外部服务调用通常放在短事务之外，并由领域状态描述其进展。

## 保持领域语言可用

术语直接来自业务操作，明确同名对象在不同上下文中的区别。需要共享词汇时在现有规格中写清；不要因为认识一个新名词就创建整套术语表、决策编号和审批记录。模型改变时同步现行说明，删除失效定义。
