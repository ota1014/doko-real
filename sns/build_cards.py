#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全155スポットのブランドカード(1080x1080)を sns/cards/ に一括生成。
GitHub Pagesで公開され、Instagram/Threadsの投稿画像URLとして使う。"""
import os, json
import assets as A

HERE = os.path.dirname(os.path.abspath(__file__))
spots = json.load(open(os.path.join(HERE, "spots_data.json"), encoding="utf-8"))
out_dir = os.path.join(HERE, "cards")
os.makedirs(out_dir, exist_ok=True)

ok = miss = 0
for r in spots:
    p = os.path.join(out_dir, f"{r['slug']}.jpg")
    if A.make_card(r, p):
        ok += 1
    else:
        miss += 1
print(f"カード生成: 成功{ok} / 失敗{miss}")
if miss:
    print("※ Pillow または日本語フォント未検出。requirements.txt と fonts-noto-cjk を確認。")
