# 全球分发与长期保存台账
> 《劳动价值论是历史性范畴：当代价值危机》 · Didgeridoo · CC BY 4.0 · 2026-11-16
> 本文件只列出**干净、可安全传播**的公开副本。

## 一、可引用的正式记录

| 平台 | 标识 | 链接 | 状态 | 备注 |
|---|---|---|---|---|
| Zenodo（主 DOI） | `10.5281/zenodo.24270266` | https://doi.org/10.5281/zenodo.24270266 | 已发布 | CERN 托管，CC BY 4.0，PDF 可下载；作者 Didgeridoo |
| Figshare（干净记录） | `10.6084/m9.figshare.35018998.v1` | https://doi.org/10.6084/m9.figshare.35018998.v1 | 已发布 | CC BY 4.0，作者 Didgeridoo |
| Zenodo 概念 DOI | `10.5281/zenodo.24269665` | https://doi.org/10.5281/zenodo.24269665 | 有效 | 始终指向最新版本，适合长期引用 |
| OSF | `项目 wubs2` | https://osf.io/wubs2/ | public | 开放科学框架项目，含完整 PDF |
| GitHub Release | `v1.0.0` | https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0 | 已发布 | 版本化快照 |

## 二、全文入口与 CDN 副本

| 入口 | URL | 说明 |
|---|---|---|
| GitHub Pages 阅读页 | https://kiloiam.github.io/labor-value-theory-preprint/ | 全文、摘要、引用与分发清单入口 |
| 在线全文阅读（含 9 页影印） | https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/ | 逐页原稿影印 + 可检索正文 |
| jsDelivr 全球 CDN（PDF） | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf | CDN 边缘副本，实测 200 |
| raw.githubusercontent（PDF） | https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/main/paper.pdf | GitHub 原始文件副本，实测 200 |
| GitHub 仓储 | https://github.com/kiloiam/labor-value-theory-preprint | 全部源文件、元数据与历史 |
| GitHub Pages（Markdown 全文） | https://kiloiam.github.io/labor-value-theory-preprint/manuscript.md | 纯文本全文，便于索引 |

所有 PDF 均为同一去标识化文件（9 页，1,389,530 字节），`/Author` = Didgeridoo。

## 三、长期保存与学术索引

| 服务 | 类型 | 状态 | 核验说明 |
|---|---|---|---|
| Software Heritage | 永久源码/文档存档 | 已存档 | 请求 2654490：`save_task_status=succeeded`、`visit_status=full`（2026-11-16 06:18 UTC）；最新提交另发请求 2654599 重抓 |
| Internet Archive Wayback | 网页时间胶囊 | 已存档 12 处 | 阅读页、分发页、PDF、Markdown、DataCite XML、Zenodo、Figshare、OSF、GitHub、Release、CDN、在线阅读页，12/12 成功 |
| IndexNow | 搜索引擎即时收录 | 已受理 26 个 URL | 官方聚合 202、Bing 202、Yandex 202（success=true）、Seznam 200 |
| OpenAIRE | 欧盟开放学术索引 | 已收录 | 查询结果 total=1，标题与 DOI 均命中 |
| DataCite | DOI 注册元数据 | 已注册 | api.datacite.org/dois/10.5281/zenodo.24270266 返回 200 |
| Zenodo 社区 political economy | 主题社区收录 | 申请已提交 | 收录申请 21fad38a… 状态 submitted，等待社区处理；主 DOI 与记录不受影响 |
| OSF 项目 | 额外元数据副本 | 已上传 16 个 | DataCite / OAI-DC / MARCXML / METS / JSON-LD / Atom / RSS / 多语种摘要 / 分发台账等，全部 201 |
| GitHub Release v1.0.0 | 版本化资产 | 已挂载 16 个资产 | PDF 之外新增 15 个机器可读元数据文件 |
| GitHub 主题标签 | 站内与搜索引擎检索 | 已扩展至 11 个 | 新增 automation、historical-materialism、marxian-economics、open-access、zenodo、political-philosophy |
| OpenAlex | 开放学术图谱 | 尚未收录 | 由 DataCite 周期性抓取，通常需数周；当前 API 返回 404 |
| Semantic Scholar | 学术索引 | 尚未收录 | 自动抓取，当前 API 返回 404；不作人工提交承诺 |
| Google Scholar / CORE / BASE / Unpaywall | 自动聚合索引 | 等待自动抓取 | 页面已提供 Highwire、Dublin Core、EPrints、COinS、OAI-DC、Schema.org 与 sitemap，供抓取器识别 |

