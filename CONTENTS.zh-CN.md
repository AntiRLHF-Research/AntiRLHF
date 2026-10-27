# 专项技能目录

每个入口直接对应一项工作。按当前问题读取正文，再沿正文中的具体条件打开本地参考。

## 判断与系统设计

### 需求发现

[`requirements-discovery`](skills/requirements-discovery/SKILL.md)

处理产品需求、方案讨论和会改变实现的歧义；先读已有答案，明确使用者、行为与授权，禁止无关访谈和普遍审批门禁。

参考：[read-before-asking.en.md](skills/requirements-discovery/references/read-before-asking.en.md)；[read-before-asking.md](skills/requirements-discovery/references/read-before-asking.md)；[scope-and-decisions.md](skills/requirements-discovery/references/scope-and-decisions.md)；[离线收藏：把模糊需求变成实际能力](skills/requirements-discovery/references/offline-capability.md)。

### 研究与决策

[`research-decision`](skills/research-decision/SKILL.md)

完成技术调查、综述、方案比较和研究判断；从原始材料形成结论，明确决定性未知，禁止用风险、引用堆积和无限调查代替成果。

参考：[choice-and-uncertainty.md](skills/research-decision/references/choice-and-uncertainty.md)；[evidence-to-result.md](skills/research-decision/references/evidence-to-result.md)；[本地搜索：调查到可以作出选择](skills/research-decision/references/local-search-selection.md)。

### 系统架构

[`system-architecture`](skills/system-architecture/SKILL.md)

设计新项目、跨组件能力或重新划分系统；从产品行为确定领域、共享基础能力和依赖方向，避免重复所有者、浅层包装与万能管理器。

参考：[architecture-evolution.md](skills/system-architecture/references/architecture-evolution.md)；[greenfield-design.md](skills/system-architecture/references/greenfield-design.md)；[ownership-and-depth.md](skills/system-architecture/references/ownership-and-depth.md)；[预约系统：从用户动作建立完整结构](skills/system-architecture/references/reservation-system.md)。

### 领域建模

[`domain-modeling`](skills/domain-modeling/SKILL.md)

设计或调整业务实体、不变量、状态迁移与修改权；集中同一业务规则，避免内部模型版本链、可变镜像和分散判断。

参考：[model-and-migration.md](skills/domain-modeling/references/model-and-migration.md)；[state-and-invariants.md](skills/domain-modeling/references/state-and-invariants.md)；[文档审批：身份、内容版本和状态分工](skills/domain-modeling/references/revision-approval.md)。

### 依赖选型与采用

[`dependency-selection`](skills/dependency-selection/SKILL.md)

为新能力或现有机制选择并接入成熟库、平台功能和开源源码；优先复用，完整替换不合适的自制实现，禁止依赖洁癖及重复许可核验。

参考：[selection-and-integration.md](skills/dependency-selection/references/selection-and-integration.md)；[source-adoption.md](skills/dependency-selection/references/source-adoption.md)；[采用成熟解析器：CSV 导入的完整接入](skills/dependency-selection/references/csv-import-adoption.md)。

## 实现与结构演进

### 结构替换

[`structural-refactoring`](skills/structural-refactoring/SKILL.md)

重构、精简或替换架构、内部契约与重复实现；迁移生产者和消费者，删除旧路径及专属支撑，禁止为历史和旧测试保留内部双轨。

参考：[consumer-migration.md](skills/structural-refactoring/references/consumer-migration.md)；[data-and-public-contracts.md](skills/structural-refactoring/references/data-and-public-contracts.md)；[reduction-traps.md](skills/structural-refactoring/references/reduction-traps.md)；[批量发布：替换内部契约并完成所有消费者](skills/structural-refactoring/references/replace-internal-contract.md)。

### 根因调试

[`root-cause-debugging`](skills/root-cause-debugging/SKILL.md)

排查已发生的错误、跨组件异常和不稳定行为；沿真实数据与调用找到负责位置并修复，禁止症状补偿和排错流程膨胀。

