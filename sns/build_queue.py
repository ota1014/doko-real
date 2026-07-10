#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SNS自動投稿の「弾」を全155スポットから抽出して spots_data.json を生成する。
各スポット: slug / name / url / area / genre / video_id / thumb / blurb / hashtags
再実行で最新化。ページ・articles.json を更新したら流し直すだけ。
"""
import os, re, json, glob, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # ドコリアル/
SITE = "https://dokoriaru.com"
articles = json.load(open(os.path.join(BASE, "articles.json"), encoding="utf-8"))

def clean(s): return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s or ""))).strip()

def pick(pattern, text, default=""):
    m = re.search(pattern, text, re.S)
    return clean(m.group(1)) if m else default

rows = []
for f in sorted(glob.glob(os.path.join(BASE, "spots", "*", "index.html"))):
    slug = os.path.basename(os.path.dirname(f))
    t = open(f, encoding="utf-8").read()
    name  = pick(r"<h1>(.*?)</h1>", t)
    area  = pick(r"📍([^<]+)", t)
    genre = pick(r"🏷️([^<]+)", t)
    vid_m = re.search(r"youtube\.com/embed/([A-Za-z0-9_-]{6,})", t)
    vid   = vid_m.group(1) if vid_m else ""
    # 紹介文: articles.jsonのintroを優先、無ければmeta description
    blurb = clean(articles.get(slug, {}).get("intro", "")) or pick(r'name="description" content="(.*?)"', t)
    # ハッシュタグ: エリア県名・ジャンル語から生成
    tags = ["#ドコリアル", "#観光", "#旅行好きな人と繋がりたい"]
    pref = re.sub(r"(県|都|府|市|町|村).*$", r"\1", area)  # 先頭の行政区
    pref = re.sub(r"(市|町|村)$", "", pref)
    for w in re.split(r"[・/、\s]+", genre):
        w = w.strip()
        if w and len(w) <= 6:
            tags.append("#" + w)
    if area:
        tags.insert(1, "#" + re.split(r"[県都府]", area)[0] + ("県" if "県" in area else ""))
    tags.append("#" + re.sub(r"[（(].*", "", name).strip())
    # 重複除去・最大6
    seen, uniq = set(), []
    for tg in tags:
        if tg not in seen and len(tg) > 1:
            seen.add(tg); uniq.append(tg)
    rows.append({
        "slug": slug,
        "name": name,
        "url": f"{SITE}/spots/{slug}/",
        "area": area,
        "genre": genre,
        "video_id": vid,
        "thumb_max": f"https://i.ytimg.com/vi/{vid}/maxresdefault.jpg" if vid else "",
        "thumb_hq":  f"https://i.ytimg.com/vi/{vid}/hqdefault.jpg" if vid else "",
        "blurb": blurb[:180],
        "hashtags": uniq[:6],
    })

out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spots_data.json")
json.dump(rows, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"抽出: {len(rows)}スポット → {out}")
print("サンプル:", json.dumps(rows[0], ensure_ascii=False)[:300])
