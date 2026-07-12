#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""検証用: 1スポットのShort動画を生成して sns/sample/ に出力（投稿はしない）。
GitHub Actionsの本番環境（フォント/edge-tts/ffmpeg/Wikimedia）が通るかの確認に使う。"""
import os, sys, json, time
import video

HERE = os.path.dirname(os.path.abspath(__file__))
slug = sys.argv[1] if len(sys.argv) > 1 else "beppu-onsen"
spots = json.load(open(os.path.join(HERE, "spots_data.json"), encoding="utf-8"))
row = next((x for x in spots if x["slug"] == slug), None)
if not row:
    print(f"slug '{slug}' が見つかりません"); sys.exit(1)

out_dir = os.path.join(HERE, "sample")
os.makedirs(out_dir, exist_ok=True)
out = os.path.join(out_dir, f"{slug}.mp4")

t0 = time.time()
path, attr = video.build_short(row, out)
dt = round(time.time() - t0, 1)

print(f"slug      : {slug}")
print(f"生成結果  : {path}")
print(f"所要秒    : {dt}")
print(f"出典      : {attr}")
if path and os.path.exists(path):
    print(f"サイズ    : {os.path.getsize(path)} bytes")
    print(f"長さ(秒)  : {round(video._dur(path),1)}")
    print("RESULT=OK")
else:
    print("RESULT=FAIL")
    sys.exit(1)
