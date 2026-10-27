# 有界工作队列：背压、失败与取消

## 教学场景

批量转码任务需要处理大量输入。旧实现为每个输入创建一个 task，再在任务内部等 Semaphore；虽然并行执行数量受限，待执行 task 和闭包仍随输入数增长。把输入放进有界队列，由固定数量的 worker 消费。

如果项目已经采用成熟任务队列，使用其并发与取消机制。以下示例处理单进程内的有限批次，复用 asyncio.Queue 与 TaskGroup，不引入持久调度系统。

## 可运行的批次执行器

```python
import asyncio
from collections.abc import Awaitable, Callable, Iterable
from typing import TypeVar, cast

T = TypeVar("T")

async def run_batch(
    items: Iterable[T],
    handle: Callable[[T], Awaitable[None]],
    *,
    workers: int = 4,
    capacity: int = 16,
) -> None:
    if workers < 1 or capacity < 1:
        raise ValueError("workers and capacity must be positive")
    queue: asyncio.Queue[object] = asyncio.Queue(maxsize=capacity)
    end = object()

    async def produce() -> None:
        for item in items:
            await queue.put(item)
        for _ in range(workers):
            await queue.put(end)

    async def consume() -> None:
        while True:
            item = await queue.get()
            try:
                if item is end:
                    return
                await handle(cast(T, item))
            finally:
                queue.task_done()

    async with asyncio.TaskGroup() as group:
        group.create_task(produce())
        for _ in range(workers):
            group.create_task(consume())
```

队列满时生产者等待，单个 worker 异常会使 TaskGroup 取消其余任务并向外传播失败。外部取消同样进入这个范围。语义见 [asyncio Queue](https://docs.python.org/3.13/library/asyncio-queue.html) 与 [TaskGroup](https://docs.python.org/3.13/library/asyncio-task.html#task-groups)。

输入迭代器应快速地产生已准备的项目；阻塞式磁盘扫描、同步 SDK 等使用项目已有异步接口或线程边界。不要在事件循环中执行长时间阻塞操作。

## 业务失败决定批次行为

示例采用整体停止语义。产品要求“失败一项仍继续”时，业务 `handle` 捕获明确的单项失败并记录该项结果，再正常结束该次处理；程序错误和任务取消继续传播。禁止用 `except BaseException` 吞掉全部异常并返回成功。

worker 内部取得临时文件、网络响应或子进程时，用对应上下文或 finally 释放。只在资源真正创建成功后执行清理。外部任务已经产生副作用时，取消本地等待不会撤销远端操作，后续恢复依赖业务操作身份。

## 用户取消与服务退出

界面提交取消请求后，任务所有者发出取消信号并等待资源回收，再更新终态。正在关闭期间可以显示“正在停止”；不得仅关闭弹窗就把后台任务标为已取消。

服务退出先停止接收新批次，再按照产品约定完成在途任务或取消它们。持久任务需要恢复时，使用已选队列的重投和租约能力；内存批次无需为了“以后可能恢复”增加任务数据库。

## 有价值的使用检查

确认输入压力不会创建无界数量的 task，单项异常能结束或记录为既定结果，用户取消后资源确实释放。运行原来发生卡住的操作即可提供有效反馈。队列每次 put/get 的内部行为由运行时维护。
