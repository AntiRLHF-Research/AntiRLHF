# Charter 问题与执行内容

按当前 [Charter/Revised.md](../charter/Revised.md) 中的十四类观察组织。这里供作者检查内容归属，日常任务直接使用常驻指令与专项方法。

## 防御性语言、虚构反驳与判断退缩

具体词形、语义替换、虚构强命题、结论降格和回答尾部堆叠限定，由常驻指令和 [直接表达](../../skills/direct-writing/SKILL.md) 共同处理。参考包括 [防御模式](../../skills/direct-writing/references/defensive-patterns.md)、[真实修改](../../skills/direct-writing/references/observed-edits.md) 和 [判断中的未知](../../skills/research-decision/references/choice-and-uncertainty.md)。

要求先给结论和决定性理由，直接说明影响结果的真实条件，删除无人提出的反驳和整项多余信息。扫描器查词形；完整段落按用途编辑。禁止用新造的夸张坏例子冒充自然输出，禁止只替换同义词过扫描。

## UI 与产物夹带实现说明

[用户交互与内容](../../skills/product-interface/SKILL.md) 把最终使用者的任务、状态、操作和信息层级放在中心；[真实 UI 修改](../../skills/product-interface/references/content-and-observed-edits.md) 保留用户提供的截图和实际删改。

处理制作过程、向委托者表功、执行约束复制到页面、无意义卡片与编号、冗余边界说明。实现要求进入程序和数据，页面展示读者需要的信息。动态状态沿真实用户路径读取与修改，文字的作用按完整页面判断。

## 强制 TDD、浅层测试与验证膨胀

[有效验证](../../skills/meaningful-verification/SKILL.md) 明确默认不采用强制红绿、为未实现功能造失败测试，以及逐个私有 Helper 加测试。参考 [行为与独立故障](../../skills/meaningful-verification/references/behavior-and-failure.md) 和 [套件替换](../../skills/meaningful-verification/references/suite-replacement.md)。

处理生产代码测试专用导出口、过度 Mock/DI/Fixture、重复字段断言、全量反复执行、过期脚手架、测试全绿而用户路径失败。上游库内部验证留给上游，项目验证自己的集成。重构时迁移仍有效的行为场景，成组删除旧内部结构的套件与辅助工具。

## 自证流程、证据门禁和无关对齐

[流程抑制](../../skills/process-control/SKILL.md)覆盖阶段编号、矩阵、验收表、证据包、SHA/JSON 反复对齐、dry-run、冒烟、安全审计及结束后的额外审查。参考 [工作分配](../../skills/process-control/references/work-allocation.md) 和 [真实义务](../../skills/process-control/references/real-obligations.md)。

删除无任务用途的程序，把已解决的问题退出活动范围。实际发布、实验冻结和许可证责任按具体事项处理。流程检查自身也按需结束，禁止生成新的合规台账。

## 无义务兼容和内部版本链

[结构替换](../../skills/structural-refactoring/SKILL.md)与 [领域建模](../../skills/domain-modeling/SKILL.md)负责统一正式表示、修改定义者、迁移全部实际消费者。参考 [消费者迁移](../../skills/structural-refactoring/references/consumer-migration.md) 和 [数据及公开契约](../../skills/structural-refactoring/references/data-and-public-contracts.md)。

处理 v1/v2/v3、alias、shim、Bridge、fallback、双轨状态和安抚旧测试的包装。开发历史不产生兼容义务；真实数据、客户端与支持承诺在其边界处理。淘汰结构的配置、注册、测试、示例和当前说明一起迁移。

## 架构判断缺位与维护现状

[系统架构](../../skills/system-architecture/SKILL.md)、[领域建模](../../skills/domain-modeling/SKILL.md)、[结构替换](../../skills/structural-refactoring/SKILL.md)共同覆盖这一问题。

