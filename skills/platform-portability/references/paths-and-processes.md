# 路径、进程和编码的责任边界

## 使用路径对象

Python 使用 `pathlib.Path`，其它技术栈采用标准或成熟路径能力。明确相对路径的基准目录；用户输入、项目根和程序安装位置属于不同来源。不要依赖随机的当前工作目录，让功能只能在开发者机器的某个目录工作。

```python
from pathlib import Path
import subprocess

project = Path(project_directory).expanduser().resolve()
result = subprocess.run(
    ['git', 'status', '--short'],
    cwd=project,
    check=True,
    capture_output=True,
    text=True,
    encoding='utf-8',
)
```

示例展示结构化参数和显式工作目录。实际命令编码、超时与交互方式按工具契约设置。生产输入来自不可信用户时，额外落实真实文件访问权限与路径边界，复用框架提供的安全机制。

## 进程生命周期

处理返回码、必要输出与取消。后台进程由实际生命周期所有者等待和释放；禁止启动后丢失句柄。需要 shell 特性时明确使用的 shell 与引用方式，普通程序调用采用参数数组。

## 文件系统语义

原子替换、文件锁和目录权限按实际系统能力使用。Windows 文件占用、大小写不同和符号链接会改变操作结果，定位当前失败所涉及的差异。不要通过到处增加 try/except 继续隐藏错误。

## 成熟能力优先

配置目录、进程控制、文件监视和压缩格式通常已有成熟库。先检查项目现有实现，采用正式能力并删除私有工具。别为了少一个依赖手写多个系统分支。

技术参考：[pathlib](https://docs.python.org/3/library/pathlib.html)、[subprocess](https://docs.python.org/3/library/subprocess.html)。
