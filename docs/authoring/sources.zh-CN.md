# 内容来源

## 项目材料

本包以用户审阅过的自包含常驻指令、专项技能结构和 Superpowers 摘编 ZIP 为基础，按 [AntiRLHF Charter](../charter/Revised.md) 的十四类问题展开。对应关系见 [覆盖说明](charter-coverage.zh-CN.md)。

作者上传的原始文稿、人工修订、Diff 与图片保存在 [本地对照材料](../../skills/direct-writing/references/cases/charter/README.md)。案例说明区分真实修改和教学设定，通用方法按读者任务组织。

现有 [arsvine-skills/AntiRLHF](https://github.com/ArsvineZhu/arsvine-skills/tree/main/AntiRLHF) 中的规则、作者声音和所有权方法参与整合。旧 Plan／Exec 路由退出新包，其有效专业知识进入实际责任技能。

## 语言工具

`skills/direct-writing/scripts/check/governance_prose.py` 与相邻 `scripts/.config/scanner.toml` 来自 arsvine-skills 的 documentation 技能，保留其原有匹配、分级和精确豁免机制。包检查工具调用该实现，并对原始文本作补充扫描，处理代码块、比较稿及其它 UTF-8 文件。

来源：[扫描器](https://github.com/ArsvineZhu/arsvine-skills/blob/main/AntiRLHF/skills/documentation/scripts/check/governance_prose.py)、[规则](https://github.com/ArsvineZhu/arsvine-skills/blob/main/AntiRLHF/skills/documentation/scripts/.config/scanner.toml)。

## 直接采用的第三方文本

[obra/superpowers](https://github.com/obra/superpowers) 的六组片段按 [摘编说明](superpowers-adoption.zh-CN.md)保留原句与技术步骤。上游许可原文留在 [LICENSE.superpowers.txt](LICENSE.superpowers.txt)。

## 技术参考

各参考文件在相关技术位置给出官方资料链接。本地正文已描述具体工作方法，外部资料用于实际项目选型时确认当前 API 与环境。

配置示例使用 Pydantic Settings；网络客户端示例使用 HTTPX；事务示例使用 SQLAlchemy 和 PostgreSQL 的既有能力；异步与平台示例使用 Python 标准库；国际化使用 ICU 消息和 Intl；日志与链路上下文参考 OpenTelemetry；权限方法参考 OWASP；交互状态参考 W3C 的状态反馈指导。

这些是领域方法与具体使用片段，技术选择仍从当前项目实际框架和能力出发。完整来源链接在相应参考文件中，不要求所有项目采用同一技术栈。

## 分发与发现格式

[Agent Skills 规范](https://agentskills.io/specification)用于入口格式；[Codex Skills](https://developers.openai.com/codex/skills/)用于本地发现与元数据；[用户指令](https://developers.openai.com/codex/guides/agents-md/)用于常驻文本位置；[插件文档](https://developers.openai.com/plugins/build/plugins)用于根目录清单。

本包使用根 `plugin.json` 和实际 `skills/` 内容。安装脚本在明确目标目录复制整套技能，并按 [使用说明](../../README.md) 删除其中的豁免注释。常驻指令由用户在有效设置中采用。
