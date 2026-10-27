# 异步下载失败：找到过早关闭的资源所有者

## 教学场景

单项下载函数测试正常，API 接受批量下载后，后台却报告客户端已关闭。有人提议给下载函数增加三次重试，另一个方案是每个失败任务重新创建客户端。

沿[根因回溯方法](root-cause-tracing.md)检查错误发生点和调用链。首先读取真实失败信息，确认是客户端生命周期错误，随后找到客户端创建、任务启动和关闭的位置。

## 沿调用链找到错误

以下是教学反例，`client_factory` 和 `download` 表示项目已经提供的能力：

```python
import asyncio

async def start_download(client_factory):
    async with client_factory() as client:
        return asyncio.create_task(download(client))
```

函数返回任务时，客户端作用域已经结束；新 task 可能还没开始读取。失败点在下载调用，责任错误在启动函数。为下载函数加重试不会延长已经结束的资源生命周期。

继续确认这个操作应该同步等待完成，还是返回持久后台作业。原产品已经确定时直接采用该语义，不把简单生命周期错误升级为全面架构讨论。

## 修复实际所有者

调用应等待整个批次时，让任务组位于资源作用域内部：

```python
async def download_all(client_factory, items):
    async with client_factory() as client:
        async with asyncio.TaskGroup() as tasks:
            for item in items:
                tasks.create_task(download(client, item))
```

该片段用于有限的小批次。输入规模较大时使用[有界队列](../../async-lifecycle/references/bounded-worker-case.md)，避免一次创建全部 task。TaskGroup 的失败和取消传播由运行时承担，业务决定是否允许单项失败后继续。

产品需要 API 立即返回作业 ID 时，后台执行器拥有任务和客户端的生命周期；请求只提交到现有队列或执行器。服务关闭时停止接收并等待或取消在途任务。禁止把请求级客户端通过闭包偷偷交给跨请求任务。

## 诊断只服务当前未知

若仍无法区分“任务未启动”和“客户端提前关闭”，在创建、启动和关闭处加最少的临时事件，带同一作业身份。观察一次失败后移除无持续价值的探针。无需在每个网络调用加永久日志、全局审计器和新的超时状态机。

验证运行原来失败的 API 路径。已经存在的下载单元测试继续保护本地解析等行为；为资源生命周期补一项能暴露该独立错误的检查即可。不要把运行时 TaskGroup 和成熟客户端内部行为重测一遍。

## 回到原始能力

真实下载完成后，继续任务仍缺少的保存、状态呈现或取消能力。若修复产生新证据，例如任务在持久化提交前就被读取，沿新的实际数据关系处理。每次调查都围绕已经观察到的故障，修好就返回产品主线。
