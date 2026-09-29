# lhg-benchmark-topic-factory · 对标拆解选题工厂

[English](#english) | [中文](#中文)

---

## English

**Benchmark Topic Factory** turns "find benchmark accounts → tear down their content → produce your own topic library" into an executable 8-phase pipeline for **any industry, platform, or niche**. Topics are never brainstormed from scratch — every one of the 100 topics is reverse-engineered from verified hit formulas, and each one names whose formula it came from.

### Workflow

1. **Phase 0 · Scope** — confirm niche, platforms, persona, content mix, and the **red-line list** (banned topics/words, compliance defaults).
2. **Phase 1 · Landscape** — market scan: who earns, how, and where the ceiling is. Ceiling/anti-hype deep reports are the highest-value single source.
3. **Phase 2 · Benchmark teardown** — one read-only agent per account; pull 20–80 titles with real metrics, hook formulas, script structure, presentation format, monetization traces. API-verified where possible (Bilibili public API, third-party open pages, api.github.com). Missing data is marked "not found" — never fabricated.
4. **Phase 3 · Metadata** — annual rankings + community style-distillation repos + benchmark authors' own open-sourced methodology (the single highest-value discovery).
5. **Phase 4 · Topic library (100)** — six-series method: A reality-show spine (20) / B methodology (20) / C hands-on hot-take tests (20) / D "I tried it so you don't have to" (15) / E recurring column (10) / F opinion & moat (15). Every topic tagged with its benchmark formula.
6. **Phase 5 · Copy library** — a creation spec (hook templates, Feynman analogies, double CTA, banned words) then batch-written scripts, 5 fields per topic: title / cover text / per-platform hashtags / 45–60s oral script / production notes. All numbers are placeholders until replaced with real screenshots.
7. **Phase 6 · Schedule** — weekly template + milestone binding (Day-0 pledge → Day-90 review loop) + a 6-step production line.
8. **Phase 7 · Smoke test** — `scripts/smoke_test.py` mechanically checks structure: item completeness, numbering, script length, banned words (scoped to script fields only), platform hashtags. FAIL must be fixed to green; content quality still needs human review.

### Output

Landscape report · per-account teardown reports · 100-topic library · full copy library · schedule · smoke-test pass.

### Install

```bash
npx skills add lhg-skills/lhg-benchmark-topic-factory
```

Or copy the folder to `~/.agents/skills/benchmark-topic-factory/` (any agent that reads Markdown skills).

---

## 中文

**对标拆解选题工厂**：把"找对标 → 内容深拆 → 逆向选题 → 文案生产 → 排期"做成可执行流水线，适用于**任何行业/赛道/平台**。选题不靠拍脑袋——100 条选题全部从已验证的爆款公式逆向产出，每条标注出处。

### 流程（8 个 Phase）

0. **定参数**：赛道、平台、人设、内容配比、**红线清单**（禁话题/禁词/合规默认项）
1. **生态大盘**：谁在赚钱、怎么赚、天花板在哪；天花板类深度报道是最高价值单篇信源
2. **对标深挖**：一个账号一个只读 agent；挖 20-80 条标题+真实数据、标题公式、稿子结构、展现形式、变现痕迹；能 API 实测就实测（B站公开 API/第三方公开页/api.github.com），拿不到的明确标"未找到"，严禁编造
3. **元数据层**：年度榜单 + 圈内风格蒸馏库 + 对标博主本人开源的方法论（最高价值发现）
4. **100 条选题库**：六系法——A 真人秀主线 20 / B 方法论 20 / C 实测借势 20 / D 避坑"替你试完了" 15 / E 固定栏目 10 / F 认知观点 15；每条标注对标公式
5. **文案库**：先固化创作规范（钩子模板/费曼类比/双钩结尾/禁词表），再批次扩写；每条五件套：标题/封面大字/分平台标签/45-60 秒口播稿/创作思路；所有数字为占位，上镜前换真实截图
6. **排期规划**：周模板 + 里程碑绑定（第 0 天宣言 → 第 90 天答辩闭环）+ 六步生产流水线
7. **冒烟测试**：`scripts/smoke_test.py` 机械校验结构（条目完整性/编号/字数/禁词只扫口播字段/平台标签）；FAIL 修到全绿，内容质量仍需人工过目

### 安装

```bash
npx skills add lhg-skills/lhg-benchmark-topic-factory
```

或将文件夹拷贝到 `~/.agents/skills/benchmark-topic-factory/`（任何读 Markdown skill 的 agent 通用）。

---

作者：刘洪光（keepliu28）· lhg-skills
