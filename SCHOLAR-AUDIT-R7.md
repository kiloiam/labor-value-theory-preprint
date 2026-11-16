# Google Scholar 收录合规审计 · Round 7

本审计只陈述可核验事实，不承诺 Google Scholar 一定收录。

| 官方要求 | 本站状态 | 本轮动作 |
|---|---|---|
| `citation_title` | 已存在 | 保持 |
| `citation_author` | 已存在（Didgeridoo） | 保持 |
| `citation_publication_date` | 已存在（2026/11/16） | 保持 |
| `citation_pdf_url` 指向可下载全文 PDF | 原为相对路径 `paper.pdf` | **改为绝对 URL** |
| PDF 可被 Googlebot 抓取 | `robots.txt` 全文允许 `/` | 复核通过 |
| PDF 文档属性含作者 | `/Author=Didgeridoo`（pypdf 核验） | 复核通过 |
| 摘要页 / 全文 HTML 地址 | 原先缺失 | **补 `citation_abstract_html_url` / `citation_fulltext_html_url`** |
| 语言、关键词、页码、许可 | 原先缺失 | **补 `citation_language` / `citation_keywords` / 页码 / `citation_license`** |
| 学术文档性质明确 | 声明为 preprint、未经同行评审 | 保持，不伪装成期刊论文 |

## 本轮修复的两个排名抑制项

1. **跨域名 canonical**：`index.html` 原先把规范链接指向带 `?sharecode=` 的 WorkBuddy 分享页，而其余 61 个页面与 sitemap 都声明 GitHub Pages 为规范地址。跨域 + 查询参数会让权重分散，并可能使规范 Pages URL 被判为副本。现已改为自引用绝对 URL，并同步 `og:url`。
2. **sitemap 重复 URL**：同一文档同时以 `/` 与 `/index.html` 提交。已移除后者。

## 不做的部分

Google Indexing API 仅适用于 `JobPosting` / `BroadcastEvent`，普通论文页调用属滥用；Google Search Console 的站点验证与「请求编入索引」需要账号本人操作，见 `webmaster-console.html`。不购买外链、不刷点击、不建站群、不堆砌关键词、不承诺具体排名。

