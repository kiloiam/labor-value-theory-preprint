# 去标识化报告（Anonymization Report）

**署名**：Didgeridoo（笔名）　·　**执行日期**：2026-11-16　·　**许可**：CC BY 4.0（不变）

## 结论

除下文「平台限制造成的残留」明确列出的**只读历史版本快照**外，
所有**当前对外分享的页面、元数据、引用文件、投稿材料与 PDF 文档属性**统一使用笔名 `Didgeridoo`，
不含真实姓名、通讯邮箱、工作单位等个人识别信息；第二轮追加核验显示，
用户指定的 QQ 号及所有 QQ 邮箱形态字段在全部公开位置均为 0 命中（详见下节）。原稿正文一字未改，仅重写了 PDF 的
`/Author`、`/Creator`、`/Title` 等文档属性并移除创建/修改时间指纹；清洗前后 9 页正文逐字一致。

**重要例外（用户于 2026-11-16 指出的具体链接）**：Figshare 旧记录 `35018683` 的
**v2 历史版本页**（用户提供的 `/2?file=71484547` 链接）的作者字段，
以及该页附件 PDF（文件 `71484547`）的内嵌 `/Author` 文档属性，仍是早期真实署名；v1 页面为账号显示名。
为免扩散，本报告不复述完整 URL；精确链接只写入给支持团队的 `FIGSHARE-TAKEDOWN-REQUEST.md`。
该链接属于平台只读历史版本，账号令牌无法改写，详见下节与 `FIGSHARE-TAKEDOWN-REQUEST.md`。
所有对外分享链接均已切到干净记录，不再指向该页。

## 已更新的公开位置

| 位置 | 当前状态 |
|---|---|
| Zenodo 主记录 | `10.5281/zenodo.24270266`（新版本）：creators = Didgeridoo，PDF 已去标识化 |
| Zenodo 概念 DOI | `10.5281/zenodo.24269665`：始终指向最新版（即上述去标识化版本） |
| Zenodo 旧版本 | `10.5281/zenodo.24269666` 的**公开署名已改为笔名**；其历史 PDF 被平台锁定，见下方残留 |
| Figshare 主记录 | `10.6084/m9.figshare.35018998.v1`：全新干净记录，作者 Didgeridoo，PDF 已去标识化 |
| OSF | https://osf.io/wubs2/ ：描述改为笔名；旧 PDF 已删除，上传去标识化版本 |
| GitHub Pages | https://kiloiam.github.io/labor-value-theory-preprint/ ：`citation_*`、JSON-LD、OG、正文、PDF 全部为笔名 |
| WorkBuddy 在线站点 | 阅读页与投递台：全文、元数据、引用、投稿信、预填表单全部为笔名 |
| 本地提交包 | `submission-package.zip` 及其 4 个目录副本：39+ 文件全部为笔名 |
| GitHub 仓库 | 历史重写为单一干净提交，提交者 `Didgeridoo <didgeridoo@users.noreply.github.com>`；Release 附件换为清洗后 PDF |

### 额外清理的隐性泄露点

- PDF 内嵌 `/Author` 原为真实姓名（用阅读器「文档属性」即可看到），已重写为 Didgeridoo。
- URL 百分号编码的姓名、BibTeX/CSL 中以姓氏拼音构成的引用键、拆分的姓/名字段，均已替换。
- 本地填写页、私有配置、工作区日志与所有生成脚本同步脱敏，避免后续重跑把旧署名带回来。

## 第二轮：QQ 号与联系方式字段清除（2026-11-16）

**目标**：用户指定的 QQ 号，以及由它衍生的邮箱、mailto 链接、表单值、文档属性与平台元数据字段。

### 全量核验（均为 0 命中）

