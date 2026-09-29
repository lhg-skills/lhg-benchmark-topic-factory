# 数据源工具箱（各平台获取路径与坑）

> 原则：API 实测 > 官方页 > 主流媒体报道 > 第三方数据站 > 转载/索引。所有数字标注来源与获取时间；拿不到的写"未找到"，严禁编造。

## B站（API 最友好）

- 粉丝数（免登录）：`https://api.bilibili.com/x/relation/stat?vmid={UID}`
- 单条数据：`https://api.bilibili.com/x/web-interface/view?bvid={BV号}` → 播放/点赞/收藏/时长
- 空间投稿数：`https://api.bilibili.com/x/space/navnum?mid={UID}`
- 投稿列表：**有风控（-352）**，改走搜索引擎索引 + 转载站 + 用户手动浏览
- UID 获取：搜"B站空间页"或从分享链接提取；space.bilibili.com/{UID}
- 注意：商单视频不走联合投稿标记（is_cooperation 常为 0），识别只能靠内容和媒体披露

## 抖音（全反爬，间接拼图）

- 站内页需登录+签名，直接抓基本失败
- 路径：飞瓜/抖查查/蝉妈妈**免费公开页**（bloggeropen 页常可读：粉丝、近7/30/90天涨粉、作品数、直播场次）→ 搜索引擎索引的视频标题 → 西瓜视频/今日头条镜像页 → 媒体报道口径
- 直播间页 live.douyin.com/{web_rid} 的页面 JSON 有时可提取昵称/头像实锤账号归属

## 微信公众号（原文难，走转载）

- 按文章标题搜知乎 / 腾讯新闻 / 优设 uisdc / 虎嗅 / 36氪转载版
- 博主方法论若开源过 GitHub skill，直接抓原文（最高价值）
- 公众号广告不存档，商单识别靠媒体点名

## 微博 / 小红书（难抓，靠转载与数据站公开页）

- 微博页反爬：靠搜索摘要 + 知乎/CSDN/公众号转载 + 平台年度榜单口径
- 小红书（数据可得性最差，提前向用户说明降级预期）：
  - 站内笔记数据搜索引擎基本不可抓，粉丝数取媒体报道口径
  - 第三方数据站公开页：新红（新榜旗下）、千瓜数据的免费博主页，能看多少拿多少
  - 选题清单：搜"博主名 + 笔记标题关键词"、搜转载（公众号/知乎常整篇搬运爆款笔记）
  - 笔记样式/封面：搜博主名字+「小红书」看截图类盘点文
  - 结构拆解照常可做：爆款笔记的标题公式、封面大字、正文结构与平台无关

## GitHub（只走 api.github.com）

- 仓库目录：`https://api.github.com/repos/{OWNER}/{REPO}/contents/{PATH}`
- 全量树：`https://api.github.com/repos/{OWNER}/{REPO}/git/trees/{branch}?recursive=1`
- 文件原文：contents 接口 + `Accept: application/vnd.github.raw` 头（或解码 base64）
- 搜索：`https://api.github.com/search/repositories?q={关键词}`
- **git clone 和 raw.githubusercontent.com 直链在本机常失败，不要浪费时间**

## 榜单与数据站

- AIGCRank（AI赛道博主榜）：官网可能抓不到，搜掘金/搜狐转载全文
- 飞瓜数据：`dy.feigua.cn/bloggeropen/{hash}` 公开页免费可读核心增量数据
- 新榜：公开文章有生态数据；新抖垂类榜多需付费
- YouTube：频道页可直接 WebFetch（订阅数/播放列表）

## 通用搜索策略

- 中文内容 WebSearch 直接中文关键词；一个角度搜不到就换词（账号名+合集名/单集名/"博主名+粉丝"）
- 深度报道（天花板/风口/灰产曝光类）是最重要的单篇信息源，务必 WebFetch 全文
- 西瓜视频 m.ixigua.com 的视频页有时 404，多试时间戳链接
- 存疑信息（SEO 垃圾站、单一来源的数字）标注"存疑"，有第二来源独立印证才可采用
