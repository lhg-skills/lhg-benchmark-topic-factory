#!/usr/bin/env python3
"""选题库冒烟测试：对"对标拆解选题工厂"的产出物做机械校验。

仅适用于条目型产出（Phase 4 选题库 / Phase 5 文案库 / Phase 6 总文件）。
Phase 1/2/3 的调研报告不适用本脚本（会因无条目报 FAIL），改做人工检查：
文件存在、信息源 URL 清单完整、"未找到"项如实标注。

用法：
  python3 smoke_test.py 文件1.md 文件2.md ... [--platforms 视频号,抖音]
                         [--banned-words 词1,词2] [--isolation-words 词1,词2 | --no-isolation]
                         [--strict] [--allow-overlap]

参数说明：
  --platforms        标签必须包含的平台名（逗号分隔，默认 视频号,抖音，按赛道实际主阵地覆盖）
  --banned-words     追加自定义 FAIL 禁词（来自 Phase 0 红线清单，逗号分隔）
  --isolation-words  覆盖默认的隔离违禁词表（默认为财经隔离词：财经/股票/炒股/基金等；
                     仅当用户账号有双账号隔离需求时使用）
  --no-isolation     完全关闭隔离词检查（当赛道本身就是隔离词所属领域时，如财经自媒体）
  --allow-overlap    允许跨文件条目编号重复（总文件=分文件合集场景）

检查项：
  1. 条目提取：### 第 N 条，编号无缺失/重复
  2. 五件套字段完整：标题/封面大字/标签/文案/创作思路
  3. 文案字段字数：机械宽限带 100-400（越界 = 警告；创作目标是 160-260，
     以创作规范为准，脚本只拦结构性越界）
  4. 禁词/红线词扫描：只扫每条的"文案"字段内容（备注与规则说明不扫）
  5. 标签字段包含所有平台名
  6. 多文件间条目一致（--allow-overlap 除外）

退出码：有 FAIL 时为 1，全绿为 0。WARN 不影响退出码。
"""
import argparse
import re
import sys
from pathlib import Path

# 结构性缺失 = FAIL；措辞风险 = WARN
BANNED_FAIL = ["保姆级", "7天速成", "七天速成", "家人们谁懂啊", "在当今"]
BANNED_WARN = ["首先", "其次", "最后", "众所周知", "干货满满", "月入过万", "轻松赚钱", "稳赚", "躺赚"]
ISOLATION_FAIL = ["财经", "股票", "炒股", "基金", "证券", "期货", "加仓", "清仓", "个股", "涨停"]

ITEM_RE = re.compile(r"^###\s*第\s*(\d+)\s*条", re.M)
FIELD_RE = {
    "标题": re.compile(r"- \*\*标题\*\*[:：]"),
    "封面大字": re.compile(r"- \*\*封面大字\*\*[:：]"),
    "标签": re.compile(r"- \*\*标签\*\*[:：]"),
    "文案": re.compile(r"- \*\*文案\*\*[:：]?\s*\n(.+?)(?=\n- \*\*创作思路\*\*|\n###\s*第|\Z)", re.S),
    "创作思路": re.compile(r"- \*\*创作思路\*\*[:：]"),
}


def extract_items(text):
    """返回 {编号: (item_text, 文案字段内容)}"""
    items = {}
    matches = list(ITEM_RE.finditer(text))
    for i, m in enumerate(matches):
        num = int(m.group(1))
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        block = text[m.start():end]
        copy_m = FIELD_RE["文案"].search(block)
        copy_text = copy_m.group(1).strip() if copy_m else ""
        items[num] = (block, copy_text)
    return items


def scan_words(text, words, level, path, num, fails, warns):
    hits = [w for w in words if w in text]
    if hits:
        (fails if level == "FAIL" else warns).append(f"{path} 第{num}条 文案含禁词: {','.join(hits)}")


