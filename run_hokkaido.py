#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""北海道エリア生成。"""
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
    "region_slug": "hokkaido", "region_label": "北海道エリア", "region_short": "北海道",
    "spots_oneline": "小樽運河・札幌・富良野・函館・旭山動物園",
    "nav_spots": [("otaru-canal", "小樽"), ("hakodate", "函館")],
    "area_nav_html": FINAL_NAV,
}

SPOTS = [
    {"slug": "otaru-canal", "name": "小樽運河", "area_label": "北海道エリア",
     "location": "北海道小樽市", "tag": "運河・レトロ・ガラス工芸",
     "desc": "大正時代に築かれた、北海道を代表するレトロな観光名所。運河沿いに石造りの倉庫が並び、夕暮れにガス灯がともる風景は幻想的。クルーズ船での遊覧や、堺町通り商店街でのガラス工芸・オルゴール・スイーツめぐりも楽しめます。雪化粧した冬の運河も格別の美しさです。",
     "videos": [{"id": "uBODyikKYPk", "title": "【小樽観光】定番街歩き 堺町通り商店街〜小樽運河／小樽の歩き方"},
                {"id": "J6HzCwKZan4", "title": "【北海道】小樽ひとり旅〜運河とニシン、鉄道のまち 1日大満喫モデルコース"},
                {"id": "SYQ9BwYk5uM", "title": "小樽運河クルーズ観光 4K"},
                {"id": "hC3ouILq55E", "title": "【小樽】冬の散歩！三角市場・小樽運河・北一硝子 4K"}],
     "shorts": [{"id": "7Sv36xK7iFc", "title": "JG 4K 北海道 小樽運河"},
                {"id": "GgTQG2h3nL8", "title": "小樽 運河と坂の港町さんぽ"}],
     "access": "JR函館本線・小樽駅から徒歩約8分", "hours": "散策自由（店舗により異なる）",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "石造倉庫・ガス灯・運河クルーズ・堺町通り・ガラス工芸・オルゴール堂",
     "lat": 43.1979, "lng": 140.9947, "kw_jp": "小樽", "kw_en": "Otaru Hokkaido", "kw_book": "Otaru Hokkaido",
     "card_tag": "運河・レトロ", "card_desc": "ガス灯が灯る大正ロマンの運河。ガラス工芸やスイーツ巡りも人気。",
     "related": [("sapporo", "北海道 札幌市", "札幌・大通公園"), ("hakodate", "北海道 函館市", "函館山の夜景"), ("asahiyama-zoo", "北海道 旭川市", "旭山動物園")]},

    {"slug": "sapporo", "name": "札幌・大通公園", "area_label": "北海道エリア",
     "location": "北海道札幌市", "tag": "都市・公園・グルメ",
     "desc": "北海道の中心都市・札幌のシンボル「大通公園」を中心とした繁華街エリア。さっぽろテレビ塔や時計台などの名所、雪まつりやビアガーデンなど季節イベントの会場としても有名です。歓楽街「すすきの」では味噌ラーメン・ジンギスカン・海鮮など北海道グルメを満喫でき、観光の拠点に最適です。",
     "videos": [{"id": "LNqMdxH1_DQ", "title": "【4K 札幌散歩】札幌駅から大通公園を歩く HOKKAIDO Sapporo Walk"},
                {"id": "FpRa8L_Rq_w", "title": "【北海道】札幌駅周辺・大通公園 歴史的建造物ぶら散歩"},
                {"id": "z69YqFviio4", "title": "Sapporo Autumn Walking Tour - Hokkaido Japan [4K/HDR]"},
                {"id": "acx0bCQxeic", "title": "札幌駅からすすきのへ 夜散歩 Sapporo Night Walk"}],
     "shorts": [{"id": "BOs90D_Ng-w", "title": "雪化粧の札幌 すすきの〜大通公園"},
                {"id": "jP7nNHNszgk", "title": "札幌ライラック祭り 散歩"}],
     "access": "JR札幌駅から地下鉄・徒歩。大通公園は地下鉄各線「大通駅」直結", "hours": "公園は終日（施設・店舗により異なる）",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "大通公園・さっぽろテレビ塔・時計台・すすきの・雪まつり・味噌ラーメン",
     "lat": 43.0608, "lng": 141.3469, "kw_jp": "札幌", "kw_en": "Sapporo Hokkaido", "kw_book": "Sapporo Hokkaido",
     "card_tag": "都市・グルメ", "card_desc": "北海道の中心都市。大通公園・すすきの・北海道グルメを満喫できる。",
     "related": [("otaru-canal", "北海道 小樽市", "小樽運河"), ("asahiyama-zoo", "北海道 旭川市", "旭山動物園"), ("furano", "北海道 富良野市", "富良野・ファーム富田")]},

    {"slug": "furano", "name": "富良野・ファーム富田", "area_label": "北海道エリア",
     "location": "北海道中富良野町", "tag": "花畑・ラベンダー・絶景",
     "desc": "北海道を代表するラベンダーの名所。ファーム富田では、丘一面を彩る紫のラベンダー畑と色とりどりの花のグラデーションが広がり、夏にはまるで絵画のような絶景に。ラベンダーソフトクリームなどの名物も人気です。富良野・美瑛の雄大な丘陵風景とあわせて、北海道の夏を満喫できます。",
     "videos": [{"id": "vZt2xUWM2x4", "title": "ラベンダー開花！！『ファーム富田』最新版 【北海道 富良野】4K"},
                {"id": "J8c1xHBTuaQ", "title": "7月第1週ラベンダー真っ盛り！ファーム富田〜ラベンダーイースト 4K"},
                {"id": "C68ZUSUx4pE", "title": "【最新版】ファーム富田、町営ラベンダー園、ラベンダーイースト 富良野ラベンダー 4K"},
                {"id": "-Zl0mCYUOjU", "title": "ベストシーズンに行く！【富良野ラベンダー巡り】中富良野編"}],
     "shorts": [{"id": "pTJaq0bkY8k", "title": "早咲きラベンダー満開 ファーム富田 4K"},
                {"id": "5NYWB7GOs34", "title": "ファーム富田 ラベンダーイースト"}],
     "access": "JR富良野線・ラベンダー畑駅（夏季臨時駅）から徒歩約7分／旭川・富良野から車", "hours": "見学自由（季節・施設により異なる）",
     "holiday": "なし（冬季は一部休業）", "parking": "あり（無料）",
     "feature": "ラベンダー畑・花のグラデーション・ラベンダーソフト・富良野美瑛の丘",
     "lat": 43.4216, "lng": 142.4197, "kw_jp": "富良野", "kw_en": "Furano Lavender Hokkaido", "kw_book": "Furano Hokkaido",
     "card_tag": "花畑・絶景", "card_desc": "丘一面を彩るラベンダー畑。夏の北海道を代表する絶景スポット。",
     "related": [("shirogane-blue-pond", "北海道 美瑛町", "青い池（美瑛）"), ("asahiyama-zoo", "北海道 旭川市", "旭山動物園"), ("sapporo", "北海道 札幌市", "札幌・大通公園")]},

    {"slug": "hakodate", "name": "函館山の夜景", "area_label": "北海道エリア",
     "location": "北海道函館市", "tag": "夜景・展望",
     "desc": "「世界三大夜景」「日本三大夜景」に数えられる函館の象徴。函館山の山頂展望台からは、両側を海に挟まれたくびれた地形に街の明かりが輝く、宝石箱のような絶景が広がります。ロープウェイで手軽に山頂へ。ふもとには赤レンガ倉庫や元町の坂、函館朝市など見どころも豊富です。",
     "videos": [{"id": "MBtm2R-scPo", "title": "【函館夜景】世界三大夜景の函館山からの夜景 ベイエリア・元町・朝市も巡る旅"},
                {"id": "ftKNY9DSOSY", "title": "【函館山】函館観光に必須！昼も夜も大満足の景色 ロープウェイのベスト時間も紹介"},
                {"id": "IzLQNKa4TgE", "title": "【函館】函館山！100万ドルの夜景！ロープウェイで行ってみた"},
                {"id": "XAeio736Tos", "title": "函館観光・函館の夜景【函館山の夜景】"}],
     "shorts": [{"id": "cCrdWf4u5DM", "title": "函館山で冬の夜景 ロープウェイ"},
                {"id": "XcKCW-eYEKQ", "title": "函館山の朝日 北海道絶景スポット"}],
     "access": "函館山ロープウェイ山麓駅まで市電「十字街」から徒歩約10分→ロープウェイ約3分", "hours": "ロープウェイ10:00〜22:00（時季変動）",
     "holiday": "整備運休あり", "parking": "山麓に周辺駐車場（山頂へは夜間車両規制あり）",
     "feature": "函館山展望台・100万ドルの夜景・ロープウェイ・赤レンガ倉庫・元町・函館朝市",
     "lat": 41.7587, "lng": 140.7041, "kw_jp": "函館", "kw_en": "Hakodate Hokkaido", "kw_book": "Hakodate Hokkaido",
     "card_tag": "夜景・展望", "card_desc": "世界三大夜景に数えられる函館山の絶景。100万ドルの夜景が広がる。",
     "related": [("otaru-canal", "北海道 小樽市", "小樽運河"), ("sapporo", "北海道 札幌市", "札幌・大通公園"), ("furano", "北海道 富良野市", "富良野・ファーム富田")]},

    {"slug": "asahiyama-zoo", "name": "旭山動物園", "area_label": "北海道エリア",
     "location": "北海道旭川市", "tag": "動物園",
     "desc": "動物本来の生き生きとした姿を見せる「行動展示」で全国的な人気を誇る動物園。空を飛ぶように泳ぐペンギンを見上げる水中トンネルや、ホッキョクグマの豪快なダイブ、冬の名物「ペンギンの散歩」など、ここでしか見られない展示が満載。子どもから大人まで夢中になれる北海道屈指の人気スポットです。",
     "videos": [{"id": "m6kdGwV6sEY", "title": "【北海道 旭川】旭山動物園で大興奮！動物好き必見の一人旅 旭川観光モデルコース"},
                {"id": "6bfNE2dhtQE", "title": "【旭川】ペンギンの散歩が可愛いすぎた！旭山動物園 4K Asahiyama Zoo"},
                {"id": "M-SmGYZ5tDk", "title": "【北海道観光】たった4分でわかる、冬の旭山動物園の巡り方入門"},
                {"id": "1GFMiDGs_AY", "title": "旭川から行く北海道観光レポ 旭山動物園と美瑛・富良野"}],
     "shorts": [{"id": "6bfNE2dhtQE", "title": "旭山動物園 ペンギンの散歩"},
                {"id": "rVjBzfiN7M4", "title": "北海道旭山動物園ハイライト"}],
     "access": "JR旭川駅からバス約40分「旭山動物園」下車すぐ／旭川空港から車約30分", "hours": "夏季9:30〜17:15・冬季10:30〜15:30（時季変動）",
     "holiday": "年末年始ほか（公式要確認）", "parking": "あり（無料・周辺有料あり）",
     "feature": "行動展示・ペンギン水中トンネル・ホッキョクグマ・ペンギンの散歩（冬）",
     "lat": 43.7686, "lng": 142.4804, "kw_jp": "旭川", "kw_en": "Asahikawa Hokkaido", "kw_book": "Asahikawa Hokkaido",
     "card_tag": "動物園", "card_desc": "行動展示で人気の動物園。冬のペンギンの散歩は必見。",
     "related": [("sapporo", "北海道 札幌市", "札幌・大通公園"), ("furano", "北海道 富良野市", "富良野・ファーム富田"), ("shirogane-blue-pond", "北海道 美瑛町", "青い池（美瑛）")]},

    {"slug": "shirogane-blue-pond", "name": "青い池（美瑛）", "area_label": "北海道エリア",
     "location": "北海道美瑛町", "tag": "絶景・自然",
     "desc": "美瑛の白金エリアにある、神秘的なコバルトブルーの水をたたえた池。立ち枯れたカラマツが水面から突き出す光景は幻想的で、SNSや写真愛好家に大人気のフォトスポットです。季節や天候、光の角度で青の色合いが変化するのも魅力。近くの白ひげの滝とあわせて、美瑛の絶景ドライブが楽しめます。",
     "videos": [{"id": "OuDDMUKnbQ0", "title": "青い池がやばい！！ 初夏【北海道 美瑛 青い池】4K"},
                {"id": "EmhF4JhZ2aQ", "title": "春の美瑛の素敵な景観〜青い池〜白金の道〜白ひげの滝 4K"},
                {"id": "eN3UeSMvXAw", "title": "【北海道 美瑛】夏の白金絶景ドライブ〜青い池〜白ひげの滝〜望岳台 4K"},
                {"id": "P21qCz8ULiI", "title": "【北海道 美瑛】日本で一番美しい道、青い池、白金の素敵な景観 4K"}],
     "shorts": [{"id": "SlCJQJ3A9sA", "title": "人がいない青い池 今だけの贅沢"},
                {"id": "eTn_uqX_1fw", "title": "秋の美瑛 紅葉・青い池"}],
     "access": "JR美瑛駅から車約20分／道北バス「白金青い池入口」下車徒歩約5分", "hours": "見学自由（夜間ライトアップ期間あり）",
     "holiday": "なし", "parking": "あり（有料）",
     "feature": "コバルトブルーの池・立ち枯れの木・白ひげの滝・美瑛の丘・ライトアップ",
     "lat": 43.4925, "lng": 142.6406, "kw_jp": "美瑛", "kw_en": "Biei Blue Pond Hokkaido", "kw_book": "Biei Hokkaido",
     "card_tag": "絶景・自然", "card_desc": "神秘的なコバルトブルーの池。美瑛を代表する人気のフォトスポット。",
     "related": [("furano", "北海道 富良野市", "富良野・ファーム富田"), ("asahiyama-zoo", "北海道 旭川市", "旭山動物園"), ("sapporo", "北海道 札幌市", "札幌・大通公園")]},
]

if __name__ == "__main__":
    run(CFG, SPOTS)
