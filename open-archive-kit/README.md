# 全球开放平台投递包 · 使用说明

本包只提供**预填内容**；注册、勾选权属声明、上传与提交均由你本人完成。

## 顺序

1. `OSF-Preprints-form.md` → https://osf.io/preprints/ （首选，免费、给 DOI）
2. `SocArXiv-form.md` → https://osf.io/preprints/socarxiv
3. `viXra-form.md` + **`VIXRA-SUBMIT.md`** → 上传 `paper-vixra.pdf`；`vixra-autofill.js` 可一键填好除邮箱与文件外的全部字段（真实英文姓名已满足其 real-name 要求；需你的联系邮箱与本人提交）
4. `PhilArchive-form.md` → https://philarchive.org/
5. `Preprints-org-form.md` → https://www.preprints.org/
6. `ia-item-metadata.json` → Internet Archive（需你自己的 IA 凭证）

## 通用字段

`metadata-universal.json`、`abstract-zh.txt`、`abstract-en.txt`、`cover-letter-preprint.md`。

## 上传文件

- 通用平台：下载 `paper.pdf`（`/Author` 已为 `Didgeridoo`，不含其他身份信息）。
- **viXra 专用**：下载 `paper-vixra.pdf`，它在原 PDF 后附加英文声明页，内含英文标题、
  298 词英文摘要、CC BY 4.0 许可、DOI 与规范链接——viXra 规定站外链接只能写在 PDF 内，
  因此投 viXra 必须用这个版本，不要用 `paper.pdf`。

## 三条硬约束

- 署名只填 `Didgeridoo`；机构字段留空；不填真实姓名、单位、QQ 号或私人联系方式。
- 类型选 Preprint；任何场合都保留「未经同行评审，不等同期刊正式发表」。
- `Didgeridoo` 是真实英文姓名，可满足 viXra 的 real-name 要求；但不要填其他姓名、机构或 QQ 相关信息。
  若平台要求提供其他法定姓名或机构认证（arXiv、HAL、SSRN），**不要提交**。

## 提交之后

把新链接补进 `ARCHIVE-LINKS.md` / `MIRRORS.md`，并通过 IndexNow 重新提交新 URL。
