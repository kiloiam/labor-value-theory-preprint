#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
论文预印本「一键分发」脚本
==========================

用途：把本目录中的 paper.pdf 与 metadata.json 分发到有公开 API 的开放仓储；
      对没有公开 API 的平台，生成可直接粘贴的预填表单数据。

重要：
1. 默认 --dry-run，只预演、不联网、不提交。
2. --live 只有在同目录提供 tokens.json（或设置了对应环境变量）时才会真正提交。
3. 提交动作会以你的账号名义完成，等同于你本人勾选原创性声明与许可协议。
   请确认你是作者本人、且已阅读各平台的条款后再运行 --live。
4. 平台 API 可能调整；若返回 404/410/401，请按各平台官方文档核对端点。
   本脚本不存储、不回传任何令牌。

用法：
    python submit_all.py                # 预演全部平台
    python submit_all.py --live         # 真正提交（需 tokens.json / 环境变量）
    python submit_all.py --live --only zenodo
"""

import argparse
import hashlib
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PDF = ROOT / "paper.pdf"
META_FILE = ROOT / "metadata.json"
TOKENS_FILE = ROOT / "tokens.json"
FORM_DIR = ROOT / "form-data"
LOG_FILE = ROOT / "submission-log.json"

MANUAL_PLATFORMS = [
    {
        "key": "chinaxiv",
        "name": "ChinaXiv 中国科学院科技论文预发布平台",
        "url": "https://chinaxiv.org/",
        "reason": "无公开提交 API；需实名注册、学科审核",
        "fields_hint": "标题 / 摘要 / 关键词 / 学科分类（马克思主义理论、政治经济学）/ 作者实名与单位 / PDF",
    },
    {
        "key": "academic-world",
        "name": "哲学社会科学预印本平台（中国人民大学「学术世界」）",
        "url": "https://www.xueshushijie.cn/",
        "reason": "国内首个哲社预印本平台，500 余家期刊共建；无公开提交 API，需注册作者账号",
        "fields_hint": "标题 / 摘要 / 关键词 / 学科（马克思主义理论·政治经济学）/ 作者实名与单位 / PDF",
    },
    {
        "key": "ssrn",
        "name": "SSRN (Elsevier)",
        "url": "https://www.ssrn.com/",
        "reason": "无开放提交 API；需账号与邮箱验证",
        "fields_hint": "Title / Abstract / Keywords / JEL / Author profile / PDF",
    },
    {
        "key": "arxiv",
        "name": "arXiv",
        "url": "https://arxiv.org/",
        "reason": "本稿属人文社科，学科适配度低；且需 endorsement 背书",
        "fields_hint": "不建议优先投递；如确需，先确认分类与保举人",
    },
    {
        "key": "philpapers",
        "name": "PhilPapers",
        "url": "https://philpapers.org/",
        "reason": "索引/聚合平台，需账号提交条目",
        "fields_hint": "标题 / 作者 / 摘要 / 分类 / 预印本 URL",
    },
    {
        "key": "repec",
        "name": "RePEc / EconPapers",
        "url": "https://repec.org/",
        "reason": "需机构仓储或系列登记，个人无法直接提交",
        "fields_hint": "通过所在机构知识库登记后自动汇聚",
    },
]

API_PLATFORMS = [
    {"key": "zenodo", "name": "Zenodo (CERN)", "env": "ZENODO_TOKEN", "url": "https://zenodo.org/"},
    {"key": "figshare", "name": "Figshare", "env": "FIGSHARE_TOKEN", "url": "https://figshare.com/"},
    {"key": "osf", "name": "OSF (Open Science Framework)", "env": "OSF_TOKEN", "url": "https://osf.io/"},
]


def load_meta():
    if not META_FILE.exists():
        fail("缺少 metadata.json")
    raw = json.loads(META_FILE.read_text(encoding="utf-8"))
    return raw.get("metadata", raw)


def load_tokens():
    tokens = {}
    if TOKENS_FILE.exists():
        try:
            tokens = json.loads(TOKENS_FILE.read_text(encoding="utf-8"))
        except Exception as exc:
            fail("tokens.json 解析失败: %s" % exc)
    for platform in API_PLATFORMS:
        env_val = os.environ.get(platform["env"])
        if env_val:
            tokens[platform["key"]] = env_val
    return tokens


def fail(msg):
    print("[ERROR] " + msg)
    sys.exit(1)


def http(method, url, token=None, body=None, payload=None, extra_headers=None):
    headers = {"Accept": "application/json"}
    data = None
    if payload is not None:
        data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        headers["Content-Type"] = "application/json"
    elif body is not None:
        data = body
        headers["Content-Type"] = "application/octet-stream"
    if token:
        headers["Authorization"] = token
    if extra_headers:
        headers.update(extra_headers)
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
            return resp.status, (json.loads(raw) if raw.strip().startswith(("{", "[")) else raw)
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        return exc.code, {"error": detail}
    except Exception as exc:
        return 0, {"error": str(exc)}


def zenodo_submit(meta, token, pdf_bytes):
    """Zenodo legacy deposition API（若返回 404/410 请改用新版 /api/records 流程）。"""
    base = "https://zenodo.org/api/deposit/depositions"
    deposition_meta = {
        "title": meta["title"],
        "upload_type": "publication",
        "publication_type": "preprint",
        "description": meta["description"],
        "creators": [{"name": c["name"], "affiliation": c.get("affiliation", "")} for c in meta["creators"]],
        "keywords": meta.get("keywords", []),
        "language": "zho",
        # 实测：legacy deposition API 接受小写 cc-by-4.0；"CC-BY-4.0" 会被服务端拒绝。
        "license": "cc-by-4.0",
        "publication_date": meta.get("publication_date"),
        # 实测：传 related_identifiers（含 scheme:url）会让 Zenodo 返回 500。
        # 改为把等价链接写进 notes，既保留交叉引用又能成功发布。
        "notes": (meta.get("notes", "") + "\n\n网络预发布副本：\n" + "\n".join(
            "- " + x["identifier"] for x in meta.get("related_identifiers", []) if x.get("identifier"))).strip(),
    }
    status, dep = http("POST", base + "?access_token=" + urllib.parse.quote(token),
                       payload={"metadata": deposition_meta})
    if status >= 400 or not isinstance(dep, dict) or "id" not in dep:
        return {"ok": False, "step": "create_deposition", "status": status, "response": dep}
    dep_id = dep["id"]
    links = dep.get("links", {})
    upload = None
    if links.get("bucket"):
        url = links["bucket"].rstrip("/") + "/" + urllib.parse.quote("paper.pdf") + "?access_token=" + urllib.parse.quote(token)
        upload = http("PUT", url, body=pdf_bytes)
    elif links.get("files"):
        # 旧版 multipart 上传；此处用简化 body，必要时按官方文档改为 multipart/form-data
        upload = http("POST", links["files"] + "?access_token=" + urllib.parse.quote(token), body=pdf_bytes)
    else:
        return {"ok": False, "step": "find_upload_endpoint", "response": dep}
    status_u, resp_u = upload
    if status_u >= 400:
        return {"ok": False, "step": "upload_file", "status": status_u, "response": resp_u}
    status_p, pub = http("POST", "%s/%s/actions/publish?access_token=%s" %
                         (base, dep_id, urllib.parse.quote(token)))
    if status_p >= 400:
        return {"ok": False, "step": "publish", "status": status_p, "response": pub}
    return {"ok": True, "deposition_id": dep_id,
            "doi": pub.get("doi") if isinstance(pub, dict) else None,
            "record_url": ("https://doi.org/" + pub.get("doi")) if isinstance(pub, dict) and pub.get("doi") else links.get("html")}


def figshare_submit(meta, token, pdf_bytes):
    auth = "token " + token
    api = "https://api.figshare.com/v2/account/articles"
    payload = {
        "title": meta["title"],
        "description": meta["description"],
        "keywords": meta.get("keywords", []),
        "defined_type": "preprint",
        # 实测：/v2/licenses 中 CC BY 4.0 的 id 是 1；id=3 是 MIT（软件许可），勿用。
        "license": 1,
        # 实测：不设 categories 时 /publish 会返回 400 "Missing mandatory value: categories"。
        # 27517 = Political economy and social change（is_selectable=true 的叶子分类）。
        "categories": [27517],
    }
    status, art = http("POST", api, token=auth, payload=payload)
    if status >= 400 or not isinstance(art, dict):
        return {"ok": False, "step": "create_article", "status": status, "response": art}
    loc = art.get("location") or (api + "/" + str(art.get("id")))
    art_id = str(art.get("id") or loc.rstrip("/").split("/")[-1])
    file_payload = {"name": "paper.pdf", "size": len(pdf_bytes),
                    "md5": hashlib.md5(pdf_bytes).hexdigest()}
    status_f, f = http("POST", api + "/" + art_id + "/files", token=auth, payload=file_payload)
    if status_f >= 400 or not isinstance(f, dict):
        return {"ok": False, "step": "create_file_record", "status": status_f, "response": f}
    f_loc = f.get("location") or (api + "/" + art_id + "/files/" + str(f.get("id")))
    status_i, info = http("GET", f_loc, token=auth)
    # 实测：分片上传端点是 file info 的 upload_url（形如
    # https://fup-eu-west-1.figshare.com/upload/<token>），而非 /account/articles/.../files/...
    # 用后者会得到 404。该端点靠 URL 中的 upload_token 鉴权，不要带 Authorization。
    up_url = info.get("upload_url") if isinstance(info, dict) else None
    if not up_url:
        return {"ok": False, "step": "get_upload_url", "status": status_i, "response": info}
    parts = info.get("parts") or [{"partNo": 1, "startOffset": 0,
                                  "endOffset": len(pdf_bytes) - 1}]
    for part in parts:
        start = int(part.get("startOffset", 0))
        end = int(part.get("endOffset", len(pdf_bytes) - 1)) + 1
        no = part.get("partNo", 1)
        status_u, resp_u = http("PUT", up_url.rstrip("/") + "/" + str(no),
                                body=pdf_bytes[start:end])
        if status_u >= 400:
            return {"ok": False, "step": "upload_part", "status": status_u, "response": resp_u}
    # 标记上传完成，等待文件进入 available 后再发布
    http("POST", f_loc, token=auth, payload={})
    status_p, pub = http("POST", api + "/" + art_id + "/publish", token=auth)
    if status_p >= 400:
        return {"ok": False, "step": "publish", "status": status_p, "response": pub}
    return {"ok": True, "article_id": art_id, "url": "https://figshare.com/articles/" + art_id}


def osf_submit(meta, token, pdf_bytes):
    auth = "Bearer " + token
    api = "https://api.osf.io/v2/nodes/"
    payload = {"data": {"type": "nodes", "attributes": {
        "title": meta["title"],
        "description": meta["description"],
        "category": "project",
        "tags": meta.get("keywords", [])[:10],
        "public": True,
    }}}
    status, node = http("POST", api, token=auth, payload=payload)
    if status >= 400 or not isinstance(node, dict):
        return {"ok": False, "step": "create_node", "status": status, "response": node}
    node_id = node.get("data", {}).get("id")
    if not node_id:
        return {"ok": False, "step": "node_id", "response": node}
    up_url = ("https://files.osf.io/v1/resources/%s/providers/osfstorage/?kind=file&name=%s" %
              (node_id, urllib.parse.quote("paper.pdf")))
    status_u, resp_u = http("PUT", up_url, token=auth, body=pdf_bytes)
    if status_u >= 400:
        return {"ok": False, "step": "upload_file", "status": status_u, "response": resp_u}
    return {"ok": True, "node_id": node_id, "url": "https://osf.io/" + node_id + "/"}


SUBMITTERS = {"zenodo": zenodo_submit, "figshare": figshare_submit, "osf": osf_submit}


def write_form_data(meta):
    FORM_DIR.mkdir(exist_ok=True)
    common = {
        "title": meta["title"],
        "abstract": meta["description"][:1200],
        "keywords": meta.get("keywords", []),
        "author": [c["name"] for c in meta["creators"]],
        "affiliation": "（待补：工作单位）",
        "license": "CC BY 4.0",
        "language": meta.get("language", "zh"),
        "file": "paper.pdf",
        "preprint_url": meta.get("related_identifiers", [{}])[0].get("identifier", ""),
        "note": "提交前请补齐单位、ORCID、通讯邮箱；本文件仅供粘贴，不代表已提交",
    }
    for p in MANUAL_PLATFORMS:
        data = {
            "platform": p["name"],
            "entry_url": p["url"],
            "submission_method": "人工网页提交（无公开 API）",
            "reason": p["reason"],
            "fields": dict(common, extra_fields_hint=p["fields_hint"]),
        }
        (FORM_DIR / (p["key"] + ".json")).write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description="论文预印本一键分发")
    ap.add_argument("--live", action="store_true", help="真正调用 API 提交（需 tokens.json 或环境变量）")
    ap.add_argument("--only", help="只处理指定平台 key，如 zenodo / figshare / osf")
    args = ap.parse_args()

    if not PDF.exists():
        fail("缺少 paper.pdf")
    meta = load_meta()
    pdf_bytes = PDF.read_bytes()
    tokens = load_tokens()

    write_form_data(meta)

    print("=" * 68)
    print("论文预印本分发 · " + ("LIVE 模式" if args.live else "DRY-RUN 预演（不会联网提交）"))
    print("=" * 68)
    print("标题：%s" % meta["title"])
    print("作者：%s" % ", ".join(c["name"] for c in meta["creators"]))
    print("文件：%s (%d bytes, md5 %s)" % (PDF.name, len(pdf_bytes), hashlib.md5(pdf_bytes).hexdigest()))
    print("许可：%s" % meta.get("license", {}).get("id", "CC-BY-4.0"))
    print("时间戳：%s" % datetime.now(timezone.utc).isoformat())
    print()

    results = []
    for p in MANUAL_PLATFORMS:
        if args.only and args.only != p["key"]:
            continue
        print("[表单] %-42s %s" % (p["name"], p["url"]))
        print("       预填数据 -> form-data/%s.json（需本人登录网页提交）" % p["key"])
        results.append({"platform": p["key"], "mode": "manual", "status": "form_data_ready"})

    for p in API_PLATFORMS:
        if args.only and args.only != p["key"]:
            continue
        token = tokens.get(p["key"])
        print("[API ] %-42s %s" % (p["name"], p["url"]))
        if not args.live:
            print("       将创建条目并上传 paper.pdf；token = %s" % ("已提供" if token else "未提供"))
            results.append({"platform": p["key"], "mode": "dry-run", "status": "previewed"})
            continue
        if not token:
            print("       跳过：未找到 %s（tokens.json 或环境变量）" % p["env"])
            results.append({"platform": p["key"], "mode": "live", "status": "skipped_no_token"})
            continue
        print("       正在提交 ...")
        out = SUBMITTERS[p["key"]](meta, token, pdf_bytes)
        print("       结果：%s" % json.dumps(out, ensure_ascii=False)[:400])
        results.append({"platform": p["key"], "mode": "live", "status": "ok" if out.get("ok") else "failed",
                        "detail": out})

    LOG_FILE.write_text(json.dumps({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "live": args.live,
        "results": results,
    }, ensure_ascii=False, indent=2), encoding="utf-8")

    print()
    print("结果已写入 submission-log.json（已加入 .gitignore，不会被推送）")
    if not args.live:
        print("确认无误后运行： python submit_all.py --live")
    print("提醒：API 提交以你的账号名义完成，等同本人确认原创性与许可协议。")


if __name__ == "__main__":
    main()
