#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""福岡エリア生成。"""
from add_region import run

FINAL_NAV = (
    '        <a href="/shizuoka/" class="nav-menu-item">🗾 静岡 <span class="badge badge-live">掲載中</span></a>\n'
    '        <a href="/tokyo/" class="nav-menu-item">🗼 東京 <span class="badge badge-live">掲載中</span></a>\n'
    '        <a href="/osaka/" class="nav-menu-item">🏯 大阪 <span class="badge badge-live">掲載中</span></a>\n'
    '        <a href="/hokkaido/" class="nav-menu-item">🐻 北海道 <span class="badge badge-live">掲載中</span></a>\n'
    '        <a href="/fukuoka/" class="nav-menu-item">🍜 福岡 <span class="badge badge-live">掲載中</span></a>\n'
    '        <div class="nav-menu-divider"></div>\n'
    '        <span class="nav-menu-item coming">🌸 京都 <span class="badge badge-soon">準備中</span></span>\n'
    '        <span class="nav-menu-item coming">🌺 沖縄 <span class="badge badge-soon">準備中</span></span>\n'
)

CFG = {
    "region_slug": "fukuoka", "region_label": "福岡エリア", "region_short": "福岡",
    "spots_oneline": "太宰府天満宮・中洲屋台・福岡タワー・大濠公園・糸島",
    "nav_spots": [("dazaifu", "太宰府"), ("nakasu-yatai", "中洲屋台")],
    "area_nav_html": FINAL_NAV,
}