| 核验范围 | 结果 |
|---|---|
| 工作区全部文件（含隐藏目录、PDF/PNG/ZIP 二进制、git 跟踪文件） | 字节级扫描 0 命中 |
| 4 份公开 `paper.pdf` 的 `/Info`、XMP 及原始字节 | 0 命中 |
| Downloads 原稿 PDF 及同目录 30+ 个文件 | 0 命中 |
| 在线阅读页、投递台、Pages 落地页的 20+ 页面与静态资源 | 0 命中 |
| Zenodo / Figshare / OSF 的 API 元数据、历史版本页面与历史 PDF 文档属性 | 0 命中 |
| DataCite 四个 DOI 的注册元数据 | 0 命中（但发现一处真名残留，见下方残留第 5 条） |
| GitHub 提交历史、Release 说明、仓库描述、API 提交作者 | 0 命中 |
| 提交包 ZIP 全部 40 个条目 | 0 命中 |

### 唯一命中与处理

该号此前**从未进入任何公开内容或私有配置**；唯一出现位置是本次对话产生的
本地会话记录（用户消息与本轮工具输出）与两个临时诊断脚本。

- 临时诊断脚本已删除；其余生成脚本中残留的旧号字面量已替换为 `[QQ-REDACTED]`。
- 本地会话记录中的完整号已批量替换为 `[QQ-REDACTED]`。
  但会话记录由客户端实时追加且受写权限保护：本轮后续工具输出仍可能重新写入该号，
  最后一次写入被客户端权限规则拒绝，因此该文件**可能仍有少量残留**。
  这是**本地私有会话数据、不是公开内容**；如需彻底清除，请在本轮会话结束后
  自行删除对应会话记录文件（会同时丢失本次对话历史）。

### 已执行的预防性收紧

- **通用脱敏 guard**：`build_web.py` 与 `merge_site.py` 已内置自动脱敏，
  每次重建站点或打包时，把 QQ 邮箱形态（`\d{5,12}@qq.com`）与孤立的 10 位 QQ 号
  统一替换为占位，防止后续重建把号码带回来。
- **联系方式字段复核**：公开物料中的「通讯邮箱」值统一为
  「请在投稿系统内填写（本机私有保存）」，不预置任何真实邮箱、QQ 号或电话。
- **本地 git 历史**：删除含旧 QQ 邮箱的备份分支并执行 `git gc --prune=now`，
  本地不再保留旧提交对象；远程 GitHub 的旧提交对象仍可按 SHA 访问，见残留第 4 条。

## 第三轮：用户指定链接的定向核查与下架请求（2026-11-16）

用户给出的链接指向 Figshare 旧记录 `35018683` 的 v2 版本页（带 `file=71484547` 文件参数）。
对该链接做了逐字段核查，真名残留**两处**，均属平台只读历史快照：

| 位置 | 核查结果 |
|---|---|
| v2 页面作者字段（`/articles/35018683/versions/2` 的 `authors[0].full_name`） | 早期真实署名（作者记录 id 26455234，只读） |
| v2 附件 PDF（文件 `71484547`，1,388,974 字节）的内嵌 `/Author` | 早期真实署名（UTF-16BE，1 命中）；正文提取文本 0 命中 |
| v1 页面作者字段 | 账号显示名（非论文署名，同属个人标识） |
| v3 页面与当前默认版本 | `Didgeridoo`，干净；附件 `71486362` 为去标识化 PDF |
| 该页 QQ 号 / QQ 邮箱 / 通讯邮箱 | 0 命中 |

本轮穷举了账号令牌可用的全部官方端点，结论是**免费账号无法自助抹除**：

- `PATCH` / `PUT /account/articles/35018683/versions/2`：`403 Insufficient permissions`；
  该端点 schema 只允许 `supplementary_fields` 与 `internal_metadata`，不能改 `authors`。
- `POST /account/articles/35018683/unpublish`：`403 Insufficient permissions`。
  Figshare 官方帮助明确说明：免费 figshare.com 账号**不能自行 unpublish**，须提交
  标题为 `Take down request` 的支持工单，由团队处理。
