# 第四轮全量报告：可发现性、全球留存与合规传播

> 2026-11-16 · 劳动价值论是历史性范畴：当代价值危机 · 笔名 Didgeridoo · CC BY 4.0
> 主 DOI `10.5281/zenodo.24270266` · 概念 DOI `10.5281/zenodo.24269665` · Figshare `10.6084/m9.figshare.35018998.v1` · OSF https://osf.io/wubs2/

## 一、本轮做了什么（与前三轮的差别）

前三轮已完成：27 处公开副本、8 个法域、40+ Wayback 快照、10 语种落地页、63 URL 站点地图、四大 DOI / 仓储。本轮**不重复堆副本**，而是补齐此前没有的四个层次：

| 层 | 新增 | 解决的问题 |
|---|---|---|
| 机器可发现 | FAIR Signposting（linkset + 15 页 `<link rel>`）、RO-Crate 1.1、CodeMeta、OAI-PMH 静态快照、Wikidata `about` | 收割器 / 引用管理器 / 知识图谱不必解析正文就能找到 DOI、全文、许可、元数据 |
| 生成式引擎 | `llms-full.txt`、DefinedTermSet 术语本体、20 条中英结构化问答、主题导览页、17 类 AI 爬虫显式许可 | 让「劳动价值论是什么 / 自动化时代是否成立」等真实问句能命中并可被引用 |
| 去中心化留存 | BitTorrent + WebSeed + Magnet、BagIt holey bag、IPFS CIDv1、Memento TimeMap | 不再依赖任何单一网站；任一份幸存副本可重建其余 |
| 合规传播 | 10 语种文案 + 12 平台一键预填发布入口 | 把发布能力交给作者本人，不代发、不刷量 |

## 二、实测结果（全部为真实执行）

| 项目 | 结果 |
|---|---|
| GitHub commit | `4599dd3d5f0a71f9482dfb30f84ef9fef227a90e`（main 已推送） |
| 站点地图 URL | 99 个，Pages 实测 99/99 可达 |
| IndexNow | 99 个 URL × 4 个端点，4 个 `200` |
| AI 爬虫许可 | 17 类（GPTBot / OAI-SearchBot / PerplexityBot / ClaudeBot / Google-Extended / CCBot 等） |
| SHA-256 校验 | 68/68 ALL OK |
| 脱敏扫描 | PASS · 0 处硬违规 · 传播面 0 泄露 |
| 离线保存包 | 55 条目、1,557,043 字节（另有独立 `.sha256`） |
| BitTorrent | 2 个 swarm，7 个 HTTP WebSeed，浏览器内 WebTorrent 下载 |
| BagIt | 28 个 payload 文件，`fetch.txt` 指向 jsDelivr 全球 CDN |
| IPFS | 13 个 CIDv1 raw（**未 pin**，见边界） |
| Memento | 40 个 Wayback 快照的机器可读 TimeMap |
| 全球镜像实测 | 28/29 可达 |
| GitHub Release `v3.0.0` | 30 个不可变资产 |
| 公开 Gist | 19 个文件 |
| OSF 项目 | 60 个文件 |
| Software Heritage | 主仓库 + Gist 两次存档请求受理 |
| Zenodo 新版本 | `10.5281/zenodo.24274919`（DataCite 已登记，creators 仅 `Didgeridoo`） |
| Wayback 本轮 | 10 个目标受理，CDX 确认 10 个 |

## 三、可直接使用入口

- 全文与影印：<https://kiloiam.github.io/labor-value-theory-preprint/>
- 主题导览（搜索「劳动价值论」的入口页）：<https://kiloiam.github.io/labor-value-theory-preprint/topic-ltv.html>
- 结构化问答：<https://kiloiam.github.io/labor-value-theory-preprint/discovery-qa.html> · 术语表：<https://kiloiam.github.io/labor-value-theory-preprint/terms.html>
- 一键传播台：<https://kiloiam.github.io/labor-value-theory-preprint/broadcast.html>（**由你本人点击发布**）
- P2P 留存：<https://kiloiam.github.io/labor-value-theory-preprint/torrents.html> · 冗余地图：<https://kiloiam.github.io/labor-value-theory-preprint/forever.html>
- AI 全文语料：<https://kiloiam.github.io/labor-value-theory-preprint/llms-full.txt> · 站点地图：<https://kiloiam.github.io/labor-value-theory-preprint/sitemap.xml>

