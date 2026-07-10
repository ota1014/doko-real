#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ドコリアル SNS自動投稿 メインランナー（GitHub Actions cronから実行）
- spots_data.json から本日分をローテーションで自動選択
- 各SNS向けキャプション生成 → 画像/動画アセット用意 → 有効な媒体へ投稿
- APIキーが無い媒体は自動スキップ。state.json でローテーション位置を保持。
使い方: python3 sns/post.py [--dry-run]
"""
import os, sys, json, tempfile, datetime
import captions as C
import platforms as P
import assets as A

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://dokoriaru.com"
DRY  = "--dry-run" in sys.argv

def load(p, default):
    return json.load(open(p, encoding="utf-8")) if os.path.exists(p) else default

def main():
    cfg    = load(os.path.join(HERE, "config.json"), {})
    spots  = load(os.path.join(HERE, "spots_data.json"), [])
    state  = load(os.path.join(HERE, "state.json"), {"cursor": 0, "history": []})
    if not spots:
        print("spots_data.json が空。build_queue.py を先に実行。"); return

    n = cfg.get("posts_per_run", 1)
    cur = state["cursor"] % len(spots)
    picks = [spots[(cur + i) % len(spots)] for i in range(n)]
    plat_cfg = cfg.get("platforms", {})
    cards_dir = os.path.join(HERE, "cards")
    log_lines = []

    for row in picks:
        slug = row["slug"]
        # アセット: 事前生成済みカード（公開URL）＋ローカルパス
        card_local = os.path.join(cards_dir, f"{slug}.jpg")
        card_url   = f"{SITE}/sns/cards/{slug}.jpg" if os.path.exists(card_local) else None
        if not os.path.exists(card_local):
            A.make_card(row, card_local) if not DRY else None
            card_local = card_local if os.path.exists(card_local) else None
        # 動画（TikTok/YouTube用）は都度生成
        video = None
        if any(plat_cfg.get(p, {}).get("enabled") and P._env(*{
                    "tiktok": ["TIKTOK_TOKEN"],
                    "youtube": ["YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN"]}[p])
               for p in ("tiktok", "youtube")) and not DRY:
            video = A.make_slideshow(row, os.path.join(tempfile.gettempdir(), f"{slug}.mp4"))

        print(f"\n=== {row['name']} ({slug}) ===")
        for plat, builder in C.BUILDERS.items():
            if not plat_cfg.get(plat, {}).get("enabled"):
                continue
            payload = builder(row)
            if DRY:
                print(f"[{plat}] DRY-RUN\n{payload if isinstance(payload,str) else payload['title']}")
                continue
            poster = P.POSTERS[plat]
            if plat == "x":
                status, detail = poster(payload, card_path=card_local)
            elif plat in ("threads", "instagram"):
                status, detail = poster(payload, card_url=card_url)
            elif plat == "tiktok":
                status, detail = poster(payload, video_path=video)
            elif plat == "youtube":
                status, detail = poster(payload, video_path=video)
            icon = {"ok": "✅", "skip": "⏭", "error": "❌"}.get(status, "?")
            print(f"{icon} [{plat}] {status}: {detail}")
            log_lines.append({"slug": slug, "platform": plat, "status": status, "detail": detail})

    # 状態更新（1件でも投稿成功した時だけローテを進める。全スキップ=キー未設定の間は据え置き）
    posted = any(l["status"] == "ok" for l in log_lines)
    if not DRY and posted:
        state["cursor"] = (cur + n) % len(spots)
        state["history"] = (state.get("history", []) + [{
            "at": os.environ.get("RUN_STAMP", ""),
            "slugs": [r["slug"] for r in picks],
            "results": log_lines,
        }])[-60:]
        json.dump(state, open(os.path.join(HERE, "state.json"), "w", encoding="utf-8"),
                  ensure_ascii=False, indent=2)
        print(f"\nローテーション: {cur} → {state['cursor']} / {len(spots)}")

if __name__ == "__main__":
    main()