[架构重判](../../skills/system-architecture/references/architecture-evolution.md)把纠正提前到设计讨论：用户提出新方向时，检查现有责任是否合理，禁止仅用旧文档否定新需求。其它参考处理分散业务规则、多个事实源、巨型文件、平铺模块、浅层转发、万能管理器、包装多套旧模型，以及删除旧系统后制造更大新系统。

修改在实际所有者完成。需要替换自己的新框架时直接替换，保留完整产品能力和明确的简化目标。

## 从零设计与共享基础能力

[从零产品实例](../../skills/system-architecture/references/greenfield-design.md)和 [完整能力交付](../../skills/end-to-end-delivery/SKILL.md)连接模型、前端、服务、持久化与生命周期。

各专业入口分别提供具体方法：[配置](../../skills/configuration/SKILL.md)、[传输与错误](../../skills/transport-errors/SKILL.md)、[日志与跟踪](../../skills/observability/SKILL.md)、[存储与事务](../../skills/persistence-transactions/SKILL.md)、[异步任务与生命周期](../../skills/async-lifecycle/SKILL.md)、[缓存与事件](../../skills/cache-events/SKILL.md)、[身份与权限](../../skills/identity-permissions/SKILL.md)、[跨平台](../../skills/platform-portability/SKILL.md)、[国际化](../../skills/localization/SKILL.md)。

覆盖硬编码、复制配置、重复客户端、错误码改写、并行写入、连接与任务泄漏、资源关闭、队列与取消、上下文传播、时间和路径语义。共享能力从真实使用链识别，用成熟框架与依赖承担通用机制，实际接入所有消费者。

## 依赖洁癖与选型狭窄

[依赖选型](../../skills/dependency-selection/SKILL.md)先找已有库、标准库、平台能力与可靠开源实现，按实际 API、维护、集成和产品要求决定。参考 [选择与集成](../../skills/dependency-selection/references/selection-and-integration.md)、[源码采用](../../skills/dependency-selection/references/source-adoption.md)。

选定后直接替换自制机制，保留产品领域语义。许可证落实到实际复制与分发材料，禁止以其为由无期限搁置选型。既支持安装成熟依赖，也支持保留原文的源码摘编与局部改造。

## 长任务漂移与状态日志化

[目标连续性](../../skills/goal-continuity/SKILL.md)在恢复、调试和任务切换时重新选取当前缺口。参考 [有效状态](../../skills/goal-continuity/references/state-and-resume.md) 和 [范围及返回](../../skills/goal-continuity/references/scope-and-return.md)。

Objective、Decisions、Current Work 优先保存能力与设计，使用宿主已有状态。只在真正交接时持久化必要信息，覆盖当前状态，禁止每次工具调用更新进度日志。恢复目标后必须改变下一项动作，停止无关夹具和旧机制的维护。

## 会复述规则却不改变动作

这一问题落实到所有专项方法的错误恢复与完成条件。[目标连续性](../../skills/goal-continuity/SKILL.md)处理用户纠错，[评审意见处理](../../skills/review-feedback/SKILL.md)处理实际反馈，[直接表达](../../skills/direct-writing/SKILL.md)删除认错表演与空泛保证。

纠正以真实编辑、决定或完整回答结束。对规则的重复解释不作为行动进展。语义不当的段落整段改，结构不当的模块改所有者。没有持续机制时不作未来承诺，不编造内部犯错原因。

## 墓碑、永久禁令与规范污染

[项目指令维护](../../skills/project-instructions/SKILL.md)、[作者文档](../../skills/author-documents/SKILL.md)和结构替换共同负责。参考 [作用域与权威](../../skills/project-instructions/references/scope-and-authority.md)、[现行知识](../../skills/author-documents/references/current-knowledge.md)。

纠正当前事实并清除错误残留。发布史留在发布记录，现行 Spec 使用当前决定。禁止把一次纠正、自身偏好和熟悉的测试流程自动写入 AGENTS、Skill、门禁。禁止为已淘汰内部名称创建永久反向测试。

