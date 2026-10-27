## The Response Pattern

```
WHEN receiving code review feedback:

1. READ: Complete feedback without reacting
2. UNDERSTAND: Identify the requested behavior and any unresolved facts that change it
3. VERIFY: Check against codebase reality
4. EVALUATE: Technically sound for THIS codebase?
5. RESPOND: State the technical conclusion briefly; omit performative agreement
6. IMPLEMENT: Within the authorized scope, group changes by their responsible owner, update affected callers, and verify the affected behavior
```

## GitHub Thread Replies

When replying to inline review comments on GitHub, reply in the comment thread (`gh api repos/{owner}/{repo}/pulls/{pr}/comments/{id}/replies`), not as a top-level PR comment.
