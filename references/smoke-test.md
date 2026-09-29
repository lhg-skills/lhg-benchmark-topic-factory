# 标准冒烟测试（skill 自检用）

> 触发时机：SKILL.md「自检与反馈」命中疑似自身缺陷时运行。
> 说明：`scripts/smoke_test.py` 本是校验 skill **产出物**（选题库/文案库）的脚本；
> 以下用例用最小 fixture 反向验证脚本本身的检查能力（禁词透传、隔离开关、
> 字段完整性），属于 skill 级冒烟。以下全部用例已于 2026-09-29 实测通过。

## S-1 红线禁词透传
- 目的：Phase 0 红线禁词必须通过 `--banned-words` 传入，否则脚本只扫通用禁词，
  红线形同虚设。
- fixture：`references/fixtures/fixture-banned.md`（第 2 条文案含红线词"绝绝子"）
- 期望 FAIL：
  ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-banned.md --banned-words 绝绝子 --no-isolation
  ```
  → 退出码 1，FAIL 为 `第2条 文案含禁词: 绝绝子`
- 反向期望 PASS（证明透传机制是 `--banned-words` 在起作用，而非内置表误伤）：
  ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-banned.md --no-isolation
  ```
  → 退出码 0，`✅ 冒烟测试全绿`

## S-2 内置禁词表生效
- fixture：`references/fixtures/fixture-default-banned.md`（文案含"保姆级"）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-default-banned.md --no-isolation
  ```
  → 退出码 1，FAIL 为 `第1条 文案含禁词: 保姆级`

## S-3 隔离词开关
- fixture：`references/fixtures/fixture-isolation.md`（文案含"股票"）
- 默认运行 → 退出码 1，FAIL 为 `第1条 文案含禁词: 股票`（默认财经隔离词表生效）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-isolation.md --no-isolation
  ```
  → 退出码 0（开关有效；赛道本身是财经时必须加 `--no-isolation`，否则误杀）

## S-4 条目完整性
- fixture：`references/fixtures/fixture-incomplete.md`（编号 1、3，缺 2；第 3 条缺"创作思路"字段）
- ```bash
  python3 scripts/smoke_test.py references/fixtures/fixture-incomplete.md --no-isolation
  ```
  → 退出码 1，FAIL 含 `编号缺失 [2]` 与 `第3条: 缺字段 [创作思路]`

## S-5 人工检查项（脚本扫不到的）
- [ ] Phase 2 报告抽查 3 个数字：是否标注来源与获取时间，"未找到"是否如实标注
- [ ] Phase 5 文案库抽查：具体数据是否为占位示例，文件头是否有"上镜前换真实截图"声明
- [ ] 选题库抽查 5 条：是否标注对标公式出处（"抄的是谁的哪个公式"）
- [ ] 平台降级预期是否已向用户如实说明（如小红书粉丝数据只能取媒体口径）
