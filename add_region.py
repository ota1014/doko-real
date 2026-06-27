#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""汎用エリア追加ツール。実在YouTube動画でスポットページ＋エリア一覧ページを生成する。
各エリアのデータモジュール（例: data_osaka.py）から CFG と SPOTS を渡して使う。
generate_spots.py の generate_html を再利用。冪等。"""

import os
import re
import json
from urllib.parse import quote
from generate_spots import generate_html

BASE = os.path.dirname(os.path.abspath(__file__))


def head_extra(spot):
    slug, name, tag, location = spot["slug"], spot["name"], spot["tag"], spot["location"]
    url = f"https://dokoriaru.com/spots/{slug}/"
    desc = (f"{name}の{tag}をSNS動画でリアルにチェック。"
            f"YouTube・Instagram・TikTokの動画をまとめて確認できます。行く前に雰囲気をチェック。")
    schema = (
        '{\n  "@context": "https://schema.org",\n  "@type": "TouristAttraction",\n'
        f'  "name": "{name}",\n  "description": "{desc}",\n  "url": "{url}",\n'
        '  "image": "https://dokoriaru.com/ogp.png",\n'
        '  "address": {\n    "@type": "PostalAddress",\n'
        f'    "addressRegion": "{location}",\n    "addressCountry": "JP"\n  }},\n'
        '  "geo": {\n    "@type": "GeoCoordinates",\n'
        f'    "latitude": {spot["lat"]},\n    "longitude": {spot["lng"]}\n  }},\n'
        '  "touristType": "観光客",\n  "inLanguage": "ja"\n}'
    )
    return (
        f'<link rel="canonical" href="{url}">\n<link rel="icon" href="../../favicon.ico">\n'
        '<meta property="og:type" content="article">\n'
        f'<meta property="og:url" content="{url}">\n'
        f'<meta property="og:title" content="{name}｜SNS動画でリアルチェック — ドコリアル">\n'
        f'<meta property="og:description" content="{desc}">\n'
        '<meta property="og:image" content="https://dokoriaru.com/ogp.png">\n'
        '<meta property="og:site_name" content="ドコリアル">\n'
        '<meta name="twitter:card" content="summary_large_image">\n'
        '<script async src="https://www.googletagmanager.com/gtag/js?id=G-CK7XK7SNHB"></script>\n'
        "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-CK7XK7SNHB');</script>\n"
        '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6942069552168215" crossorigin="anonymous"></script>\n'
        '<script type="application/ld+json">\n' + schema + '\n</script>\n'
    )


def affiliate_block(spot):
    name = spot["name"]
    kw_jp, kw_en, kw_book = quote(spot["kw_jp"]), quote(spot["kw_en"]), quote(spot["kw_book"])
    rakuten = (f'https://hb.afl.rakuten.co.jp/hgc/547aa6cd.f4da91da.547aa6ce.994ce031/'
               f'?pc=https%3A%2F%2Ftravel.rakuten.co.jp%2Fyado%2Fsearch%2F%3Ff_keyword%3D{kw_jp}&link_type=text')
    klook = (f'https://affiliate.klook.com/redirect?aid=123307&aff_adid=1293166'
             f'&k_site=https%3A%2F%2Fwww.klook.com%2Fja%2Fsearch%2F%3Fquery%3D{kw_en}')
    booking = f'https://www.booking.com/searchresults.ja.html?ss={kw_book}&lang=ja'
    return (
        '  <div class="affiliate-section reveal">\n'
        f'    <h3>{name}周辺の宿・体験を予約する</h3>\n'
        f'    <p>{name}エリアの宿泊・観光・体験はこちら</p>\n'
        '    <div class="affiliate-btns">\n'
        f'      <a href="{booking}" class="btn-affiliate btn-booking" target="_blank" rel="noopener">🏨 Booking.comで宿を探す</a>\n'
        f'      <a href="{rakuten}" class="btn-affiliate btn-rakuten" target="_blank" rel="nofollow sponsored noopener">🏨 楽天トラベルで宿を探す</a>\n'
        f'      <a href="{klook}" class="btn-affiliate btn-klook" target="_blank" rel="nofollow sponsored noopener">🎟 Klookで体験を探す</a>\n'
        '    </div>\n  </div>'
    )


def fix_nav(html, cfg):
    n = cfg["nav_spots"]  # [(slug,label),(slug,label)]
    nav_new = (
        '  <nav>\n    <a href="../../">トップ</a>\n'
        f'    <a href="../../{cfg["region_slug"]}/">{cfg["region_short"]}</a>\n'
        f'    <a href="../{n[0][0]}/">{n[0][1]}</a>\n'
        f'    <a href="../{n[1][0]}/">{n[1][1]}</a>\n  </nav>'
    )
    return re.sub(r'  <nav>\s*<a href="\.\./\.\./">トップ</a>.*?</nav>', nav_new, html, count=1, flags=re.DOTALL)


def build_spot_pages(cfg, spots):
    created, skipped = [], []
    for spot in spots:
        spot.setdefault("jalan", ""); spot.setdefault("tabelog", "")
        d = os.path.join(BASE, "spots", spot["slug"]); fp = os.path.join(d, "index.html")
        os.makedirs(d, exist_ok=True)
        if os.path.exists(fp):
            skipped.append(spot["slug"]); continue
        html = generate_html(spot)
        html = html.replace('</head>', head_extra(spot) + '</head>', 1)
        html = fix_nav(html, cfg)
        html = re.sub(r'  <div class="affiliate-section reveal">.*?</div>\s*</div>',
                      affiliate_block(spot), html, count=1, flags=re.DOTALL)
        open(fp, "w", encoding="utf-8").write(html)
        created.append(spot["slug"])
    return created, skipped


def build_area_page(cfg, spots):
    cards = ""
    for s in spots:
        thumb = f'https://i.ytimg.com/vi/{s["videos"][0]["id"]}/hqdefault.jpg'
        cards += (
            f'      <a href="../spots/{s["slug"]}/" class="spot-card reveal">\n'
            f'        <div class="spot-card-thumb">\n'
            f'          <img src="{thumb}" alt="{s["name"]}" loading="lazy">\n'
            f'          <span class="spot-card-tag">{s["card_tag"]}</span>\n'
            f'          <span class="spot-card-video-count">▶ 動画</span>\n'
            f'        </div>\n'
            f'        <div class="spot-card-body">\n'
            f'          <div class="spot-card-area">{s["location"]}</div>\n'
            f'          <div class="spot-card-name">{s["name"]}</div>\n'
            f'          <div class="spot-card-desc">{s["card_desc"]}</div>\n'
            f'        </div>\n'
            f'        <div class="spot-card-footer"><span class="spot-card-cta">動画を見る →</span></div>\n'
            f'      </a>\n'
        )
    nav_items = cfg["area_nav_html"]
    html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{cfg['region_label']}｜SNS動画でお出かけ先を探そう — ドコリアル</title>
<meta name="description" content="SNS動画で{cfg['region_short']}のお出かけ先をリアルにチェック。{cfg['spots_oneline']}など人気スポットを動画で比較できます。行く前に雰囲気をチェック。">
<meta property="og:type" content="website">
<meta property="og:url" content="https://dokoriaru.com/{cfg['region_slug']}/">
<meta property="og:title" content="{cfg['region_label']}｜SNS動画でお出かけ先を探そう — ドコリアル">
<meta property="og:description" content="SNS動画で{cfg['region_short']}のお出かけ先をリアルにチェック。{cfg['spots_oneline']}など。">
<meta property="og:image" content="https://dokoriaru.com/ogp.png">
<meta property="og:site_name" content="ドコリアル">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://dokoriaru.com/{cfg['region_slug']}/">
<link rel="icon" href="/favicon.ico" type="image/x-icon">
<link rel="stylesheet" href="../css/style.css">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-CK7XK7SNHB"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments);}}gtag('js',new Date());gtag('config','G-CK7XK7SNHB');</script>
<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6942069552168215" crossorigin="anonymous"></script>
</head>
<body>

<header>
  <a href="/" class="logo">ドコ<span>リアル</span></a>
  <nav>
    <div class="nav-dropdown">
      <button class="nav-btn">エリア <span class="caret">▾</span></button>
      <div class="nav-dropdown-menu">
{nav_items}      </div>
    </div>
  </nav>
</header>

<section class="hero">
  <div class="hero-eyebrow">{cfg['region_short']}エリア SNS動画まとめ {len(spots)}スポット掲載中</div>
  <h1>行く前に、<span class="accent">リアル</span>を見よう。</h1>
  <p>{cfg['region_short']}の人気スポットをSNS動画でチェック。<br>口コミじゃわからないリアルな雰囲気を、行く前に確認できます。</p>
</section>

<section class="section">
  <div class="section-inner">
    <h2 class="section-title reveal">{cfg['region_short']}のスポットを<span>探す</span></h2>
    <p class="section-sub reveal">{cfg['spots_oneline']}など人気の{len(spots)}スポット掲載中</p>

    <div class="spots-grid">

{cards}
    </div>
  </div>
</section>

<footer>
  <div class="footer-logo">ドコ<span>リアル</span></div>
  <div class="footer-links">
    <a href="/">トップ</a>
    <a href="/about/">運営者情報</a>
    <a href="/contact/">お問い合わせ</a>
    <a href="/privacy/">プライバシーポリシー</a>
  </div>
  <p>掲載動画・投稿はYouTube・Instagram・TikTokの公式埋め込み機能を使用しています。</p>
  <p style="margin-top:8px;">&copy; 2026 ドコリアル</p>
</footer>

<script src="../js/main.js"></script>
</body>
</html>
"""
    d = os.path.join(BASE, cfg["region_slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(html)


def update_sitemap(cfg, spots):
    p = os.path.join(BASE, "sitemap.xml"); c = open(p, encoding="utf-8").read()
    urls = [f"https://dokoriaru.com/{cfg['region_slug']}/"] + \
           [f"https://dokoriaru.com/spots/{s['slug']}/" for s in spots]
    add = "".join(f'  <url><loc>{u}</loc><changefreq>monthly</changefreq><priority>0.7</priority></url>\n'
                  for u in urls if u not in c)
    if add:
        c = c.replace("</urlset>", add + "</urlset>")
        open(p, "w", encoding="utf-8").write(c)
    return add.count("<url>")


def run(cfg, spots):
    created, skipped = build_spot_pages(cfg, spots)
    build_area_page(cfg, spots)
    n = update_sitemap(cfg, spots)
    print(f"[{cfg['region_slug']}] スポット作成{len(created)} / スキップ{len(skipped)} / sitemap+{n} / エリアページ生成")
    return created
