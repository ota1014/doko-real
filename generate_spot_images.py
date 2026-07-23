#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
スポット詳細ページのヒーロー画像を無料画像生成API(Pollinations.ai / Flux)で作成する。
各 spots/{slug}/index.html から名称・所在地を読み取り、統一トーンの写実風写真を生成。

使い方:
  全スポット生成(既存はスキップ): python3 generate_spot_images.py
  特定スポットのみ(上書き):      python3 generate_spot_images.py --only numazu-port,atami
  全て強制再生成:                python3 generate_spot_images.py --force

出力先: images/spots/{slug}.jpg (1200x800)
"""
import argparse, glob, os, re, sys, time, urllib.parse, urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))

# 固有の建造物・被写体を持つスポット(被写体を明示しないと乖離が大きいもの)
SUBJECTS = {
    "fushimi-inari": "endless tunnel of red torii gates at Fushimi Inari shrine, Kyoto",
    "kinkakuji": "Kinkaku-ji Golden Pavilion, three story zen temple completely covered in shining gold leaf, reflected in mirror pond, Kyoto",
    "kiyomizu": "Kiyomizu-dera temple wooden stage on the hillside overlooking Kyoto",
    "arashiyama": "Arashiyama bamboo grove path with tall green bamboo, Kyoto",
    "gion": "Gion historic geisha district street with wooden machiya houses at dusk, Kyoto",
    "mishima-skywalk": "Mishima Skywalk long pedestrian suspension bridge over forest valley with Mount Fuji view",
    "mishima-taisha": "Mishima Taisha shrine main gate and worship hall, Japan",
    "kamakura-daibutsu": "Great Buddha of Kamakura, giant outdoor bronze seated buddha statue",
    "tsurugaoka-hachimangu": "Tsurugaoka Hachimangu shrine vermilion main hall on stone steps, Kamakura",
    "skytree": "Tokyo Skytree tall broadcasting tower over the city skyline at dusk",
    "tokyo-tower": "Tokyo Tower red and white lattice tower illuminated at dusk",
    "asakusa": "Asakusa Sensoji temple Kaminarimon gate with giant red lantern, Tokyo",
    "meiji-jingu": "Meiji Jingu shrine giant wooden torii gate in forest, Tokyo",
    "osaka-castle": "Osaka Castle green roofed white castle keep with golden decorations above stone walls",
    "tsutenkaku": "Tsutenkaku tower over the retro Shinsekai district neon streets, Osaka",
    "umeda-sky": "Umeda Sky Building twin towers with floating garden observatory, Osaka",
    "himeji-castle": "Himeji Castle elegant white heron castle keep, Japan",
    "matsumoto-castle": "Matsumoto Castle black wooden castle keep reflected in moat with red bridge",
    "nagoya-castle": "Nagoya Castle white castle keep with green copper roofs and golden shachihoko",
    "hiroshima-castle": "Hiroshima Castle wooden castle keep surrounded by moat",
    "sendai-castle": "Sendai Castle site stone walls and equestrian statue of Date Masamune overlooking city",
    "kanazawa-castle": "Kanazawa Castle white walled turrets and stone walls",
    "sunpu-castle": "Sunpu Castle park moat and reconstructed turret, Shizuoka",
    "hamamatsu-castle": "Hamamatsu Castle small white castle keep on stone base in park",
    "kakegawa-castle": "Kakegawa Castle wooden reconstructed castle keep",
    "shurijo": "Shuri Castle vermilion red palace main hall, Okinawa",
    "itsukushima": "Itsukushima shrine giant floating red torii gate in the sea, Miyajima",
    "peace-memorial": "Hiroshima Peace Memorial atomic bomb dome ruins by the river",
    "todaiji": "Todaiji temple giant wooden great buddha hall, Nara",
    "horyuji": "Horyuji temple five story wooden pagoda, Nara",
    "kofukuji": "Kofukuji temple five story pagoda, Nara",
    "kasuga-taisha": "Kasuga Taisha shrine vermilion corridors with hanging bronze lanterns, Nara",
    "nara-park": "wild deer resting on grass in Nara Park with temple in background",
    "zenkoji": "Zenkoji temple large wooden main hall with pilgrims approach street, Nagano",
    "zuihoden": "Zuihoden ornate colorful mausoleum with carved decorations in cedar forest, Sendai",
    "kenrokuen": "Kenrokuen landscape garden with Kotoji two-legged stone lantern by pond, Kanazawa",
    "higashi-chaya": "Higashi Chaya historic teahouse district street with wooden lattice facades, Kanazawa",
    "shirakawago": "Shirakawa-go village steep thatched gassho-zukuri farmhouses",
    "monet-pond": "crystal clear pond with colorful koi carp swimming like a Monet painting, Gifu",
    "megane-bridge": "Meganebashi spectacles stone arch bridge reflected in river, Nagasaki",
    "oura-church": "Oura Catholic white church on hillside, Nagasaki",
    "gunkanjima": "Gunkanjima abandoned concrete battleship island in the sea, Nagasaki",
    "otaru-canal": "Otaru canal with historic stone warehouses and gas lamps",
    "shirogane-blue-pond": "surreal milky blue pond with bare larch trees, Biei Hokkaido",
    "numazu-byuo": "large water gate observation deck structure at Numazu port",
    "nirayama-hansharyo": "Nirayama historic brick reverberatory furnace chimneys, Izu",
    "oigawa-sl": "vintage black steam locomotive train running along Oigawa river valley",
    "yumenotsuribashi": "Yume no Tsuribashi suspension footbridge over emerald green lake in forest gorge",
    "horaibashi": "Horaibashi long wooden pedestrian bridge over wide river, Shizuoka",
    "jigokudani-monkey": "wild snow monkeys bathing in natural hot spring, Nagano",
    "zao-okama": "Zao Okama emerald green volcanic crater lake",
    "usj": "colorful theme park globe entrance and attractions at dusk",
    "ghibli-park": "whimsical european style fantasy park building among green forest",
    "kaiyukan": "large aquarium building with red exterior near ferris wheel, Osaka bay",
    "churaumi": "giant aquarium tank with whale shark and visitors silhouettes, Okinawa",
    "fujisan-hongu": "Fujisan Hongu Sengen Taisha shrine vermilion two-story gate with Mount Fuji behind",
    "kunozan": "Kunozan Toshogu ornate colorful shrine gate on mountain, Shizuoka",
    "shizuoka-sengen": "Shizuoka Sengen shrine ornate vermilion and gold buildings",
    "atsuta-jingu": "Atsuta Jingu shrine wooden torii and forest approach, Nagoya",
    "oasis21": "Oasis 21 glass spaceship roof structure illuminated at night, Nagoya",
    "fukuoka-tower": "Fukuoka Tower mirrored triangular seaside tower at sunset",
    "dazaifu": "Dazaifu Tenmangu shrine vermilion main hall and pond bridge, Fukuoka",
    "kokonoe-bridge": "Kokonoe Yume long pedestrian suspension bridge high over forest valley, Oita",
    "beppu-jigoku": "Beppu Umi Jigoku cobalt blue steaming hot spring pond",
    "ryugashido": "illuminated limestone cave with stalactites, Shizuoka",
    "omuroyama": "Mount Omuro perfectly round green volcanic hill with spiral path, Izu",
    "kouri-island": "long straight bridge crossing emerald sea to Kouri island, Okinawa",
    "cape-manza": "Cape Manzamo elephant trunk rock cliff over emerald sea, Okinawa",
    "minatomirai": "Yokohama Minato Mirai waterfront skyline with ferris wheel at dusk",
    "yokohama-chinatown": "Yokohama Chinatown ornate colorful chinese gate and lantern street",
    "kitano-ijinkan": "Kitano Ijinkan historic western style houses on hillside, Kobe",
    "nankinmachi": "Nankinmachi Kobe chinatown gate with red lanterns",
    "kobe-harbor": "Kobe harbor red Port Tower and ferris wheel at dusk",
    "glover-garden": "Glover Garden historic western mansion overlooking Nagasaki harbor",
    "inasayama": "panoramic night view of Nagasaki city and harbor from Mount Inasa",
}

STYLE = ("High quality professional travel photograph of {s}, Japan. "
         "Golden hour light, vivid natural colors, sharp focus, wide angle, "
         "no text, no letters, no watermark")


def spot_info(path):
    c = open(path, encoding="utf-8").read()
    name = re.search(r'<h1>([^<]+)</h1>', c)
    loc = re.search(r'<span>📍 ([^<]+)</span>', c)
    return (name.group(1) if name else None,
            loc.group(1).strip() if loc else "")


def subject_of(slug, name, loc):
    if slug in SUBJECTS:
        return SUBJECTS[slug]
    words = slug.replace("-", " ")
    return f"{words}, {name}, {loc}" if loc else f"{words}, {name}"


def seed_of(slug):
    return sum(ord(c) for c in slug) * 7


def generate(prompt, out_path, seed, retries=3):
    q = urllib.parse.quote(prompt)
    url = (f"https://image.pollinations.ai/prompt/{q}"
           f"?width=1200&height=800&nologo=true&model=flux&seed={seed}")
    req = urllib.request.Request(url, headers={"User-Agent": "curl/8.4.0"})
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                data = r.read()
            if len(data) > 10000:
                os.makedirs(os.path.dirname(out_path), exist_ok=True)
                with open(out_path, "wb") as f:
                    f.write(data)
                return True
        except Exception as e:
            print(f"  リトライ {attempt+1}/{retries}: {e}", flush=True)
            time.sleep(20)
    return False


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", help="特定slugのみ(カンマ区切り・上書き)")
    ap.add_argument("--force", action="store_true", help="既存画像も再生成")
    args = ap.parse_args()

    paths = sorted(glob.glob(os.path.join(BASE, "spots", "*", "index.html")))
    only = set(args.only.split(",")) if args.only else None

    ok, ng, skip = 0, 0, 0
    for path in paths:
        slug = os.path.basename(os.path.dirname(path))
        if only and slug not in only:
            continue
        out = os.path.join(BASE, "images", "spots", f"{slug}.jpg")
        if os.path.exists(out) and not args.force and not only:
            skip += 1
            continue
        name, loc = spot_info(path)
        if not name:
            print(f"NG(名称不明): {slug}", flush=True)
            ng += 1
            continue
        print(f"生成中: {slug} ({name})", flush=True)
        if generate(STYLE.format(s=subject_of(slug, name, loc)), out, seed_of(slug)):
            ok += 1
        else:
            ng += 1
        time.sleep(5)

    print(f"完了: 成功{ok} / 失敗{ng} / スキップ{skip}", flush=True)
    if ng:
        sys.exit(1)


if __name__ == "__main__":
    main()
