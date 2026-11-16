# 第七轮：世界资料站与数据库备份 · 白帽搜索优化

日期：2026-11-16　|　规范链接：https://kiloiam.github.io/labor-value-theory-preprint/　|　许可：CC BY 4.0

> **状态声明**：本文是有 DOI、可引用的**开放预印本**，**未经同行评审**，**不等同期刊正式发表**。
> 本轮不承诺任何具体搜索排名，不购买外链、不刷点击、不建站群、不堆砌关键词、不伪装账号。

## 一、本轮目标

按作者要求「还需要更多的世界备份和真正可以提高搜索排名的方法」，并在补充要求中明确为
「世界各个资料网站和数据库的备份」，本轮分两条线执行：

1. **真实新增独立副本**：把去标识化后的公开全文包写入多个独立法域的资料托管站，
   并在 Zenodo / Figshare / OSF / GitHub / Software Heritage 上新增不可变版本或独立仓库。
2. **真正影响排名的合规动作**：修复会实质抑制排名的技术缺陷、补齐作者／状态／版本等
   信任信号、完成搜索引擎索引提交，并给出需要本人账号的站长验证入口。

## 二、真实新增的独立备份

### 2.1 公开存档包（可独立验证）

先生成 `archives/ARCHIVE-BUNDLE-R7.txt`（37,349 字节）：含中英题名、署名、
CC BY 4.0、概念／版本 DOI、规范链接、12 个存档入口、PDF SHA-256，以及
从去标识化主 PDF 提取的 13,864 字全文；配套 `archives/ARCHIVE-MANIFEST-R7.json`。
包内无邮箱、无 QQ 标识、无私人联系方式、无早期 Figshare 记录链接。

### 2.2 独立资料托管站（逐个回抓验证）

| 站点 | 层级 | URL | 回抓 HTTP |
|---|---|---|---|
| paste.rs | full-text | https://paste.rs/yNhEo | 200 |
| dpaste.com | full-text | https://dpaste.com/ABNZB3JY7 | 200 |
| rentry.co | pointer | https://rentry.co/ltv-r7-a75b94dc | 200 |
| pomf2.lain.la | full-text | https://pomf2.lain.la/f/noq3t2xn.txt | 200 |
| uguu.se | pointer | https://n.uguu.se/KNClfThekCBb.txt | 200 |

「全文层」指回抓内容含全文标记且超过 12,000 字符；「指针层」指含规范链接、
DOI 与校验和的精简指针副本。匿名托管站是**低成本跨法域冗余层**，不承诺长期留存，
权威版本始终是规范站点与带 DOI 的不可变存档。

### 2.3 仅上传回执、内容未独立验证

| 站点 | 下载页 |
|---|---|
| gofile.io | https://gofile.io/d/H7HPxcaG |
| tmpfiles.org | https://tmpfiles.org/dl/w5AjytrPsXcx/archive-pointer-r7.txt |

这两处返回的是下载页，直链 API 需要 token（实测 401），因此**不把文件内容算作已验证副本**，
如实单列。

### 2.4 数据库级不可变版本与独立仓库

| 通道 | 结果 | 回执 |
|---|---|---|
| **Zenodo 第四版本** | `10.5281/zenodo.24280895`，27/27 资产，publish 202；概念 DOI `10.5281/zenodo.24269665` 现指向此版本 | 新增信任页、存档包、SEO 审计与公开回执 |
| **Figshare 第二版本** | `10.6084/m9.figshare.35018998.v2`，公开版本 2，3 个文件（原 PDF + 全文包 + 清单） | 真实 md5 与真实字节上传，非占位 |
| **第二个 GitHub 仓库** | https://github.com/kiloiam/labor-value-theory-archive （独立 URL／独立存储） | Release `v1.0.0` 含 PDF、存档包、清单、副本列表 |
| **GitHub Release `v6.0.0`** | 27 个不可变资产 | 主仓库 |
| **OSF 项目** | 26/26（1 个 403 重试后 201 修复） | `wubs2` |
| **公开 Gist** | 7/7 | 关键审计与语料文件 |

Software Heritage 对两个仓库分别发起存档请求，均已实测转为成功：

| 仓库 | POST | 状态 | visit | snapshot SWHID |
|---|---|---|---|---|
| `labor-value-theory-preprint` | 200 | succeeded | full | `swh:1:snp:0477f61a5e0a07167cbaff0aac2f1603aa436eaa` |
| `labor-value-theory-archive` | 200 | succeeded | full | `swh:1:snp:d8534ced5e84019f05eaff359899ebc4a4aa23c5` |

