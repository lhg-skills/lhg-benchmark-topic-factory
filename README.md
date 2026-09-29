# lhg-benchmark-topic-factory · 对标拆解选题工厂

> **一句话**：对标拆解选题工厂：找对标 → 内容深拆 → 逆向 100 条选题库 → 口播文案库 → 排期规划，8 阶段流水线，任意行业可复刻。
>
> **一键安装**：`npx skills add lhg-skills/lhg-benchmark-topic-factory`


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

## 什么时候用 / 什么时候不用

**用它，当你**：
- 做 IP/内容账号，需要系统化的选题库而不是灵感
- 想复制对标账号的内容打法

**别用它，当你**：
- 只想偶尔写一篇，不需要选题库

---

## lhg-skills 矩阵

刘洪光出品的中文 Agent Skills，全开源：

| Skill | 名称 | 一句话 |
|---|---|---|
| `lhg-writing` | 中文写作 | 风格指纹 → Orwell 六规则 → AI 味诊断，写出有人味的中文 |
| `lhg-slides` | HTML 演示文稿 | 大纲/文档一键生成可编辑的单文件 HTML slides |
| `lhg-trend` | 近30天热点扫描 | 话题火不火、为什么火、还能不能追 |
| `lhg-deep-research` | 深度调研 | 多源检索 → 结构化中文调研报告 |
| `lhg-benchmark-topic-factory` | 对标拆解选题工厂 | 找对标 → 逆向 100 条选题库 → 口播文案 |
| `lhg-net` | 互联网能力层 | 中文优先多平台取数，取不到诚实说 |
| `lhg-craft` | AI 编程工程规范 | 分级澄清 → TDD → 独立评审 → 证据门禁 |
| `lhg-debug` | 系统化调试 | 复现 → 定位 → 修复 → 验证 |
| `lhg-secure` | 代码安全审计 | 九维度扫描 + 对抗验证，分级风险清单 |
| `lhg-finder` | 找 skill 质检门 | 装第三方 skill 前的 blocker 检查 + 六维评分 |

安装任意一个：`npx skills add lhg-skills/<上表 slug>`

---

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