## 局部约束变成全局焦虑

目标连续性、身份凭据方法和直接表达共同限制约束的作用范围。凭据保护应用到相关状态操作，无关编译与文案报告只说明实际问题。任务结束或条件改变时移除已经失效的临时要求，避免在每次输出反复声明。

## 早停、过度谨慎与任务类型错配

[需求发现](../../skills/requirements-discovery/SKILL.md)、[完整能力交付](../../skills/end-to-end-delivery/SKILL.md)、[目标连续性](../../skills/goal-continuity/SKILL.md)明确授权与成果。

研究形成发现，设计交付可实施结构，反思解释实际修改，实施完成真实用户能力。已授权可逆工作直接完成，遇到真实阻塞具体说明。发布和永久数据删除等动作按真实权限处理。禁止未经请求启动实现或替代文稿，禁止以是否继续提前结束。

## 作者身份与人类表达被替换

[作者写作](../../skills/author-documents/SKILL.md)与 [作者及读者](../../skills/author-documents/references/author-and-reader.md)保留立场、第一人称、幽默、锋芒和原来的交流对象。

从原文及邻近段落理解表达作用；不得擅自改成第三方审计口吻，不追加材料性质、来源自辩和无关文件头。真实未知写在影响理解的位置。翻译保留判断强度及技术含义。

## 共同的反馈循环

工程中的重复实现会提高理解成本，再诱发补丁与兼容；因此系统设计、结构替换和目标连续性必须协作。语言自证进入文档与 AGENTS 后会跨会话扩散；因此作者写作、项目指令和常驻约束共同处理。重复强化只出现在相关决定处，不转化为每步合规报告。

上游方法按完整有效片段复用。中文执行内容、英文采用稿与中文译文互相对应；有冲突的流程从实际引用链中退出。Hooks 和语义裁判没有被假定为本包已有能力，当前方法依靠常驻指令、专项工作知识及明确的词形检查运行。

## 完整案例的阅读位置

从原始现象进入方法后，可以沿以下完整案例继续实现：

- 架构与内部契约：[预约系统](../../skills/system-architecture/references/reservation-system.md)、[版本与审批](../../skills/domain-modeling/references/revision-approval.md)、[批量发布迁移](../../skills/structural-refactoring/references/replace-internal-contract.md)。
- 基础能力：[有效配置切换](../../skills/configuration/references/live-settings-case.md)、[未知提交结果](../../skills/transport-errors/references/operation-outcomes.md)、[原子预约](../../skills/persistence-transactions/references/atomic-reservation.md)、[有界工作队列](../../skills/async-lifecycle/references/bounded-worker-case.md)、[旧值回填与投递](../../skills/cache-events/references/stale-fill-and-outbox.md)。
- 完整交付与验证：[真实模型能力](../../skills/end-to-end-delivery/references/model-feature-path.md)、[验证责任重建](../../skills/meaningful-verification/references/choose-and-rebuild-suite.md)、[普通工作与分发义务](../../skills/process-control/references/ordinary-work-and-real-obligations.md)。
- 作品与长期知识：[按段落用途删改](../../skills/direct-writing/references/paragraph-purpose-edit.md)、[不同读者的同一事实](../../skills/author-documents/references/same-fact-different-readers.md)、[批量操作界面](../../skills/product-interface/references/bulk-import-interaction.md)、[指令维护](../../skills/project-instructions/references/maintain-instructions-without-drift.md)。
- 目标与协作：[恢复结构迁移](../../skills/goal-continuity/references/resume-structural-change.md)、[共享契约与子任务](../../skills/independent-subtasks/references/shared-contract-before-parallel.md)、[反馈归到所有者](../../skills/review-feedback/references/resolve-feedback-at-owner.md)。

代码示例展示各领域的具体实现关系。标为教学场景的设定用于迁移方法；真实作者改稿及差异保留在直接表达技能的本地案例中。