Telegraph 新增 3 个索引页（中、英、最终总索引）：

| 语种 | URL |
|---|---|
| zh | https://telegra.ph/世界备份索引--劳动价值论是历史性范畴-11-16 |
| en | https://telegra.ph/World-Backup-Index---Labor-Theory-of-Value-as-a-Historical-Category-11-16 |
| final | https://telegra.ph/Round-7-world-backup-index--labor-theory-of-value-11-16 |

### 2.5 失败、限流与安全拦截（如实记录）

- **匿名托管失败 12 处**：`paste.rs`（201）、`hastebin.com`（401）、`catbox.moe`（412）、`paste.debian.net`（200）、`controlc.com`（403）、`write.as`（201）、`sourceb.in`（404）、`litterbox.catbox.moe`（412）、`ix.io`（0）、`paste.mod.gg`（35）、`0x0.st`（35）、`clbin.com`（35）。
  包括反爬拦截、API 字段不匹配、上传页返回错误页、TLS 握手失败等；均**未计入成功**。
- **`write.as` 假成功已剔除**：首次返回 201 与一个 id，但回抓是 `Blocked Post` 反垃圾页，
  不是文章；已移出成功清单并记为失败。
- **`paste.c-net.org/EmptyPaste` 假成功已剔除**：回抓 403，同样不计入。
- **一个文本托管域名被本地安全中心判定为恶意域名并拦截**，未访问、未重试、未寻找等效替代。
- **IPFS / Arweave 无匿名持久写入**：`ipfs.io /api/v0/add` 410、`dweb.link` 525、
  Pinata 401、Arseed 404、`arweave.net/tx` 400。**CID 与本地哈希不等于已 pin**，
  本轮没有伪造任何 Web3 副本。
- **Wayback 仍被限流**：第一批 1/5 确认
  （补上第六轮失败的报告页），第二批针对新页 0/10 确认，
  多数返回 429 / 523，全部记为未存档。
- **Figshare `versions` 端点仍 404**：但 `publish` + 真实分片上传可用，因此改为上传
  两个真实文件后发布 v2，而非伪造新版本。

## 三、真正影响搜索排名的合规动作

### 3.1 修复两个实质抑制项（本轮最有价值的一处）

1. **跨域名 canonical**：`index.html` 原先把规范链接指向带 `?sharecode=` 的 WorkBuddy 分享页，
   而其余 61 个页面与 sitemap 都声明 GitHub Pages 为规范地址。跨域 + 查询参数会分散权重，
   并可能让规范 Pages URL 被判为副本。现已改为**自引用绝对 URL**，`og:url` 同步对齐。
2. **sitemap 重复 URL**：同一文档同时以 `/` 与 `/index.html` 提交，已移除后者。

### 3.2 Google Scholar 收录合规

`citation_pdf_url` 由相对路径改为绝对 URL，并补齐 `citation_abstract_html_url`、
`citation_fulltext_html_url`、`citation_language`、`citation_keywords`、页码、
`citation_online_date`、`citation_license`。逐项对照见 `SCHOLAR-AUDIT-R7.md`。
**不调用 Google Indexing API**：官方只接受 JobPosting / BroadcastEvent，普通论文页调用属滥用。
Google / Bing 旧 sitemap ping 端点已停用（404 / 410）。

### 3.3 信任与溯源信号（E-E-A-T）

新增 **14 个实质页面**（非 doorway page）：6 组主题 × 中英双版共 12 页
（作者与署名、研究方法、数据可用性与校验、同行评审状态、版本与存档历史、更正／撤稿与隐私处理），
加英文术语表与站长提交台。每页有实质内容、FAQ、`Article` + `FAQPage` + `BreadcrumbList`
结构化数据、hreflang、自引用 canonical 与 Signposting；作者页另含 `ProfilePage`。
中文术语表 `terms.html` 扩展 8 个高频术语，新增 `terms-en.html` 的 `DefinedTermSet`。

### 3.4 抓取质量与索引覆盖

- 修补时全站 65 页审计：缺 canonical / description 的 3 页补齐，5 处过薄中文描述扩充，
  **最终 0 问题**（`SEO-AUDIT-R7.json`）；本轮新增 14 页另单独校验 canonical、description 与
  JSON-LD，全部通过（现共 79 页）。
