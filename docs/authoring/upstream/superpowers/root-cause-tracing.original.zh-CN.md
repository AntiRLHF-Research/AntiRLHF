## 回溯过程

### 观察症状
```
Error: git init failed in ~/project/packages/core
```

### 找到直接原因
**定位直接触发错误的代码。**
```typescript
await execFileAsync('git', ['init'], { cwd: projectDir });
```

### 找到调用方
```typescript
WorktreeManager.createSessionWorktree(projectDir, sessionId)
  → 由 Session.initializeWorkspace() 调用
  → 由 Session.create() 调用
  → 由测试中的 Project.create() 调用
```

### 继续向上回溯
**查看传入的值。**
- `projectDir = ''`，竟然是空字符串！
- 作为 `cwd` 的空字符串被解析为 `process.cwd()`。
- 那正是源代码目录！

### 找到最初触发点
**定位空字符串的来源。**
```typescript
const context = setupCoreTest(); // 返回 { tempDir: '' }
Project.create('name', context.tempDir); // 在 beforeEach 之前就访问了！
```
