# viXra 提交 · 最后一步操作说明

> **当前状态（2026-11-16）：作者已本人提交，回执显示「已接收 · 待管理员检查」。**
> 官方原文：两天内无回复即视为未接受，且 `Do not resubmit`——**不要重复提交**。
> 目前**没有** viXra 编号或公开链接。如需在处理前取消，用回执中的 cancellation form 与 form reference。
> 本文件以下的操作顺序与字段表保留，仅用于核对当时上传的 PDF 版本（`paper-vixra.pdf`，10 页）
> 以及后续撤销／替换流程。联系邮箱与 form reference 均未写入本包。

**表单**：https://fs23.formsite.com/viXra/form2/index.html
**官方提交说明**：https://vixra.org/submit
**专用投稿 PDF**：`paper-vixra.pdf`（10 页，文件名纯 ASCII，符合 viXra 要求）

> 提交是不可逆的公开发布行为：一经上线即永久记录，替换最多 4 次，
> 撤稿需理由且旧版本通常保留。**由你本人点击提交**，不代点。

## 两条来自官方表单原文的必读说明

1. **联系邮箱不会公开**。表单原文：*Your e-mail address will not be published unless you
   include it yourself in the PDF file, abstract or comment.* 因此你可以放心填一个能收信的邮箱；
   本包中的 PDF、摘要与 comment 均不含任何邮箱。不要填 QQ 邮箱或 GitHub noreply 地址。
2. **AI 辅助撰写声明**。表单原文：*The article should be written without AI assistance
   (Please go to ai.viXra.org to submit new scholarly article written with AI assistance).*
   The live viXra form states verbatim: "The article should be written without AI assistance (Please go to ai.viXra.org to submit new scholarly article written with AI assistance)." Only the author can judge whether this applies. If AI assistance was used, submit to https://ai.viXra.org instead of the main form. This kit does not make that declaration on the author's behalf.

## 操作顺序

1. 打开表单（建议 Chrome，表单注明 Firefox 有问题反馈）。
2. **方式 A（推荐，最快）**：按 `F12` 打开控制台，把 `vixra-autofill.js` 全文粘贴回车。
   脚本会自动填好除邮箱与文件外的所有字段，并把邮箱栏与文件栏标红。
3. **方式 B（不用控制台）**：按下方字段表逐项复制粘贴，值在 `vixra-prefill.json` 里。
4. 填入你的联系邮箱（标红栏）。
5. 在文件栏选择 `paper-vixra.pdf`。
6. 确认 AI 辅助条件、通读权属声明，勾选后**由你本人点击 Submit**。
7. 保存 viXra 返回的编号 / 链接，补进 `ARCHIVE-LINKS.md` 与 `MIRRORS.md`，并重新提交 IndexNow。

## 字段映射（来自实时表单，formsite `RESULT_*` 命名）

| 字段名 | 题目 | 填入值 |
|---|---|---|
| `RESULT_TextField-3` | Your e-mail address | （你本人填） |
| `RESULT_RadioButton-5` | PDF submission method (Upload / Link) | Radio-0 |
| `RESULT_FileUpload-6` | PDF document | （你本人填） |
| `RESULT_TextField-8` | Hyperlink to PDF | https://kiloiam.github.io/labor-value-theory-preprint/paper-vixra.pdf |
| `RESULT_RadioButton-10` | Science Category | Radio-32 |
| `RESULT_TextField-12` | Title of Paper (English) | The Labor Theory of Value as a Historical Category: The Contemporary Crisis of… |
| `RESULT_TextField-14` | Author(s) | Didgeridoo |
| `RESULT_TextArea-16` | Abstract (English) | Grounding its analysis in historical materialism, this article delineates the … |
| `RESULT_TextField-17` | Number of pages | 10 |
| `RESULT_TextField-19` | Comment (published on the abstract page) | CC BY 4.0. Online preprint, not peer reviewed. DOI 10.5281/zenodo.24270266. |
| `RESULT_TextArea-21` | Other instructions (NOT published) | The author publishes under the real English name Didgeridoo (not a pseudonym).… |

## 逐字段说明

- **`RESULT_TextField-3`** Your e-mail address：Required. viXra states this address will NOT be published unless you put it in the PDF, abstract or comment. Use a mailbox you can actually receive; do not use a QQ address or a noreply address.
- **`RESULT_RadioButton-5`** PDF submission method (Upload / Link)：Radio-0 = Upload (the recommended method). Use Radio-1 = Link only if the file exceeds 10 MB.
- **`RESULT_FileUpload-6`** PDF document：Browser security forbids scripts from choosing local files. Select paper-vixra.pdf yourself. Filename is pure ASCII, as viXra requires.
- **`RESULT_TextField-8`** Hyperlink to PDF：Direct .pdf URL, included as a redundancy. If the form complains it is not needed for Upload mode, clear this field.
- **`RESULT_RadioButton-10`** Science Category：Radio-32 = Humanities - Economics and Finance (closest match). No cross-listing is possible.
- **`RESULT_TextField-12`** Title of Paper (English)：viXra asks for an English title when the paper is not in English.
- **`RESULT_TextField-14`** Author(s)：Full author name, no titles, no all-caps. Didgeridoo is the author's real English name, satisfying viXra's real-name rule.
- **`RESULT_TextArea-16`** Abstract (English)：298 words (< 400 limit). Single line, no links, no formatting, ASCII only.
- **`RESULT_TextField-17`** Number of pages：paper-vixra.pdf has 10 pages (9 original + 1 supplementary English notice).
- **`RESULT_TextField-19`** Comment (published on the abstract page)：Keep it short; this appears on the abstract page and in listings.
- **`RESULT_TextArea-21`** Other instructions (NOT published)：For the administrator only. Do not paste any e-mail address or other personal detail here.

## 边界

- 脚本**不填邮箱、不选本地文件、不勾权属声明、不点提交**——浏览器安全策略与权属决定这四步只能由你完成。
- `RESULT_RadioButton-10` 选 `Radio-32`（Humanities - Economics and Finance）；viXra 不支持交叉分类。
- 摘要已压成单行纯 ASCII、298 词，低于 400 词上限；表单要求不要链接、图片、粗体、字号或颜色。
- 请勿在摘要、comment 或 PDF 中写入任何邮箱、即时通讯账号或其他姓名。
