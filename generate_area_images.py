#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
エリアカード画像を無料画像生成API(Pollinations.ai / Flux)で作成する。
APIキー不要・¥0。生成した画像はリポジトリに保存して自前ホストする。

使い方:
  全18エリア生成:      python3 generate_area_images.py --style photo
  特定エリアのみ:      python3 generate_area_images.py --style photo --only shizuoka,kyoto
  サンプル(3エリア×2): python3 generate_area_images.py --sample

出力先: images/areas/  (サンプルは images/areas/samples/)
※ Gemini API版は無料枠が画像生成limit:0のため廃止(2026/07確認)
"""
import argparse, os, sys, time, urllib.parse, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))

# エリアごとの代表ランドマーク（画像の主題）
AREAS = {
    "shizuoka": "Mount Fuji seen across Suruga Bay with a small fishing port town",
    "tokyo":    "Asakusa Sensoji temple red five-story pagoda in Tokyo at dusk, street level view with lanterns",
    "osaka":    "Dotonbori Osaka at dusk, colorful neon billboards reflecting on the canal river, lively crowds on the bridge",
    "hokkaido": "Otaru canal in Hokkaido with historic warehouses in snow",
    "fukuoka":  "Fukuoka yatai open-air street food stalls at night along the river with warm lantern light and city lights",
    "kyoto":    "Fushimi Inari endless red torii gates path in Kyoto",
    "okinawa":  "Okinawa emerald blue ocean with Kouri island bridge and white beach",
    "nagoya":   "Nagoya Castle Japan, white castle keep with green copper roofs seen across the moat from castle park",
    "kanagawa": "Enoshima island and Shonan coastline at sunset with distant Mount Fuji silhouette over the sea",
    "hiroshima":"Itsukushima floating red torii gate in the sea at Miyajima",
    "sendai":   "Matsushima bay with pine covered islets in Miyagi",
    "kanazawa": "Kenrokuen garden with stone lantern and Kanazawa teahouse street",
    "nagano":   "Matsumoto Castle with dark wooden walls and a red bridge reflected in its moat, snow capped Japanese Alps behind, vivid color photograph",
    "nara":     "Nara park deer in front of Todaiji great buddha hall",
    "gifu":     "Shirakawa-go village with steep thatched gassho-zukuri farmhouses among green fields, misty mountains behind",
    "kobe":     "Kobe harbor at dusk with the red steel lattice Port Tower, ferris wheel and waterfront promenade",
    "nagasaki": "Nagasaki harbor night view from Mount Inasa with Glover garden",
    "oita":     "Beppu onsen hot spring steam rising over the town and hells",
}

STYLES = {
    "illust": ("Flat modern travel poster illustration of {s}, minimal vector art style, "
               "warm coral orange and deep navy palette, soft cream sky, clean geometric composition, "
               "no text, no letters, no watermark"),
    "photo":  ("High quality professional travel photograph of {s}, golden hour light, "
               "vivid natural colors, sharp focus, wide angle, no text, no watermark"),
}

SAMPLE_AREAS = ["shizuoka", "kyoto", "okinawa"]


def generate(prompt, out_path, seed, width=1200, height=800, retries=3):
    q = urllib.parse.quote(prompt)
    url = (f"https://image.pollinations.ai/prompt/{q}"
           f"?width={width}&height={height}&nologo=true&model=flux&seed={seed}")
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = r.read()
            if len(data) > 10000:  # エラーページ等の小さいレスポンスを弾く
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(data)
                return True
        except Exception as e:
            print(f"  リトライ {attempt+1}/{retries}: {e}")
            time.sleep(15)
    return False


def seed_of(slug):
    """slugから決定的なseedを作る(再実行で同じ絵になる)"""
    return sum(ord(c) for c in slug) * 7


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--sample", action="store_true")
    ap.add_argument("--style", choices=["illust", "photo"])
    ap.add_argument("--only", help="特定エリアslugのみ(カンマ区切り)")
    args = ap.parse_args()

    ok, ng = 0, 0
    if args.sample:
        for slug in SAMPLE_AREAS:
            for style, tpl in STYLES.items():
                out = os.path.join(BASE, "images", "areas", "samples", f"{slug}_{style}.jpg")
                print(f"生成中: {slug} / {style}")
                ok, ng = (ok+1, ng) if generate(tpl.format(s=AREAS[slug]), out, seed_of(slug)) else (ok, ng+1)
                time.sleep(5)
    else:
        if not args.style:
            sys.exit("--sample か --style を指定してください")
        tpl = STYLES[args.style]
        targets = args.only.split(",") if args.only else list(AREAS)
        for slug in targets:
            out = os.path.join(BASE, "images", "areas", f"{slug}.jpg")
            print(f"生成中: {slug} ({args.style})")
            ok, ng = (ok+1, ng) if generate(tpl.format(s=AREAS[slug]), out, seed_of(slug)) else (ok, ng+1)
            time.sleep(5)

    print(f"完了: 成功{ok} / 失敗{ng}")
    if ng:
        sys.exit(1)


if __name__ == "__main__":
    main()