- **下架工单页加 `noindex,nofollow,noarchive,nosnippet` 并移出 sitemap**：既避免搜索引擎
  收录含历史链接的页面，也符合去标识化要求。
- 新增 `sitemap-round7.xml`（21 个 URL）、加入 sitemap index 与 robots；
  主 sitemap 追加到 **176 URL**。
- **IndexNow 在 Pages 构建确认新页 200 之后重提**：176 URL × 4 端点全部 200；
  WebSub 两个 feed 均 204。
- `llms-topics-r7.txt` 提供 10 组中英溯源问答，供生成式引擎准确回答作者、许可、
  DOI、校验与同行评审状态。
- `webmaster-console.html` 给出 GSC / Bing / 百度 / 搜狗 / 360 / Yandex / Seznam 的
  站点验证与 sitemap 提交入口，并预填三个 sitemap 地址。

**说明**：上述都是真实、合规的排名因素（可抓取性、规范一致性、内容深度、来源透明、
索引覆盖），但**任何具体名次都不作承诺**，也不做买链、刷量、站群或关键词堆砌。

## 四、学术数据库复测

以新 DOI `10.5281/zenodo.24280895` 复测：

| 端点 | HTTP |
|---|---|
| datacite | 200 |
| openaire | 200 |
| openalex | 404 |
| semantic_scholar | 404 |
| crossref | 404 |
| zenodo | 200 |

DataCite 与 OpenAIRE 已登记；OpenAlex / Semantic Scholar / Crossref 仍为 404，
它们从 DOI 注册表与开放仓储**自动收割**，不接受单篇人工投稿，只能等待延迟。
CORE 有速率限制、BASE 有反爬页，本轮均不作政策断言。

## 五、复验

- 页面：79 个 HTML；主 sitemap 176 个 URL，
  本地目标缺失 0 个。
- 内联 JSON-LD 71 块，无效 0 块；
  内部断链 0 处。
- 脱敏回归：扫描 234 文件，硬违规 0，
  QQ 邮箱命中 0，`VERDICT PASS`。
- SHA-256 全量校验表由 `finalize_r5.py` 在报告写完后重算并推送，以其输出为准。

## 六、边界与不做的事

- 「无门槛期刊」不是准确说法：正式期刊都需同行评审与通讯作者；真正无门槛的是预印本服务器与开放仓储。
- 不代注册账号、不代勾选权属声明、不代填联系邮箱、不代点击提交；
  arXiv / HAL / SSRN / RePEc / ResearchGate / Academia.edu 需背书或机构认证，
  OSF Preprints / SocArXiv / PhilArchive / Preprints.org / IA item 需作者本人账号。
- 不承诺「劳动价值论」搜索第一、不保证推送到每个关注者、不承诺绝对永久保存。
- 所有记录仍是有 DOI、可引用、**未经同行评审**的预印本。

## 七、仍需你本人完成

1. **viXra**：回执为「已接收、待管理员检查」，尚无编号或链接；两天内无回复视为未接受，
   官方要求 `Do not resubmit`。若分配了编号，把链接发我，我补进清单并重提 IndexNow。
2. **站长平台站点验证**：GSC / 百度 / 搜狗 / 360 等需你本人账号；若采用 HTML 文件验证，
   把验证文件放进 `ltv-paper-site/` 根目录，回一句「重新发布并同步」即可。
3. **WorkBuddy 线上阅读页**：本轮未覆盖（发布授权需逐轮明确）。差异是新增页面与报告文字；
   若想让已分享链接同步第七轮内容，回一句「重新发布」，链接不变。
4. Figshare 早期历史记录的下架工单仍等官方执行，**请勿传播该历史链接**。

## 八、文件与回执

报告 `ROUND7-REPORT.md` · 公开副本清单 `HOSTS-R7.json` · SEO 审计 `SEO-AUDIT-R7.json` ·
Scholar 审计 `SCHOLAR-AUDIT-R7.md` · 站长清单 `SEARCH-CONSOLE-R7.md` ·
构建回执 `BUILD-R7.json` · 复验 `VERIFY-R7.json` · 学术库 `AGGREGATORS-R7.json` ·
完整外部回执 `build/EXTERNAL-R7.json`（工作区私有目录，不同步到公开站点）。

存档包 `archives/ARCHIVE-BUNDLE-R7.txt` · `archives/ARCHIVE-MANIFEST-R7.json` ·
`archives/` 下两份文件均已随 Zenodo v4、OSF、Release v6 同步。
