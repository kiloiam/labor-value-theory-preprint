# 全部操作状态清单（2026-11-16 · 最终）
<!-- R5-REALNAME -->

> **署名性质澄清（2026-11-16）**：作者确认 `Didgeridoo` 为**真实英文姓名**，非笔名。
> 全站表述已中性化；viXra 的 real-name 要求已满足，现已解锁为可投平台；
> 去标识化边界（不出现其他姓名、QQ 号、QQ 邮箱、单位与联系方式）不变。
> 详见 `AUTHOR-NAME-CLARIFICATION.md`。

## 已真实执行完成

1. **Zenodo**：主 DOI `10.5281/zenodo.24270266` → https://doi.org/10.5281/zenodo.24270266 ，CC BY 4.0，作者Didgeridoo，paper.pdf 完整可下载。
2. **Figshare**：v2 DOI `10.6084/m9.figshare.35018998.v1` → https://doi.org/10.6084/m9.figshare.35018998.v1 ，分类 Political economy and social change，CC BY 4.0；作者 Didgeridoo。旧记录 `35018683` 已弃用：其 v1/v2 为含早期署名的只读历史版本，切勿分享；下架请求见 `FIGSHARE-TAKEDOWN-REQUEST.md`。
3. **OSF**：公开项目 https://osf.io/wubs2/ ，public=True，PDF 1,388,974 字节，项目描述已标注作者。
4. **GitHub**：公开仓储 https://github.com/kiloiam/labor-value-theory-preprint ，v1.0.0 Release 附 PDF；本轮更新后推送新版本。
5. **在线阅读页与投递工作台**：同一站点两个页面，全文、9 页原稿影印、元数据、投稿信、门槛与核验结果全部在线；静态资源分享码问题已修复。
6. **完整提交包**：PDF、全文 Markdown、中英文摘要、metadata.json、CITATION.cff、投稿信、政策要点、校对记录、预填表单、一键脚本。
7. **文字校对**：英文摘要 19 类连写/标点错误已在所有在线交付物与元数据中修正，原稿 PDF 一字未改。
8. **百晓智能**：期刊匹配、10/10 条参考文献核验、审稿人候选、预印本政策检索，结果已写入投递台。
9. **一键脚本已按实测修复**：Zenodo 的 related_identifiers/500 与 license 写法、Figshare 的 upload_url 分片端点、license id、必填 categories；dry-run 通过。

## 全球留存与分发（2026-11-16 追加，已真实执行）

10. **Software Heritage**：仓库已完整存档，`visit_status=full`；另发请求 2654599 抓取含新增元数据的最新提交。
11. **Internet Archive Wayback**：12 个干净公开入口全部生成永久快照（含阅读页、分发页、PDF、Zenodo / Figshare / OSF / GitHub / Release / CDN）。
12. **IndexNow**：26 个 URL 提交至官方聚合、Bing、Yandex、Seznam，全部受理。
13. **机器可读元数据**：新增 DataCite 4.5、OAI-PMH oai_dc、Dublin Core、MARC21、METS、Schema.org JSON-LD、EndNote、Zotero RDF、APA / MLA / Chicago、7 语种摘要、Atom / RSS；两个阅读页注入 Highwire / DC / EPrints / COinS 标签。
14. **冗余副本**：OSF 项目上传 16 个元数据文件，GitHub Release 挂载 15 个元数据资产，仓库主题标签扩至 11 个。
15. **索引核验**：OpenAIRE 已收录主 DOI（`total=1`）；Zenodo 社区 `political economy` 收录申请已提交（status `submitted`）；OpenAlex / Semantic Scholar 尚未收录，属自动抓取时滞。

完整链接与返回码见 `DISTRIBUTION.md`、`distribution.html`、`PRESERVATION.md`。

## 未执行与原因

- **未向编辑部发送投稿信**：《中南大学学报(社会科学版)》2026-06-08 官方声明明确「通常情况下只接受在线投稿」「从未授权任何机构或个人代投」，`znsk@csu.edu.cn` 仅作咨询核实。填写页虽勾选授权，但未提供收件邮箱，且期刊规则排除代投。请本人在 https://zndxsk.csu.edu.cn 的「作者在线投稿」系统提交，正文见 `cover-letter.md`。
- **ChinaXiv / 学术世界·哲社预印本平台 / SSRN / PhilPapers / RePEc**：无公开提交 API，须本人实名注册、邮箱验证并勾选原创性声明；`form-data/` 已备好预填字段。
- **期刊正式投稿与同行评审**：只能由作者本人在投稿系统完成，需先核实该刊预印本政策。

