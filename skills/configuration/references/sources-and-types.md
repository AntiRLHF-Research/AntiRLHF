# 配置的类型、来源和组合根

## 先采用项目已有能力

查看框架提供的设置加载、依赖注入和环境管理。Python 可采用 Pydantic Settings，Java/Spring 使用框架配置绑定，.NET 使用现有 Options 与 Configuration，Rust 或 Node 项目优先现有设置库与运行时能力。选择必须匹配实际技术栈，不为统一形式跨栈造框架。

## Python 设置模型示例

下面使用 `pydantic-settings` 的正式加载方式。启动时构造一次，再把设置传给资源创建位置。

```python
from pathlib import Path
from pydantic import Field, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='APP_', frozen=True)
    data_dir: Path = Path('./data')
    request_timeout_seconds: float = Field(default=15.0, gt=0, le=300)
    api_key: SecretStr

settings = Settings()
```

默认来源顺序及命名规则交给所采用库管理。项目确有自定义优先级时在一个位置扩展，禁止每个功能分别调用 `getenv` 并填写不同默认值。示例中的参数属于应用运行配置；实际业务记录仍由领域模型负责。

## 单位和空值

超时使用明确单位，路径说明相对于哪个目录。空字符串、缺失和显式禁用按产品语义区分。非法输入在边界报告字段和可采取动作，不吞掉错误后偷偷采用另一份配置。

## 组合根的责任

应用入口加载配置，创建连接池、客户端和工作者，再把这些对象交给实际消费者。业务函数只接收它需要的值或能力。不要让每个调用者重新解释整个配置对象，也不要用全局可变字典作为隐藏依赖。

## 配置来源

技术 API 与优先级说明：[Pydantic Settings 官方文档](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)。实际采用时按项目版本核对可用项；本地治理材料直接使用，无需联网预加载。
