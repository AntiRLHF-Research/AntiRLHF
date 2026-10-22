# 实验用法

[English](INSTALL.md)

本仓库不装进个人日常环境。`scripts/install.py` 只用于实验程序指定的任务环境。

实验程序从仓库根目录读取 Constitution 和五个核心技能，冻结进批次后放进任务环境：

- C 组：按宿主的技能发现方式安装，用户请求不点名 AntiRLHF。任务明确要求接入、CI 或发布时，才加入 `project-workflows`。
- B 组：由同一文件生成静态规则文本，与 C 组同时提供。
- A 组：不安装本仓库的任何材料。

检查链接和打包不把材料装进个人环境：

```bash
python scripts/validate.py
python scripts/package_skills.py --with-project-workflows --out dist/AntiRLHF-skills-full.zip
```

`docs/` 和 `archive/` 不进入被试环境。

冻结时记录 `.version`、对应 Git 提交和文件摘要。已冻结批次不随后续修改自动更换。
