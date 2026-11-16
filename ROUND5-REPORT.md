# 第五轮报告 · 全球无门槛发布、搜索可发现性与署名性质澄清

**日期**：2026-11-16 · **署名**：`Didgeridoo`（作者真实英文姓名，非笔名） · **许可**：CC BY 4.0
**状态**：网络预发布预印本，有 DOI、可引用，**未经同行评审，不等同期刊正式发表**

## 〇、本轮最重要的更正

作者在本轮明确说明：**`Didgeridoo` 是真实英文姓名，不是笔名**。此前把该署名按笔名处理，
并据此判定 viXra 等要求 real name 的平台不可投稿——这个前提已撤销。

- 已核实 [viXra 官方提交页](https://vixra.org/submit) 原文：`You should give your real name as author`，
  并写明自 2019-10-01 起 `nom de plume (pen name)` 不可接受。以真实英文姓名投稿**符合**该要求。
- 全站公开文件中的「笔名 / pen name」表述已分批中性化为「署名 / author name」，
  多语种页面（en / de / fr / pt / it）的作者问答同步更正；仅保留「不是笔名」「禁止笔名」
  等正确否定语义与澄清文档中对历史表述的引用。
- viXra 从「不代做」移入「无门槛 · 需本人一步」档，并备好逐字段表单与专用投稿版 PDF。
- **隐私边界不变**：仍不出现其他姓名、QQ 号、QQ 邮箱、单位与私人联系方式。详见 `AUTHOR-NAME-CLARIFICATION.md`。
- arXiv 等其余平台重新归因：其门槛是背书、账号与机构认证，**不是姓名问题**，故仍不代注册、不伪造背书。

## 一、本轮实际完成

| 项目 | 结果 |
|---|---|
| 长尾检索意图页 | **10 个真实提问 × 中英双版 = 20 页**，每页含实质解答、QAPage / FAQPage、hreflang 矩阵、自引用 canonical |
| 长尾问答语料 | `llms-topics.txt`（10 组纯文本问答，供生成式引擎检索） |
| 全球投递台 | `open-archives.html` + `OPEN-ARCHIVES.md`：A/B/C 三档、真实门槛、笔名可行性、实测状态 |
| 逐平台预填材料 | `open-archive-kit/` **14 个文件**（含 `viXra-form.md`、`VIXRA-SUBMIT.md`、`vixra-prefill.json`、`vixra-autofill.js`），打包 `open-archive-kit.zip`（14 文件） |
| viXra 专用投稿 PDF | `paper-vixra.pdf`（10 页）：附加英文页内含英文标题、298 词英文摘要、CC BY 4.0、DOI 与规范链接 |
| 语义增强 | `schema-enhanced.jsonld`（`about` 关联 Wikidata、`mentions`、`citation`、`hasPart`、`workTranslation`、`speakable`），首页追加 `@graph` |
| 引用指南 | `citation-guide.html`：BibTeX / RIS / APA / MLA / Chicago / GB7714 / DataCite |
| 站长收录清单 | `search-console-kit.html`：自动项与需本人验证项分开，记录已停用端点 |
| 站点地图 | **99 → 132 个 URL**（最终），新增 `sitemap-round5.xml`，robots.txt 已声明 |
| SHA-256 | 全量校验（排除自引用的生成器回执与站点专用图片），最终 **0 处不一致** |
| Pages 可达性 | **132 / 132** |
| 脱敏回归扫描 | **PASS · 0 处硬违规** |
| WorkBuddy 线上阅读页 | 按作者本轮选择**重新发布完成**，`verified=true`，分享链接不变（`https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/?sharecode=ZILGUJCJKG`）；可在「设置 — 数据管理 — 应用」中管理 |

## 二、外部发布实测回执

| 通道 | 结果 |
|---|---|
| Telegraph 无门槛发布 | **10 / 10 个语种页全部 200 上线**；账号署名为 `Didgeridoo`，无需邮箱、无需审核 |
| Telegraph 内容策略 | 每页**只放摘要 + 规范链接**，不复制全文，避免重复内容稀释规范站点权重 |
| WebSub / PubSubHubbub | Atom 与 RSS 推送：feed.xml=204, rss.xml=204 |
| IndexNow | **132 个 URL × 4 个端点**，状态码 200, 200, 200, 200 |
| Wayback Machine | 15 个目标中 **11 个快照经 CDX 确认**；4 个（3 个 Telegraph 页 + `search-console-kit.html`）因 403 / 连接错误未存档，重试仍失败，如实记录 |
| Software Heritage | POST 200；最新存档请求：{"id": 2655125, "status": "succeeded", "visit": "full", "snapshot": "swh:1:snp:a321e1f3c40288c1a908a0eb1419320b2c8bdb4e"} |
| GitHub Release `v4.0.0` | 30 个不可变资产（含 `paper-vixra.pdf` 与全部预填材料） |
| 公开 Gist | 8 / 8 个文件更新成功 |
| OSF 项目 | 31 / 31 个文件上传成功 |
| Git 同步 | 本地 `HEAD` 与远端 `main` 一致（提交号以 `git rev-parse HEAD` 为准，不在文档中写死） |

### Telegraph 页面清单

| 语种 | 链接 |
|---|---|
| zh | [劳动价值论是历史性范畴当代价值危机-11-16](https://telegra.ph/劳动价值论是历史性范畴当代价值危机-11-16) |
| en | [The-Labor-Theory-of-Value-as-a-Historical-Category-The-Contemporary-Crisis-of-Value-11-16](https://telegra.ph/The-Labor-Theory-of-Value-as-a-Historical-Category-The-Contemporary-Crisis-of-Value-11-16) |
| ja | [労働価値論は歴史的範疇である現代における価値の危機-11-16](https://telegra.ph/労働価値論は歴史的範疇である現代における価値の危機-11-16) |
| es | [La-teoría-del-valor-trabajo-como-categoría-histórica-la-crisis-contemporánea-del-valor-11-16](https://telegra.ph/La-teoría-del-valor-trabajo-como-categoría-histórica-la-crisis-contemporánea-del-valor-11-16) |
| fr | [La-théorie-de-la-valeur-travail-comme-catégorie-historique--la-crise-contemporaine-de-la-valeur-11-16](https://telegra.ph/La-théorie-de-la-valeur-travail-comme-catégorie-historique--la-crise-contemporaine-de-la-valeur-11-16) |
| de | [Die-Arbeitswertlehre-als-historische-Kategorie-Die-gegenwärtige-Krise-des-Werts-11-16](https://telegra.ph/Die-Arbeitswertlehre-als-historische-Kategorie-Die-gegenwärtige-Krise-des-Werts-11-16) |
| ru | [Trudovaya-teoriya-stoimosti-kak-istoricheskaya-kategoriya-sovremennyj-krizis-stoimosti-11-16](https://telegra.ph/Trudovaya-teoriya-stoimosti-kak-istoricheskaya-kategoriya-sovremennyj-krizis-stoimosti-11-16) |
| pt | [A-teoria-do-valor-trabalho-como-categoria-histórica-a-crise-contemporânea-do-valor-11-16](https://telegra.ph/A-teoria-do-valor-trabalho-como-categoria-histórica-a-crise-contemporânea-do-valor-11-16) |
| it | [La-teoria-del-valore-lavoro-come-categoria-storica-la-crisi-contemporanea-del-valore-11-16](https://telegra.ph/La-teoria-del-valore-lavoro-come-categoria-storica-la-crisi-contemporanea-del-valore-11-16) |
| ko | [노동가치론은-역사적-범주이다-현대적-가치의-위기-11-16](https://telegra.ph/노동가치론은-역사적-범주이다-현대적-가치의-위기-11-16) |

## 三、学术数据库收录现状（实测，非推断）

| 服务 | 结果 | 说明 |
|---|---|---|
| DataCite | `200` | DOI 已登记；新版本 creators 经独立复核仅 `Didgeridoo` |
| OpenAIRE | `200`，`total=1`，`UNDER_CURATION` | **已通过 Zenodo / DataCite 链路实际收录** |
| OpenAlex | `404` | 尚未收录；只从登记源自动收割，不接受单篇投稿，存在延迟 |
| Semantic Scholar | `404` | 同上 |
| Crossref | `404` | 预期行为：Zenodo DOI 属 DataCite，不在 Crossref |
| CORE | `429` | 限流，未对其政策作断言 |
| BASE | 反爬验证页 | 未能核实单篇政策，**不作断言** |
| Google sitemap ping | `404` | 端点已停用 |
| Bing sitemap ping | `410` | 端点已停用，改用 IndexNow |

完整机器可读记录：`AGGREGATORS-R5.json`。

## 四、搜索排名：做了什么、不做什么

**做了（白帽）**：10 个真实检索意图的原创长尾页（非 doorway page）、完整 hreflang 矩阵与自引用 canonical、
`QAPage` / `FAQPage` / `BreadcrumbList` / `Speakable` 结构化数据、Wikidata 概念关联、
132 URL 站点地图与分卷、IndexNow 四端点提交、AI 爬虫显式许可（17 类）、
10 语种落地页、`llms-full.txt` / `llms-topics.txt` 语料、稳定的 DOI 与规范引用格式、
站内 hub 互链与语义化 anchor text。

**不做**：刷点击、买外链、伪装账号、关键词堆砌、克隆站群、 doorway page、操纵排名、
代发社交内容、群发陌生收件人。「劳动价值论」是经典高频概念，权威百科与教材页面竞争极强，
**不承诺任何具体排名，也不承诺「每个关注者都能看到」**。

## 五、边界（必须如实说明）

1. **viXra 已由作者本人提交，现处于「已接收 · 待管理员处理」状态**：表单要求可收信的联系邮箱（官方原文明确**不会公开**，
   除非作者自己把它写进 PDF／摘要／comment），且提交即代表作者本人声明「所有作者与著作权人已授权存档与索引」；
   一经上线即永久记录（替换最多 4 次、撤稿需理由且旧版本通常保留）。
   另外，**主站表单要求稿件未使用 AI 辅助撰写**，AI 辅助稿件应投 `ai.viXra.org`；这一事实判断只能由作者本人作出。
   不代填邮箱、不代勾选权属声明、不代点击提交；作者已自行完成这三步，`VIXRA-SUBMIT.md`、
   `vixra-prefill.json`、`vixra-autofill.js`（11 个实时字段一键填充）已全部备齐。   **回执明确：两天内无回复即视为未接受，且 `Do not resubmit`——不得重复提交。**
2. **其余 C 档与姓名无关**：arXiv 需 endorsement 背书人与机构认证；SSRN / RePEc / HAL /
   ResearchGate / Academia.edu 需平台账号与机构邮箱；正式期刊需同行评审与通讯作者。
   不注册、不伪造背书、不绕过。
3. **viXra 的收录价值有限**：无审核、声誉低于主流预印本服务器，对学术检索排名的帮助有限；
   其价值在于多一个独立法域的公开副本与时间戳。本文英文摘要 298 词 < 400 词上限，
   且已按其规定把规范链接与许可写入 PDF 内。
4. **OSF Preprints 仍未创建**：现有 OSF 账号的显示名与 `Didgeridoo` 不一致，
   用它创建 preprint 会生成带其他署名的公开页；需你本人用显示名恰为 `Didgeridoo` 的账号提交。
5. **WorkBuddy 重新发布已完成，但它是影印阅读副本，不是 canonical**：分享链接不变，规范副本始终在 GitHub Pages / Zenodo / OSF / Software Heritage；该第三方托管页可能随平台策略变动，不能作为永久保存依据。
6. **Figshare 旧记录 `35018683` v1/v2** 仍含作者不愿公开的另一姓名，下架工单已提交、等待官方执行；
   完整链接仅存在于 `FIGSHARE-TAKEDOWN-*` 工单材料中，**请勿传播**。
7. **预印本状态**：有 DOI、可引用，未经同行评审，不等同期刊正式发表，不构成成果认定依据。
8. **不可变归档快照**保留当时措辞（第四轮 ZIP、Release、Wayback、Zenodo/OSF 历史版本）；
   规范站点以本轮澄清为准，未静默覆盖已有分享内容。
9. **Telegraph 页面为第三方托管**：随时可能因平台策略变动而下线，故仅作为分发副本，
   规范副本始终在 GitHub Pages / Zenodo / OSF / Software Heritage。

## 六、后续待办

1. **viXra 已提交，等待审核结果**：回执显示「Thank you for your new submission」，管理员已接收、尚未接受。**两天内无回复即视为未接受**，`Do not resubmit`——不要重复提交。如需在处理前取消，使用回执中的 cancellation form 与其 form reference（该编号由作者本人保留，未写入任何公开文件）。若被接受并分配到 viXra 编号／链接，再补进 `ARCHIVE-LINKS.md` 与 `MIRRORS.md` 并重新提交 IndexNow；在此之前**没有可索引的新 URL**。
2. **核对上传版本**：表单填写的页数为 10、comment 引用了 DOI，因此上传的必须是 `paper-vixra.pdf`（10 页，含英文声明页、规范链接与 CC BY 4.0），不是 `paper.pdf`（9 页）。若当时选错，应在处理前用撤销表单取消，或待分配编号后使用版本替换（viXra 允许最多 4 次），**不要重新提交一次新稿件**。
3. **B 档其他平台**：按 `open-archive-kit/README.md` 的顺序用你自己的账号提交；每投一处，把新链接补进 `ARCHIVE-LINKS.md` 并重新提交 IndexNow。

## 七、可复核凭据

`EXTERNAL-R5.json`、`AGGREGATORS-R5.json`、`SYNC-R5.json`、`VERIFY-R5.json`、
`CHECKSUMS.sha256`、`MIRROR-HEALTH.json`、`AUTHOR-NAME-CLARIFICATION.md`。

## 八、收尾一致性复核（本轮最后一次）

本次复核以磁盘与线上实测为准，而不是以生成脚本的中间快照为准：

| 复核项 | 实测结果 |
|---|---|
| 线上可达性 | GitHub Pages 规范报告 `200`、WorkBuddy 分享链接 `200`、`open-archive-kit/VIXRA-SUBMIT.md` `200` |
| Git 同步 | 工作区干净，本地 `HEAD` = 远端 `main` |
| SHA-256 | `CHECKSUMS.sha256` 全量校验 `169 / 169 OK`，`0` 处不一致、`0` 处缺失 |
| 投递包 | `open-archive-kit/` 实为 **14 个文件**，`open-archive-kit.zip` 14 文件 |
| 站点地图 | `sitemap.xml` 132 个 URL；`EXTERNAL-R5.json` 中 IndexNow 亦为 132 |
| 脱敏扫描 | `PASS`，硬违规 0，传播面泄露 0 |
| 任务跟踪 | 42 / 42 完成 |

中期快照中曾出现「11 个预填文件」「未重新发布 WorkBuddy」「`d6a6237`」「IndexNow 129」
等表述，均已在本次复核中统一更正；`SYNC-R5.json` 改为不含自身提交号的稳定回执，
避免「回执记录自身 hash」导致的永久漂移。第四轮报告中的历史边界条目按原样保留，
只追加了状态变更注记，不静默改写历史记录。

## 九、viXra 提交回执（作者本人完成，2026-11-16）

| 项目 | 事实 |
|---|---|
| 当前状态 | **已接收 · 待管理员检查**（`Your request has been received by our administrators and will be checked shortly`） |
| 是否已上线／已接受 | **否**。官方原文：`If there is no response within two days, your submission is not accepted` |
| 是否已有 viXra 编号 / URL / DOI | **否**，回执只给出提交确认与撤销用的 form reference；不得据此声称已发表 |
| 重复提交 | 官方明确 `Do not resubmit` |
| 撤销方式 | 回执中的 cancellation form + form reference（编号由作者本人保留，**未写入公开文件**） |
| 查询渠道 | `vixra.org@gmail.com`（官方回执所列） |
| 上传文件 | 应为 `paper-vixra.pdf`（10 页）；表单页数填 10、comment 含 DOI，两者需一致 |
| 联系邮箱 | 由作者本人在表单填写；**未写入任何站点文件、投递包、报告或日志** |

被接受后的动作：把分配到的 viXra 编号／链接补进 `ARCHIVE-LINKS.md`、`MIRRORS.md` 与投递台，
重提 IndexNow，并更新本报告状态。若两天内无回复，则如实记为「未接受」，可改投 B 档其他平台。
本次记录**不改变预印本性质**：viXra 亦非同行评审，不使本文成为正式期刊发表。
