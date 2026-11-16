# Figshare 历史版本下架请求（Take down request）

> **状态更新（2026-11-16 14:06）**：作者本人已通过 https://support.figshare.com/en/contact-us 提交本工单，等待 Figshare 团队处理（官方通常 48 小时内回复）。下方模板保留作存档与后续沟通依据；下架执行前 v1/v2 页面仍含早期署名。

**用途**：Figshare 免费账号无法通过 API 或网页自行下架已发布记录，官方要求提交支持工单。
本文件提供可直接发送的英文邮件／工单正文，以及中文对照。**全文不含任何真实姓名、QQ 号、邮箱等个人识别信息。**

- 支持邮箱：`support@figshare.com`（官方政策：邮件即自动创建工单，通常 48 小时内回复）
- 支持门户：https://support.figshare.com/
- 工单标题必须写：`Take down request`
- 官方要求提供的四项：Figshare DOI、需下架的版本号、requester name、reason

## 一、英文正文（建议用 Figshare 注册邮箱发送）

    To: support@figshare.com
    Subject: Take down request — Figshare DOI 10.6084/m9.figshare.35018683 (versions 1 and 2)

    Dear Figshare Support,

    Ticket title: Take down request

    I am the author and account owner of the public item identified below. I request
    that published versions 1 and 2 be taken down. If per-version removal is not
    possible, please remove the whole legacy item instead. A clean, anonymised
    replacement record is already published at DOI 10.6084/m9.figshare.35018998.v1.

    - Figshare DOI(s): 10.6084/m9.figshare.35018683.v1,
      10.6084/m9.figshare.35018683.v2
      (concept DOI 10.6084/m9.figshare.35018683)
    - Item versions to be taken down: version 1 and version 2
      (e.g. https://figshare.com/articles/preprint/___/35018683/2?file=71484547).
      Version 3 is already anonymised; removing the entire legacy item is also
      acceptable if that is simpler.
    - Requester name: Didgeridoo (pen name used for this work)
    - Reason: These two published historical versions still display the author's
      legal name in the page author field, and the attached PDF (file 71484547)
      still carries that name in its embedded document properties. The author now
      publishes under a pen name for privacy and does not wish the legal name to
      remain publicly associated with this work. The name is deliberately not
      reproduced in this request. Please also update or withhold the creators
      metadata registered with DataCite for the v1/v2 DOIs.

    Free figshare.com accounts cannot unpublish items themselves; the API unpublish
    endpoint returns "Insufficient permissions" and published versions are read-only
    snapshots. Support-assisted take-down is therefore required. The account owner
    can confirm this request from the registered email address if you need verification.

    Thank you,
    Didgeridoo

## 二、中文对照（便于本人核对，勿作为邮件正文发送）

- **Figshare DOI**：`10.6084/m9.figshare.35018683.v1`、`10.6084/m9.figshare.35018683.v2`（概念 DOI `10.6084/m9.figshare.35018683`）
- **需下架版本**：v1 与 v2；若平台无法按版本下架，可整条删除旧记录 `35018683`。v3 已是笔名版本，全新干净记录为 `10.6084/m9.figshare.35018998.v1`
- **requester name**：Didgeridoo（笔名）
- **reason**：两个历史版本页面的作者字段、以及附件 PDF（`71484547`）的内嵌文档属性中仍含作者不愿公开的法定姓名；作者已改用笔名发表，请求移除，并同步更新／遮蔽 DataCite 中 v1/v2 DOI 的 creators 元数据。邮件中不复述该姓名。

## 三、本轮已尝试但平台拒绝的自动途径（供支持团队参考）

| 操作 | 结果 |
|---|---|
| `PATCH` / `PUT /account/articles/35018683/versions/2`（改 authors） | `403 Insufficient permissions`；含 `full_name` 时 `422 Invalid params`。该端点 schema 仅允许 supplementary_fields / internal_metadata |
| `POST /account/articles/35018683/unpublish` | `403 Insufficient permissions`（免费账号无此权限，官方说明须由支持团队处理） |
| `DELETE /account/articles/35018683` | `400 Cannot delete a public article` |
| `PUT /account/articles/35018683/embargo`（article / file 级永久 embargo） | `400 Cannot add embargo to public item` |
| `DELETE /account/articles/35018683/files/71484547` | `204`，但只移除草稿引用；v1/v2 历史版本快照与下载链接不受影响 |
| `PUT /account/articles/35018683` 传 `is_public=false` / `status=draft` | `205`，平台忽略，公开状态仍为 true |
| `GET/PUT/PATCH /account/authors/26455234` | 仅 GET 可用，作者记录只读 |

## 四、本人操作清单（最快路径）

1. 用 **注册 Figshare 账号的邮箱**，把上面英文正文发到 `support@figshare.com`，标题保留 `Take down request`；或登录 https://support.figshare.com/ 提交同标题工单。
2. 如支持团队回复要求验证所有权，用注册邮箱回复确认即可（不要在回复里写出原姓名）。
3. 收到下架完成回复后，如需清除搜索引擎缓存，再向 Google Search Console / Bing 提交对应 URL 的移除请求；DataCite 的 v1/v2 DOI 元数据由 Figshare 侧更新。
4. 对外只分享干净记录：`10.6084/m9.figshare.35018998.v1`、Zenodo `10.5281/zenodo.24270266`、OSF https://osf.io/wubs2/ 。**不要再传播 `35018683` 的 v1/v2 链接。**

> 边界：以上均为网络预发布预印本，有 DOI、可引用，但未经同行评审，不等同期刊正式发表。