## 四、机器可读元数据

| 文件 | 标准 | 用途 |
|---|---|---|
| `datacite.xml` | DataCite Metadata Schema 4.5 | DOI 注册机构与仓储交换格式 |
| `oai_dc.xml` | OAI-PMH GetRecord + oai_dc | 供 OAI 收割器 / OpenAIRE / BASE 类聚合器 |
| `dublincore.xml` | Dublin Core / DCTERMS | 通用图书馆元数据 |
| `marcxml.xml` | MARC21 XML | 图书馆编目系统导入 |
| `mets.xml` | METS + MODS | 数字对象长期保存包装 |
| `schema.jsonld` | Schema.org ScholarlyArticle | 搜索引擎富结果 / 知识图谱 |
| `citation.enw` | EndNote | 参考文献管理软件导入 |
| `citation.rdf` | Zotero RDF / Dublin Core | Zotero / 语义网工具 |
| `citation.bib / citation.ris / citation.csl.json` | BibTeX / RIS / CSL-JSON | 主流写作与引用工具 |
| `CITATION.cff` | Citation File Format | GitHub 原生「Cite this repository」 |
| `citation-gb7714.txt / citation-apa.txt / citation-mla.txt / citation-chicago.txt` | GB/T 7714 / APA / MLA / Chicago | 中英文投稿格式 |
| `abstracts.json` | 7 语种检索摘要与关键词 | 跨语言检索；引用以中文原文与作者英文摘要为准 |
| `feed.xml / rss.xml` | Atom / RSS 2.0 | 订阅与聚合 |
| `sitemap.xml / robots.txt` | 站点地图 / 抓取许可 | 搜索引擎收录 |

页面头部提供 Highwire `citation_*`、Dublin Core、EPrints、COinS (Z39.88-2004) 与 Schema.org JSON-LD；
根目录提供 `sitemap.xml`、`robots.txt`、`feed.xml`、`rss.xml`、`59fd9bcf22086ae7947fd1777b9c56e0.txt`（IndexNow 密钥）。

## 五、建议引用

```
Didgeridoo. 劳动价值论是历史性范畴：当代价值危机[Z/OL]. Zenodo, 2026. https://doi.org/10.5281/zenodo.24270266.
```

```bibtex
@misc{didgeridoo2026ltv,
  author = {Didgeridoo},
  title  = {劳动价值论是历史性范畴：当代价值危机},
  year   = {2026},
  doi    = {10.5281/zenodo.24270266},
  howpublished = {Preprint, Zenodo},
  note   = {网络预发布，非期刊正式发表；CC BY 4.0}
}```

## 六、跨语言检索

`abstracts.json` 含中文、英文、日文、西班牙文、法文、德文、俄文简要摘要与关键词，仅供检索；
引用与学术表述以中文原文与作者英文摘要为准。

## 七、Internet Archive 永久快照（12 处）

| 原始地址 | 永久快照 |
|---|---|
| https://kiloiam.github.io/labor-value-theory-preprint/ | https://web.archive.org/web/20261116061932/https://kiloiam.github.io/labor-value-theory-preprint/ |
| https://kiloiam.github.io/labor-value-theory-preprint/distribution.html | https://web.archive.org/web/20261116063441/https://kiloiam.github.io/labor-value-theory-preprint/distribution.html |
| https://kiloiam.github.io/labor-value-theory-preprint/paper.pdf | https://web.archive.org/web/20261116063502/https://kiloiam.github.io/labor-value-theory-preprint/paper.pdf |
| https://kiloiam.github.io/labor-value-theory-preprint/manuscript.md | https://web.archive.org/web/20261116063617/https://kiloiam.github.io/labor-value-theory-preprint/manuscript.md |
| https://kiloiam.github.io/labor-value-theory-preprint/datacite.xml | https://web.archive.org/web/20261116063625/https://kiloiam.github.io/labor-value-theory-preprint/datacite.xml |
| https://zenodo.org/records/24270266 | https://web.archive.org/web/20261116063639/https://zenodo.org/records/24270266 |
| https://figshare.com/articles/preprint/_/35018998 | https://web.archive.org/web/20261116063709/https://figshare.com/articles/preprint/_/35018998 |
| https://osf.io/wubs2/ | https://web.archive.org/web/20261116063738/https://osf.io/wubs2/ |
| https://github.com/kiloiam/labor-value-theory-preprint | https://web.archive.org/web/20261116063802/https://github.com/kiloiam/labor-value-theory-preprint |
| https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0 | https://web.archive.org/web/20261116063826/https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0 |
| https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf | https://web.archive.org/web/20261116063848/https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf |
| https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/ | https://web.archive.org/web/20261116063948/https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/ |

