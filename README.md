# lhg-benchmark-topic-factory · 对标拆解选题工厂

把任意行业/赛道/平台的头部博主"深挖 → 逆向选题 → 文案生产 → 排期"做成流水线的 ZCode skill。

**流程**：Phase 0 定参数（赛道/平台/人设/红线）→ 1 生态大盘 → 2 对标深挖（并行 agent，B站 API 实测/飞瓜间接路径/api.github.com）→ 3 元数据层（榜单+博主开源方法论）→ 4 六系逆向选题库 → 5 文案库（创作规范+批次扩写）→ 6 排期规划 → 7 冒烟测试（脚本修到全绿）。

**触发**：用户说"找对标 / 挖选题 / 做选题库 / 100条选题 / 起号规划"，或"调研某赛道博主并产出内容"时自动触发。

**安装**：拷贝到 `~/.agents/skills/benchmark-topic-factory/` 即可。

**质检**：`scripts/smoke_test.py` 对选题库做机械校验（条目完整性/禁词/红线词/平台标签），支持 `--banned-words` 传入自定义红线、`--no-isolation`、`--platforms`、`--allow-overlap`。

作者：刘洪光（keepliu28）· lhg-skills