def check_file(path, platforms, strict, banned_extra, isolation_words):
    text = Path(path).read_text(encoding="utf-8")
    items = extract_items(text)
    fails, warns = [], []

    if not items:
        fails.append(f"{path}: 未提取到任何条目（### 第 N 条 格式）")
        return items, fails, warns

    nums = sorted(items)
    dup = {n for n in nums if nums.count(n) > 1}
    if dup:
        fails.append(f"{path}: 重复条目编号 {sorted(dup)}")
    missing = set(range(nums[0], nums[-1] + 1)) - set(nums)
    if missing:
        fails.append(f"{path}: 编号缺失 {sorted(missing)}")

    for num, (block, copy_text) in items.items():
        for field, pattern in FIELD_RE.items():
            if field == "文案":
                continue
            if not pattern.search(block):
                fails.append(f"{path} 第{num}条: 缺字段 [{field}]")
        if not copy_text:
            fails.append(f"{path} 第{num}条: 文案字段为空或无法提取")
            continue
        n = len(re.sub(r"\s", "", copy_text))
        if not (100 <= n <= 400):
            level = "FAIL" if (strict and n < 80) else "WARN"
            msg = f"{path} 第{num}条: 文案字数 {n} 越界（期望100-400）"
            (fails if level == "FAIL" else warns).append(msg)
        scan_words(copy_text, list(BANNED_FAIL) + list(banned_extra), "FAIL", path, num, fails, warns)
        if isolation_words:
            scan_words(copy_text, isolation_words, "FAIL", path, num, fails, warns)
        scan_words(copy_text, BANNED_WARN, "WARN", path, num, fails, warns)
        if "标签" in FIELD_RE and FIELD_RE["标签"].search(block):
            tag_line = FIELD_RE["标签"].search(block).group(0)
            tag_block = re.search(r"- \*\*标签\*\*[:：](.+)", block)
            if tag_block:
                for p in platforms:
                    if p not in tag_block.group(1):
                        warns.append(f"{path} 第{num}条: 标签缺平台 [{p}]")

    return items, fails, warns


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--platforms", default="视频号,抖音")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--allow-overlap", action="store_true",
                    help="允许跨文件条目编号重复（总文件=分文件合集场景）")
    ap.add_argument("--banned-words", default="",
                    help="追加自定义 FAIL 禁词，逗号分隔（来自 Phase 0 红线清单）")
    ap.add_argument("--isolation-words", default=None,
                    help="覆盖默认隔离违禁词表，逗号分隔")
    ap.add_argument("--no-isolation", action="store_true",
                    help="关闭隔离词检查（赛道本身属于隔离词领域时使用）")
    args = ap.parse_args()
    platforms = [p for p in args.platforms.split(",") if p]
    banned_extra = [w for w in args.banned_words.split(",") if w]
    if args.no_isolation:
        isolation_words = None
    elif args.isolation_words is not None:
        isolation_words = [w for w in args.isolation_words.split(",") if w]
    else:
        isolation_words = ISOLATION_FAIL

    all_nums, total_fails, total_warns = {}, [], []
    for f in args.files:
        if not Path(f).exists():
            total_fails.append(f"文件不存在: {f}")
            continue
        items, fails, warns = check_file(f, platforms, args.strict, banned_extra, isolation_words)
        all_nums[f] = set(items)
        total_fails += fails
        total_warns += warns
        print(f"[文件] {f}: {len(items)} 条")

    if len(all_nums) > 1 and not args.allow_overlap:
        keys = list(all_nums)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                overlap = all_nums[keys[i]] & all_nums[keys[j]]
                if overlap:
                    total_fails.append(f"跨文件条目重复: {keys[i]} 与 {keys[j]} → {sorted(overlap)}")

    print(f"\n[标签平台] {platforms}")
    print(f"[FAIL] {len(total_fails)} 项")
    for x in total_fails:
        print(f"  ✗ {x}")
    print(f"[WARN] {len(total_warns)} 项")
    for x in total_warns[:30]:
        print(f"  ⚠ {x}")
    if len(total_warns) > 30:
        print(f"  ...（其余 {len(total_warns) - 30} 条 WARN 略）")

    print(f"\n结论: {'❌ 未通过（须修复后重跑）' if total_fails else '✅ 冒烟测试全绿'}")
    sys.exit(1 if total_fails else 0)


if __name__ == "__main__":
    main()
