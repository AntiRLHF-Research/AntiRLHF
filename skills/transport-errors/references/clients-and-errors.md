# 客户端生命周期与错误映射

## 使用一个适用的资源所有者

Python 服务可在应用生命周期中创建 HTTPX Client 或 AsyncClient；提供方已有正式 SDK 就优先采用。Node、Rust 等环境使用项目运行时或成熟客户端。连接池和关闭由现有客户端管理，避免手写通用连接池。

HTTPX 结构示例：

```python
from contextlib import asynccontextmanager
import httpx

@asynccontextmanager
async def transport(
    base_url: str, timeout_seconds: float, connect_timeout_seconds: float
):
    timeout = httpx.Timeout(timeout_seconds, connect=connect_timeout_seconds)
    async with httpx.AsyncClient(base_url=base_url, timeout=timeout) as client:
        yield client
```

由应用组合根调用该上下文，并把客户端传给依赖它的实际服务。示例展示创建与关闭关系；业务操作使用客户端正式 API，不再包出第二套生命周期框架。

## 三层错误职责

连接超时属于传输失败；对方返回限流或无效凭据由提供方边界解释；业务记录状态冲突属于领域。入口把这些类别映射为协议和用户提示，诊断记录保留必要原因。

错误表示可以沿用项目已有异常层级或判别联合类型。决定后的代码只能有一套正式语义。不要让 `null`、任意字符串、数字码和自造枚举各自表示同一个失败，也不要根据异常文案做程序分支。

## 上游状态的保存

需要排错时保留非敏感的请求标识、错误类别与因果链。完整认证头、响应中的秘密和私人输入不进入日志。公开错误信息给使用者下一步，底层堆栈留给相应开发诊断。

## 直接修正上游形状

三个消费者都把相同异常改成自己的字典，说明正式契约可能不合适。修改提供方边界的结果，再迁移三个消费者。禁止新增一个“兼容所有错误”的万能转换器继续隐藏重复模型。

技术参考：[HTTPX Clients](https://www.python-httpx.org/advanced/clients/)、[HTTPX Exceptions](https://www.python-httpx.org/exceptions/)、[HTTPX Async Support](https://www.python-httpx.org/async/)。