参考：[condition-waiting.en.md](skills/root-cause-debugging/references/condition-waiting.en.md)；[condition-waiting.md](skills/root-cause-debugging/references/condition-waiting.md)；[investigation-and-return.md](skills/root-cause-debugging/references/investigation-and-return.md)；[root-cause-tracing.en.md](skills/root-cause-debugging/references/root-cause-tracing.en.md)；[root-cause-tracing.md](skills/root-cause-debugging/references/root-cause-tracing.md)；[异步下载失败：找到过早关闭的资源所有者](skills/root-cause-debugging/references/resource-lifetime-failure.md)。

### 完整能力交付

[`end-to-end-delivery`](skills/end-to-end-delivery/SKILL.md)

实施已授权的产品能力，接通用户入口、真实依赖、状态与可观察结果；禁止以 Mock、局部绿测或初步实现替代完整交付。

参考：[real-integrations.md](skills/end-to-end-delivery/references/real-integrations.md)；[user-paths.md](skills/end-to-end-delivery/references/user-paths.md)；[摘要功能：从入口到真实模型结果](skills/end-to-end-delivery/references/model-feature-path.md)。

## 测试、流程与审查

### 有效验证

[`meaningful-verification`](skills/meaningful-verification/SKILL.md)

在实现、修复和重构中选择保护真实行为的检查，并精简失效测试；默认避免红绿 TDD，禁止浅层重复、测试专用生产接口及临时脚手架入库。

参考：[behavior-and-failure.md](skills/meaningful-verification/references/behavior-and-failure.md)；[suite-replacement.md](skills/meaningful-verification/references/suite-replacement.md)；[按独立失败重建验证](skills/meaningful-verification/references/choose-and-rebuild-suite.md)。

### 流程抑制

[`process-control`](skills/process-control/SKILL.md)

组织开发工作并裁剪失去用途的测试、审查和流程；按真实需求推进能力，禁止自行添加证据矩阵、固定门禁、摘要核对和反复收尾。

参考：[real-obligations.md](skills/process-control/references/real-obligations.md)；[work-allocation.md](skills/process-control/references/work-allocation.md)；[工作负担的具体取舍](skills/process-control/references/ordinary-work-and-real-obligations.md)。

### 变更审查

[`change-review`](skills/change-review/SKILL.md)

按请求审查代码、PR、架构或文档，沿实际行为确认缺陷并给出负责位置；保持授权范围，禁止自发逐任务评审和循环收尾。

参考：[defect-reasoning.md](skills/change-review/references/defect-reasoning.md)；[沿实际行为发现缺陷](skills/change-review/references/follow-the-changed-behavior.md)。

### 评审意见处理

[`review-feedback`](skills/review-feedback/SKILL.md)

处理代码、设计和文档反馈，依据当前需求与实际材料判断并按根因修正；禁止表演式附和、旧架构保留特权和逐条补丁循环。

参考：[grouping-and-correction.md](skills/review-feedback/references/grouping-and-correction.md)；[review-feedback-method.en.md](skills/review-feedback/references/review-feedback-method.en.md)；[review-feedback-method.md](skills/review-feedback/references/review-feedback-method.md)；[把反馈合并到责任所有者](skills/review-feedback/references/resolve-feedback-at-owner.md)。

## 基础工程能力

### 配置

[`configuration`](skills/configuration/SKILL.md)

建立、扩展或迁移应用配置，统一来源、类型、有效值和生效方式；避免硬编码、重复默认值、私有解析和配置副本竞争。

参考：[effective-state.md](skills/configuration/references/effective-state.md)；[sources-and-types.md](skills/configuration/references/sources-and-types.md)；[配置快照切换：保存、生效和资源释放](skills/configuration/references/live-settings-case.md)。

### 传输与错误

[`transport-errors`](skills/transport-errors/SKILL.md)

设计和集成网络访问、超时、取消及错误契约；复用成熟客户端，集中重试和资源所有权，避免重复请求栈与多层错误改写。

参考：[clients-and-errors.md](skills/transport-errors/references/clients-and-errors.md)；[retry-and-cancellation.md](skills/transport-errors/references/retry-and-cancellation.md)；[外部操作：结果、重试与用户恢复](skills/transport-errors/references/operation-outcomes.md)。

