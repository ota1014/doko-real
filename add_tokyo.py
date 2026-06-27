#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""東京エリアのスポットページ生成（実在YouTube動画を使用）。
generate_spots.py の generate_html を再利用し、ヘッダーnav・アフィリエイトを東京用に調整する。
冪等（既存ファイルはスキップ）。"""

import os
import re
from urllib.parse import quote
from generate_spots import generate_html

BASE = os.path.dirname(os.path.abspath(__file__))

TOKYO_SPOTS = [
    {
        "slug": "asakusa", "name": "浅草寺・雷門", "area_label": "東京エリア",
        "location": "東京都台東区", "tag": "寺・下町・食べ歩き",
        "desc": "東京最古の寺院として知られる浅草のシンボル。巨大な提灯がかかる「雷門」、土産物や食べ歩きグルメが並ぶ「仲見世通り」、荘厳な本堂と五重塔が見どころ。下町情緒あふれる街並みと、外国人観光客でにぎわう活気が魅力で、東京観光の定番スポットです。",
        "videos": [
            {"id": "ntJ3qHZZw6E", "title": "【東京観光】浅草ってどんな所？雷門・五重塔・寺院巡り・食べ歩き"},
            {"id": "Z3646X3hxKw", "title": "【東京】浅草ひとり旅〜浅草寺の見どころまとめ＆散策モデルコース"},
            {"id": "YRssQs5L1G4", "title": "【街ブラ4K】浅草 雷門〜仲見世通り〜浅草寺 ぶらぶら散歩"},
            {"id": "3oKIYTu9rls", "title": "【浅草 観光 2024年最新版】失敗しない浅草観光モデルコース 食べ歩き"},
        ],
        "shorts": [
            {"id": "Z3646X3hxKw", "title": "浅草寺 散策モデルコース"},
            {"id": "YRssQs5L1G4", "title": "浅草 仲見世通り 4K"},
        ],
        "access": "東京メトロ銀座線・浅草駅から徒歩約5分 / 都営浅草線・つくばエクスプレス浅草駅から徒歩圏",
        "hours": "本堂6:00〜17:00（10〜3月は6:30〜）／仲見世は店舗により異なる",
        "holiday": "なし（年中無休）", "parking": "周辺有料駐車場",
        "feature": "雷門・仲見世通り・五重塔・本堂・食べ歩きグルメ・人力車",
        "lat": 35.7148, "lng": 139.7967,
        "kw_jp": "浅草", "kw_en": "Asakusa Tokyo", "kw_book": "Asakusa Tokyo",
        "related": [("shibuya", "東京都 渋谷区", "渋谷スクランブル交差点"),
                    ("skytree", "東京都 墨田区", "東京スカイツリー"),
                    ("ueno", "東京都 台東区", "上野公園・アメ横")],
    },
    {
        "slug": "shibuya", "name": "渋谷スクランブル交差点", "area_label": "東京エリア",
        "location": "東京都渋谷区", "tag": "都市・カルチャー",
        "desc": "一度の青信号で数千人が行き交う、世界的に有名な交差点。若者文化の発信地・渋谷の象徴で、四方から人が交差する光景は圧巻。ハチ公像や渋谷スクランブルスクエアの展望施設「SHIBUYA SKY」も人気で、ショッピング・グルメ・夜遊びまで楽しめる東京随一の繁華街です。",
        "videos": [
            {"id": "3vh7ClhMTm4", "title": "4K Shibuya Crossing Walking 渋谷スクランブル交差点 散歩"},
            {"id": "2tqt_l43AHM", "title": "【東京散歩】休日渋谷の中心を散歩 4K Shibuya Center walk"},
            {"id": "n2KSpEiC_sk", "title": "【4K】大人気の撮影スポット 渋谷スクランブル交差点を散歩"},
            {"id": "HyP3GRyfvaM", "title": "【4K】夕方の渋谷を散歩 スクランブル交差点で有名な若者の街"},
        ],
        "shorts": [
            {"id": "3vh7ClhMTm4", "title": "渋谷スクランブル交差点 4K"},
            {"id": "n2KSpEiC_sk", "title": "渋谷 撮影スポット散歩"},
        ],
        "access": "JR・東京メトロ・東急・京王井の頭線 渋谷駅すぐ（ハチ公口）",
        "hours": "終日（店舗・SHIBUYA SKYは営業時間あり）",
        "holiday": "なし", "parking": "周辺有料駐車場",
        "feature": "スクランブル交差点・ハチ公像・SHIBUYA SKY・ショッピング・夜景",
        "lat": 35.6595, "lng": 139.7005,
        "kw_jp": "渋谷", "kw_en": "Shibuya Tokyo", "kw_book": "Shibuya Tokyo",
        "related": [("asakusa", "東京都 台東区", "浅草寺・雷門"),
                    ("meiji-jingu", "東京都 渋谷区", "明治神宮"),
                    ("tokyo-tower", "東京都 港区", "東京タワー")],
    },
    {
        "slug": "skytree", "name": "東京スカイツリー", "area_label": "東京エリア",
        "location": "東京都墨田区", "tag": "展望・ランドマーク",
        "desc": "高さ634mを誇る世界一高いタワー（自立式電波塔）。地上350mと450mの2層の展望台からは、東京の街並みや富士山まで360度の大パノラマが広がります。ふもとの商業施設「東京ソラマチ」にはグルメやショップ、すみだ水族館も。夜のライトアップも美しく、下町の新たなシンボルです。",
        "videos": [
            {"id": "GPphS1wolFc", "title": "【PV】Discover your excitement｜東京スカイツリー【公式】"},
            {"id": "41srFEpBZYQ", "title": "東京スカイツリー 展望台の景色【富士山・初日の出・花火・雲海】【公式】"},
            {"id": "nBI09ASgaRU", "title": "東京の一大観光スポット スカイツリー周辺と内部を散策！地上350mの景色"},
            {"id": "PteJvuWrUwY", "title": "【4K】東京スカイツリー展望フロアをぐるっとご案内 天望回廊"},
        ],
        "shorts": [
            {"id": "GPphS1wolFc", "title": "東京スカイツリー 公式PV"},
            {"id": "41srFEpBZYQ", "title": "スカイツリー展望台の絶景"},
        ],
        "access": "東武スカイツリーライン・とうきょうスカイツリー駅すぐ / 半蔵門線・押上駅から徒歩約5分",
        "hours": "展望台10:00〜22:00（最終入場21:00）※変動あり",
        "holiday": "なし", "parking": "東京ソラマチ駐車場（有料）",
        "feature": "展望デッキ・天望回廊・東京ソラマチ・すみだ水族館・夜景・富士山",
        "lat": 35.7101, "lng": 139.8107,
        "kw_jp": "東京スカイツリー", "kw_en": "Tokyo Skytree", "kw_book": "Tokyo Skytree Oshiage",
        "related": [("asakusa", "東京都 台東区", "浅草寺・雷門"),
                    ("ueno", "東京都 台東区", "上野公園・アメ横"),
                    ("tokyo-tower", "東京都 港区", "東京タワー")],
    },
    {
        "slug": "tokyo-tower", "name": "東京タワー", "area_label": "東京エリア",
        "location": "東京都港区", "tag": "展望・ランドマーク",
        "desc": "高さ333m、1958年の開業以来東京を見守ってきた赤と白のシンボルタワー。メインデッキ（150m）とトップデッキ（250m）から東京の景色を一望でき、夜にはライトアップが街を彩ります。ふもとには増上寺や芝公園もあり、レトロな東京の魅力を感じられる定番スポットです。",
        "videos": [
            {"id": "o0reV0gfBV4", "title": "🗼【4K.東京観光】東京タワーが全部わかる‼ 展望フロアをぐるっとご案内"},
            {"id": "YiT1adrTy9Y", "title": "【東京観光】東京タワーってどんな所？展望台・東京お土産タウン"},
            {"id": "gIXjUEc2pN8", "title": "【東京旅行/vlog】5時間で巡る東京 東京タワー/増上寺/銀座/浅草/上野"},
        ],
        "shorts": [
            {"id": "DrxPlizXSsk", "title": "東京タワーの楽しみ方"},
            {"id": "o0reV0gfBV4", "title": "東京タワー 展望フロア案内"},
        ],
        "access": "都営大江戸線・赤羽橋駅から徒歩約5分 / 日比谷線・神谷町駅から徒歩約7分",
        "hours": "メインデッキ9:00〜22:30（最終入場22:00）※変動あり",
        "holiday": "なし", "parking": "あり（有料）",
        "feature": "メインデッキ・トップデッキ・夜景・ライトアップ・増上寺・芝公園",
        "lat": 35.6586, "lng": 139.7454,
        "kw_jp": "東京タワー", "kw_en": "Tokyo Tower", "kw_book": "Tokyo Tower Minato",
        "related": [("shibuya", "東京都 渋谷区", "渋谷スクランブル交差点"),
                    ("skytree", "東京都 墨田区", "東京スカイツリー"),
                    ("meiji-jingu", "東京都 渋谷区", "明治神宮")],
    },
    {
        "slug": "meiji-jingu", "name": "明治神宮", "area_label": "東京エリア",
        "location": "東京都渋谷区", "tag": "神社・自然",
        "desc": "明治天皇と昭憲皇太后を祀る、初詣参拝者数日本一を誇る神社。原宿駅のすぐそばにありながら、約70万平方mの広大な杜（もり）に包まれ、都心とは思えない静寂と緑が広がります。荘厳な社殿や清正井（きよまさのいど）などパワースポットも多く、参拝と森林浴を一度に楽しめます。",
        "videos": [
            {"id": "WJt78DGUFCU", "title": "⛩️【4K.明治神宮】原宿駅から境内までの行き方を参道MAP付きでご案内"},
            {"id": "xiwjHz2bIrw", "title": "明治神宮散歩 |【4K】Walking Meiji Jingu Shrine Tokyo"},
            {"id": "2antnSv7dpQ", "title": "【東京観光】日本一の参拝者数を誇る聖地『明治神宮』境内散策"},
            {"id": "RXmJlxgj_98", "title": "[4K] MEIJI JINGU Tokyo Walking Tour 明治神宮 散歩"},
        ],
        "shorts": [
            {"id": "xiwjHz2bIrw", "title": "明治神宮 4K散歩"},
            {"id": "RXmJlxgj_98", "title": "明治神宮 ウォーキングツアー"},
        ],
        "access": "JR山手線・原宿駅／東京メトロ・明治神宮前駅すぐ（南参道入口）",
        "hours": "日の出〜日の入り（月により変動）",
        "holiday": "なし", "parking": "あり（有料）",
        "feature": "大鳥居・社殿・清正井・御苑・初詣・森林浴・原宿至近",
        "lat": 35.6764, "lng": 139.6993,
        "kw_jp": "原宿", "kw_en": "Harajuku Meiji Jingu Tokyo", "kw_book": "Harajuku Tokyo",
        "related": [("shibuya", "東京都 渋谷区", "渋谷スクランブル交差点"),
                    ("asakusa", "東京都 台東区", "浅草寺・雷門"),
                    ("tokyo-tower", "東京都 港区", "東京タワー")],
    },
    {
        "slug": "ueno", "name": "上野公園・アメ横", "area_label": "東京エリア",
        "location": "東京都台東区", "tag": "公園・下町・グルメ",
        "desc": "博物館・美術館・動物園が集まる文化の杜「上野恩賜公園」と、活気あふれる商店街「アメ横（アメヤ横丁）」。上野動物園のパンダや、桜の名所として知られる園内、不忍池の蓮、所狭しと店が並ぶアメ横での食べ歩き・買い物まで、一日中楽しめる下町の人気エリアです。",
        "videos": [
            {"id": "dJ8K_HedLfo", "title": "【上野】上野公園&アメ横を散策♪"},
            {"id": "K_yho-6nAtU", "title": "【4K】お昼時の上野 アメ横を散歩 Walk around Ameyoko"},
            {"id": "MV1GbNIiFXA", "title": "4K【東京上野・夜散歩】上野公園・不忍池辯天堂・上野アメ横"},
            {"id": "eBYA_aUd-qc", "title": "【4K】上野 アメ横 観光客で賑わう商店街を散歩"},
        ],
        "shorts": [
            {"id": "K_yho-6nAtU", "title": "上野アメ横 お昼の散歩"},
            {"id": "eBYA_aUd-qc", "title": "上野アメ横 賑わう商店街"},
        ],
        "access": "JR・東京メトロ・京成線 上野駅すぐ（公園口・不忍口）",
        "hours": "公園は終日／施設・アメ横は店舗により異なる",
        "holiday": "施設により異なる（動物園は月曜休園など）", "parking": "周辺有料駐車場",
        "feature": "上野動物園・パンダ・博物館・美術館・桜・不忍池・アメ横食べ歩き",
        "lat": 35.7156, "lng": 139.7745,
        "kw_jp": "上野", "kw_en": "Ueno Tokyo", "kw_book": "Ueno Tokyo",
        "related": [("asakusa", "東京都 台東区", "浅草寺・雷門"),
                    ("skytree", "東京都 墨田区", "東京スカイツリー"),
                    ("shibuya", "東京都 渋谷区", "渋谷スクランブル交差点")],
    },
]


def affiliate_block(spot):
    name = spot["name"]
    kw_jp = quote(spot["kw_jp"])
    kw_en = quote(spot["kw_en"])
    kw_book = quote(spot["kw_book"])
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
        '    </div>\n'
        '  </div>'
    )


def head_extra(spot):
    """canonical・OGP・GA・AdSense・TouristAttraction構造化データを生成（静岡ページと同等）。"""
    slug, name, tag, location = spot["slug"], spot["name"], spot["tag"], spot["location"]
    url = f"https://dokoriaru.com/spots/{slug}/"
    desc = (f"{name}の{tag}をSNS動画でリアルにチェック。"
            f"YouTube・Instagram・TikTokの動画をまとめて確認できます。行く前に雰囲気をチェック。")
    schema = (
        '{\n'
        '  "@context": "https://schema.org",\n'
        '  "@type": "TouristAttraction",\n'
        f'  "name": "{name}",\n'
        f'  "description": "{desc}",\n'
        f'  "url": "{url}",\n'
        '  "image": "https://dokoriaru.com/ogp.png",\n'
        '  "address": {\n'
        '    "@type": "PostalAddress",\n'
        f'    "addressRegion": "{location}",\n'
        '    "addressCountry": "JP"\n'
        '  },\n'
        '  "geo": {\n'
        '    "@type": "GeoCoordinates",\n'
        f'    "latitude": {spot["lat"]},\n'
        f'    "longitude": {spot["lng"]}\n'
        '  },\n'
        '  "touristType": "観光客",\n'
        '  "inLanguage": "ja"\n'
        '}'
    )
    return (
        f'<link rel="canonical" href="{url}">\n'
        '<link rel="icon" href="../../favicon.ico">\n'
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


def fix_nav(html):
    nav_new = (
        '  <nav>\n'
        '    <a href="../../">トップ</a>\n'
        '    <a href="../../tokyo/">東京</a>\n'
        '    <a href="../asakusa/">浅草</a>\n'
        '    <a href="../shibuya/">渋谷</a>\n'
        '  </nav>'
    )
    return re.sub(r'  <nav>\s*<a href="\.\./\.\./">トップ</a>.*?</nav>', nav_new, html, count=1, flags=re.DOTALL)


def main():
    created, skipped = [], []
    for spot in TOKYO_SPOTS:
        # generate_html はこれらのキーを使わないが互換のため補完
        spot.setdefault("jalan", "")
        spot.setdefault("tabelog", "")
        dir_path = os.path.join(BASE, "spots", spot["slug"])
        fp = os.path.join(dir_path, "index.html")
        os.makedirs(dir_path, exist_ok=True)
        if os.path.exists(fp):
            skipped.append(spot["slug"]); print(f"skip: {spot['slug']}"); continue
        html = generate_html(spot)
        # head情報（canonical/OGP/GA/AdSense/構造化データ）を注入
        html = html.replace('</head>', head_extra(spot) + '</head>', 1)
        # ヘッダーnavを東京用に
        html = fix_nav(html)
        # アフィリエイトを楽天/Klook/Booking（既存IDを流用）に置換
        html = re.sub(r'  <div class="affiliate-section reveal">.*?</div>\s*</div>',
                      affiliate_block(spot), html, count=1, flags=re.DOTALL)
        with open(fp, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(spot["slug"]); print(f"created: {spot['slug']} — {spot['name']}")
    print(f"\n完了: {len(created)}件作成 / {len(skipped)}件スキップ")


if __name__ == "__main__":
    main()