## 八、注意

- **请勿传播** Figshare 旧记录 `35018683` 的 v1/v2 历史版本链接，其中仍含早期署名；官方下架工单已提交，等待处理。
- 以上均为**网络预发布预印本**，未经同行评审，不等同于期刊正式发表，不构成成果认定依据。
- 自动抓取型索引（OpenAlex、Semantic Scholar、Google Scholar、CORE、BASE、Unpaywall）有正常时滞，不作人工收录承诺。
- 全文 CC BY 4.0，署名须保留署名 Didgeridoo。


---

## 八、第三轮新增：跨机构冗余与 10 语种检索入口

| 类别 | 新增 |
|---|---|
| 第 4 个 DOI | Zenodo `10.5281/zenodo.24273568`（永久保存包版本，作者 Didgeridoo，CC BY 4.0） |
| 新机构 / 新法域 | 公开 GitHub Gist + Software Heritage 独立 gist 存档（请求 `2654743` succeeded/full） |
| 新不可变快照 | GitHub Release `v2.0.0`（18 个资产）；6 个 commit-SHA 固定 CDN 永久链接 |
| 新网页时间胶囊 | Wayback 第三轮 29 处，累计 40 处 |
| 新副本登记 | 共 27 处，覆盖 8 个法域或区域、8 类存储层，见 `forever.html` / `MIRRORS.md` / `PRESERVATION-MANIFEST.json` |
| 新离线资产 | `PAPER-PLAINTEXT.txt`、`paper-standalone.html`、`FOREVER-README.txt`、`CHECKSUMS.sha256`、`preservation-bundle.zip` |
| 新检索资产 | 10 语种落地页、互指 hreflang、`@graph` JSON-LD、`llms.txt`、`opensearch.xml`、`search.html`、63 URL sitemap |
| 搜索引擎 | IndexNow 四端点提交 63 个 URL，全部 `200` |

可安全传播的新入口：

- 冗余地图：https://kiloiam.github.io/labor-value-theory-preprint/forever.html
- 10 语种入口：https://kiloiam.github.io/labor-value-theory-preprint/en.html（及 ja / es / fr / de / ru / pt / it / ko）
- 零依赖纯文本：https://kiloiam.github.io/labor-value-theory-preprint/PAPER-PLAINTEXT.txt
- 单文件离线 HTML：https://kiloiam.github.io/labor-value-theory-preprint/paper-standalone.html
- Zenodo 永久包 DOI：https://doi.org/10.5281/zenodo.24273568
- 公开 Gist：https://gist.github.com/kiloiam/d286d7f3b8ee3adf0e8f2ba0595f7ab7
- Release v2.0.0：https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v2.0.0
- 固定 SHA 永久 PDF：https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@49a0fc78f5953c47add0a39e78c4b6bf0dac9c69/paper.pdf

**对外仍只分享干净记录**：Figshare `10.6084/m9.figshare.35018998.v1`、
Zenodo `10.5281/zenodo.24270266`（或新版本 `24273568`）、OSF https://osf.io/wubs2/ 。
Figshare 旧记录 `35018683` 的 v1 / v2 仍含早期署名，下架工单已提交、等待官方执行，请勿传播。


## 第五轮：全球无门槛发布、长尾可发现性与署名澄清（2026-11-16）

- **署名性质更正**：作者确认 `Didgeridoo` 为真实英文姓名，非笔名；全站表述已中性化，
  viXra 的 real-name 要求已满足并解锁为可投平台。详见 `AUTHOR-NAME-CLARIFICATION.md`。
