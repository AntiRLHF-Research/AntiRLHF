# Superpowers 原文采用

完整保留所选有效技术片段；行为冲突在原文对应位置修改。采用稿进入实际技能的本地参考。原文、中文译本与差异保存在 [upstream/superpowers](upstream/superpowers)，供维护者审阅。

## 根因回溯

采用 `systematic-debugging/root-cause-tracing.md` 的完整 `The Tracing Process`：观察症状、找直接原因、追调用方、追参数、定位最初触发。

[英文原文](upstream/superpowers/root-cause-tracing.original.en.md)与[中文译文](upstream/superpowers/root-cause-tracing.original.zh-CN.md)完整对应。[执行参考](../../skills/root-cause-debugging/references/root-cause-tracing.md)保留该译文；英文片段位于同一参考目录。

没有采用外围默认逐层防护、每层加验证及绿测数量展示。根因定位后由实际职责决定修复，完成原功能。

## 先读后问

采用 `brainstorming/SKILL.md` 的完整 `Look Before You Ask`。[英文](upstream/superpowers/read-before-asking.original.en.md)、[中文](upstream/superpowers/read-before-asking.original.zh-CN.md)和[执行参考](../../skills/requirements-discovery/references/read-before-asking.md)均在本地。

外围无条件触发、固定问题轮次、设计审批及强制跳转计划技能没有引入。已明确的任务直接进入其实际专业方法。

## 独立子任务

摘取 `Create Focused Agent Tasks`、`Agent Prompt Structure` 引导段和 `When NOT to Use`。聚焦、自包含、明确输出和共享状态判断保留原文。

采用稿修改目标、范围和协调责任：完成真实行为，允许迁移受影响调用方，共同所有者统一协调。取消以测试文件和测试变绿为唯一目标的默认分工。

[原文](upstream/superpowers/independent-subtasks.original.en.md)、[原文译本](upstream/superpowers/independent-subtasks.original.zh-CN.md)、[采用稿](upstream/superpowers/independent-subtasks.adopted.en.md)、[采用稿译本](upstream/superpowers/independent-subtasks.adopted.zh-CN.md)、[差异](upstream/superpowers/independent-subtasks.diff)。实际加载 [中文方法](../../skills/independent-subtasks/references/independent-task-method.md)。

## 评审意见处理

摘取 `The Response Pattern` 与 `GitHub Thread Replies`。保留读取反馈、核对现实、作技术判断和原线程回复的操作。

修改理解、回应及实施三行：用真实要求代替强制复述；回应给技术结论；按责任所有者合并修改和验证。外围全问题停工、逐项测试以及无视当前需求的旧架构保留理由没有引入。

[原文](upstream/superpowers/review-feedback.original.en.md)、[原文译本](upstream/superpowers/review-feedback.original.zh-CN.md)、[采用稿](upstream/superpowers/review-feedback.adopted.en.md)、[采用稿译本](upstream/superpowers/review-feedback.adopted.zh-CN.md)、[差异](upstream/superpowers/review-feedback.diff)。实际加载 [反馈方法](../../skills/review-feedback/references/review-feedback-method.md)。

## 等待实际条件

从 `systematic-debugging/condition-based-waiting.md` 原文摘取 `Core Pattern` 及 `When Arbitrary Timeout IS Correct`，完整保留代码和所选要求。[英文](upstream/superpowers/condition-waiting.original.en.md)与[中文](upstream/superpowers/condition-waiting.original.zh-CN.md)在本地。

[执行参考](../../skills/root-cause-debugging/references/condition-waiting.md)增加具体 API 语义提醒和标准库事件示例。上游示例辅助函数未被包装成新依赖；实际项目优先采用现有等待与取消能力。没有采用自制通用轮询函数、固定轮询间隔和效果数字展示。

## 已有工作区识别

从 `using-git-worktrees/SKILL.md` 选取已有隔离检测。Git 命令保留；采用稿将子模块关系作为独立事实读取，结合工作树列表判断，删除跳转上游强制初始化步骤的链接。

[原文](upstream/superpowers/existing-isolation.original.en.md)、[原文译本](upstream/superpowers/existing-isolation.original.zh-CN.md)、[采用稿](upstream/superpowers/existing-isolation.adopted.en.md)、[采用稿译本](upstream/superpowers/existing-isolation.adopted.zh-CN.md)、[差异](upstream/superpowers/existing-isolation.diff)。实际加载 [已有隔离识别](../../skills/git-workspaces/references/existing-isolation.md)。

`--git-common-dir` 与 `--show-superproject-working-tree` 的具体含义按 [Git 官方文档](https://git-scm.com/docs/git-rev-parse)处理。目录隔离由实际工作需要触发；没有引入所有任务强制工作树、全量测试基线和自动创建提交。

## 素材边界

没有作为执行入口导入 `using-superpowers`、强制 `test-driven-development`、普遍 `verification-before-completion`、逐任务强制审查及 Skill 编写的红绿仪式。保留的技术片段已经置于对应任务方法中；其链接在本地闭合。

上游许可原文留在 [LICENSE.superpowers.txt](LICENSE.superpowers.txt)。原文译本保留原义；采用稿的改动通过差异和上述说明呈现。
