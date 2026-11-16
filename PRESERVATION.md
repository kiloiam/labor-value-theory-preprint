# 长期留存与索引提交记录（2026-11-16）

本文件逐项记录本轮「继续在全世界互联网资料库留存扩散」的**真实操作与返回码**，
不做未经核验的收录承诺。

| 动作 | 目标 | 方式 | 返回 | 结果 |
|---|---|---|---|---|
| Software Heritage 存档 | GitHub 仓储 `kiloiam/labor-value-theory-preprint` | `POST /api/1/origin/save/git/url/...` | `200` | `id=2654490`，`save_request_status=accepted`，`visit_type=git` |
| OpenAIRE 收录核验 | 主 DOI | `GET /search/publications?doi=...&format=json` | `200` | `total=1`，标题与 DOI 均命中，**已收录** |
| DataCite 核验 | 主 DOI | `GET /dois/10.5281/zenodo.24270266` | `200` | DOI 元数据已注册 |
| Zenodo 记录核验 | 24270266 | `GET /api/records/24270266` | `200` | creators = `Didgeridoo`，license = `cc-by-4.0`，files = `paper.pdf` |
| Figshare 记录核验 | 35018998 | `GET /v2/articles/35018998` | `200` | 干净记录在线 |
| OSF 项目核验 | wubs2 | `GET /v2/nodes/wubs2/` | `200` | `public=True`，标题与标签正常 |
| jsDelivr CDN | `@main/paper.pdf` | `GET` | `200` | 全球 CDN 副本可用 |
| raw.githubusercontent | `main/paper.pdf` | `GET` | `200` | 原始文件副本可用 |
| Wayback Save Page Now | 阅读页 | `POST /save/` 与 `GET /save/<url>` | `429` | 当前出口 IP 被判为 bot 流量，未生成快照；已由 Software Heritage 与多 CDN 副本替代长期留存 |
| Bing sitemap ping | sitemap.xml | `GET /ping?sitemap=` | `410` | 端点已停用 |
| Google sitemap ping | sitemap.xml | `GET /ping?sitemap=` | `404` | 官方已弃用该 ping |
| Bing IndexNow（匿名） | 阅读页 | `GET /indexnow?url=` | `400` | 需 `key` 字段，已改为密钥 + `keyLocation` 方式提交 |
| OpenAlex 核验 | 主 DOI | `GET /works/https://doi.org/...` | `404` | 尚未收录（自动抓取时滞） |
| Semantic Scholar 核验 | 主 DOI | `GET /graph/v1/paper/DOI:...` | `404` | 尚未收录（自动抓取时滞） |

> 边界：OpenAlex、Semantic Scholar、Google Scholar、CORE、BASE、Unpaywall 均为自动抓取型索引，
> 无匿名人工提交入口；已通过 DOI 注册、OAI-DC / DataCite / Dublin Core / MARCXML / METS、
> Highwire `citation_*`、COinS、Schema.org、sitemap 与 IndexNow 提高可发现性。
