# lhg-benchmark-topic-factory · 对标拆解选题工厂

把任意行业/赛道/平台的头部博主"深挖 → 逆向选题 → 文案生产 → 排期"做成 8 阶段流水线的 skill（lhg-skills 出品）。

**流程**：Phase 0 定参数 → 1 生态大盘 → 2 对标深挖（每个账号一个独立调研 agent，B站 API 实测 + 第三方数据站间接路径 + api.github.com）→ 3 元数据层 → 4 六系逆向选题库（100 条）→ 5 文案库（创作规范 + 批次扩写）→ 6 排期规划 → 7 冒烟测试（`scripts/smoke_test.py` 修到全绿）。

**触发**：用户说"找对标 / 挖选题 / 做选题库 / 100条选题 / 起号规划"，或"调研某赛道博主并产出内容"时自动触发。

## 安装

- 通用：将本仓库放到各平台的 skill 目录（如 `~/.agents/skills/benchmark-topic-factory/`，注意 SKILL.md 须在目录根）。
- 平台无关：本 skill 写法平台中立（联网搜索/网页抓取/子 agent/任务清单），不依赖任何单一生态的专有工具名。

## 自检与反馈

本 skill 每次执行后自动做一次轻量自检；只有发现疑似自身缺陷时，才运行 `references/smoke-test.md` 标准用例并输出质检报告。报告经你确认后，可一键向 GitHub 提交 `[QC]` issue（模板见 `.github/ISSUE_TEMPLATE/qc-report.md`）。

## 版本

- 1.0.0（2026-09-29）：首版。8 阶段流水线 + 冒烟脚本；补齐自检与反馈机制、平台中立写法、manifest 与发布文件。

作者：刘洪光（keepliu28）· lhg-skills
