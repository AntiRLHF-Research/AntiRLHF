## 创建前识别已有隔离

**创建任何内容之前，先检查自己是否已经处于隔离工作区。**

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

**子模块防护：** 在 Git 子模块中，`GIT_DIR != GIT_COMMON` 同样成立。在认定自己已经处于 worktree 前，先检查是否处于子模块：

```bash
# 若返回路径，当前处于子模块而非 worktree，按普通仓库处理
git rev-parse --show-superproject-working-tree 2>/dev/null
```

**若 `GIT_DIR != GIT_COMMON` 且不是子模块：** 已处于 linked worktree。跳到上游第二步“项目设置”，不要再创建 worktree。
