# 识别已有工作区

**创建任何内容之前，先检查自己是否已经处于隔离工作区。**

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

**子模块上下文：** 单独读取上级仓库路径：

```bash
git rev-parse --show-superproject-working-tree 2>/dev/null
```

**若 `GIT_DIR != GIT_COMMON`：** 使用 `git worktree list --porcelain` 查看 linked worktree 和上级仓库关系。已有工作区满足所需隔离时继续使用。外部宿主管理的工作区按其所有权处理。
