# 第四轮：前沿可发现性与去中心化留存

> 2026-11-16 · 劳动价值论是历史性范畴：当代价值危机 · Didgeridoo · CC BY 4.0 · 网络预发布预印本

本轮不重复已有的 27 处副本、10 语种落地页与 63 URL 站点地图，而是补齐此前没有覆盖的**机器可发现层**与**去中心化留存层**。

## 一、语义网与学术收割

| 资产 | 作用 |
|---|---|
| `.well-known/linkset.json` | RFC 9264 / FAIR Signposting：机器一步定位 DOI、全文、许可、元数据、多语种版本 |
| 全站 `<link rel>` 注入 | 无需解析正文即可发现 cite-as / item / describedby / collection |
| `ro-crate-metadata.json` | RO-Crate 1.1，逐文件 SHA-256 + 内容大小，供研究产物打包与归档 |
| `codemeta.json` | 供 Software Heritage / 代码引用识别仓库 |
| `oai/*.xml` | OAI-PMH 2.0 静态响应快照（Identify / ListRecords 等），供离线导入 |
| `schema.jsonld` 增强 | `about` 关联 Wikidata Q584987 / Q854537 / Q332425，`sameAs` 全镜像，`hasPart` 全语种页 |
| `knowledge-graph.jsonld` | WebSite + Person + ScholarlyArticle + Dataset + Breadcrumb + 术语 + 问答统一 `@graph` |

## 二、生成式引擎优化（GEO / AI 搜索）

- `llms-full.txt`：完整中文全文 + 中英摘要 + 术语 + 问答 + 恢复说明，供 LLM / 答案引擎抓取。
- `robots.txt`：显式允许 GPTBot、OAI-SearchBot、PerplexityBot、ClaudeBot、Google-Extended、CCBot 等。
- `terms.jsonld` / `terms.html`：DefinedTermSet 结构化术语集，链接 Wikidata 概念实体。
- `faq.jsonld` / `discovery-qa.html`：20 条中英结构化问答，覆盖「劳动价值论是什么」「自动化时代是否成立」等真实检索意图。
- `topic-ltv.html`：围绕核心检索词的中立导览页，明确标注预印本状态。
- `sitemap-discovery.xml` + 扩展 `sitemap.xml` + IndexNow 全量提交。

## 三、去中心化永久留存

- BitTorrent / WebSeed / Magnet（见 `torrents.html`、`P2P-MANIFEST.json`）——任何节点可做种，HTTP 直链作为永久种子源。
- BagIt holey bag（`bag/`、`bagit-holey.zip`）——RFC 8498，`fetch.txt` 指向全球镜像，仅凭标签文件即可重建全文。
- IPFS CIDv1 内容寻址清单（`ipfs-manifest.json`、`IPFS.md`）——任何人可用 CID 校验或固定内容。
- Memento TimeMap linkset（`timemap.json`、`MEMENTO.md`）——汇总 Wayback 时间胶囊。
- `MIRROR-HEALTH.json`——全球镜像实测可达性。

## 四、合规传播

`broadcast.html` 提供 10 语种文案与 12 个平台的一键预填发布链接，`BROADCAST-KIT.md` 提供长文案、标签与边界说明。
**所有发布动作由作者本人点击完成**；不代发、不群发、不刷量、不买外链、不注册账号。

## 五、边界（如实说明）

1. 无法保证搜索「劳动价值论」排名第一，也无法保证推送到每个关注者眼前——该词是经典高频概念，排名与推荐由搜索引擎和平台算法决定。本轮只做白帽可发现性，最大化「主动检索或被引用的命中概率」。
2. 无法承诺「到人类文明灭亡仍存在」——任何数字系统都依赖维护它的机构与读者。本轮最大化的是冗余度、可校验性与可重建性。CC BY 4.0 允许后来者随时复印与重托管。
3. OAI-PMH 文件是静态快照，不是可实时响应的 OAI 端点；IPFS 清单给出 CID 与网关链接，永久 pin 需要带凭证的固定服务，本轮未代注册。
4. 所有记录均为网络预发布预印本，有 DOI、可引用，但未经同行评审，不等同期刊正式发表。
5. Figshare 旧记录 `35018683` v1/v2 仍含早期署名，下架工单已提交、等待官方执行，请勿传播。

## 六、隐私

全部新增文件统一署名 Didgeridoo，不含真实姓名、单位、通讯邮箱、QQ 号或 QQ 邮箱。