## 仍需本人补齐 / 复核

- 工作单位（现填「暂无」）、ORCID iD（空）、基金项目与利益冲突声明；通讯邮箱与作者简介已填，保存在本机私有文件 `intake/author-profile.json`，未写入公开页面或仓库。
- [9] *Fanged Noumena* 年份按实体书版权页核定（稿件 2011 / 数据库主记录 2012）；[8] 补页码 68-74 与 ISSN 1000-114X；[2][3] 文集卷次 ISBN。
- 确认目标期刊的预印本政策；投稿时如实说明本稿已有公开记录与 DOI。

## 复用脚本

```
cd submission-kit/package
python submit_all.py            # 预演，不联网
python submit_all.py --live --only zenodo   # 仅提交指定平台（注意避免重复条目）
```

`tokens.json`、`submission-log.json`、`intake/author-profile.json` 均已加入 .gitignore，不会进入公开仓库。

## 重要边界

所有记录均为**网络预发布预印本**：有 DOI、无同行评审、不等同于期刊正式发表，不构成学术成果认定依据。DOI 只解决可引用性与长期保存。

<!-- ANONYMITY-NOTE -->

## 署名与隐私说明

应作者要求，本预印本在所有**对外分享**的公开页面、元数据、引用文件、投稿材料与 PDF 内嵌属性中统一使用署名 **Didgeridoo**，不含真实姓名、通讯邮箱、单位等个人识别信息。PDF 的 `/Author`、`/Creator` 及创建/修改时间等文档属性已清洗。许可仍为 CC BY 4.0，引用时请著录署名。**例外**：Figshare 旧记录 `35018683` 的 v1/v2 历史版本页及其附件 PDF 文档属性仍含早期署名，属平台只读快照，账号令牌无法改写。

注：Figshare 旧记录 `35018683` 的 v1/v2 版本快照、DataCite 中对应 DOI 的 creators 元数据，以及 Zenodo 旧版本的历史 PDF 文档属性仍可能保留早期署名，作者无法自行抹除。已按 Figshare 官方流程备妥并由本人于 2026-11-16 提交 `Take down request` 工单（见 `FIGSHARE-TAKEDOWN-REQUEST.md`），等待团队下架；当前对外分享的版本与本站全部内容均为署名。


## 第三轮已完成（无需本人操作）

- 27 处公开副本登记、8 个法域或区域、8 类存储层；Zenodo 新 DOI `10.5281/zenodo.24273568` 已发布。
- Wayback 累计 40 处永久快照；Software Heritage 主仓库与 Gist 均 `succeeded / full`。
- OSF 追加 22 个副本、GitHub Release `v2.0.0` 18 个资产、6 个 SHA 固定永久链接全部 `200`。
- IndexNow 四端点提交 63 个 URL 全部受理；10 语种页、hreflang、`@graph` JSON-LD、llms.txt 上线。
- 提交包重建、全量脱敏扫描 0 处违规、23 项校验全部通过。

## 仍待本人处理

1. Figshare 旧记录 `35018683` 的 v1 / v2 早期署名：官方 `Take down request` 工单已提交，等待平台执行；执行前请勿传播该记录。
2. 若官方回复要求验证所有权或提供工单号，用注册邮箱回复确认即可，回复中不要写出真实姓名。
3. 下架完成后，DataCite 中 v1/v2 DOI 的 creators 元数据与搜索引擎缓存需按支持团队回复另行处理。


## 第四轮：前沿可发现性与去中心化留存（2026-11-16，已真实执行）

