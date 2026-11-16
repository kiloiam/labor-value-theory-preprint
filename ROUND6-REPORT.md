# 第六轮报告 · 继续全球开放发布与搜索可发现性最大化

**日期**：2026-11-16 · **署名**：`Didgeridoo`（作者真实英文姓名） · **许可**：CC BY 4.0
**状态**：网络预发布预印本，有 DOI、可引用，**未经同行评审，不等同期刊正式发表**

> 本轮回执见 `EXTERNAL-R6.json`、`AGGREGATORS-R6.json`、`BUILD-R6.json`、`VERIFY-R6.json`。
> 最终数字由收尾复验脚本写入，本文不预先写死未经实测的结果。

## 一、本轮目标与边界

用户要求「继续发布到全球各地的无门槛期刊和数据库和资料库，并尽最大可能优化搜索排名，做到能力范围内的最大值」。
本轮在第五轮成果上做**可验证的增量**，同时保留以下不可跨越的边界：

- 「无门槛期刊」不是准确说法：正式期刊都需同行评审与通讯作者；真正无门槛的是预印本服务器与开放仓储。不代注册账号、不代勾选权属声明、不伪造背书。
- 不承诺任何具体搜索排名，不承诺推送到每个关注者眼前，不承诺「文明灭亡为止」绝对存在。
- 白帽 SEO：不做 doorway page、不关键词堆砌、不买外链、不刷量、不伪装账号、不建站群、不操纵排名。
- 去标识化不变：不出现其他姓名、QQ 号、QQ 邮箱、单位或私人联系方式。

## 二、内容增量（本地已构建并校验）

| 项目 | 结果 |
|---|---|
| 新增检索意图 | **10 个**与第五轮不重叠的真实提问：主观价值论之别、马克思与李嘉图、价值与价格、抽象／具体劳动、价值形式、生产／非生产劳动、服务业、利润率趋向下降、经验检验、入门阅读顺序 |
| 新增页面 | 10 主题 × 中英双版 = **20 页**，每页含实质解答、3 条 FAQ、`QAPage` / `FAQPage` / `BreadcrumbList` / `Article` JSON-LD、hreflang、自引用 canonical、FAIR Signposting |
| 站内互链 | 重建第五轮 20 页，使全部 **40 页**互链覆盖 20 个主题（每页 19 个相关入口） |
| 生成式引擎语料 | `llms-topics-r6.txt`（10 组中英问答纯文本）；`llms.txt` 追加第六轮入口 |
| 机器可读页面图 | `schema-round6.jsonld`（`ScholarlyArticle` → `hasPart` 20 个新页） |
| 站点地图 | **132 → 158 个 URL**；新增 `sitemap-round6.xml`、`sitemap-index.xml` 收录、`robots.txt` 声明 |
| 内容诚实性 | 每页明确区分「背景通识」与「本预印本论点」，并声明论文不处理转型问题／经验检验／思想史考证，且未经同行评审 |

## 三、渠道实测与取舍（如实记录）

| 渠道 | 本轮结论 |
|---|---|
| Figshare | 干净记录 `35018998` v1 保持不动。`POST /account/articles/{id}/versions` 实测返回 **404**（该 API 无此路径），因此**未新建版本**，避免伪造成功或破坏唯一干净 DOI |
| Zenodo | 见 `EXTERNAL-R6.json` 的 `zenodo_v3` 回执；若失败则如实记录失败步骤与状态码 |
| viXra | 作者本人已于本轮前提交，状态为「已接收 · 待管理员检查」，**尚无编号或链接**，详见 `VIXRA-SUBMISSION-STATUS.md`；不得重复提交 |
| OpenAlex / Semantic Scholar / Crossref | 第五轮与本轮实测均 `404`：只从登记源自动收割，不接受单篇投稿；Crossref 404 属预期（Zenodo DOI 属 DataCite） |
| CORE / BASE | `429` 限流／反爬验证页，本轮不对二者单篇政策作断言 |
| Google / Bing sitemap ping | 端点已停用（`404` / `410`），改用 IndexNow |
| arXiv / HAL / SSRN / RePEc / ResearchGate / Academia.edu | 需背书、机构认证或同行评审；不代注册、不绕过 |
| OSF Preprints / SocArXiv / PhilArchive / Preprints.org / IA item | 需作者本人账号与权属声明；不代做 |

## 四、外部发布与索引提交

详见 `EXTERNAL-R6.json`（每步即时落盘，只记录真实 API 回执）。本轮覆盖：
Telegraph 索引页、GitHub Release `v5.0.0`、OSF 增量、公开 Gist、Software Heritage、Wayback、IndexNow 四端点、WebSub 两 feed。

## 五、边界与待办

1. viXra 若被接受，把分配到的编号／链接补进 `ARCHIVE-LINKS.md` / `MIRRORS.md` 并重提 IndexNow。
2. B 档其他平台仍需作者本人账号；不代提交。
3. Figshare 旧记录 `35018683` v1/v2 的下架工单仍等待官方执行，完整链接仅存在于工单材料，**请勿传播**。
4. OAI-PMH 为静态快照、IPFS 只算 CID 未永久 pin、torrent 需做种或 WebSeed 在线。
5. WorkBuddy 线上阅读页是否覆盖已分享链接，需作者本轮明确授权；未获授权不擅自重新发布。
