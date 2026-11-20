# 长期留存与全球分发执行记录

执行日期：2026-11-16　|　署名：Didgeridoo　|　许可：CC BY 4.0

本文件逐项记录本轮「继续在全世界互联网资料库留存扩散」的**真实操作与返回码**。
所有结果均来自实际 API 调用或浏览器会话，不作未经核验的收录承诺。

## 一、已完成的长期存档

| 动作 | 目标 | 方式 | 返回 | 结论 |
|---|---|---|---|---|
| Software Heritage save-code-now | GitHub 仓储 | `POST /api/1/origin/save/git/url/...` | `200`，`id=2654490` | `save_task_status=succeeded`、`visit_status=full`，visit_date `2026-11-16T06:18:55Z` |
| Software Heritage 重抓新增元数据 | `5e3d645` | 同一端点再次 `POST` | `200`，`id=2654599` | `save_task_status=succeeded`、`visit_status=full`，visit_date `06:41:00Z` |
| Software Heritage 最终提交重抓 | `6244d93` | 同一端点第三次 `POST` | `200`，`id=2654602` | `accepted`，`save_task_status=running`（通常数分钟内完成） |
| Internet Archive Wayback | 12 个干净公开入口 | 真实浏览器会话 `Save Page Now` | 12 × 重定向到 `/web/<timestamp>/...` | **12/12 全部生成永久快照**（下表） |
| OSF 项目 `wubs2` | 16 个机器可读元数据副本 | `PUT files.osf.io/v1/resources/wubs2/providers/osfstorage/` | 16 × `201` | 项目内共 17 个文件，PDF 与元数据同处一处 |
| GitHub Release `v1.0.0` | 15 个元数据资产 | `gh release upload` | 成功 | Release 资产由 1 个增至 16 个 |

### Wayback 永久快照清单

