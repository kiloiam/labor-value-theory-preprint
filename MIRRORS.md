# 跨机构副本登记表（Redundancy Map）

> 《劳动价值论是历史性范畴：当代价值危机》 · Didgeridoo · CC BY 4.0 · 2026-11-16
> 生成依据：`PRESERVATION-MANIFEST.json`。本表只列干净、可安全传播的公开副本。

## 设计原则

任何**单独一个**幸存副本都必须足以还原全文、署名、许可协议与其他副本地址。
因此副本分散在不同机构、不同法域、不同协议：DOI 仓储、Git 版本库、UNESCO 源代码永久存档、
网页时间胶囊、全球 CDN、学术索引，以及无需任何软件即可阅读的纯文本 / 单文件 HTML 离线包。

共 **27 处**登记副本，覆盖 **8 个法域或区域**、**8 类存储层**。

| 机构 | 法域 / 区域 | 类型 | 地址 |
|---|---|---|---|
| Zenodo (CERN / OpenAIRE) | EU / Switzerland | DOI-registered open repository | https://doi.org/10.5281/zenodo.24270266 |
| Zenodo (CERN) | EU / Switzerland | concept DOI (always resolves to latest version) | https://doi.org/10.5281/zenodo.24269665 |
| Figshare (Digital Science) | UK | DOI-registered open repository | https://doi.org/10.6084/m9.figshare.35018998.v1 |
| Open Science Framework (Center for Open Science) | US | open project storage with versioned files | https://osf.io/wubs2/ |
| GitHub Pages | US | static full-text site | https://kiloiam.github.io/labor-value-theory-preprint/ |
| GitHub | US | versioned git repository | https://github.com/kiloiam/labor-value-theory-preprint |
| GitHub Releases | US | immutable tagged release with binary assets | https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0 |
| WorkBuddy hosted site | CN | hosted reading page with 9 facsimile pages | https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/?sharecode=ZILGUJCJKG |
| Software Heritage (UNESCO / Inria) | FR / EU | permanent source-code archive with SWHID | https://archive.softwareheritage.org/ |
| Internet Archive Wayback Machine | US | web time-capsule snapshots (12 + new captures) | https://web.archive.org/web/20261116061932/https://kiloiam.github.io/labor-value-theory-preprint/ |
| OpenAIRE | EU | Europe-wide open scholarly index (already indexed) | https://api.openaire.eu/search/publications?doi=10.5281/zenodo.24270266 |
| DataCite | international | DOI metadata registry | https://commons.datacite.org/doi.org/10.5281/zenodo.24270266 |
| jsDelivr global CDN | multi-region | CDN edge copy | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf |
| raw.githubusercontent.com | US | raw file mirror | https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| raw.githack.com | multi-region | independent CDN mirror | https://raw.githack.com/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| gitcdn.link | multi-region | independent CDN mirror | https://gitcdn.link/cdn/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| Zenodo (CERN) — version 2 | EU / Switzerland | second DOI-registered deposit carrying the offline survival bundle | https://doi.org/10.5281/zenodo.24273568 |
| GitHub Gist | US | public gist with plain text, offline HTML, checksums and manifest | https://gist.github.com/kiloiam/d286d7f3b8ee3adf0e8f2ba0595f7ab7 |
| Software Heritage (UNESCO / Inria) | FR / EU | permanent source archive of the public gist (request 2654743) | https://archive.softwareheritage.org/ |
| GitHub Releases | US | immutable tagged release v2.0.0 with 18 assets | https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v2.0.0 |
| jsDelivr global CDN | multi-region | commit-pinned immutable PDF (never changes even if main moves) | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf |
| raw.githubusercontent.com | US | commit-pinned immutable raw file | https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf |
| raw.githack.com | multi-region | commit-pinned immutable CDN copy | https://raw.githack.com/kiloiam/labor-value-theory-preprint/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf |
| GitHub repository archive | US | commit-pinned immutable ZIP of the whole repository | https://github.com/kiloiam/labor-value-theory-preprint/archive/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69.zip |
| jsDelivr global CDN | multi-region | commit-pinned immutable plain-text full text | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/PAPER-PLAINTEXT.txt |
| jsDelivr global CDN | multi-region | commit-pinned immutable offline single-file HTML | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper-standalone.html |
| IndexNow (Bing / Yandex / Seznam / aggregator) | international | search-engine URL submission, 63 URLs accepted by all four endpoints | https://www.bing.com/indexnow |

## 三层可读性

| 层级 | 文件 | 所需软件 |
|---|---|---|
| 1 · 零依赖 | `PAPER-PLAINTEXT.txt` | 任意文本读取器（甚至打印在纸上） |
| 2 · 单文件 | `paper-standalone.html` | 任意浏览器，不需联网、不需外部资源 |
| 3 · 原排版 | `paper.pdf` | PDF 阅读器 |

## 校验

`CHECKSUMS.sha256` 给出每个核心文件的 SHA-256。恢复某副本后先比对哈希，
再以 `PRESERVATION-MANIFEST.json` 查其余副本地址。全文 CC BY 4.0，
重新托管、翻译、再发布均无需额外授权，保留署名 `Didgeridoo` 即可。

## 边界

