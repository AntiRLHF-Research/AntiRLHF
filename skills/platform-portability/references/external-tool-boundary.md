# 外部工具的跨平台边界

## 教学场景

媒体工具需要调用现有转换程序。Unix 上使用拼接 shell 字符串，Windows 上又维护一套带引号的模板，带空格路径和非 ASCII 文件名经常失败。各入口对退出码和错误文字的处理也不同。

先确定支持的操作系统与交付形式。命令行工具、桌面安装包和受限沙箱对可执行文件发现与子进程能力有实际差异。统一业务操作，再在平台边界选择具体机制。

## 标准库调用模式

对于独立可执行文件，传参数序列、明确 cwd，避免 shell 字符串拼接。以下 Python 片段展示受控工具调用；程序是项目配置或受支持发现机制找到的可执行文件，参数来自该工具的正式契约。

```python
import subprocess
from pathlib import Path
from typing import Sequence

class ToolExecutionError(RuntimeError):
    pass

def run_tool(
    executable: Path,
    arguments: Sequence[str],
    *,
    working_directory: Path,
    timeout: float,
) -> bytes:
    try:
        result = subprocess.run(
            [str(executable), *arguments],
            cwd=working_directory,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
            check=False,
            shell=False,
        )
    except subprocess.TimeoutExpired as exc:
        raise ToolExecutionError("外部工具执行超时") from exc
    except OSError as exc:
        raise ToolExecutionError(f"外部工具无法启动：{exc}") from exc
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace")[-2000:]
        raise ToolExecutionError(f"外部工具退出码 {result.returncode}：{detail}")
    return result.stdout
```

这是短输出命令的调用形式。长时间媒体流应复用流式管道和受控日志输出，避免把全部 stdout/stderr 积累在内存。编码依工具协议选择，不能把所有二进制输出强行当文本。参数中的用户路径使用该程序支持的显式选项或参数终止符处理，避免以 `-` 开头的文件名被解释为选项。

`subprocess.run`、超时和平台行为见 [Python subprocess](https://docs.python.org/3.13/library/subprocess.html)。需要同时终止子孙进程时，采用平台支持的进程组、作业对象或现有框架能力；普通子进程退出不能替整个进程树完成清理。

## 路径和资源各有来源

可执行文件路径来自安装包或用户配置，输入输出路径来自用户操作，临时目录来自系统 API。不要用当前工作目录拼出所有位置，也不要把开发机绝对路径写进代码。

对同一文件身份使用平台和文件系统的真实语义。大小写、符号链接和路径分隔符处理放在文件边界，领域模块使用正式资源身份。Windows 批处理脚本与独立可执行文件调用不同，按目标平台文档处理，不把 shell=False 视作任意脚本的统一适配。

## 完成迁移

Web 后端、桌面按钮和 CLI 共用转换操作与错误模型，各自映射交互形式。删除历史 shell 模板、私有路径修补和重复查找逻辑。实际目标平台运行包含空格和非 ASCII 名称的合法输入；只支持一个平台的项目不建立全平台兼容层。