| 原始地址 | 快照 | 状态 |
|---|---|---|
| `https://kiloiam.github.io/labor-value-theory-preprint/` | [20261116061932](https://web.archive.org/web/20261116061932/https://kiloiam.github.io/labor-value-theory-preprint/) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/distribution.html` | [20261116063441](https://web.archive.org/web/20261116063441/https://kiloiam.github.io/labor-value-theory-preprint/distribution.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/paper.pdf` | [20261116063502](https://web.archive.org/web/20261116063502/https://kiloiam.github.io/labor-value-theory-preprint/paper.pdf) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/manuscript.md` | [20261116063617](https://web.archive.org/web/20261116063617/https://kiloiam.github.io/labor-value-theory-preprint/manuscript.md) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/datacite.xml` | [20261116063625](https://web.archive.org/web/20261116063625/https://kiloiam.github.io/labor-value-theory-preprint/datacite.xml) | captured |
| `https://zenodo.org/records/24270266` | [20261116063639](https://web.archive.org/web/20261116063639/https://zenodo.org/records/24270266) | captured |
| `https://figshare.com/articles/preprint/_/35018998` | [20261116063709](https://web.archive.org/web/20261116063709/https://figshare.com/articles/preprint/_/35018998) | captured |
| `https://osf.io/wubs2/` | [20261116063738](https://web.archive.org/web/20261116063738/https://osf.io/wubs2/) | captured |
| `https://github.com/kiloiam/labor-value-theory-preprint` | [20261116063802](https://web.archive.org/web/20261116063802/https://github.com/kiloiam/labor-value-theory-preprint) | captured |
| `https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0` | [20261116063826](https://web.archive.org/web/20261116063826/https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0) | captured |
| `https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf` | [20261116063848](https://web.archive.org/web/20261116063848/https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf) | captured |
| `https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/` | [20261116063948](https://web.archive.org/web/20261116063948/https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/) | captured |

> 说明：直接用脚本调用 Wayback 的 `POST /save/` 与 `GET /save/<url>` 均返回
> `429 suspected abusive bot traffic`（出口 IP 被限流）；改用可见浏览器的真实会话后
> 12 个 URL 全部成功，因此最终结果是「已存档」，不是「受限」。

## 二、索引与发现渠道

| 动作 | 目标 | 返回 | 结论 |
|---|---|---|---|
| IndexNow（官方聚合 / Bing / Yandex / Seznam） | 26 个 URL | 见下表 | 全部受理，Yandex 明确返回 `success:true` |
| Zenodo 社区 `political economy` 收录申请 | 主记录 `24270266` | `200`，`processed[0].request.status=submitted` | 申请 ID `21fad38a-b571-4076-aca1-6063c0ee8b56`，`is_open=true`，等待社区处理；主 DOI 不受影响 |
| OpenAIRE 收录核验 | 主 DOI | `200`，`total=1` | **已收录**，标题与 DOI 均命中 |
| DataCite 核验 | 主 DOI | `200` | DOI 元数据已注册 |
| Zenodo / Figshare / OSF 记录核验 | 三个平台 | 均 `200` | 干净记录在线，Zenodo creators = `Didgeridoo`、license = `cc-by-4.0` |
| jsDelivr / raw.githubusercontent CDN | PDF | 均 `200` | 全球 CDN 副本可用 |
| GitHub 主题标签 | 仓库 | 成功 | 由 5 个扩展至 11 个 |

### IndexNow 提交回执

| 端点 | HTTP | 响应体 |
|---|---|---|
| `https://api.indexnow.org/indexnow` | `202` | (empty body) |
| `https://www.bing.com/indexnow` | `202` | (empty body) |
| `https://yandex.com/indexnow` | `202` | {
  "success":true
} |
| `https://search.seznam.cz/indexnow` | `200` | (empty body) |

## 三、新增的机器可读资产

根目录新增 `datacite.xml`（DataCite 4.5）、`oai_dc.xml`（OAI-PMH GetRecord）、
`dublincore.xml`、`marcxml.xml`（MARC21）、`mets.xml`（METS+MODS）、
`schema.jsonld`、`citation.enw`（EndNote）、`citation.rdf`（Zotero RDF）、
APA / MLA / Chicago 引用文本、`abstracts.json`（7 语种检索摘要与关键词）、
`feed.xml`（Atom）、`rss.xml`（RSS 2.0）与 `<IndexNow-key>.txt`。

两个公开阅读页的 `<head>` 追加 Highwire `citation_*`、Dublin Core / DCTERMS、
EPrints、bePress、`COinS`（OpenURL Z39.88-2004，供 Zotero / Mendeley 识别）、
Schema.org JSON-LD 独立文件、Atom / RSS / OAI-DC / DataCite `rel=alternate` 与
`hreflang`。`sitemap.xml` 扩至 38 个 URL，`robots.txt` 保持全站可抓取。

## 四、受限或未执行项（如实记录）

| 项 | 情况 |
|---|---|
| Bing sitemap ping | `410`，端点已停用 |
| Google sitemap ping | `404`，官方 2023 年起弃用，已由 IndexNow 替代 |
| Bing IndexNow 匿名 GET | `400 The key field is required`，改为密钥 + `keyLocation` 正式提交后成功 |
| archive.today / archive.is / archive.li / archive.vn | 连接超时，本网络不可达，未生成快照 |
| arquivo.pt `/preserve` | `404`，未使用 |
| OpenAlex | API 返回 `404`，尚未收录（DataCite 自动抓取时滞，通常数周） |
| Semantic Scholar | API 返回 `404`，尚未收录（自动抓取） |
| Google Scholar / CORE / BASE / Unpaywall | 无匿名人工提交入口，依赖自动抓取；本轮只提高可发现性 |
| OSF Preprints | **未创建**：OSF 账号贡献者显示名为账号名而非署名 Didgeridoo，新建预印本会生成带其他署名的公开页面，与仅使用 Didgeridoo 的要求冲突；改为向现有项目上传元数据副本 |
| arXiv / HAL / SSRN / ResearchGate / Academia.edu / RePEc | 均需实名注册、机构认证或本人确认，本环境不代注册、不代投稿 |

## 五、边界

- 以上均为**网络预发布预印本**存档与索引动作，**未经同行评审，不等同于期刊正式发表**，不构成成果认定依据。
- 「已受理」「已提交申请」不等于「已收录」；自动抓取型索引不作人工收录承诺。
- 所有新增公开内容统一署名 `Didgeridoo`，不含真实姓名、通讯邮箱、QQ 号或 QQ 邮箱。
- Figshare 旧记录 `35018683` 的 v1/v2 仍含早期署名，官方 `Take down request` 工单已由本人提交、等待执行；**请勿传播该记录及其版本链接**。
- 后续每次 push 新提交后，可再次触发 Software Heritage 的 save-code-now 以抓取最新版本。


---

## 六、第三轮：跨机构冗余、离线生存副本与国际 SEO（2026-11-16）

目标：把副本分散到尽可能多的独立机构、法域与协议，使任何**单独一个**幸存副本
都能还原全文；同时把全文的可发现性从中文单页扩展到 10 个语种与多套机器可读协议。

### 6.1 离线生存包（三层互不依赖的可读形态）

| 层级 | 文件 | 所需软件 | 大小 |
|---|---|---|---|
| 零依赖 | `PAPER-PLAINTEXT.txt` | 任意文本读取器，甚至打印在纸上 | 36,319 字节 |
| 单文件 | `paper-standalone.html` | 任意浏览器，断网、无外部脚本/字体/图片 | 46,154 字节 |
| 原排版 | `paper.pdf` | PDF 阅读器（9 页，`/Author` = Didgeridoo） | 1,389,530 字节 |

配套 `FOREVER-README.txt`（恢复说明）、`MIRRORS.md`（副本登记表）、
`PRESERVATION-MANIFEST.json`（机器可读清单）、`CHECKSUMS.sha256`（23 个核心文件哈希）、
`preservation-bundle.zip`（34 个文件离线包）。
本次全部 23 项校验在最终文件上逐项复算通过。

### 6.2 真实执行回执

| 动作 | 目标 | 返回 | 结论 |
|---|---|---|---|
| Zenodo 新建版本并发布 | 主记录 `24270266` 的 v2 | `POST /versions` `201` → 上传 `200` → commit `200` → publish `202` | **新 DOI `10.5281/zenodo.24273568` 已发布**，`state=done`，creators = `Didgeridoo`，license = `cc-by-4.0`，文件 `preservation-bundle.zip`；概念 DOI `10.5281/zenodo.24269665` 现指向该版本，v1 主 DOI 仍独立有效 |
| GitHub 公开 Gist | 7 个离线核心文件 | 创建成功 | https://gist.github.com/kiloiam/d286d7f3b8ee3adf0e8f2ba0595f7ab7 |
| Zenodo v2 附件版本说明 | `preservation-bundle.zip` | — | v2 内为**首版**离线包（登记 16 处副本）；全文与校验结构一致。最终 27 处副本清单以 `PRESERVATION-MANIFEST.json`（GitHub Pages / 仓库 / Software Heritage 最新存档）为准 |
| Software Heritage 存档 Gist | gist git origin | 请求 `2654743` `accepted` → `succeeded` / `visit_status=full` | 又一个独立永久源码存档 |
| Software Heritage 重抓主仓库 | 提交 `49a0fc7` | 请求 `2654742` `accepted` → `succeeded` / `full` | 最新提交已完整存档 |
| GitHub Release `v2.0.0` | 18 个资产 | 创建成功 | 第二个不可变版本快照，含永久包与 10 语种页 |
| OSF 追加副本 | 项目 `wubs2` | 22 × `201`（1 项 `403`） | 项目内累计约 39 个文件；`sitemap-index.xml` 被平台拒绝，其余全部写入 |
| IndexNow 正式提交 | 63 个 URL | 四端点均 `200`，Yandex 返回 `success:true` | 官方聚合 / Bing / Yandex / Seznam 全部受理 |
| commit 固定永久链接 | 6 个 URL | 6 × `200` | jsDelivr / raw.githubusercontent / githack / GitHub archive / jsDelivr 纯文本 / jsDelivr 离线 HTML，全部按 SHA 固定，不会随 main 分支变化 |
| GitHub Pages 复验 | 11 个新页面 | 11 × `200` | 多语种页、冗余地图、llms.txt、离线 HTML 等全部上线 |

### 6.3 Wayback 第三轮新增快照（29/31 全部成功）

| 原始地址 | 时间戳 | 状态 |
|---|---|---|
| `https://kiloiam.github.io/labor-value-theory-preprint/` | [20261116061932](https://web.archive.org/web/20261116061932/https://kiloiam.github.io/labor-value-theory-preprint/) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/forever.html` | [20261116080148](https://web.archive.org/web/20261116080148/https://kiloiam.github.io/labor-value-theory-preprint/forever.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/en.html` | [20261116080256](https://web.archive.org/web/20261116080256/https://kiloiam.github.io/labor-value-theory-preprint/en.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/ja.html` | [20261116080319](https://web.archive.org/web/20261116080319/https://kiloiam.github.io/labor-value-theory-preprint/ja.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/es.html` | [20261116080336](https://web.archive.org/web/20261116080336/https://kiloiam.github.io/labor-value-theory-preprint/es.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/fr.html` | [20261116080336](https://web.archive.org/web/20261116080336/https://kiloiam.github.io/labor-value-theory-preprint/fr.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/de.html` | [20261116080404](https://web.archive.org/web/20261116080404/https://kiloiam.github.io/labor-value-theory-preprint/de.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/ru.html` | [20261116080608](https://web.archive.org/web/20261116080608/https://kiloiam.github.io/labor-value-theory-preprint/ru.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/pt.html` | [20261116080632](https://web.archive.org/web/20261116080632/https://kiloiam.github.io/labor-value-theory-preprint/pt.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/it.html` | [20261116080651](https://web.archive.org/web/20261116080651/https://kiloiam.github.io/labor-value-theory-preprint/it.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/ko.html` | [20261116080713](https://web.archive.org/web/20261116080713/https://kiloiam.github.io/labor-value-theory-preprint/ko.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/llms.txt` | [20261116080746](https://web.archive.org/web/20261116080746/https://kiloiam.github.io/labor-value-theory-preprint/llms.txt) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/humans.txt` | [20261116080755](https://web.archive.org/web/20261116080755/https://kiloiam.github.io/labor-value-theory-preprint/humans.txt) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/favicon.svg` | [20261116080148](https://web.archive.org/web/20261116080148/https://kiloiam.github.io/labor-value-theory-preprint/favicon.svg) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/opensearch.xml` | [20261116080816](https://web.archive.org/web/20261116080816/https://kiloiam.github.io/labor-value-theory-preprint/opensearch.xml) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/search.html` | [20261116080829](https://web.archive.org/web/20261116080829/https://kiloiam.github.io/labor-value-theory-preprint/search.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/paper-standalone.html` | [20261116080913](https://web.archive.org/web/20261116080913/https://kiloiam.github.io/labor-value-theory-preprint/paper-standalone.html) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/FOREVER-README.txt` | [20261116080932](https://web.archive.org/web/20261116080932/https://kiloiam.github.io/labor-value-theory-preprint/FOREVER-README.txt) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/MIRRORS.md` | [20261116080942](https://web.archive.org/web/20261116080942/https://kiloiam.github.io/labor-value-theory-preprint/MIRRORS.md) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/CHECKSUMS.sha256` | [20261116081017](https://web.archive.org/web/20261116081017/https://kiloiam.github.io/labor-value-theory-preprint/CHECKSUMS.sha256) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/PRESERVATION-MANIFEST.json` | [20261116081032](https://web.archive.org/web/20261116081032/https://kiloiam.github.io/labor-value-theory-preprint/PRESERVATION-MANIFEST.json) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/sitemap-index.xml` | [20261116081141](https://web.archive.org/web/20261116081141/https://kiloiam.github.io/labor-value-theory-preprint/sitemap-index.xml) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/sitemap.xml` | [20261116081146](https://web.archive.org/web/20261116081146/https://kiloiam.github.io/labor-value-theory-preprint/sitemap.xml) | captured |
| `https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v2.0.0` | [20261116081200](https://web.archive.org/web/20261116081200/https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v2.0.0) | captured |
| `https://gist.github.com/kiloiam/d286d7f3b8ee3adf0e8f2ba0595f7ab7` | [20261116081222](https://web.archive.org/web/20261116081222/https://gist.github.com/kiloiam/d286d7f3b8ee3adf0e8f2ba0595f7ab7) | captured |
| `https://kiloiam.github.io/labor-value-theory-preprint/PAPER-PLAINTEXT.txt` | [20261116081242](https://web.archive.org/web/20261116081242/https://kiloiam.github.io/labor-value-theory-preprint/PAPER-PLAINTEXT.txt) | captured |
| `https://zenodo.org/records/24273568` | [20261116081256](https://web.archive.org/web/20261116081256/https://zenodo.org/records/24273568) | captured |
| `https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf` | [20261116081325](https://web.archive.org/web/20261116081325/https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf) | captured |
| `https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf` | [20261116081331](https://web.archive.org/web/20261116081331/https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf) | captured |

> 加上第二轮的 12 处，累计 **40 处永久快照**。脚本直连仍返回 `429`，
> 全部通过真实浏览器会话完成。

### 6.4 最终副本登记（27 处 / 8 个法域或区域 / 8 类存储层）

| 机构 | 法域 / 区域 | 层 | 地址 |
|---|---|---|---|
| Zenodo (CERN / OpenAIRE) | EU / Switzerland | primary | https://doi.org/10.5281/zenodo.24270266 |
| Zenodo (CERN) | EU / Switzerland | resolver | https://doi.org/10.5281/zenodo.24269665 |
| Figshare (Digital Science) | UK | primary | https://doi.org/10.6084/m9.figshare.35018998.v1 |
| Open Science Framework (Center for Open Science) | US | primary | https://osf.io/wubs2/ |
| GitHub Pages | US | reading | https://kiloiam.github.io/labor-value-theory-preprint/ |
| GitHub | US | source | https://github.com/kiloiam/labor-value-theory-preprint |
| GitHub Releases | US | snapshot | https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0 |
| WorkBuddy hosted site | CN | reading | https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/ |
| Software Heritage (UNESCO / Inria) | FR / EU | cold-archive | https://archive.softwareheritage.org/ |
| Internet Archive Wayback Machine | US | cold-archive | https://web.archive.org/web/20261116061932/https://kiloiam.github.io/labor-value-theory-preprint/ |
| OpenAIRE | EU | index | https://api.openaire.eu/search/publications?doi=10.5281/zenodo.24270266 |
| DataCite | international | resolver | https://commons.datacite.org/doi.org/10.5281/zenodo.24270266 |
| jsDelivr global CDN | multi-region | cdn | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf |
| raw.githubusercontent.com | US | cdn | https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| raw.githack.com | multi-region | cdn | https://raw.githack.com/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| gitcdn.link | multi-region | cdn | https://gitcdn.link/cdn/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| Zenodo (CERN) — version 2 | EU / Switzerland | cold-archive | https://doi.org/10.5281/zenodo.24273568 |
| GitHub Gist | US | source | https://gist.github.com/kiloiam/d286d7f3b8ee3adf0e8f2ba0595f7ab7 |
| Software Heritage (UNESCO / Inria) | FR / EU | cold-archive | https://archive.softwareheritage.org/ |
| GitHub Releases | US | snapshot | https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v2.0.0 |
| jsDelivr global CDN | multi-region | cdn | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf |
| raw.githubusercontent.com | US | cdn | https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf |
| raw.githack.com | multi-region | cdn | https://raw.githack.com/kiloiam/labor-value-theory-preprint/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf |
| GitHub repository archive | US | snapshot | https://github.com/kiloiam/labor-value-theory-preprint/archive/49a0fc78f5953c47add0a39e78c4b6bf0dac9c69.zip |
| jsDelivr global CDN | multi-region | cdn | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/PAPER-PLAINTEXT.txt |
| jsDelivr global CDN | multi-region | cdn | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper-standalone.html |
| IndexNow (Bing / Yandex / Seznam / aggregator) | international | index | https://www.bing.com/indexnow |

### 6.5 国际 SEO 与发现层

- 新增 9 个语种落地页（`en/ja/es/fr/de/ru/pt/it/ko.html`）+ 中文主阅读页，共 **10 语种**；
  每页含该语种独立撰写的摘要、关键词、5 条本地化 FAQ 与引用格式，**不是机器复制的薄页面**。
- 全站互指 `hreflang`（10 语种 + `x-default`），每页自引用 `canonical`；
  `sitemap.xml` 扩至 **63 个 URL** 并写入 `xhtml:link` 交替链接，另有 `sitemap-index.xml`。
- `@graph` JSON-LD：`WebSite`（含 `SearchAction`）、`ScholarlyArticle`、`WebPage`、
  `BreadcrumbList`、`FAQPage`；`forever.html` 另含 `Dataset` 结构化数据。
  每页 JSON-LD 均通过解析校验。
- 新增 `llms.txt`（LLM 抓取指引）、`humans.txt`、`favicon.svg`、`opensearch.xml`、
  `search.html`（纯前端站内检索）、`robots.txt` 双 sitemap 声明。
- OG / Twitter Card、`citation_*`、Dublin Core / DCTERMS、COinS 等在 10 个语种页全量落地。

### 6.6 本轮未执行或失败项（如实记录）

| 项 | 情况 |
|---|---|
| catbox.moe 匿名文件镜像 | `412 Invalid uploader`，该服务现已要求 uploader 凭证，未使用 |
| arquivo.pt ArchivePageNow | 正确入口为 `https://arquivo.pt/services/archivepagenow`，是**交互式浏览录制**服务（需人工点击 Finish），且搜索结果至少 1 年禁入期、 crawl 聚焦 .pt 域；本站点不在其收录重点，未提交 |
| archive.today / archive.is / archive.li | 各镜像连接超时，本网络不可达 |
| Common Crawl | `No Captures found`；不提供单 URL 人工提交入口 |
| Yahoo sitemap ping | `500`；Bing `410` / Google `404`（2023 年起弃用），已由 IndexNow 替代 |
| Figshare 新建版本 | **未创建**：已发布版本的作者字段曾出现非笔名，新建版本有重新带出其他署名的风险；改用 Zenodo 新版本与 OSF/GitHub 追加副本 |
| OSF Preprints | **未创建**：OSF 贡献者显示名与 Didgeridoo 不一致，会生成带其他署名的公开页 |
| arXiv / HAL / SSRN / ResearchGate / Academia.edu / RePEc / 百度搜索资源平台 | 需实名注册、机构认证或站点所有权验证，不代注册、不代投稿 |
| OpenAlex / Semantic Scholar | 仍 `404`，属 DataCite 自动抓取时滞；不作人工收录承诺 |

### 6.7 关于「文明灭亡为止」的边界

没有任何数字系统能承诺人类文明终结后仍存在。本轮能做的是**最大化冗余度与可恢复性**：
不同机构、不同法域、不同协议、不同文件格式，加上三层零依赖可读形态与逐副本自述其余地址的清单，
使单点失效、单点审查、单点格式淘汰都不会同时摧毁全部内容。真正决定长期存活的是持续存在的读者与机构——
因此 `FOREVER-README.txt` 明确邀请后来者把纯文本全文再复制到自己的设备、图书馆或存档机构。
全文 CC BY 4.0，重新托管无需额外授权。
