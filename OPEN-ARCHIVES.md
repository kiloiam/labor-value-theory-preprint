# 全球无门槛期刊与资料库投递台 · 第五轮

> 署名统一 `Didgeridoo`；本文为网络预发布预印本，未经同行评审，不等同期刊正式发表。
> 本清单只记录真实门槛与实测结果，不代注册账号、不代勾选权属声明、不传播含早期署名的历史版本。

## 0. 概念澄清

「无门槛期刊」并不是准确说法：期刊均有同行评审与作者身份核验。真正无门槛的是
**预印本服务器与开放仓储**——无机构要求、无同行评审、自助发布、常带 DOI。

## 1. A 档 · 已发布 / 已收录

| 平台 | 状态 | 凭证 |
|---|---|---|
| [Zenodo](https://zenodo.org/records/24270266) | 已发布 · 并有新版本 24274919 | 自动被 DataCite / OpenAIRE 收割 |
| [Figshare](https://doi.org/10.6084/m9.figshare.35018998.v1) | 已发布（干净版本） | 旧记录历史版本已提交下架工单，勿传播 |
| [OSF](https://osf.io/wubs2/) | 已发布 | 项目可作 preprint 的补充材料关联 |
| [GitHub / Pages / Releases / Gist](https://github.com/kiloiam/labor-value-theory-preprint) | 已发布 · v3.0.0 | Pages 为规范站点，Release 为不可变资产 |
| [DataCite](https://api.datacite.org/dois/10.5281/zenodo.24270266) | 已收录（实测 200） | 无需操作 |
| [OpenAIRE](https://api.openaire.eu/search/publications?doi=10.5281/zenodo.24270266) | 已收录（实测 total=1, UNDER_CURATION） | 无需操作 |
| [Wayback Machine](https://web.archive.org/) | 40+ 快照已确认 | 本轮继续补存 |
| [Software Heritage](https://archive.softwareheritage.org/) | succeeded / full | 本轮继续请求存档 |
| [Telegraph (本轮新增)](https://telegra.ph/) | 本轮发布 10 语种摘要页 | 摘要 + 规范链接，不复制全文 |

## 2. B 档 · 无门槛，但需本人一步

| 平台 | 真实门槛 | 预填材料 |
|---|---|---|
| [viXra（本轮解锁）](https://vixra.org/submit) | 无审核、无需账号；官方要求 real name（自 2019-10-01 禁止笔名）——Didgeridoo 为作者真实英文姓名，已满足；需联系邮箱与本人权属声明 | **已由作者本人提交 · 待管理员处理（2026-11-16）**；见 viXra-form.md 与 paper-vixra.pdf。回执要求两天内等待结果、`Do not resubmit`；尚无编号／URL |
| [OSF Preprints（首选）](https://osf.io/preprints/) | 免费、无需机构邮箱、不验证作者身份；预审核（非同行评审） | 需你本人用该账号粘贴预填表单；见 open-archive-kit/OSF-Preprints-form.md |
| [SocArXiv](https://osf.io/preprints/socarxiv) | OSF 托管，社会科学方向；明确不验证作者身份 | 预填表单见 SocArXiv-form.md |
| [PhilArchive / PhilPapers](https://philarchive.org/) | 自助存档、无需机构，需账号；无同行评审 | 预填表单见 PhilArchive-form.md |
| [Preprints.org (MDPI)](https://www.preprints.org/) | 免费自助投稿，有范围与基本合规筛查（非同行评审） | 预填表单见 Preprints-org-form.md |
| [Internet Archive (item)](https://archive.org/) | 需 IA 账号与 S3 访问密钥才能上传 item；Wayback 存档无需账号 | 元数据与脚本已备好；需你提供 IA 凭证，见 ia-item-metadata.json |
| [BASE / CORE / OpenAlex / Semantic Scholar](https://www.base-search.net/) | 仅收割机构仓储 / DOI 登记源，不接受单篇投稿 | 靠 DOI 与 OAI-PMH 自动收割，有延迟；不可人工催收录 |

### 为什么必须由本人提交

- 这些平台需要一个属于你的账号，并要求勾选「本人有权发布该作品」的作者声明；
  代注册、代勾选权属声明都不合适。
- 现有 OSF 账号显示名与作者署名不一致；直接用它创建 preprint 会显示另一个名字，
  与去标识化要求冲突，故不代创建 OSF Preprints。
- 逐字段预填材料在 `open-archive-kit/`，打包为 `open-archive-kit.zip`。

### 推荐顺序

1. **OSF Preprints**（免费、无机构要求、录用后给 DOI、被 Google Scholar / OpenAlex 索引）
2. **SocArXiv**（社会科学对口，OSF 托管，明确不验证作者身份）
3. **PhilArchive / PhilPapers**（哲学与政治经济学方向自助存档）
4. **Preprints.org**（免费自助，有范围与合规筛查）

## 3. 自动收割链路（不可人工催收录）

```
Zenodo DOI → DataCite 登记 → OpenAIRE 收割（实测已收录）
            → OpenAlex / Semantic Scholar / BASE / CORE / Google Scholar（有延迟）
```

本轮实测（见 `AGGREGATORS-R5.json`）：

- DataCite `200`；OpenAIRE `total=1`，状态 `UNDER_CURATION`（已收录）
- OpenAlex `404`、Semantic Scholar `404`、Crossref `404`（Zenodo DOI 归属 DataCite，不在 Crossref）
- CORE `429`（限流）、BASE 提交页被反爬验证拦截，未核实其单篇政策，不作断言
- Google sitemap ping `404`、Bing sitemap ping `410`：端点已停用，改走 IndexNow + sitemap

## 4. C 档 · 不代做（身份与权属门槛）

| 平台 | 原因 |
|---|---|
| [arXiv](https://arxiv.org/) | 需 endorsement 背书人与机构认证，2026 年政策收紧（与姓名无关） |
| [SSRN / RePEc / EconStor / HAL / ResearchGate / Academia.edu](https://www.ssrn.com/) | 需平台账号与机构邮箱 / 机构认证（与姓名无关） |
| [正式期刊 / DOAJ 收录期刊](https://doaj.org/) | 需同行评审、通讯作者与身份核验（与姓名无关） |

特别说明：**viXra** 官方要求 real name、禁止笔名；作者已澄清 `Didgeridoo` 为真实英文姓名，
故该要求已满足，本轮已解锁并备好表单与 `paper-vixra.pdf`（仍需本人邮箱与提交）。
**arXiv** 2026 年政策收紧，
需背书与机构认证；正式期刊需同行评审与作者身份核验。

## 5. 预印本状态提醒

所有对外文案必须保留「网络预发布预印本，有 DOI、可引用，未经同行评审，
不等同期刊正式发表」。若日后正式发表，请在各平台补充 `relatedIdentifier` / 期刊 DOI。
