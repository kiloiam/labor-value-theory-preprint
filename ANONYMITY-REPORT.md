# 去标识化报告（Anonymization Report）

**署名**：Didgeridoo（笔名）　·　**执行日期**：2026-11-16　·　**许可**：CC BY 4.0（不变）

## 结论

所有**当前公开页面、元数据、引用文件、投稿材料与 PDF 文档属性**统一使用笔名 `Didgeridoo`，
不含真实姓名、通讯邮箱、工作单位等个人识别信息。原稿正文一字未改，仅重写了 PDF 的
`/Author`、`/Creator`、`/Title` 等文档属性并移除创建/修改时间指纹；清洗前后 9 页正文逐字一致。

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
- URL 百分号编码的姓名、BibTeX/CSL 的 `chen2026ltv` 拼音键、拆分的姓/名字段，均已替换。
- 本地填写页、私有配置、工作区日志与所有生成脚本同步脱敏，避免后续重跑把旧署名带回来。

## 平台限制造成的残留（无法通过 API 抹除）

1. **Zenodo 旧版本 `24269666` 的历史 PDF**：Zenodo 对已发布记录锁定存储桶，
   尝试删除/覆盖文件均返回 `403 Bucket is locked for modifications`，
   删除已发布 deposition 返回 404。该 PDF 的文档属性可能仍含早期署名；记录页面本身已是笔名。
2. **Figshare 旧记录 `35018683` 的 v1 / v2 版本快照**：其默认版本 v3 已是笔名，
   但 v1 显示账号显示名、v2 显示早期署名。实测：修改已发布版本返回
   `403 Insufficient permissions`；删除公开记录返回 `400 Cannot delete a public article`；
   加永久 embargo 返回 `400 Cannot add embargo to public item`。
3. **DOI 注册机构（DataCite）、搜索引擎缓存与第三方聚合站点**的早期元数据快照，
   不属于作者可自行修改的范围。
4. **OSF 项目贡献者账号显示名**与 **GitHub 仓库 URL 中的账号名**属于账号层面标识，
   不是论文署名；GitHub 也可能在短期内缓存被重写前的提交对象。

> 本轮已把所有对外分享链接切换到上述**干净记录**，不再指向含早期署名的页面。
> 若需彻底清除第 1–3 项，须由作者本人分别联系 Zenodo 与 Figshare 支持
> （Figshare：support@figshare.com）请求删除或遮蔽历史版本，并请求搜索引擎刷新缓存；
> 本环境没有该权限。

## 引用格式

    Didgeridoo. 劳动价值论是历史性范畴：当代价值危机[Z/OL]. Zenodo, 2026.
    https://doi.org/10.5281/zenodo.24270266.

**边界不变**：以上均为网络预发布预印本，有 DOI、可引用，但未经同行评审，
不等同于期刊正式发表。
