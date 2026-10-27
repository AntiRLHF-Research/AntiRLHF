# 教学情境：三套记录模型收敛

## 现状

导入入口返回 `RawItem`，存储模块使用 `StoredItemV2`，界面维持一份可修改的 `DisplayItem`。三个类型都含身份、名称与状态，各有一套默认值和错误枚举。增加重命名功能时，每个调用者都再次转换字段。

## 选择正式语义

先判断这些对象是否确实表示同一个领域实体。如果是，记录服务拥有身份、名称和状态修改。使用一个当前领域类型；存储行负责数据库表示，页面视图负责展示格式。页面只能通过重命名操作提交更改。

业务操作可以采用如下形状：

```typescript
type RenameResult =
  | { ok: true; record: RecordView }
  | { ok: false; reason: 'not-found' | 'conflict' | 'invalid-name' };

interface Records {
  rename(id: RecordId, expectedVersion: number, name: string): Promise<RenameResult>;
  get(id: RecordId): Promise<RecordView | undefined>;
}
```

这是契约示意；实际代码复用项目已使用的错误和结果风格。避免为了这一接口引入通用 Result 框架、注册容器或新的版本命名规则。

## 连续迁移

先把名称校验与版本判断移到记录服务。让导入、编辑和后台处理调用它。存储在一处将持久化字段映射为领域类型；真实对外协议在入口做协议转换。随后删除内部 `RawItem → V2 → DisplayItem → V1` 的多次往返。

把有价值的场景迁到新公开操作：名称无效、并发更改、正常重命名后从另一个入口读取。删除只验证旧字段转抄的测试和 Mock。用户仍需读取旧持久数据时完成一次真实迁移；开发临时数据按用户授权处理。

## 判断收敛是否完成

从每个仍使用的入口追踪一次更改，查看同一规则是否在定义者处执行；查找旧类型和转换函数的实际引用，清理淘汰支撑。禁止给所有旧类型加别名以延缓迁移。返回结果保持用户需要的能力，更新现行接口说明。
