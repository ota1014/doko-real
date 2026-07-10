# -*- coding: utf-8 -*-
"""
Wikimedia Commons から「その場所の本物の写真」をライセンス確認付きで取得する。
- CC-BY / CC-BY-SA / CC0 / パブリックドメイン のみ採用
- 作者・ライセンスを出典として返す（動画概要欄に記載する）
- 画像が乏しいスポットは少数/ゼロを返す → 呼び出し側でフォールバック
"""
import os, re, json, urllib.parse, urllib.request

API = "https://commons.wikimedia.org/w/api.php"
UA  = "DokorearuBot/1.0 (https://dokoriaru.com; info.dokoriaru@gmail.com)"
OK_LICENSES = ("cc by", "cc0", "public domain", "pdm", "パブリック", "attribution")

def _get(params):
    params = {**params, "format": "json"}
    url = API + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())

def _license_ok(meta):
    lic = (meta.get("LicenseShortName", {}).get("value", "")
           or meta.get("UsageTerms", {}).get("value", "")).lower()
    lic = lic.replace("-", " ")  # "CC-BY-SA" と "CC BY-SA" を同一視
    return any(k in lic for k in OK_LICENSES)

def _clean(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s or "")).strip()

def fetch_images(query, n=5, want_width=1080, out_dir="/tmp/dokowiki"):
    """query（スポット名など）に一致する使用可能な写真を最大n枚DL。
    戻り値: [{path, author, license, source_url}] """
    os.makedirs(out_dir, exist_ok=True)
    try:
        data = _get({
            "action": "query", "generator": "search",
            "gsrsearch": query, "gsrnamespace": 6, "gsrlimit": n * 4,
            "prop": "imageinfo",
            "iiprop": "url|extmetadata|size|mime",
            "iiurlwidth": want_width,
        })
    except Exception as e:
        print(f"  wiki検索失敗: {e}")
        return []
    pages = (data.get("query", {}) or {}).get("pages", {})
    results = []
    for p in pages.values():
        ii = (p.get("imageinfo") or [{}])[0]
        meta = ii.get("extmetadata", {}) or {}
        if ii.get("mime") not in ("image/jpeg", "image/png"):
            continue
        if ii.get("width", 0) < 800:
            continue
        if not _license_ok(meta):
            continue
        thumb = ii.get("thumburl") or ii.get("url")
        if not thumb:
            continue
        author = _clean(meta.get("Artist", {}).get("value", "")) or "Wikimedia Commons"
        lic = _clean(meta.get("LicenseShortName", {}).get("value", "")) or "CC"
        fname = os.path.join(out_dir, f"w{len(results)}.jpg")
        try:
            req = urllib.request.Request(thumb, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=30) as r, open(fname, "wb") as f:
                f.write(r.read())
        except Exception:
            continue
        results.append({"path": fname, "author": author[:60],
                        "license": lic, "source_url": ii.get("descriptionurl", "")})
        if len(results) >= n:
            break
    return results

def fetch_images_multi(queries, n=5, out_dir="/tmp/dokowiki"):
    """複数クエリを順に試し、n枚集まるまで蓄積。ニッチなスポットのフォールバック用。"""
    got, seen = [], set()
    for q in queries:
        if not q:
            continue
        for img in fetch_images(q, n=n, out_dir=out_dir + "_" + re.sub(r"\W+", "", q)[:12]):
            key = (img["author"], img["license"])
            if img["path"] not in seen:
                seen.add(img["path"]); got.append(img)
            if len(got) >= n:
                return got
    return got

if __name__ == "__main__":
    import sys
    q = sys.argv[1] if len(sys.argv) > 1 else "湯布院"
    imgs = fetch_images(q, n=5)
    print(f"'{q}' → {len(imgs)}枚取得")
    for i in imgs:
        print(" ", os.path.basename(i["path"]), "|", i["license"], "|", i["author"][:30])
