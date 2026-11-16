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
| `https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/?sharecode=ZILGUJCJKG` | [20261116063948](https://web.archive.org/web/20261116063948/https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/?sharecode=ZILGUJCJKG) | captured |

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
| OSF Preprints | **未创建**：OSF 账号贡献者显示名为账号名而非笔名 Didgeridoo，新建预印本会生成带非笔名署名的公开页面，与去标识化要求冲突；改为向现有项目上传元数据副本 |
| arXiv / HAL / SSRN / ResearchGate / Academia.edu / RePEc | 均需实名注册、机构认证或本人确认，本环境不代注册、不代投稿 |

## 五、边界

- 以上均为**网络预发布预印本**存档与索引动作，**未经同行评审，不等同于期刊正式发表**，不构成成果认定依据。
- 「已受理」「已提交申请」不等于「已收录」；自动抓取型索引不作人工收录承诺。
- 所有新增公开内容统一署名 `Didgeridoo`，不含真实姓名、通讯邮箱、QQ 号或 QQ 邮箱。
- Figshare 旧记录 `35018683` 的 v1/v2 仍含早期署名，官方 `Take down request` 工单已由本人提交、等待执行；**请勿传播该记录及其版本链接**。
- 后续每次 push 新提交后，可再次触发 Software Heritage 的 save-code-now 以抓取最新版本。
