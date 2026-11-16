# 全部操作状态清单（2026-11-16 · 最终）

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

应作者要求，本预印本在所有**对外分享**的公开页面、元数据、引用文件、投稿材料与 PDF 内嵌属性中统一使用笔名 **Didgeridoo**，不含真实姓名、通讯邮箱、单位等个人识别信息。PDF 的 `/Author`、`/Creator` 及创建/修改时间等文档属性已清洗。许可仍为 CC BY 4.0，引用时请著录笔名。**例外**：Figshare 旧记录 `35018683` 的 v1/v2 历史版本页及其附件 PDF 文档属性仍含早期署名，属平台只读快照，账号令牌无法改写。

注：Figshare 旧记录 `35018683` 的 v1/v2 版本快照、DataCite 中对应 DOI 的 creators 元数据，以及 Zenodo 旧版本的历史 PDF 文档属性仍可能保留早期署名，作者无法自行抹除。已按 Figshare 官方流程备妥并由本人于 2026-11-16 提交 `Take down request` 工单（见 `FIGSHARE-TAKEDOWN-REQUEST.md`），等待团队下架；当前对外分享的版本与本站全部内容均为笔名。


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