- 新增 10 个真实检索意图 × 中英双版长尾页、`llms-topics.txt`、`open-archives.html`、
  `OPEN-ARCHIVES.md`、`open-archive-kit/`（14 个预填文件，含 viXra 一键预填三件套）、
  `paper-vixra.pdf`、`citation-guide.html`、`search-console-kit.html`、`schema-enhanced.jsonld`。
- 站点地图 132 个 URL；IndexNow 132 个 URL × 4 端点；Telegraph 10 个语种摘要页上线；
  GitHub Release `v4.0.0`；Pages 实测 132/132 可达；SHA-256 全量校验通过；脱敏扫描 PASS。
- 学术库实测：DataCite 与 OpenAIRE 已收录，OpenAlex / Semantic Scholar 尚未（自动收割有延迟）。
- viXra：**已由作者本人提交，待管理员处理**（回执两天内无回复即视为未接受、`Do not resubmit`）；一经接受则永久记录；
  arXiv 需背书与机构认证，其余需账号/机构邮箱/同行评审；不承诺排名；
  WorkBuddy 线上站点已按作者选择重新发布，`verified=true`，分享链接不变；可在「设置 — 数据管理 — 应用」中管理。完整报告见 `ROUND5-REPORT.md`。

## 第六轮：继续全球开放发布与 SEO 深化（2026-11-16）

- 新增 10 个与第五轮不重叠的真实检索意图 × 中英双版 = **20 页**；重建第五轮 20 页使 40 页互链完整；
  `llms-topics-r6.txt`、`schema-round6.jsonld`、站点地图 **132 → 158 URL**。
- 外部实测回执：Zenodo 第三版本 DOI `10.5281/zenodo.24279668`（28 资产）、Release `v5.0.0`（34 资产）、OSF 30/30、Gist 7/7、
  Telegraph 2 个索引页、IndexNow 158 URL × 4 端点全 200、WebSub 204、SWH 请求 2655381（scheduled）。
- 如实保留的失败项：Figshare `versions` 端点 404 未新建版本；Wayback 本轮被 `429`/`523` 限流，
  25 个目标仅 1 个 CDX 确认、慢速重试 8 个 0 确认；OpenAlex / Semantic Scholar / Crossref 仍 404。
- 边界不变：不承诺排名、不刷量买链、不代注册账号与权属声明；viXra 仍待审核、其余 B/C 档需作者本人。
- 完整报告 `ROUND6-REPORT.md`；回执 `EXTERNAL-R6.json` / `AGGREGATORS-R6.json` / `VERIFY-R6.json`。

## 第七轮：世界资料站与数据库备份 · 白帽搜索优化（2026-11-16）

- **新增独立资料托管副本（已回抓验证）**：paste.rs、dpaste.com、pomf2.lain.la（全文层），
  rentry.co、uguu.se（指针层）。另有 gofile.io、tmpfiles.org 仅下载页，内容未独立验证。
- **数据库级**：Zenodo 第四版本 `10.5281/zenodo.24280895`（27 资产）、
  Figshare 第二版本 `10.6084/m9.figshare.35018998.v2`（3 文件）、
  第二个独立仓库 https://github.com/kiloiam/labor-value-theory-archive （Release v1.0.0）、
  主仓库 Release `v6.0.0`（27 资产）、OSF 26/26、Gist 7/7、
  Software Heritage 两个仓库均 `succeeded / full`。
- **SEO 实质修复**：主站 canonical 由跨域名 `?sharecode=` 改为自引用绝对 URL；
  sitemap 移除重复 `/index.html` 与两个工单页；工单页 `noindex`；Scholar `citation_*` 全套补齐；
  全站 65 页审计 0 问题；新增 14 个信任／术语／站长页；主 sitemap 176 URL；
  IndexNow 176 × 4 端点全 200（在 Pages 构建确认后重提）。
- **如实保留**：12 个托管端点失败、1 个恶意域名被安全中心拦截且未重试、
  IPFS/Arweave 无匿名持久写入、Wayback 限流、OpenAlex/S2/Crossref 仍 404。
- 完整报告 `ROUND7-REPORT.md`；公开副本清单 `HOSTS-R7.json`；复验 `VERIFY-R7.json`。
