# AntiRLHF 导航

AntiRLHF 由持久 Constitution 与五个核心技能及一个可选项目工作流技能组成。先阅读[治理思路与演变](README.md)，再[安装 AntiRLHF](docs/install-skills.md)。

## 组成

| 入口                                           | 职责                                       |
| ---------------------------------------------- | ------------------------------------------ |
| [Constitution](CONSTITUTION.md)                | 写入持久用户指令的共同治理原则。           |
| [Plan](skills/antirlhf-plan/SKILL.md)          | 研究、判断、架构与规格设计。               |
| [Exec](skills/antirlhf-exec/SKILL.md)          | 实现、调试、验证与交付。                   |
| [Refactoring](skills/refactoring/SKILL.md)     | 职责划分、数据流、结构简化与测试体系重整。 |
| [Documentation](skills/documentation/SKILL.md) | 面向读者的写作、文档结构及语言与导航检查。 |
| [AntiRLHF 版本](.version)                      | 集成技能共同使用的版本。                   |

Plan 与 Exec 按任务加载各自的 `references/`。Refactoring 与 Documentation 提供专项任务方法。Documentation 统一拥有可复用的[语言扫描器](skills/documentation/scripts/check/governance_prose.py)、[导航检查器](skills/documentation/scripts/check/doc_graph.py)及[扫描配置](skills/documentation/scripts/.config/scanner.toml)。

## 扩展与安装

- [Review](skills/antirlhf-review/SKILL.md)：独立只读审查，直接报告确认问题。
- [Project Workflows](skills/project-workflows/SKILL.md)：可选的项目接入、CI 与发布。
- [调用与内容归属](docs/skill-architecture.md)：主要角色直接触发，专项方法按需读取。
- [安装说明](docs/install-skills.md)：独立仓库的打包与安装。

## 背景资料

- [研究档案](docs/README.md)：现场观察、机制假设、提示词干预与文献阅读。
- [历史档案](archive/README.md)：JDD、TED、COST 的历史文本。

本独立仓库的打包、安装与验证由根目录 `scripts/` 管理。

## Navigation / 导航

- [治理介绍](README.md)
- [安装](docs/install-skills.md)
- [AntiRLHF 介绍](README.md)
- [研究档案](docs/README.md)
- [指令中文审阅](TRANSLATION-REVIEW.md)
