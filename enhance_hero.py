#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ドコリアル 詳細ページ 画像最適化 & AdSense審査対応スクリプト（一括・冪等）
- 各スポットページのヒーローに先頭YouTube動画のサムネイルを背景挿入（maxres→hqのフォールバック付き）
- 審査で嫌われるダミー広告枠「【広告】Google AdSense」を空スロット化（AdSense審査クリーン）
再実行しても二重挿入しない（冪等）。
"""
import re, glob, sys

files = sorted(glob.glob("spots/*/index.html"))
hero_done = ad_done = skipped = 0

VID_RE   = re.compile(r'youtube\.com/embed/([A-Za-z0-9_-]{6,})')
H1_RE    = re.compile(r'<h1>(.*?)</h1>', re.S)
HERO_RE  = re.compile(r'(<div class="spot-hero">\s*\n)(\s*)(<div class="spot-hero-inner">)')
AD_RE    = re.compile(r'<div class="ad-slot">【広告】Google AdSense</div>')

for f in files:
    html = open(f, encoding="utf-8").read()
    orig = html

    # --- 広告ダミー文字を空スロット化（審査対応） ---
    if AD_RE.search(html):
        html = AD_RE.sub('<div class="ad-slot"></div>', html)
        ad_done += 1

    # --- ヒーロー背景画像を挿入（冪等） ---
    if "spot-hero-bg" not in html:
        vm = VID_RE.search(html)
        hm = H1_RE.search(html)
        if vm and hm:
            vid  = vm.group(1)
            name = re.sub(r'<[^>]+>', '', hm.group(1)).strip()
            img = (
                f'<img class="spot-hero-bg" '
                f'src="https://i.ytimg.com/vi/{vid}/maxresdefault.jpg" '
                f'onerror="this.onerror=null;this.src=\'https://i.ytimg.com/vi/{vid}/hqdefault.jpg\'" '
                f'alt="{name}の雰囲気" loading="eager" decoding="async">\n'
                f'  <div class="spot-hero-scrim"></div>\n  '
            )
            html = HERO_RE.sub(lambda m: m.group(1) + m.group(2) + img + m.group(3), html, count=1)
            if "spot-hero-bg" in html:
                hero_done += 1

    if html != orig:
        open(f, "w", encoding="utf-8").write(html)
    else:
        skipped += 1

print(f"対象ページ : {len(files)}")
print(f"ヒーロー画像挿入 : {hero_done}")
print(f"広告枠クリーン化 : {ad_done}")
print(f"変更なし : {skipped}")
