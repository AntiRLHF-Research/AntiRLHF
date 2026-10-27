# 等待实际条件

优先使用产品已有事件、Promise、任务句柄或测试库自带等待功能。下面分别展示等待状态，以及观察真实时间行为时的定时等待。

片段中的 `waitFor` 和 `waitForEvent` 是条件等待示意，接入项目时采用已有运行时或库的实际接口。不同库对返回值和抛出异常的等待语义不同，读取实际签名再调用；禁止为复刻示例重新造通用轮询框架。

## 核心模式

```typescript
// 错误路径：猜测操作完成所需的时间
await new Promise(r => setTimeout(r, 50));
const result = getResult();
expect(result).toBeDefined();

// 正确方向：等待目标条件成立
await waitFor(() => getResult() !== undefined);
const result = getResult();
expect(result).toBeDefined();
```

## 任意时长等待确有用途的情形

```typescript
// 工具每 100ms 触发一次，需要观察两个周期的部分输出
await waitForEvent(manager, 'TOOL_STARTED'); // 先等待触发条件
await new Promise(r => setTimeout(r, 200));   // 再等待需要观察的时间行为
// 200ms 对应两个 100ms 周期，时长有明确依据
```

**要求：**
1. 先等待触发条件。
2. 时长依据已知的时间行为确定。
3. 用注释说明这一时长的理由。


## 使用语言已有的同步原语

Python 任务明确发出就绪事件时，已有 `asyncio.Event` 足以表达等待：

```python
import asyncio

async def wait_until_ready(ready: asyncio.Event, timeout: float) -> None:
    await asyncio.wait_for(ready.wait(), timeout=timeout)
```

真实任务将 `ready.set()` 放在资源已经可用的位置。超时用于界定这次等待的失败；取消沿任务结构传播。修复时先确认事件是否在正确状态发出，停止反复增大固定 sleep。

设计异步操作时明确就绪与完成事件，调试时沿相应事件定位错误。同步操作直接使用正常返回值，避免给所有操作新增等待器和时间测试。需要对照所选技术段落时阅读 [英文片段](condition-waiting.en.md)。
