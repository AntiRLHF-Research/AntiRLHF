# 任务与资源一起拥有生命周期

## 选择结构化并发

一组工作属于一个操作时，使用运行时现有任务组或作用域管理它们。Python 可用 `asyncio.TaskGroup`，Rust 使用合适的 Tokio 任务管理能力，Node 按已有运行时的取消和 Promise 组织。具体语义按项目版本核对，禁止手写通用任务监督器。

Python 有界批处理示例：

```python
import asyncio

async def map_records(records, process, concurrency=4):
    if concurrency < 1:
        raise ValueError('concurrency must be positive')
    semaphore = asyncio.Semaphore(concurrency)
    async def run(record):
        async with semaphore:
            return await process(record)
    async with asyncio.TaskGroup() as group:
        tasks = [group.create_task(run(record)) for record in records]
    return [task.result() for task in tasks]
```

这个形状适合有限输入和同成同败的工作。大规模流输入采用有界生产消费，部分成功契约需要在对应业务位置收集各项结果。不要把所有场景硬套进一个批处理抽象。

## 资源的所有者

数据库池、网络客户端和文件句柄由创建它们的生命周期负责关闭。任务只借用资源。一次临时资源用语言或框架的上下文管理；多个资源需要顺序关闭时复用已有组合能力。

## 取消的传播

取消到达任务时释放本任务资源并继续传播。避免宽泛异常捕获吞掉取消。超时表示当前操作预算耗尽，外部副作用是否已发生需要按实际协议处理，不能静默重做。

## 关闭行为

应用停止接收新请求，通知后台工作停止，再等待或取消在途任务，最后关闭连接池。后台循环必须能观察停止信号或取消。禁止让普通退出永远等一个没有结束条件的工作者。

技术参考：[Python TaskGroup 与取消](https://docs.python.org/3/library/asyncio-task.html)、[Python contextlib](https://docs.python.org/3/library/contextlib.html)。
