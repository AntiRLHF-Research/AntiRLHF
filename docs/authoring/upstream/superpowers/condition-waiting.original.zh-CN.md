## 核心模式

```typescript
// 错误路径：猜测操作完成所需的时间
await new Promise(r => setTimeout(r, 50));
const result = getResult();
expect(result).toBeDefined();

// 正确方向：等待目标条件成立
await waitFor(() => getResult() !== undefined);
const result = getResult();
expect(result).toBeDefined();
```

## 任意时长等待确有用途的情形

```typescript
// 工具每 100ms 触发一次，需要观察两个周期的部分输出
await waitForEvent(manager, 'TOOL_STARTED'); // 先等待触发条件
await new Promise(r => setTimeout(r, 200));   // 再等待需要观察的时间行为
// 200ms 对应两个 100ms 周期，时长有明确依据
```

**要求：**
1. 先等待触发条件。
2. 时长依据已知的时间行为确定。
3. 用注释说明这一时长的理由。