## 四、边界（必须如实说明）

1. **不能保证「搜索劳动价值论排第一」，也不能保证「推送到每个关注者眼前」。**这是经典高频概念，权威页面竞争极强；排名与推荐由搜索引擎/平台算法决定。本轮做的是白帽可发现性——结构化数据、术语本体、问答内容、站点地图、AI 爬虫许可、索引提交——最大化「主动检索或被引用的命中概率」。不刷量、不买外链、不伪装账号、不操纵排名。
2. **不能代发内容。** 社交平台、邮件、论坛发帖需要账号且属于主动推送，本轮只生成预填链接与文案；请在确有研究兴趣的社群自行发布，不要群发陌生收件人。
3. **不能承诺「到人类文明灭亡仍存在」。** 任何数字系统都依赖维护它的机构与读者。本轮最大化的是冗余度、可校验性与可重建性；CC BY 4.0 明确邀请后来者复印、翻译、做种与再托管。
4. **OAI-PMH 是静态响应快照，不是可实时收割的 live endpoint**；**IPFS 只计算了 CID，未执行永久 pin**（公共固定服务需注册账号与凭证，未代作者注册）；**BitTorrent 需要有人做种或 WebSeed 在线**；**BagIt 依赖 fetch.txt 中的 URL 仍可访问**。
5. **未重新发布 WorkBuddy 线上站点**：本轮未收到明确的重新发布授权。GitHub Pages 规范站点已含全部第四轮内容；如需让 WorkBuddy 影印阅读页也同步，请明确说「重新发布」。
6. **仍为网络预发布预印本**：有 DOI、可引用，未经同行评审，不等同期刊正式发表，不构成学术成果认定依据。所有对外文案都必须保留这一表述。
7. **Figshare 旧记录 `35018683` v1/v2** 仍含早期署名，官方下架工单已提交、等待执行；完整链接仅存在于 `FIGSHARE-TAKEDOWN-*` 工单材料中，**请勿传播**。
8. **Zenodo 新版本**：`publish` 返回 `202`、DOI `10.5281/zenodo.24274919`、16 个文件上传成功；已通过 **DataCite 注册表**独立复核元数据——`creators` 仅 `Didgeridoo`，标题与 publisher（Zenodo）正确。Zenodo 网页 / 记录 API 读取时返回 `403/503`（反爬或临时不可用），本轮覆写元数据的 `PUT` 返回 `415` 未生效，因此继承的是上一版已去标识化的元数据，署名仍为笔名、未引入任何真实身份信息。

## 五、隐私

全量扫描 125 个文件（含 ZIP 内条目与 PDF 文档属性）：真实姓名 / QQ 号 / QQ 邮箱 / 旧号 / OSF 显示名 **0 命中**；公开署名统一 `Didgeridoo`；档案中的名称即笔名，邮箱为 GitHub noreply 别名，作者简介不含机构、职称、邮箱、电话或地名。

## 六、可复核凭据

<https://kiloiam.github.io/labor-value-theory-preprint/VERIFY-R4.json>、<https://kiloiam.github.io/labor-value-theory-preprint/EXTERNAL-R4.json>、<https://kiloiam.github.io/labor-value-theory-preprint/SYNC-R4.json>、<https://kiloiam.github.io/labor-value-theory-preprint/MIRROR-HEALTH.json>、`CHECKSUMS.sha256`、`PRESERVATION-MANIFEST.json`、`P2P-MANIFEST.json`、`ipfs-manifest.json`、`timemap.json`、`ro-crate-metadata.json`。