### 日志与跟踪

[`observability`](skills/observability/SKILL.md)

设计和维护日志、关联上下文及追踪，并定位当前运行问题；集中有用事件，避免重复堆栈、无关状态声明和永久诊断脚手架。

参考：[diagnostics-and-cleanup.md](skills/observability/references/diagnostics-and-cleanup.md)；[logging-and-context.md](skills/observability/references/logging-and-context.md)；[从请求到后台作业的观测](skills/observability/references/request-to-job.md)。

### 存储与事务

[`persistence-transactions`](skills/persistence-transactions/SKILL.md)

新增或调整持久化、事务、并发和数据迁移；明确写入权及提交范围，避免分散提交、重启丢失和多套读写模型。

参考：[migration-and-recovery.md](skills/persistence-transactions/references/migration-and-recovery.md)；[transactions-and-concurrency.md](skills/persistence-transactions/references/transactions-and-concurrency.md)；[原子预约与一次取消](skills/persistence-transactions/references/atomic-reservation.md)。

### 异步任务与生命周期

[`async-lifecycle`](skills/async-lifecycle/SKILL.md)

设计和实现异步任务、并发、队列、取消与资源释放，在新增后台能力和调整执行路径时使用；统一任务所有权，避免失联任务、重复重试和关闭挂起。

参考：[queues-and-recovery.md](skills/async-lifecycle/references/queues-and-recovery.md)；[tasks-and-resources.md](skills/async-lifecycle/references/tasks-and-resources.md)；[有界工作队列：背压、失败与取消](skills/async-lifecycle/references/bounded-worker-case.md)。

### 缓存与事件

[`cache-events`](skills/cache-events/SKILL.md)

设计和修改缓存、事件投递与订阅；明确正式状态、更新顺序和资源生命周期，避免缓存争写、陈旧回填、重复副作用及分散刷新。

参考：[cache-consistency.md](skills/cache-events/references/cache-consistency.md)；[events-and-subscriptions.md](skills/cache-events/references/events-and-subscriptions.md)；[旧值回填与事件投递](skills/cache-events/references/stale-fill-and-outbox.md)。

### 身份与权限

[`identity-permissions`](skills/identity-permissions/SKILL.md)

设计和接入身份认证、资源授权及凭据管理；统一业务权限规则，复用成熟认证机制，防止入口遗漏、跨租户访问和秘密泄漏。

参考：[credentials-and-scope.md](skills/identity-permissions/references/credentials-and-scope.md)；[identity-and-authorization.md](skills/identity-permissions/references/identity-and-authorization.md)；[批量导出：授权贯穿整个用户路径](skills/identity-permissions/references/batch-export-authority.md)。

### 跨平台

[`platform-portability`](skills/platform-portability/SKILL.md)

实现和维护目标平台的文件、路径、进程与编码行为；采用运行时和成熟适配能力，避免硬编码目录、散落平台分支与命令拼接。

参考：[paths-and-processes.md](skills/platform-portability/references/paths-and-processes.md)；[platform-integration.md](skills/platform-portability/references/platform-integration.md)；[外部工具的跨平台边界](skills/platform-portability/references/external-tool-boundary.md)。

### 国际化

[`localization`](skills/localization/SKILL.md)

设计和维护多语言文本、语言选择及地区格式；统一资源与偏好，避免字符串拼接、分散语言判断和翻译削弱作者表达。

参考：[locale-and-time.md](skills/localization/references/locale-and-time.md)；[resources-and-messages.md](skills/localization/references/resources-and-messages.md)；[预约时间与完整消息](skills/localization/references/calendar-and-display.md)。

## 文字、界面与项目知识

### 直接表达

[`direct-writing`](skills/direct-writing/SKILL.md)

撰写或修改回答、技术判断和说明时直接表达结果与依据；主动压制防御性限定、虚构反驳、判断退缩和自证说明，删除整项多余信息。

