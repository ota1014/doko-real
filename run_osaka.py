#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""大阪エリア生成。add_region.run を呼ぶ。"""
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
    "region_slug": "osaka", "region_label": "大阪エリア", "region_short": "大阪",
    "spots_oneline": "道頓堀・大阪城・USJ・通天閣・海遊館",
    "nav_spots": [("dotonbori", "道頓堀"), ("osaka-castle", "大阪城")],
    "area_nav_html": FINAL_NAV,
}

SPOTS = [
    {"slug": "dotonbori", "name": "道頓堀", "area_label": "大阪エリア",
     "location": "大阪府大阪市", "tag": "繁華街・食べ歩き",
     "desc": "「大阪・ミナミ」を代表する繁華街。グリコの巨大看板や動く「かに道楽」の看板が並ぶネオン街で、たこ焼き・お好み焼き・串カツなど大阪名物の食べ歩きが楽しめます。道頓堀川の遊覧船や、活気あふれる雰囲気は大阪観光の定番中の定番です。",
     "videos": [{"id": "PhRxRQtbJ38", "title": "【4K 大阪 japan】大阪観光の王道、おもろい道頓堀をご案内 vlog"},
                {"id": "j0BxRh9rkuM", "title": "【大阪観光】ミナミの有名観光地、道頓堀を徹底的に紹介！食べ歩きグルメから見どころまで"},
                {"id": "04TmMDzS6ak", "title": "【食い倒れ大阪旅行】道頓堀から新世界の名物料理をフラフラ食べ歩き"},
                {"id": "A5iWLIUYl3Q", "title": "【大阪 道頓堀】グルメ攻略ガイド たこ焼きや肉まんやミンチカツなど食べ歩き"}],
     "shorts": [{"id": "E8m7ulLSRDI", "title": "道頓堀 食べ歩きvlog 絶品グルメ8選"},
                {"id": "A5iWLIUYl3Q", "title": "道頓堀 グルメ攻略"}],
     "access": "大阪メトロ御堂筋線・なんば駅／心斎橋駅から徒歩約5分", "hours": "終日（店舗により異なる）",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "グリコ看板・かに道楽・たこ焼き・お好み焼き・串カツ・道頓堀川クルーズ",
     "lat": 34.6687, "lng": 135.5012, "kw_jp": "難波", "kw_en": "Namba Dotonbori Osaka", "kw_book": "Namba Osaka",
     "card_tag": "繁華街・グルメ", "card_desc": "グリコ看板で有名なミナミの繁華街。大阪グルメの食べ歩きの聖地。",
     "related": [("osaka-castle", "大阪府 大阪市", "大阪城"), ("tsutenkaku", "大阪府 大阪市", "通天閣・新世界"), ("kaiyukan", "大阪府 大阪市", "海遊館")]},

    {"slug": "osaka-castle", "name": "大阪城", "area_label": "大阪エリア",
     "location": "大阪府大阪市", "tag": "城・歴史・公園",
     "desc": "豊臣秀吉が築いた、大阪のシンボルともいえる名城。金の装飾が美しい天守閣は内部が歴史博物館になっており、最上階の展望台から大阪を一望できます。広大な大阪城公園は桜や梅の名所で、お堀や石垣も見応え十分。歴史と自然、絶景を一度に楽しめます。",
     "videos": [{"id": "ENo7vz7jtac", "title": "【お城紹介・大阪城】行く前に絶対観て！大阪城の楽しみ方完全紹介"},
                {"id": "AiyPvxLGa-o", "title": "【大阪城】外国人観光客に大人気の大阪城公園を歩く Osaka Castle Walk"},
                {"id": "SZBDSdw1CVE", "title": "【大阪城観光】ド定番コース！天守閣〜大阪城公園 散歩"},
                {"id": "T44yDJce4Pw", "title": "【大阪】関西で人気の観光名所 大阪城 Osaka Castle, Japan"}],
     "shorts": [{"id": "zUNFD5i8z-c", "title": "大阪城 おすすめ散策コース"},
                {"id": "AiyPvxLGa-o", "title": "大阪城公園を歩く"}],
     "access": "JR大阪環状線・大阪城公園駅／森ノ宮駅から徒歩、または大阪メトロ各線", "hours": "天守閣9:00〜17:00（最終入館16:30）",
     "holiday": "年末年始", "parking": "あり（有料）",
     "feature": "天守閣・展望台・歴史博物館・お堀・石垣・桜・梅林",
     "lat": 34.6873, "lng": 135.5259, "kw_jp": "大阪城", "kw_en": "Osaka Castle", "kw_book": "Osaka Castle Osaka",
     "card_tag": "城・歴史", "card_desc": "豊臣秀吉が築いた大阪のシンボル。天守閣からの眺めと桜が見どころ。",
     "related": [("dotonbori", "大阪府 大阪市", "道頓堀"), ("tsutenkaku", "大阪府 大阪市", "通天閣・新世界"), ("umeda-sky", "大阪府 大阪市", "梅田スカイビル空中庭園")]},

    {"slug": "usj", "name": "ユニバーサル・スタジオ・ジャパン", "area_label": "大阪エリア",
     "location": "大阪府大阪市", "tag": "テーマパーク",
     "desc": "映画の世界を体感できる世界的人気のテーマパーク。「スーパー・ニンテンドー・ワールド」や「ハリー・ポッター エリア」、ミニオンなど話題のアトラクションが満載。季節ごとのイベントやパレードも見どころで、一日中夢中になれる大阪屈指のエンターテインメントスポットです。",
     "videos": [{"id": "RSoa50TMrdE", "title": "【USJ25周年】高額課金にグリにグルメ！お祭り状態のユニバが楽しすぎた！Vlog"},
                {"id": "jvuMmeYAoRA", "title": "[USJ マリオエリア5周年] お祝いムード満載のvlog"},
                {"id": "EWGr-vPC8oE", "title": "[USJ最新] クロミ＆ブルースブラザーズ ショー体験Vlog"},
                {"id": "nHIS97kqTns", "title": "楽しすぎ1日！USJエリア全体がパワーアップ！家族で楽しむVlog"}],
     "shorts": [{"id": "jvuMmeYAoRA", "title": "USJ マリオエリア"},
                {"id": "RSoa50TMrdE", "title": "USJ25周年 お祭りユニバ"}],
     "access": "JRゆめ咲線・ユニバーサルシティ駅から徒歩約3分", "hours": "日により変動（公式サイト要確認）",
     "holiday": "なし", "parking": "あり（有料）",
     "feature": "スーパー・ニンテンドー・ワールド・ハリーポッター・ミニオン・パレード",
     "lat": 34.6654, "lng": 135.4323, "kw_jp": "ユニバーサルシティ", "kw_en": "Universal Studios Japan Osaka", "kw_book": "Universal City Osaka",
     "card_tag": "テーマパーク", "card_desc": "映画の世界を体感できる人気テーマパーク。マリオやハリポタが大人気。",
     "related": [("dotonbori", "大阪府 大阪市", "道頓堀"), ("kaiyukan", "大阪府 大阪市", "海遊館"), ("osaka-castle", "大阪府 大阪市", "大阪城")]},

    {"slug": "tsutenkaku", "name": "通天閣・新世界", "area_label": "大阪エリア",
     "location": "大阪府大阪市", "tag": "展望・下町・グルメ",
     "desc": "大阪のシンボルタワー「通天閣」と、その足元に広がるレトロな繁華街「新世界」。ネオンと大型看板がひしめく独特の街並みで、名物の串カツやどて焼きが味わえます。通天閣の展望台からは大阪の街を一望でき、幸運の神様「ビリケンさん」も鎮座する下町情緒満点のエリアです。",
     "videos": [{"id": "p0eZmEj3Un0", "title": "【ディープな大阪新世界巡り】ジャンジャン横丁や通天閣、大阪名物グルメを一日で巡る旅"},
                {"id": "vhWXtoGnqPM", "title": "【大阪 下町グルメ 新世界・通天閣 4K】大阪観光するならここは絶対外せない！"},
                {"id": "2ngbMWpiEXo", "title": "【大阪観光】新世界から特別展望台へ『大阪通天閣』散策"},
                {"id": "WEOkdom1p3U", "title": "【大阪観光】楽しめる街「新世界」、そして「通天閣」に上ってみた！"}],
     "shorts": [{"id": "r5AyvK3IN7w", "title": "新世界 通天閣の夜景 4K"},
                {"id": "vhWXtoGnqPM", "title": "新世界・通天閣 下町グルメ"}],
     "access": "大阪メトロ堺筋線・恵美須町駅／御堂筋線・動物園前駅から徒歩約5分", "hours": "通天閣展望台10:00〜20:00（最終入場19:30）",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "通天閣展望台・ビリケンさん・串カツ・ジャンジャン横丁・新世界の看板街",
     "lat": 34.6525, "lng": 135.5063, "kw_jp": "新世界 通天閣", "kw_en": "Shinsekai Tsutenkaku Osaka", "kw_book": "Shinsekai Osaka",
     "card_tag": "展望・下町", "card_desc": "大阪のシンボルタワーとレトロな新世界。串カツとビリケンさんが名物。",
     "related": [("dotonbori", "大阪府 大阪市", "道頓堀"), ("osaka-castle", "大阪府 大阪市", "大阪城"), ("umeda-sky", "大阪府 大阪市", "梅田スカイビル空中庭園")]},

    {"slug": "kaiyukan", "name": "海遊館", "area_label": "大阪エリア",
     "location": "大阪府大阪市", "tag": "水族館",
     "desc": "世界最大級の水族館のひとつ。太平洋を再現した巨大水槽では、ジンベエザメが悠々と泳ぐ姿を見られます。環太平洋の海を再現した展示を、らせん状のスロープで上から下へと巡る構成がユニーク。ベイエリアにあり、観覧車やショッピングモールと合わせて楽しめる人気スポットです。",
     "videos": [{"id": "bnihJhBCBC0", "title": "【大阪観光】海遊館の見どころ全てを紹介します。Osaka aquarium Kaiyukan"},
                {"id": "z0rx1qVaFco", "title": "海遊館行く前に見て！水族館が100倍楽しくなるプロの解説ツアー"},
                {"id": "eTD_yaAgaE4", "title": "【保存版】海遊館の見どころ完全ガイド｜全エリア徹底紹介"},
                {"id": "cLRC279PjvI", "title": "大阪観光／世界最大級の水族館 海遊館"}],
     "shorts": [{"id": "JwiVU1I7ICQ", "title": "4K 大阪 海遊館 水族館"},
                {"id": "eOOTfLcCft0", "title": "海遊館の見どころガイド"}],
     "access": "大阪メトロ中央線・大阪港駅から徒歩約5分", "hours": "10:00〜20:00（最終入館19:00）※変動あり",
     "holiday": "不定休", "parking": "あり（有料）",
     "feature": "ジンベエザメ・太平洋大水槽・環太平洋の展示・天保山観覧車・ベイエリア",
     "lat": 34.6545, "lng": 135.4289, "kw_jp": "天保山 海遊館", "kw_en": "Tempozan Kaiyukan Osaka", "kw_book": "Tempozan Osaka",
     "card_tag": "水族館", "card_desc": "ジンベエザメが泳ぐ世界最大級の水族館。ベイエリアの人気スポット。",
     "related": [("usj", "大阪府 大阪市", "ユニバーサル・スタジオ・ジャパン"), ("dotonbori", "大阪府 大阪市", "道頓堀"), ("tsutenkaku", "大阪府 大阪市", "通天閣・新世界")]},

    {"slug": "umeda-sky", "name": "梅田スカイビル空中庭園", "area_label": "大阪エリア",
     "location": "大阪府大阪市", "tag": "展望・夜景",
     "desc": "2棟の超高層ビルが空中でつながる独特の構造で知られる梅田スカイビル。最上部の「空中庭園展望台」は地上約170mの屋上が360度の展望スペースになっており、大阪随一の夜景スポットとして人気です。梅田の中心にありながら非日常的な絶景を味わえる、大阪のランドマークです。",
     "videos": [{"id": "REih8Ptd-Hc", "title": "4K60【梅田スカイビル空中庭園】展望台"},
                {"id": "cMqskSme6KY", "title": "【大阪の夜景を見るならココ！】梅田スカイビル空中庭園"},
                {"id": "jBff1jcK0p8", "title": "大阪で最も美しい夜景、梅田スカイビルに一人で行く夜【4K Vlog】空中庭園展望台"},
                {"id": "w_loeIL4ph8", "title": "【大阪 夜景巡り】梅田スカイビル空中庭園展望台 定番夜景スポット"}],
     "shorts": [{"id": "3YdR_OtgdeE", "title": "梅田スカイビルからの大阪夜景 4K"},
                {"id": "M43alJe5lYw", "title": "梅田スカイビル 空中庭園展望台に行ってみた"}],
     "access": "JR大阪駅／大阪メトロ梅田駅から徒歩約9分", "hours": "空中庭園展望台9:30〜22:30（最終入場22:00）※変動あり",
     "holiday": "なし", "parking": "あり（有料）",
     "feature": "空中庭園展望台・360度パノラマ・大阪の夜景・超高層建築・スカイウォーク",
     "lat": 34.7053, "lng": 135.4904, "kw_jp": "梅田", "kw_en": "Umeda Sky Building Osaka", "kw_book": "Umeda Osaka",
     "card_tag": "展望・夜景", "card_desc": "地上170mの空中庭園展望台。大阪随一の夜景が楽しめるランドマーク。",
     "related": [("osaka-castle", "大阪府 大阪市", "大阪城"), ("dotonbori", "大阪府 大阪市", "道頓堀"), ("tsutenkaku", "大阪府 大阪市", "通天閣・新世界")]},
]

if __name__ == "__main__":
    run(CFG, SPOTS)