- `DELETE /account/articles/35018683`：`400 Cannot delete a public article`。
- `PUT /account/articles/35018683/embargo`（article / file 级永久 embargo）：
  `400 Cannot add embargo to public item`。
- `DELETE /account/articles/35018683/files/71484547`：返回 `204`，但只移除了草稿侧文件引用；
  v1/v2 历史快照与 `https://ndownloader.figshare.com/files/71484547` 下载仍为 200。
- `PUT /account/articles/35018683` 传 `is_public=false` / `status=draft`：返回 `205` 但被平台忽略，
  公开状态复核仍为 `true / public`。
- `PUT` / `PATCH /account/authors/26455234`：`404`（该作者记录只读，仅 GET 可用）。

**已采取的处理**：生成 `FIGSHARE-TAKEDOWN-REQUEST.md`，按官方要求备齐
「Figshare DOI、需下架版本、requester name、reason」四项，全文不含真实姓名与联系方式，
可一键发往 `support@figshare.com` 或在 https://support.figshare.com/ 提交；
同时请求同步更新 DataCite 中 v1/v2 DOI 的 creators 元数据。
工作区所有对外链接已统一为干净记录 `10.6084/m9.figshare.35018998.v1`，并明确标注不再传播旧链接。

## 平台限制造成的残留（无法通过 API 抹除）

1. **Zenodo 旧版本 `24269666` 的历史 PDF**：Zenodo 对已发布记录锁定存储桶，
   尝试删除/覆盖文件均返回 `403 Bucket is locked for modifications`，
   删除已发布 deposition 返回 404。该 PDF 的文档属性可能仍含早期署名；记录页面本身已是笔名。
2. **Figshare 旧记录 `35018683` 的 v1 / v2 版本快照**（即用户指出的链接）：其默认版本 v3 已是笔名，
   但 v1 显示账号显示名、v2 显示早期真实署名，且 v1/v2 共用的附件 PDF `71484547`
   内嵌 `/Author` 也是早期署名。全部可用端点已实测失败（详见上一节表格）；
   Figshare 官方说明免费账号须由支持团队执行 take-down，
   请求模板见 `FIGSHARE-TAKEDOWN-REQUEST.md`。
3. **DOI 注册机构（DataCite）、搜索引擎缓存与第三方聚合站点**的早期元数据快照，
   不属于作者可自行修改的范围。
4. **OSF 项目贡献者账号显示名**与 **GitHub 仓库 URL 中的账号名**属于账号层面标识，
   不是论文署名；GitHub 也可能在短期内缓存被重写前的提交对象。
5. **DataCite 中 Figshare 旧版本 DOI `10.6084/m9.figshare.35018683.v2` 的 creators
   仍为早期真实署名**：本轮核验 DOI 注册元数据时发现。该版本为只读，
   Figshare 拒绝修改已发布版本（403），只能由作者本人联系 support@figshare.com
   请求更新或遮蔽该 DOI 的历史元数据。其余三个 DOI 的 creators 均为 Didgeridoo。

> 本轮已把所有对外分享链接切换到上述**干净记录**，不再指向含早期署名的页面。
> 若需彻底清除第 1–3、5 项，须由作者本人分别联系 Zenodo 与 Figshare 支持
> （Figshare：support@figshare.com，工单标题 `Take down request`，正文见
> `FIGSHARE-TAKEDOWN-REQUEST.md`）请求删除或遮蔽历史版本，并请求搜索引擎刷新缓存；
> 本环境没有该权限。

## 引用格式

    Didgeridoo. 劳动价值论是历史性范畴：当代价值危机[Z/OL]. Zenodo, 2026.
    https://doi.org/10.5281/zenodo.24270266.

**边界不变**：以上均为网络预发布预印本，有 DOI、可引用，但未经同行评审，
不等同于期刊正式发表。