参考：[defensive-patterns.md](skills/direct-writing/references/defensive-patterns.md)；[observed-edits.md](skills/direct-writing/references/observed-edits.md)；[scanner-use.md](skills/direct-writing/references/scanner-use.md)；[按段落用途删改](skills/direct-writing/references/paragraph-purpose-edit.md)。

### 作者写作与文档

[`author-documents`](skills/author-documents/SKILL.md)

编写、编辑和翻译文章、README、用户指南及开发说明；沿用原作的作者身份、风格和读者定位，删除第三方审计旁白、无关元数据与纠错残留。

参考：[author-and-reader.md](skills/author-documents/references/author-and-reader.md)；[current-knowledge.md](skills/author-documents/references/current-knowledge.md)；[按实际读者组织同一事实](skills/author-documents/references/same-fact-different-readers.md)。

### 用户交互与内容

[`product-interface`](skills/product-interface/SKILL.md)

从最终使用者视角设计和修改 CLI、Web、应用界面的操作、状态与文案；实现连贯用户路径，删除施工自述和模板化装饰。

参考：[content-and-observed-edits.md](skills/product-interface/references/content-and-observed-edits.md)；[tasks-and-states.md](skills/product-interface/references/tasks-and-states.md)；[批量导入：状态、恢复与信息层级](skills/product-interface/references/bulk-import-interaction.md)。

### 项目指令维护

[`project-instructions`](skills/project-instructions/SKILL.md)

编写和维护 AGENTS、Skills 及长期项目知识；保留有效事实、动作与作用域，删除临时纠错固化、个人测试偏好和失效规则。

参考：[authoring-method.md](skills/project-instructions/references/authoring-method.md)；[scope-and-authority.md](skills/project-instructions/references/scope-and-authority.md)；[项目事实、持续要求与临时纠正](skills/project-instructions/references/maintain-instructions-without-drift.md)。

## 连续工作与协作

### 目标连续性与纠错

[`goal-continuity`](skills/goal-continuity/SKILL.md)

在长任务、上下文恢复、用户反馈和范围变化中维持目标与有效决定；把下一步用于未完成能力，禁止日志化、任务替换和无依据早停。

参考：[scope-and-return.md](skills/goal-continuity/references/scope-and-return.md)；[state-and-resume.md](skills/goal-continuity/references/state-and-resume.md)；[恢复结构迁移主线](skills/goal-continuity/references/resume-structural-change.md)。

### 独立子任务

[`independent-subtasks`](skills/independent-subtasks/SKILL.md)

按独立责任分配并行研究、实现或迁移，并将成果整合到实际系统；提供必要上下文，协调共享契约，禁止多层评审接力。

参考：[context-and-integration.md](skills/independent-subtasks/references/context-and-integration.md)；[independent-task-method.en.md](skills/independent-subtasks/references/independent-task-method.en.md)；[independent-task-method.md](skills/independent-subtasks/references/independent-task-method.md)；[共享契约与独立子任务](skills/independent-subtasks/references/shared-contract-before-parallel.md)。

### Git 工作区

[`git-workspaces`](skills/git-workspaces/SKILL.md)

按任务管理分支、暂存区和隔离工作树，保留用户已有改动；需要隔离时复用宿主或 Git 能力，禁止例行复制工作区和强制清理。

参考：[existing-isolation.en.md](skills/git-workspaces/references/existing-isolation.en.md)；[existing-isolation.md](skills/git-workspaces/references/existing-isolation.md)；[worktree-lifecycle.md](skills/git-workspaces/references/worktree-lifecycle.md)；[提交、暂存区与工作区](skills/git-workspaces/references/index-and-working-tree.md)。

### 集成与发布

[`release-integration`](skills/release-integration/SKILL.md)

完成明确要求的提交、PR、合并、打包和发布；保存用户指定的版本与暂存边界，采用现有交付工具，禁止擅自扩大外部操作。

参考：[commits-and-integration.md](skills/release-integration/references/commits-and-integration.md)；[package-and-release.md](skills/release-integration/references/package-and-release.md)；[按使用方式组织交付](skills/release-integration/references/deliverable-shapes.md)。
