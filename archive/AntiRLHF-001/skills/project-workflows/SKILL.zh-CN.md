---
name: project-workflows
description: 明确请求项目接入、Skill 安装、CI、版本准备、部署或发布时使用；复用项目和平台现有机制，普通编码任务无需加载。
---

# 项目工作流

遵循 AntiRLHF Constitution 与项目实际约定。按用户要求的产物选择具体方法：

- [项目接入](references/setup.zh-CN.md)：安装、Skill 发现、项目级指令与入口维护。
- [CI](references/ci.zh-CN.md)：流水线、实际命令和必需检查。
- [发布](references/release.zh-CN.md)：版本、变更说明、打包、部署与发布。

读取真实平台配置、仓库约定与可用工具。实际软件修改交由 [antirlhf-exec](../antirlhf-exec/SKILL.md)；作者文档使用 [documentation](../documentation/SKILL.md)。只在真实授权、凭据、公共副作用或用户数据边界上施加相应要求。

安装应保证目标 Harness 真正发现并能读取 Skill 资源。CI 应运行真实构建和测试入口。发布应交付已授权版本及资产，遇到实际权限缺口则报告具体待决定事项。

普通实现不应自动附带项目接入、CI、审查门禁或发布流程。
