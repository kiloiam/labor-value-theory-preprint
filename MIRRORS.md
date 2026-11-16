# 跨机构副本登记表（Redundancy Map）

> 《劳动价值论是历史性范畴：当代价值危机》 · Didgeridoo · CC BY 4.0 · 2026-11-16
> 生成依据：`PRESERVATION-MANIFEST.json`。本表只列干净、可安全传播的公开副本。

## 设计原则

任何**单独一个**幸存副本都必须足以还原全文、署名、许可协议与其他副本地址。
因此副本分散在不同机构、不同法域、不同协议：DOI 仓储、Git 版本库、UNESCO 源代码永久存档、
网页时间胶囊、全球 CDN、学术索引，以及无需任何软件即可阅读的纯文本 / 单文件 HTML 离线包。

共 **16 处**登记副本，覆盖 **8 个法域或区域**、**8 类存储层**。

| 机构 | 法域 / 区域 | 类型 | 地址 |
|---|---|---|---|
| Zenodo (CERN / OpenAIRE) | EU / Switzerland | DOI-registered open repository | https://doi.org/10.5281/zenodo.24270266 |
| Zenodo (CERN) | EU / Switzerland | concept DOI (always resolves to latest version) | https://doi.org/10.5281/zenodo.24269665 |
| Figshare (Digital Science) | UK | DOI-registered open repository | https://doi.org/10.6084/m9.figshare.35018998.v1 |
| Open Science Framework (Center for Open Science) | US | open project storage with versioned files | https://osf.io/wubs2/ |
| GitHub Pages | US | static full-text site | https://kiloiam.github.io/labor-value-theory-preprint/ |
| GitHub | US | versioned git repository | https://github.com/kiloiam/labor-value-theory-preprint |
| GitHub Releases | US | immutable tagged release with binary assets | https://github.com/kiloiam/labor-value-theory-preprint/releases/tag/v1.0.0 |
| WorkBuddy hosted site | CN | hosted reading page with 9 facsimile pages | https://wbapp-qjvohz0ip85p3s9mnjs8do.app.workbuddy.host/?sharecode=ZILGUJCJKG |
| Software Heritage (UNESCO / Inria) | FR / EU | permanent source-code archive with SWHID | https://archive.softwareheritage.org/ |
| Internet Archive Wayback Machine | US | web time-capsule snapshots (12 + new captures) | https://web.archive.org/web/20261116061932/https://kiloiam.github.io/labor-value-theory-preprint/ |
| OpenAIRE | EU | Europe-wide open scholarly index (already indexed) | https://api.openaire.eu/search/publications?doi=10.5281/zenodo.24270266 |
| DataCite | international | DOI metadata registry | https://commons.datacite.org/doi.org/10.5281/zenodo.24270266 |
| jsDelivr global CDN | multi-region | CDN edge copy | https://cdn.jsdelivr.net/gh/kiloiam/labor-value-theory-preprint@main/paper.pdf |
| raw.githubusercontent.com | US | raw file mirror | https://raw.githubusercontent.com/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| raw.githack.com | multi-region | independent CDN mirror | https://raw.githack.com/kiloiam/labor-value-theory-preprint/main/paper.pdf |
| gitcdn.link | multi-region | independent CDN mirror | https://gitcdn.link/cdn/kiloiam/labor-value-theory-preprint/main/paper.pdf |

## 三层可读性

| 层级 | 文件 | 所需软件 |
|---|---|---|
| 1 · 零依赖 | `PAPER-PLAINTEXT.txt` | 任意文本读取器（甚至打印在纸上） |
| 2 · 单文件 | `paper-standalone.html` | 任意浏览器，不需联网、不需外部资源 |
| 3 · 原排版 | `paper.pdf` | PDF 阅读器 |

## 校验

`CHECKSUMS.sha256` 给出每个核心文件的 SHA-256。恢复某副本后先比对哈希，
再以 `PRESERVATION-MANIFEST.json` 查其余副本地址。全文 CC BY 4.0，
重新托管、翻译、再发布均无需额外授权，保留署名 `Didgeridoo` 即可。

## 边界

- 数字系统无法承诺「文明灭亡后仍存在」；本表最大化的是**冗余度与可恢复性**，不是永恒性。
- 所有公开副本统一署名 `Didgeridoo`，不含真实姓名、通讯邮箱、QQ 号或 QQ 邮箱。
- Figshare 旧记录 `35018683` 的 v1 / v2 含早期署名，已提交官方下架工单，**不在本表内、请勿传播**。
- 以上均为网络预发布预印本，有 DOI、可引用，但未经同行评审，不等同期刊正式发表。