SPOTS = [
    {"slug": "dazaifu", "name": "太宰府天満宮", "area_label": "福岡エリア",
     "location": "福岡県太宰府市", "tag": "神社・参道・食べ歩き",
     "desc": "学問の神様・菅原道真公を祀る、全国天満宮の総本宮として知られる名社。受験合格や学業成就を願う参拝者で一年中にぎわいます。境内の御神牛や飛梅、最強パワースポット「天開稲荷社」も見どころ。参道には名物「梅ヶ枝餅」の店が並び、食べ歩きも楽しめる福岡屈指の観光地です。",
     "videos": [{"id": "t1-ZsRiuPWU", "title": "【福岡観光名所】今、行くべき「太宰府天満宮」＆最強パワースポット「天開稲荷社」参道散策"},
                {"id": "lwjJ2ogMy_o", "title": "【完全ガイド】太宰府天満宮のご利益・参拝方法・御朱印・隠れスポットを徹底解説！"},
                {"id": "Rgaj7IYVrO0", "title": "【最新】太宰府天満宮の参道グルメ！出身者が徹底解説！梅ヶ枝餅"},
                {"id": "RRFo_xh3VQc", "title": "【福岡観光スポット】インバウンドに沸く太宰府天満宮を歩く"}],
     "shorts": [{"id": "JHn9by2sUF8", "title": "太宰府ひとり旅 モデルコース"},
                {"id": "O2BL3YMDLmI", "title": "太宰府天満宮 おすすめスポット"}],
     "access": "西鉄太宰府線・太宰府駅から徒歩約5分", "hours": "開門6:00〜（時季変動）／参道は店舗により異なる",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "本殿・御神牛・飛梅・天開稲荷社・参道の梅ヶ枝餅・九州国立博物館",
     "lat": 33.5215, "lng": 130.5347, "kw_jp": "太宰府", "kw_en": "Dazaifu Fukuoka", "kw_book": "Dazaifu Fukuoka",
     "card_tag": "神社・参道", "card_desc": "学問の神様を祀る総本宮。参道の梅ヶ枝餅の食べ歩きも人気。",
     "related": [("nakasu-yatai", "福岡県 福岡市", "中洲・屋台街"), ("ohori-park", "福岡県 福岡市", "大濠公園"), ("fukuoka-tower", "福岡県 福岡市", "福岡タワー")]},

    {"slug": "nakasu-yatai", "name": "中洲・屋台街", "area_label": "福岡エリア",
     "location": "福岡県福岡市", "tag": "屋台・グルメ・繁華街",
     "desc": "九州最大の歓楽街・中洲を流れる那珂川沿いに、夜になると数十軒の屋台が立ち並ぶ福岡名物のスポット。博多ラーメンや焼きラーメン、おでん、明太子料理など、屋台ならではのグルメと人情味あふれる雰囲気が魅力です。川面にネオンが映る夜景も美しく、福岡の夜を満喫できる定番エリアです。",
     "videos": [{"id": "pa6AWhzQ4QI", "title": "【九州最大の歓楽街】福岡市博多区の屋台街『中洲』散策"},
                {"id": "ar1NBUQwWSI", "title": "【福岡4軒】博多/中洲屋台グルメを飲み歩いてみた！焼ラーメン/明太子/おでん"},
                {"id": "lYvat-2HJfM", "title": "【福岡旅行】福岡の夜はやっぱ中洲屋台！これを食べなきゃ終われない"},
                {"id": "IrpvjmoLp08", "title": "中洲川端商店街と中洲屋台街を散策してみた【福岡観光モデルコース】"}],
     "shorts": [{"id": "BiO7HdZHLnU", "title": "リピート確定の福岡屋台"},
                {"id": "092shYd7ONo", "title": "博多中洲屋台めし"}],
     "access": "福岡市地下鉄・中洲川端駅／天神南駅から徒歩圏", "hours": "屋台は夕方〜深夜（店舗により異なる）",
     "holiday": "店舗・天候により異なる", "parking": "周辺有料駐車場",
     "feature": "那珂川沿いの屋台・博多ラーメン・焼きラーメン・明太子・川沿いの夜景",
     "lat": 33.5919, "lng": 130.4067, "kw_jp": "中洲 博多", "kw_en": "Nakasu Hakata Fukuoka", "kw_book": "Nakasu Fukuoka",
     "card_tag": "屋台・グルメ", "card_desc": "那珂川沿いに屋台が並ぶ福岡名物。博多ラーメンや焼きラーメンが楽しめる。",
     "related": [("dazaifu", "福岡県 太宰府市", "太宰府天満宮"), ("fukuoka-tower", "福岡県 福岡市", "福岡タワー"), ("canal-city", "福岡県 福岡市", "キャナルシティ博多")]},

    {"slug": "fukuoka-tower", "name": "福岡タワー", "area_label": "福岡エリア",
     "location": "福岡県福岡市", "tag": "展望・夜景・ランドマーク",
     "desc": "高さ234mを誇る日本一の海浜タワー。地上123mの展望室からは、福岡市街と博多湾を見渡す360度のパノラマが広がります。8,000枚のハーフミラーで覆われた外観は、夜になるとイルミネーションで彩られ「光のタワー」に。シーサイドももち海浜公園に隣接し、海辺の景色とあわせて楽しめる福岡のランドマークです。",
     "videos": [{"id": "hTHx5k4y9Ds", "title": "福岡タワー トワイライト〜絶景！夜景 Fukuoka Tower Superb view"},
                {"id": "wKyD43CbdhA", "title": "【美景】福岡タワーの夜景"},
                {"id": "qdcn38G7lYs", "title": "【夜の福岡市内を散策】夜景＆観光スポット 天神・博多・百道"},
                {"id": "ltOc2mKQvy4", "title": "【福岡タワー イルミネーション】サザエさん"}],
     "shorts": [{"id": "hscgpCvIA2Q", "title": "福岡タワー 地上123mの絶景"},
                {"id": "rSCG8WVn3EY", "title": "福岡市の夜景"}],
     "access": "地下鉄・西新駅から徒歩約20分、または天神からバス約20分「福岡タワー」下車", "hours": "9:30〜22:00（最終入館21:30）※変動あり",
     "holiday": "6月の年次休館ほか", "parking": "あり（有料）",
     "feature": "展望室・360度パノラマ・博多湾・イルミネーション・シーサイドももち",
     "lat": 33.5934, "lng": 130.3514, "kw_jp": "福岡 百道", "kw_en": "Fukuoka Tower Momochi", "kw_book": "Momochi Fukuoka",
     "card_tag": "展望・夜景", "card_desc": "高さ234mの海浜タワー。博多湾を望む夜景とイルミネーションが名物。",
     "related": [("nakasu-yatai", "福岡県 福岡市", "中洲・屋台街"), ("ohori-park", "福岡県 福岡市", "大濠公園"), ("itoshima", "福岡県 糸島市", "糸島")]},

    {"slug": "ohori-park", "name": "大濠公園", "area_label": "福岡エリア",
     "location": "福岡県福岡市", "tag": "公園・自然・癒やし",
     "desc": "福岡市の中心部にある、大きな池を中心とした水景公園。かつての福岡城のお堀を生かした広大な園内には、池に浮かぶ島々をつなぐ橋や、日本庭園、スターバックスなどがあり、市民や観光客の憩いの場になっています。隣接する舞鶴公園は福岡城跡と桜の名所。都会のオアシスとして散策やジョギングが楽しめます。",
     "videos": [{"id": "XaFS9hTOCec", "title": "【福岡観光】福岡市の広大な水景公園『大濠公園』散策"},
                {"id": "kB4G6hra5Lw", "title": "【4K】福岡をEnjoy！赤坂駅から大濠公園駅をお散歩"},
                {"id": "oeAFid6bU0Y", "title": "【福岡】大濠公園（舞鶴公園）都会のオアシスを散策！福岡城跡が立派"},
                {"id": "BPnJl14s8hw", "title": "【福岡観光vlog 大濠公園編】博多駅から電車で9分の癒し空間"}],
     "shorts": [{"id": "MJiGNAW0Ybg", "title": "大濠公園 福岡人気観光スポット"},
                {"id": "7XJNRt4R2CE", "title": "都会のオアシス 大濠公園・舞鶴公園"}],
     "access": "福岡市地下鉄・大濠公園駅から徒歩約3分", "hours": "終日（施設により異なる）",
     "holiday": "なし", "parking": "あり（有料）",
     "feature": "大きな池・浮島と橋・日本庭園・舞鶴公園(福岡城跡)・桜・ジョギングコース",
     "lat": 33.5856, "lng": 130.3789, "kw_jp": "福岡 大濠公園", "kw_en": "Ohori Park Fukuoka", "kw_book": "Ohori Park Fukuoka",
     "card_tag": "公園・自然", "card_desc": "お堀を生かした水景公園。福岡城跡や桜も楽しめる都会のオアシス。",
     "related": [("fukuoka-tower", "福岡県 福岡市", "福岡タワー"), ("dazaifu", "福岡県 太宰府市", "太宰府天満宮"), ("canal-city", "福岡県 福岡市", "キャナルシティ博多")]},

    {"slug": "itoshima", "name": "糸島", "area_label": "福岡エリア",
     "location": "福岡県糸島市", "tag": "絶景・ドライブ・カフェ",
     "desc": "福岡市の西に隣接する、海沿いの絶景とおしゃれなカフェで人気のドライブスポット。「桜井二見ヶ浦の夫婦岩と白い鳥居」や、SNSで話題のヤシの木ブランコ、海辺に並ぶ映えスポットが点在します。新鮮な海鮮やこだわりのカフェ、地元産の塩工房など、絶景とグルメをめぐる女子旅・デートに人気のエリアです。",
     "videos": [{"id": "1ER7NvVoCCQ", "title": "【糸島】1日で8ヶ所回る！大満足旅モデルコース【福岡】"},
                {"id": "tf_pr4BPM7c", "title": "【糸島大人旅】糸島のおすすめスポット全部行ってみた！2025年最新情報"},
                {"id": "QBr_x1VlYb0", "title": "[糸島] 福岡 車なら行きたい人気の観光地・おしゃれなスポットをピックアップ！"},
                {"id": "DZ9HFM0Rrwg", "title": "【福岡旅行】レンタカーで博多〜糸島を1日女子ドライブ旅！最強映え日帰りプラン"}],
     "shorts": [{"id": "CMsL7lY6qTM", "title": "糸島カフェ 海沿いの道 4K"},
                {"id": "EB-g9aDEQtk", "title": "糸島グルメ23選 絶景カフェ"}],
     "access": "JR筑肥線・筑前前原駅からバス・車／福岡市内から車約40分", "hours": "見学自由（店舗により異なる）",
     "holiday": "店舗により異なる", "parking": "各スポットに駐車場",
     "feature": "桜井二見ヶ浦の夫婦岩・白い鳥居・ヤシの木ブランコ・海辺のカフェ・海鮮",
     "lat": 33.6403, "lng": 130.2061, "kw_jp": "糸島", "kw_en": "Itoshima Fukuoka", "kw_book": "Itoshima Fukuoka",
     "card_tag": "絶景・カフェ", "card_desc": "海沿いの絶景と映えスポット、おしゃれカフェで人気のドライブエリア。",
     "related": [("fukuoka-tower", "福岡県 福岡市", "福岡タワー"), ("ohori-park", "福岡県 福岡市", "大濠公園"), ("dazaifu", "福岡県 太宰府市", "太宰府天満宮")]},

    {"slug": "canal-city", "name": "キャナルシティ博多", "area_label": "福岡エリア",
     "location": "福岡県福岡市", "tag": "商業施設・噴水ショー",
     "desc": "「都市の劇場」をコンセプトにした、運河を中心とする大型複合商業施設。ショップやレストラン、映画館、劇場、ホテルが集まり、館内を流れる運河では音楽と光に合わせた「アクアパノラマ噴水ショー」が一日に何度も開催されます。映画やキャラクターとコラボした演出も話題で、買い物とエンタメを一度に楽しめます。",
     "videos": [{"id": "onNUtn41rdE", "title": "「イマジネーション」キャナルシティ博多 / アクアパノラマ噴水ショー"},
                {"id": "BYTp1MK_LZQ", "title": "キャナルシティ博多 サンプラザ噴水ショー 4K"},
                {"id": "DsLfkRw4mOo", "title": "キャナルシティ博多 噴水ショー"},
                {"id": "jCoP6MeP_Fw", "title": "Canal City HAKATA 噴水ショー"}],
     "shorts": [{"id": "o6ujkrkWA5c", "title": "サンタから雪のプレゼント 噴水ショー"},
                {"id": "5C-WjNnKvZY", "title": "夜のパステル噴水ショー"}],
     "access": "福岡市地下鉄・祇園駅／中洲川端駅から徒歩約7分、博多駅から徒歩約10分", "hours": "ショップ10:00〜21:00・飲食〜23:00（店舗により異なる）",
     "holiday": "なし", "parking": "あり（有料）",
     "feature": "運河・アクアパノラマ噴水ショー・ショップ・劇場・映画館・グルメ",
     "lat": 33.5897, "lng": 130.4117, "kw_jp": "博多 キャナルシティ", "kw_en": "Canal City Hakata Fukuoka", "kw_book": "Hakata Fukuoka",
     "card_tag": "商業施設", "card_desc": "運河を中心とした大型商業施設。音と光の噴水ショーが見どころ。",
     "related": [("nakasu-yatai", "福岡県 福岡市", "中洲・屋台街"), ("dazaifu", "福岡県 太宰府市", "太宰府天満宮"), ("fukuoka-tower", "福岡県 福岡市", "福岡タワー")]},
]

if __name__ == "__main__":
    run(CFG, SPOTS)