- **语义网 / FAIR**：`.well-known/linkset.json` + 15 个页面 `<link rel>` Signposting；`ro-crate-metadata.json`（逐文件 SHA-256）、`codemeta.json`、`oai/*.xml` 静态 OAI-PMH 快照；`schema.jsonld` 关联 Wikidata Q584987 / Q854537 / Q332425，`knowledge-graph.jsonld` 统一 `@graph`。
- **生成式引擎 / 白帽 SEO**：`llms-full.txt` 全文语料、`terms.jsonld`（14 个 DefinedTerm）、`faq.jsonld`（20 条中英问答）、`topic-ltv.html` 主题导览、`discovery-qa.html`；`robots.txt` 显式允许 17 类 AI 爬虫；站点地图扩至 **99** 个 URL，IndexNow 四端点提交 99 个 URL 全部 `200`。
- **去中心化留存**：2 个 BitTorrent/WebSeed swarm（含磁力链接与浏览器内 WebTorrent）、BagIt holey bag（`fetch.txt` 指向全球镜像）、IPFS CIDv1 清单（**未代注册 pinning**）、Memento TimeMap（40 个 Wayback 快照索引）。
- **全球端点**：GitHub commit `4599dd3d`；Release `v3.0.0` 30 个资产；Gist 19 个文件；OSF 60 个文件；Software Heritage 两次存档请求受理；Pages 新页面 99/99 可达。
- **合规传播**：`broadcast.html` 一键分发台（10 语种文案 / 12 平台深链 / BibTeX 复制）与 `BROADCAST-KIT.md`；**所有发布动作由本人点击完成**，不代发、不群发、不刷量。
- **核验**：CHECKSUMS 68/68 ALL OK；全量脱敏扫描 **PASS**（真名 / QQ / QQ 邮箱 / 旧号 0 命中，传播面 0 泄露，旧 Figshare 链接仅存在于下架工单材料）。

- **Zenodo 新版本**：DOI `10.5281/zenodo.24274919`（16 个资产），已通过 DataCite 注册表复核 creators 仅 `Didgeridoo`；概念 DOI `10.5281/zenodo.24269665` 仍指向最新版本。

### 第四轮边界

- 无法保证搜索「劳动价值论」排名第一，也无法主动推送到每个关注者眼前；排名与推荐由搜索引擎和平台算法决定，且「劳动价值论」是经典高频概念、竞争极强。本轮做的是合规可发现性，不刷量、不买外链、不操纵排名。
- 无法承诺「到人类文明灭亡仍存在」；最大化的是冗余度、可校验性与可重建性。CC BY 4.0 允许任何人复印、翻译、做种与再托管。
- OAI-PMH 为静态快照，非实时端点；IPFS 已算 CID 但未执行永久 pin（需带凭证服务）。
- 所有记录仍为网络预发布预印本，有 DOI、未经同行评审，不等同期刊正式发表。
- 本轮未重新发布 WorkBuddy 线上站点（未收到本轮明确的重新发布授权）；GitHub Pages 规范站点已包含全部第四轮内容。 **此状态已在第五轮变更**：作者后续明确选择重新发布，见下节。


## 第五轮：全球无门槛发布、长尾可发现性与署名澄清（2026-11-16）

- **署名性质更正**：作者确认 `Didgeridoo` 为真实英文姓名，非笔名；全站表述已中性化，
  viXra 的 real-name 要求已满足并解锁为可投平台。详见 `AUTHOR-NAME-CLARIFICATION.md`。
- 新增 10 个真实检索意图 × 中英双版长尾页、`llms-topics.txt`、`open-archives.html`、
  `OPEN-ARCHIVES.md`、`open-archive-kit/`（14 个预填文件，含 viXra 一键预填三件套）、
  `paper-vixra.pdf`、`citation-guide.html`、`search-console-kit.html`、`schema-enhanced.jsonld`。
- 站点地图 132 个 URL；IndexNow 132 个 URL × 4 端点；Telegraph 10 个语种摘要页上线；
  GitHub Release `v4.0.0`；Pages 实测 132/132 可达；SHA-256 全量校验通过；脱敏扫描 PASS。
- 学术库实测：DataCite 与 OpenAIRE 已收录，OpenAlex / Semantic Scholar 尚未（自动收割有延迟）。
- 边界：viXra 提交仍需本人提供联系邮箱、勾选权属声明并点击提交（一经上线永久记录）；
  arXiv 需背书与机构认证，其余需账号/机构邮箱/同行评审；不承诺排名；
  WorkBuddy 线上站点已按作者选择重新发布，`verified=true`，分享链接不变；可在「设置 — 数据管理 — 应用」中管理。完整报告见 `ROUND5-REPORT.md`。
