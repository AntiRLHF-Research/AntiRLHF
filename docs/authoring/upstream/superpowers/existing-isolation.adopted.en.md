## Detect Existing Isolation

**Before creating anything, check if you are already in an isolated workspace.**

```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
```

**Submodule context:** Read the superproject path as a separate fact:

```bash
git rev-parse --show-superproject-working-tree 2>/dev/null
```

**If `GIT_DIR != GIT_COMMON`:** Inspect the linked-worktree and superproject context with `git worktree list --porcelain`. Continue in the existing workspace when it already supplies the requested isolation. Respect the harness's ownership of externally managed workspaces.
