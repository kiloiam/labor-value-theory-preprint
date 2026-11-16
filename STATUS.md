# 全部操作状态清单（2026-11-16 · 最终）

## 已真实执行完成

1. **Zenodo**：主 DOI `10.5281/zenodo.24270266` → https://doi.org/10.5281/zenodo.24270266 ，CC BY 4.0，作者Didgeridoo，paper.pdf 完整可下载。
2. **Figshare**：v2 DOI `10.6084/m9.figshare.35018998.v1` → https://doi.org/10.6084/m9.figshare.35018998.v1 ，分类 Political economy and social change，CC BY 4.0；v2 已把公开署名由账号名修正为「Didgeridoo」。
3. **OSF**：公开项目 https://osf.io/wubs2/ ，public=True，PDF 1,388,974 字节，项目描述已标注作者。
4. **GitHub**：公开仓储 https://github.com/kiloiam/labor-value-theory-preprint ，v1.0.0 Release 附 PDF；本轮更新后推送新版本。
5. **在线阅读页与投递工作台**：同一站点两个页面，全文、9 页原稿影印、元数据、投稿信、门槛与核验结果全部在线；静态资源分享码问题已修复。
6. **完整提交包**：PDF、全文 Markdown、中英文摘要、metadata.json、CITATION.cff、投稿信、政策要点、校对记录、预填表单、一键脚本。
7. **文字校对**：英文摘要 19 类连写/标点错误已在所有在线交付物与元数据中修正，原稿 PDF 一字未改。
8. **百晓智能**：期刊匹配、10/10 条参考文献核验、审稿人候选、预印本政策检索，结果已写入投递台。
9. **一键脚本已按实测修复**：Zenodo 的 related_identifiers/500 与 license 写法、Figshare 的 upload_url 分片端点、license id、必填 categories；dry-run 通过。

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

应作者要求，本预印本在所有公开页面、元数据、引用文件、投稿材料与 PDF 内嵌属性中统一使用笔名 **Didgeridoo**，不含真实姓名、通讯邮箱、单位等个人识别信息。PDF 的 `/Author`、`/Creator` 及创建/修改时间等文档属性已清洗。许可仍为 CC BY 4.0，引用时请著录笔名。

注：早期已发布记录的版本历史与 DOI 注册机构的缓存可能仍保留旧署名，平台方版本快照无法由作者自行抹除；当前公开显示版本与本站全部内容均为笔名。