- 数字系统无法承诺「文明灭亡后仍存在」；本表最大化的是**冗余度与可恢复性**，不是永恒性。
- 所有公开副本统一署名 `Didgeridoo`，不含真实姓名、通讯邮箱、QQ 号或 QQ 邮箱。
- Figshare 旧记录 `35018683` 的 v1 / v2 含早期署名，已提交官方下架工单，**不在本表内、请勿传播**。
- 以上均为网络预发布预印本，有 DOI、可引用，但未经同行评审，不等同期刊正式发表。


## 第四轮：去中心化留存层（2026-11-16）

以下不是「又一个网站副本」，而是**不依赖任何单一网站**的四种留存机制。

| 机制 | 标准 | 入口 | 状态 |
|---|---|---|---|
| BitTorrent + WebSeed + Magnet | BEP 17 / BEP 19 | https://kiloiam.github.io/labor-value-theory-preprint/torrents.html | 2 个 swarm，7 个 HTTP 永久种子源 |
| BagIt holey bag | RFC 8498 | https://kiloiam.github.io/labor-value-theory-preprint/bag/fetch.txt | 28 个文件 / 1711330 字节，仅凭标签文件即可重建 |
| IPFS CIDv1 | multiformats / raw codec | https://kiloiam.github.io/labor-value-theory-preprint/ipfs-manifest.json | 已计算 CID，**未代注册 pinning 服务** |
| Memento TimeMap | RFC 7089 | https://kiloiam.github.io/labor-value-theory-preprint/timemap.json | 40 个 Wayback 快照的机器可读索引 |
| RO-Crate | RO-Crate 1.1 | https://kiloiam.github.io/labor-value-theory-preprint/ro-crate-metadata.json | 逐文件 SHA-256 |

离线保存包已重建为 `55` 个条目、`1,557,043` 字节，SHA-256 `a4f3851521fe74eccacdedb7c6a8cc1af51ab5f7f7775b5c973e400daa763da9`，独立校验文件 `preservation-bundle.zip.sha256`（避免自引用）。
镜像实测：29 个端点中 28 个可达，明细见 `MIRROR-HEALTH.json`。

**边界**：torrent 需要有人做种或 WebSeed 在线；IPFS 网关需要节点提供 block；BagIt 依赖 `fetch.txt` 中的 URL 仍可访问；Memento 依赖 Internet Archive。它们提高的是冗余度与可重建性，不是「永恒」承诺。全文 CC BY 4.0，欢迎任何人复刻、做种与再托管。


## 第五轮：全球无门槛发布、长尾可发现性与署名澄清（2026-11-16）

- **署名性质更正**：作者确认 `Didgeridoo` 为真实英文姓名，非笔名；全站表述已中性化，
  viXra 的 real-name 要求已满足并解锁为可投平台。详见 `AUTHOR-NAME-CLARIFICATION.md`。
- 新增 10 个真实检索意图 × 中英双版长尾页、`llms-topics.txt`、`open-archives.html`、
  `OPEN-ARCHIVES.md`、`open-archive-kit/`（11 个预填文件，含 `viXra-form.md`）、
  `paper-vixra.pdf`、`citation-guide.html`、`search-console-kit.html`、`schema-enhanced.jsonld`。
- 站点地图 132 个 URL；IndexNow 132 个 URL × 4 端点；Telegraph 10 个语种摘要页上线；
  GitHub Release `v4.0.0`；Pages 实测 129/129 可达；SHA-256 180 项；脱敏扫描 PASS。
- 学术库实测：DataCite 与 OpenAIRE 已收录，OpenAlex / Semantic Scholar 尚未（自动收割有延迟）。
- 边界：viXra 提交仍需本人提供联系邮箱、勾选权属声明并点击提交（一经上线永久记录）；
  arXiv 需背书与机构认证，其余需账号/机构邮箱/同行评审；不承诺排名；
  WorkBuddy 线上站点未重新发布（需明确授权）。完整报告见 `ROUND5-REPORT.md`。

### Telegraph（第五轮）

- zh → https://telegra.ph/劳动价值论是历史性范畴当代价值危机-11-16
- en → https://telegra.ph/The-Labor-Theory-of-Value-as-a-Historical-Category-The-Contemporary-Crisis-of-Value-11-16
- ja → https://telegra.ph/労働価値論は歴史的範疇である現代における価値の危機-11-16
- es → https://telegra.ph/La-teoría-del-valor-trabajo-como-categoría-histórica-la-crisis-contemporánea-del-valor-11-16
- fr → https://telegra.ph/La-théorie-de-la-valeur-travail-comme-catégorie-historique--la-crise-contemporaine-de-la-valeur-11-16
- de → https://telegra.ph/Die-Arbeitswertlehre-als-historische-Kategorie-Die-gegenwärtige-Krise-des-Werts-11-16
- ru → https://telegra.ph/Trudovaya-teoriya-stoimosti-kak-istoricheskaya-kategoriya-sovremennyj-krizis-stoimosti-11-16
- pt → https://telegra.ph/A-teoria-do-valor-trabalho-como-categoria-histórica-a-crise-contemporânea-do-valor-11-16
- it → https://telegra.ph/La-teoria-del-valore-lavoro-come-categoria-storica-la-crisi-contemporanea-del-valore-11-16
- ko → https://telegra.ph/노동가치론은-역사적-범주이다-현대적-가치의-위기-11-16

以上页面仅含摘要与规范链接，不复制全文；署名为真实英文姓名 `Didgeridoo`。
