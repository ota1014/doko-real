#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ドコリアル スポットページ一括生成スクリプト"""

import os

BASE = os.path.dirname(os.path.abspath(__file__))

SPOTS = [
    {
        "slug": "asagiri-kogen",
        "name": "朝霧高原",
        "area_label": "富士山エリア",
        "location": "静岡県富士宮市",
        "tag": "自然・アクティビティ",
        "desc": "標高700〜1,000mに広がる富士山麓の高原。パラグライダー・乗馬・乳製品グルメが楽しめる。晴れた日には富士山の絶景と駿河湾を一望できるロケーションが魅力。田貫湖・白糸の滝へのアクセスも良い。",
        "videos": [
            {"id": "Us6wpUkN5lA", "title": "【公式4K】朝霧高原パラグライダー — 富士宮市観光PV"},
            {"id": "j2SLryXXhAY", "title": "奇跡が起きた感動のふもとっぱらキャンプ（富士山絶景）"},
            {"id": "9kvLzufr8fs", "title": "【公式4K】田貫湖 富士宮PV — 朝霧高原エリアの絶景湖"},
            {"id": "IJ3RhJwr7M8", "title": "【公式4K】白糸ノ滝 富士宮PV — 近隣の名瀑"},
        ],
        "shorts": [
            {"id": "Us6wpUkN5lA", "title": "朝霧高原 富士山パラグライダー"},
            {"id": "L-6TccaiC_w", "title": "富士山頂からのパラグライダー"},
        ],
        "access": "東名富士ICから車約40分 / JR富士宮駅から車約25分",
        "hours": "見学自由（各施設により異なる）",
        "holiday": "なし（施設により異なる）",
        "parking": "あり（各スポットに駐車場）",
        "feature": "富士山・パラグライダー・牛牧場・乳製品・キャンプ",
        "lat": 35.356, "lng": 138.557,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN007000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("shiraito-falls", "静岡県 富士宮市", "白糸の滝"),
            ("tanuki-lake", "静岡県 富士宮市", "田貫湖"),
            ("fumotoppara", "静岡県 富士宮市", "ふもとっぱら"),
        ],
    },
    {
        "slug": "dogashima",
        "name": "堂ヶ島",
        "area_label": "伊豆エリア",
        "location": "静岡県西伊豆町",
        "tag": "海・洞窟クルーズ",
        "desc": "西伊豆の絶景海岸。天然記念物「天窓洞」への洞窟遊覧船クルーズが人気。干潮時のみ現れる「トンボロ（陸繋砂州）」で三四郎島へ歩いて渡れる神秘的な体験ができる。",
        "videos": [
            {"id": "aX_5n9J1WFg", "title": "西伊豆・堂ヶ島 青の洞くつめぐり遊覧船（2022年）"},
            {"id": "9An9Ez10d6Y", "title": "【西伊豆・堂ヶ島トンボロ】海が割れて島へ続く道が現れる絶景"},
            {"id": "UfrO07-HOrU", "title": "【夫婦旅】伊豆・青の洞くつ〜天然記念物・堂ヶ島天窓洞"},
            {"id": "SHiCY1mKG3s", "title": "西伊豆の有名スポットが詰まった堂ヶ島が絶景だらけ"},
        ],
        "shorts": [
            {"id": "0QNPt7U3SLM", "title": "西伊豆観光モデルコース 堂ヶ島・土肥金山"},
            {"id": "aX_5n9J1WFg", "title": "堂ヶ島 洞窟クルーズ"},
        ],
        "access": "JR修善寺駅から東海バス約70分 / 沼津ICから車約90分",
        "hours": "遊覧船 9:00〜15:00（季節により変動）",
        "holiday": "荒天時運休",
        "parking": "あり（無料）",
        "feature": "洞窟クルーズ・トンボロ・夕日・天窓洞",
        "lat": 34.795, "lng": 138.756,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN018000/",
        "tabelog": "https://tabelog.com/shizuoka/A2204/A220404/",
        "related": [
            ("irozaki", "静岡県 南伊豆町", "石廊崎"),
            ("joren-falls", "静岡県 伊豆市", "浄蓮の滝"),
            ("shuzenji", "静岡県 伊豆市", "修善寺温泉"),
        ],
    },
    {
        "slug": "fujisan-hongu",
        "name": "富士山本宮浅間大社",
        "area_label": "富士山エリア",
        "location": "静岡県富士宮市",
        "tag": "神社・パワースポット",
        "desc": "全国に約1,300社ある浅間神社の総本社。世界文化遺産「富士山」の構成資産。徳川家康が造営した本殿は国の重要文化財。湧玉池は国の特別天然記念物で、富士山の雪解け水が湧き出す。",
        "videos": [
            {"id": "MehSQqzpri0", "title": "【公式4K】富士山本宮浅間大社 富士宮PV Long.ver"},
            {"id": "hRFin-p9cQY", "title": "【公式360度VR 4K】富士山本宮浅間大社 富士宮"},
            {"id": "lg3-arpihcQ", "title": "静岡の旅・御朱印 富士山本宮浅間大社と富士宮やきそば"},
            {"id": "eTF7BaGQ5qc", "title": "世界遺産登録10周年・富士山本宮浅間大社【TBSニュース】"},
        ],
        "shorts": [
            {"id": "MehSQqzpri0", "title": "富士山本宮浅間大社 4K映像"},
            {"id": "hRFin-p9cQY", "title": "浅間大社 360度VR"},
        ],
        "access": "JR富士宮駅から徒歩約10分",
        "hours": "境内自由（祈祷受付 8:30〜16:00）",
        "holiday": "なし",
        "parking": "なし（周辺有料駐車場利用）",
        "feature": "世界遺産・富士登山起点・湧玉池・富士宮やきそば",
        "lat": 35.363, "lng": 138.539,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN007000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("shiraito-falls", "静岡県 富士宮市", "白糸の滝"),
            ("asagiri-kogen", "静岡県 富士宮市", "朝霧高原"),
            ("tanuki-lake", "静岡県 富士宮市", "田貫湖"),
        ],
    },
    {
        "slug": "fumotoppara",
        "name": "ふもとっぱら",
        "area_label": "富士山エリア",
        "location": "静岡県富士宮市",
        "tag": "キャンプ・富士山絶景",
        "desc": "富士山を間近に望む日本最大級のキャンプ場。約30万坪の広大な敷地に広がる解放感と、圧倒的な富士山ビューが人気の聖地。早朝の富士山とモルゲンロートは一生の思い出になる。",
        "videos": [
            {"id": "j2SLryXXhAY", "title": "奇跡が起きた感動のふもとっぱらキャンプ（富士山絶景）"},
            {"id": "U90A0xObk2I", "title": "2年ぶり聖地！ふもとっぱらはやっぱり日本一のキャンプ場"},
            {"id": "9Re7CcTrlZs", "title": "ヒロシキャンプ IN ふもとっぱら"},
            {"id": "3ADKCeCfqDQ", "title": "【女ソロキャンプ】日本一有名なキャンプ場「ふもとっぱら」"},
        ],
        "shorts": [
            {"id": "xKTpbgirfZI", "title": "【マイナス12度】ふもとっぱら極寒冬キャンプ"},
            {"id": "j2SLryXXhAY", "title": "ふもとっぱら 感動の富士山"},
        ],
        "access": "新東名新富士ICから車約40分 / JR富士宮駅から車約30分",
        "hours": "チェックイン 13:00〜 / チェックアウト 〜11:00",
        "holiday": "不定休（公式サイト確認推奨）",
        "parking": "あり（サイト内駐車可）",
        "feature": "富士山絶景・広大なフリーサイト・星空・モルゲンロート",
        "lat": 35.378, "lng": 138.555,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN007000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("asagiri-kogen", "静岡県 富士宮市", "朝霧高原"),
            ("tanuki-lake", "静岡県 富士宮市", "田貫湖"),
            ("shiraito-falls", "静岡県 富士宮市", "白糸の滝"),
        ],
    },
    {
        "slug": "genbegawa",
        "name": "源兵衛川",
        "area_label": "三島エリア",
        "location": "静岡県三島市",
        "tag": "湧水・街中散歩",
        "desc": "富士山の雪解け水が湧き出す、市街地を流れる清流。水上に設けられた飛び石や木道を歩きながら涼める「水の都三島」を代表するスポット。ホタルが飛び交う初夏も人気。",
        "videos": [
            {"id": "VDeA2w3b6Eo", "title": "三島観光おすすめ 源兵衛川 街中の清流を歩いたら信じられないほど楽しかった"},
            {"id": "ocK0ns9IZCo", "title": "【水の都三島を歩く】みしま散歩〜源兵衛川〜"},
            {"id": "95LaPam9Y-I", "title": "富士山のめぐみ 三島湧水 源兵衛川"},
            {"id": "SaaS1b8zSOI", "title": "三島 源兵衛川 せせらぎ散歩 4K動画"},
        ],
        "shorts": [
            {"id": "ZkS3u0QVLv4", "title": "静岡県 三島市 源兵衛川"},
            {"id": "L8D82B0le1c", "title": "【三島市公式】みしま時間〜源兵衛川"},
        ],
        "access": "JR三島駅から徒歩約10分",
        "hours": "散策自由",
        "holiday": "なし",
        "parking": "周辺有料駐車場利用",
        "feature": "水上遊歩道・湧水・ホタル・楽寿園隣接",
        "lat": 35.115, "lng": 138.911,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220505/",
        "related": [
            ("mishima-taisha", "静岡県 三島市", "三嶋大社"),
            ("rakujuen", "静岡県 三島市", "楽寿園"),
            ("kakitagawa", "静岡県 清水町", "柿田川公園"),
        ],
    },
    {
        "slug": "irozaki",
        "name": "石廊崎",
        "area_label": "伊豆エリア",
        "location": "静岡県南伊豆町",
        "tag": "岬・絶景・クルーズ",
        "desc": "伊豆半島最南端の岬。100mを超える断崖絶壁が続き、海の透明度は抜群。白亜の灯台とダイナミックな景色が人気。遊覧船クルーズで断崖をめぐれる。晴れた日は伊豆諸島が見える。",
        "videos": [
            {"id": "ahMfvr0VWTA", "title": "絶景だらけの南伊豆 石廊崎オーシャンパーク・クルージングと夕陽"},
            {"id": "HSVlDJwE5ow", "title": "南伊豆 石廊崎オーシャンパーク IROZAKI CAPE TOUR"},
            {"id": "TyjCim2ZPWI", "title": "石廊崎（南伊豆町）絶景岬"},
            {"id": "SHiCY1mKG3s", "title": "西伊豆の有名スポット — 伊豆最南端の絶景"},
        ],
        "shorts": [
            {"id": "ahMfvr0VWTA", "title": "石廊崎 夕陽クルーズ"},
            {"id": "HSVlDJwE5ow", "title": "石廊崎 岬めぐり遊覧船"},
        ],
        "access": "JR下田駅から東海バス約30分 / 沼津ICから車約2時間",
        "hours": "遊覧船 9:00〜15:30（季節変動）",
        "holiday": "荒天時運休",
        "parking": "あり（有料）",
        "feature": "断崖絶壁・灯台・遊覧船クルーズ・夕日スポット",
        "lat": 34.611, "lng": 138.842,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN015000/",
        "tabelog": "https://tabelog.com/shizuoka/A2204/A220406/",
        "related": [
            ("dogashima", "静岡県 西伊豆町", "堂ヶ島"),
            ("omuroyama", "静岡県 伊東市", "大室山"),
            ("joren-falls", "静岡県 伊豆市", "浄蓮の滝"),
        ],
    },
    {
        "slug": "izu-panorama",
        "name": "伊豆パノラマパーク",
        "area_label": "伊豆エリア",
        "location": "静岡県伊豆の国市",
        "tag": "絶景・ロープウェイ",
        "desc": "標高452mの葛城山頂にある絶景リゾート「碧テラス」。ロープウェイで約7分、富士山と駿河湾を一望できる。水盤に映る逆さ富士の撮影スポットとして人気。足湯・カフェも充実。",
        "videos": [
            {"id": "ggAIUMJlEgM", "title": "2023 絶景 伊豆パノラマパーク Izu Panorama Park"},
            {"id": "pJ427IT6HDg", "title": "【伊豆旅行】碧テラス 伊豆パノラマパーク ロープウェイで行く絶景カフェ"},
            {"id": "do3QrRAxy4w", "title": "【犬連れ伊豆旅行】伊豆パノラマパーク 絶叫ロープウェイと絶景碧テラス"},
            {"id": "dJ5QNZagH7c", "title": "おしゃれな絶景 伊豆パノラマパーク 最高の癒しスポット"},
        ],
        "shorts": [
            {"id": "4JGrtoKPpg0", "title": "伊豆パノラマパーク リニューアルオープン 360度パノラマ絶景"},
            {"id": "J8Cptvu-2Dg", "title": "新たな絶景空間「アクアリング」お披露目"},
        ],
        "access": "伊豆長岡駅から徒歩約15分 / 沼津ICから車約30分",
        "hours": "9:00〜17:00（繁忙期延長）",
        "holiday": "不定休（公式サイト確認）",
        "parking": "あり（無料）",
        "feature": "ロープウェイ・碧テラス水盤・富士山絶景・足湯・カフェ",
        "lat": 35.007, "lng": 138.921,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("mishima-skywalk", "静岡県 三島市", "三島スカイウォーク"),
            ("nirayama-hansharyo", "静岡県 伊豆の国市", "韮山反射炉"),
            ("shuzenji", "静岡県 伊豆市", "修善寺温泉"),
        ],
    },
    {
        "slug": "jogasaki",
        "name": "城ヶ崎海岸・門脇つり橋",
        "area_label": "伊豆エリア",
        "location": "静岡県伊東市",
        "tag": "絶景・吊り橋",
        "desc": "約4,000年前の大室山噴火でできた溶岩海岸。高さ23mの門脇つり橋から見下ろす断崖絶壁と青い海は圧巻。9kmに及ぶ磯の遊歩道も整備されており、自然探索が楽しめる。",
        "videos": [
            {"id": "0y4IIoI2unI", "title": "城ケ崎国立公園 門脇吊り橋 伊豆 伊東市 城ケ崎海岸"},
            {"id": "eulEeOhj_ck", "title": "【伊豆リフト・ロープウェイ】大室山の全貌わかります"},
            {"id": "Q01y85gThoY", "title": "大室山 静岡県伊東市 360度の大絶景をリフトで 旅行VLOG"},
            {"id": "ahMfvr0VWTA", "title": "絶景南伊豆 クルージングと夕陽 伊豆の海を体感"},
        ],
        "shorts": [
            {"id": "0y4IIoI2unI", "title": "城ヶ崎海岸 門脇つり橋"},
            {"id": "18lHtFHCC-E", "title": "大室山 4K リフト絶景"},
        ],
        "access": "伊東駅からバス約25分 / 沼津ICから車約60分",
        "hours": "散策自由",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "吊り橋・溶岩海岸・遊歩道・灯台・磯釣り",
        "lat": 34.888, "lng": 139.119,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN014000/",
        "tabelog": "https://tabelog.com/shizuoka/A2204/A220403/",
        "related": [
            ("omuroyama", "静岡県 伊東市", "大室山"),
            ("izu-panorama", "静岡県 伊豆の国市", "伊豆パノラマパーク"),
            ("joren-falls", "静岡県 伊豆市", "浄蓮の滝"),
        ],
    },
    {
        "slug": "joren-falls",
        "name": "浄蓮の滝",
        "area_label": "伊豆エリア",
        "location": "静岡県伊豆市",
        "tag": "滝・わさび田",
        "desc": "日本の滝100選にも選ばれた伊豆の名瀑。高さ25m・幅7mの滝を囲むように広がるわさび田が独特の景観を作る。演歌「天城越え」の舞台としても有名。周辺にはわさびそば店が並ぶ。",
        "videos": [
            {"id": "KYFjk8cuOtY", "title": "【伊豆の旅】浄蓮の滝 日本の滝100選"},
            {"id": "LA1EHmILUrY", "title": "静岡県観光 日本の滝100選 伊豆 浄蓮の滝 4K"},
            {"id": "VaHv-_NkQl4", "title": "【名瀑】天城越えから浄蓮の滝！釣った魚をその場で食べる"},
            {"id": "aj36-a5QMig", "title": "アラカン夫婦の伊豆旅 浄蓮の滝と天城越えと河津七滝"},
        ],
        "shorts": [
            {"id": "KYFjk8cuOtY", "title": "浄蓮の滝 伊豆の名瀑"},
            {"id": "LA1EHmILUrY", "title": "浄蓮の滝 4K映像"},
        ],
        "access": "伊豆箱根鉄道修善寺駅から車約20分 / 天城越え国道沿い",
        "hours": "見学自由（売店 8:30〜17:00）",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "日本の滝100選・わさび田・わさびそば・天城越え",
        "lat": 34.879, "lng": 138.990,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN017000/",
        "tabelog": "https://tabelog.com/shizuoka/A2204/A220404/",
        "related": [
            ("shuzenji", "静岡県 伊豆市", "修善寺温泉"),
            ("dogashima", "静岡県 西伊豆町", "堂ヶ島"),
            ("omuroyama", "静岡県 伊東市", "大室山"),
        ],
    },
    {
        "slug": "kakitagawa",
        "name": "柿田川公園",
        "area_label": "三島エリア",
        "location": "静岡県清水町",
        "tag": "湧水・自然公園",
        "desc": "日本最短の一級河川（全長約1.2km）として知られる湧水河川。富士山の雪解け水が1日約100万トン湧き出す日本一の湧水量を誇る。湧き間を間近で見られる展望台が人気。",
        "videos": [
            {"id": "gqCDOitTIvU", "title": "柿田川公園 湧水群 名水百選 富士山の雪解け水が湧き出る公園"},
            {"id": "VDeA2w3b6Eo", "title": "源兵衛川と合わせて楽しむ 三島の湧水散歩"},
            {"id": "e2Xu-NM9fus", "title": "【三島観光】水の都 三島駅周辺を歩く 楽寿園 源兵衛川 柿田川公園"},
            {"id": "ocK0ns9IZCo", "title": "みしま散歩〜水の都三島の湧水をたどる旅〜"},
        ],
        "shorts": [
            {"id": "gqCDOitTIvU", "title": "柿田川 湧き間から湧き出る富士山の雪解け水"},
            {"id": "95LaPam9Y-I", "title": "三島湧水 清流の原風景"},
        ],
        "access": "JR三島駅から車約10分 / 東名沼津ICから車約15分",
        "hours": "散策自由（展望台 9:00〜17:00）",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "名水百選・湧き間・一級河川・日本最短の川",
        "lat": 35.101, "lng": 138.912,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220505/",
        "related": [
            ("genbegawa", "静岡県 三島市", "源兵衛川"),
            ("mishima-taisha", "静岡県 三島市", "三嶋大社"),
            ("rakujuen", "静岡県 三島市", "楽寿園"),
        ],
    },
    {
        "slug": "kanukiyama",
        "name": "香貫山",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市",
        "tag": "登山・夜景",
        "desc": "沼津市街地から気軽に登れる標高193mの低山。山頂展望台からは富士山・駿河湾・伊豆半島を一望できる。「日本夜景100山」にも選定されており、夕暮れ〜夜の眺めも絶品。",
        "videos": [
            {"id": "c3IC6I_Ary4", "title": "香貫山ハイキング：黒瀬登り口｜沼津アルプス 2025年"},
            {"id": "uDKd1Jguwc4", "title": "香貫山 山頂から見た沼津 Numazu seen from Mt. Kanuki"},
            {"id": "RcSTYM6PMAI", "title": "沼津旅行ひとり旅は絶景・グルメ最高すぎた！おすすめ絶景スポット"},
            {"id": "ko_WA-D-we4", "title": "静岡県【沼津観光VLOG】日帰りで手軽に海鮮グルメ・絶景満喫旅"},
        ],
        "shorts": [
            {"id": "c3IC6I_Ary4", "title": "香貫山 ハイキング"},
            {"id": "uDKd1Jguwc4", "title": "香貫山 山頂からの沼津"},
        ],
        "access": "JR沼津駅から徒歩約20分（登山口まで）/ 車10分",
        "hours": "散策自由",
        "holiday": "なし",
        "parking": "あり（香陵台駐車場）",
        "feature": "日本夜景100山・富士山展望・沼津アルプス・体力不要",
        "lat": 35.081, "lng": 138.875,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("osezaki", "静岡県 沼津市", "大瀬崎"),
            ("senbonmatsubara", "静岡県 沼津市", "千本松原"),
        ],
    },
    {
        "slug": "lovelinevision",
        "name": "ラブライブ！聖地（内浦）",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市 内浦",
        "tag": "アニメ聖地・絶景",
        "desc": "アニメ「ラブライブ！サンシャイン!!」の舞台・沼津市内浦。作中の学校モデルや浦の星女学院、豊川家（たこ焼き屋）などのロケ地が点在。ファンが全国から訪れる聖地巡礼スポット。",
        "videos": [
            {"id": "0Vjufc6rhH8", "title": "沼津内浦 ラブライブサンシャインの聖地巡礼 visit Lovelive! Sunshine!!"},
            {"id": "qgBkNbN6hSA", "title": "【聖地巡礼】ラブライブ！サンシャイン!! 劇場版 沼津内浦【4K】"},
            {"id": "ko_WA-D-we4", "title": "静岡県【沼津観光VLOG】日帰りで手軽に海鮮グルメ・絶景満喫旅"},
            {"id": "RcSTYM6PMAI", "title": "沼津旅行ひとり旅は絶景・グルメ最高すぎた！"},
        ],
        "shorts": [
            {"id": "0Vjufc6rhH8", "title": "沼津内浦 聖地巡礼"},
            {"id": "qgBkNbN6hSA", "title": "ラブライブ聖地 沼津内浦 4K"},
        ],
        "access": "JR沼津駅から東海バス「内浦三津」行き約40分",
        "hours": "見学自由",
        "holiday": "なし",
        "parking": "内浦周辺の各駐車場",
        "feature": "アニメ聖地・内浦湾・長浜城跡・いけすや（海鮮）",
        "lat": 35.005, "lng": 138.906,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("osezaki", "静岡県 沼津市", "大瀬崎"),
            ("numazu-byuo", "静岡県 沼津市", "展望水門「びゅうお」"),
        ],
    },
    {
        "slug": "mishima-skywalk",
        "name": "三島スカイウォーク",
        "area_label": "三島エリア",
        "location": "静岡県三島市",
        "tag": "吊り橋・絶景",
        "desc": "全長400mの日本一長い歩行者専用吊り橋。橋の上から望む富士山と駿河湾の絶景は圧巻。アドベンチャー施設・ジップライン・ソラテラスも併設。デートスポットとしても人気が高い。",
        "videos": [
            {"id": "mJazvow4IV4", "title": "三島スカイウォーク 施設紹介"},
            {"id": "AFJu-zJwGc0", "title": "【三島スカイウォーク】感動3選！日本一長い歩行者専用吊り橋"},
            {"id": "WDTJl9Uo6x8", "title": "GWにどう？大人も子供も喜ぶ 富士山が見える絶景の橋"},
            {"id": "JgBMOS9Jx74", "title": "三島スカイウォーク 日本一の吊り橋 旅行VLOG"},
        ],
        "shorts": [
            {"id": "A2kzGXZgMW0", "title": "三島スカイウォーク デートスポット 吊り橋効果"},
            {"id": "pG_3qiz_Cig", "title": "大人気観光地 三島スカイウォーク"},
        ],
        "access": "JR三島駅からバス約25分 / 新東名長泉沼津ICから車約10分",
        "hours": "9:00〜17:00（土日祝〜18:00）",
        "holiday": "不定休（公式サイト確認）",
        "parking": "あり（無料）",
        "feature": "日本一長い歩行者吊り橋・富士山絶景・ジップライン・ソラテラス",
        "lat": 35.149, "lng": 138.935,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220505/",
        "related": [
            ("mishima-taisha", "静岡県 三島市", "三嶋大社"),
            ("izu-panorama", "静岡県 伊豆の国市", "伊豆パノラマパーク"),
            ("kakitagawa", "静岡県 清水町", "柿田川公園"),
        ],
    },
    {
        "slug": "mishima-taisha",
        "name": "三嶋大社",
        "area_label": "三島エリア",
        "location": "静岡県三島市",
        "tag": "神社・パワースポット",
        "desc": "伊豆の総鎮守として源頼朝も崇敬した格式高い神社。境内には富士山の湧水が流れ、樹齢1200年を超える金木犀の古木が象徴。縁結び・商売繁昌のご利益でも有名。秋の例大祭は盛大。",
        "videos": [
            {"id": "owcvaUsdOno", "title": "三島大社へお参り 三嶋大社"},
            {"id": "6C1pED0c_uM", "title": "静岡県「三島駅」周辺を散策！美しすぎた水のエリアと三嶋大社"},
            {"id": "M0vV9ZdDi34", "title": "vlog【静岡/三島市】三島スカイウォーク＆三嶋大社＆うなぎ"},
            {"id": "e2Xu-NM9fus", "title": "【三島観光】水の都 三島 楽寿園 源兵衛川 三嶋大社"},
        ],
        "shorts": [
            {"id": "owcvaUsdOno", "title": "三嶋大社 参拝"},
            {"id": "6C1pED0c_uM", "title": "三島 水のある街散策"},
        ],
        "access": "JR三島駅から徒歩約15分",
        "hours": "境内自由（ご祈祷 9:00〜16:00）",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "伊豆の総鎮守・縁結び・金木犀古木・うなぎ街道",
        "lat": 35.119, "lng": 138.912,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220505/",
        "related": [
            ("genbegawa", "静岡県 三島市", "源兵衛川"),
            ("mishima-skywalk", "静岡県 三島市", "三島スカイウォーク"),
            ("rakujuen", "静岡県 三島市", "楽寿園"),
        ],
    },
    {
        "slug": "nirayama-hansharyo",
        "name": "韮山反射炉",
        "area_label": "伊豆エリア",
        "location": "静岡県伊豆の国市",
        "tag": "世界遺産・歴史",
        "desc": "2015年に世界遺産に登録された「明治日本の産業革命遺産」の構成資産。幕末に鉄製大砲を鋳造するために建設された国内唯一現存の実稼働した反射炉。高さ約15.7mの4基が現存。",
        "videos": [
            {"id": "vR7M3KG9M4E", "title": "世界遺産【韮山反射炉編】4K 空撮"},
            {"id": "Mkc8Qo3u-Oc", "title": "韮山反射炉が世界遺産登録へ 喜びに沸く地元"},
            {"id": "M0vV9ZdDi34", "title": "静岡/三島 日帰りドライブ 三嶋大社・伊豆観光"},
            {"id": "ggAIUMJlEgM", "title": "伊豆パノラマパーク — 伊豆の国市の絶景スポット"},
        ],
        "shorts": [
            {"id": "vR7M3KG9M4E", "title": "韮山反射炉 4K空撮"},
            {"id": "Mkc8Qo3u-Oc", "title": "世界遺産 韮山反射炉"},
        ],
        "access": "伊豆箱根鉄道韮山駅から車約5分 / 沼津ICから車約30分",
        "hours": "9:00〜17:00（最終入場16:30）",
        "holiday": "第3水曜（祝日の場合翌日）",
        "parking": "あり（無料）",
        "feature": "世界遺産・幕末歴史・4K空撮映え・ガイドツアー",
        "lat": 35.043, "lng": 138.929,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("izu-panorama", "静岡県 伊豆の国市", "伊豆パノラマパーク"),
            ("mishima-taisha", "静岡県 三島市", "三嶋大社"),
            ("mishima-skywalk", "静岡県 三島市", "三島スカイウォーク"),
        ],
    },
    {
        "slug": "numazu-goyotei",
        "name": "沼津御用邸記念公園",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市",
        "tag": "歴史・庭園",
        "desc": "明治26年に建設された皇族の別邸跡地を公園化。国の名勝に指定された松林の庭園と歴史的建築物が美しい。敷地内のカフェでは駿河湾を眺めながら休憩でき、ダルマ夕日の名所でもある。",
        "videos": [
            {"id": "PIVj8t8zbjA", "title": "【歴史民俗資料館】沼津御用邸記念公園内の案内"},
            {"id": "RcSTYM6PMAI", "title": "沼津旅行ひとり旅は絶景・グルメ最高すぎた！おすすめ観光スポット"},
            {"id": "ko_WA-D-we4", "title": "静岡県【沼津観光VLOG】日帰りで手軽に海鮮グルメ・絶景満喫旅"},
            {"id": "vszInLMcLXo", "title": "千本浜公園から見る富士山 沼津 4K 2025"},
        ],
        "shorts": [
            {"id": "PIVj8t8zbjA", "title": "沼津御用邸記念公園 施設案内"},
            {"id": "RcSTYM6PMAI", "title": "沼津 絶景スポット巡り"},
        ],
        "access": "JR沼津駅から車約10分・バス15分",
        "hours": "9:00〜16:30（最終入場16:00）",
        "holiday": "水曜（祝日の場合翌日）",
        "parking": "あり（有料）",
        "feature": "国の名勝・皇族別邸・松林庭園・ダルマ夕日・カフェ",
        "lat": 35.099, "lng": 138.864,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("senbonmatsubara", "静岡県 沼津市", "千本松原"),
            ("numazu-byuo", "静岡県 沼津市", "展望水門「びゅうお」"),
        ],
    },
    {
        "slug": "numazu-ino",
        "name": "沼津魚市場INO",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市",
        "tag": "市場・グルメ",
        "desc": "沼津港に隣接する複合施設。2階の見学通路から早朝のせり（5:45〜）を無料で見学できる。駿河湾で水揚げされた新鮮な魚介類を格安で楽しめる食堂も人気。びゅうおと合わせて観光できる。",
        "videos": [
            {"id": "ScIsMJ0HC8M", "title": "沼津港と三島周辺を散策！人気の観光スポットとグルメ旅"},
            {"id": "lEvfMSNVJNY", "title": "沼津 日帰りで人気グルメも観光も！1日で大満喫コース"},
            {"id": "ko_WA-D-we4", "title": "静岡県【沼津観光VLOG】日帰りで手軽に海鮮グルメ・絶景満喫旅"},
            {"id": "RcSTYM6PMAI", "title": "沼津旅行ひとり旅は絶景・グルメ最高すぎた！"},
        ],
        "shorts": [
            {"id": "2ZSjXABHGg0", "title": "沼津港の海鮮グルメ5選"},
            {"id": "emQVVLn1S_I", "title": "沼津港で楽しむ海鮮ランチ"},
        ],
        "access": "JR沼津駅から徒歩約20分・バス10分",
        "hours": "せり見学 5:45〜 / 食堂 8:00〜15:00（店舗により異なる）",
        "holiday": "水曜・日曜（せり見学）",
        "parking": "あり（有料）",
        "feature": "せり見学・新鮮海鮮・市場食堂・びゅうお隣接",
        "lat": 35.097, "lng": 138.864,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("numazu-byuo", "静岡県 沼津市", "展望水門「びゅうお」"),
            ("numazu-port-dining", "静岡県 沼津市", "沼津港飲食店街"),
        ],
    },
    {
        "slug": "numazu-port-dining",
        "name": "沼津港飲食店街・港八十三番地",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市",
        "tag": "グルメ・海鮮",
        "desc": "沼津港周辺に広がるグルメゾーン。深海魚・海鮮丼・アジフライ・干物など駿河湾の幸を堪能できる飲食店が集結。「港八十三番地」は10店舗以上が集まる複合施設で、深海水族館も隣接。",
        "videos": [
            {"id": "lEvfMSNVJNY", "title": "沼津 日帰りで人気グルメも観光も！1日で大満喫コース"},
            {"id": "2ZSjXABHGg0", "title": "【絶対に失敗しない】沼津港の海鮮グルメ5選！お出かけ前必見"},
            {"id": "ScIsMJ0HC8M", "title": "沼津港と三島周辺を散策！人気の観光スポットとグルメ旅"},
            {"id": "ko_WA-D-we4", "title": "静岡県【沼津観光VLOG】日帰りで手軽に海鮮グルメ・絶景満喫旅"},
        ],
        "shorts": [
            {"id": "rH-0k7WjJyw", "title": "沼津港でグルメ散策"},
            {"id": "emQVVLn1S_I", "title": "沼津港で楽しむ海鮮ランチ"},
        ],
        "access": "JR沼津駅から徒歩約20分・バス10分",
        "hours": "店舗により異なる（多くは10:00〜21:00頃）",
        "holiday": "店舗により異なる",
        "parking": "あり（有料）",
        "feature": "深海魚・海鮮丼・アジフライ・干物・深海水族館隣接",
        "lat": 35.097, "lng": 138.861,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("numazu-aquarium", "静岡県 沼津市", "沼津港深海水族館"),
            ("numazu-ino", "静岡県 沼津市", "沼津魚市場INO"),
        ],
    },
    {
        "slug": "obuchinanbasaba",
        "name": "大淵笹場",
        "area_label": "富士山エリア",
        "location": "静岡県富士市",
        "tag": "茶畑・富士山絶景",
        "desc": "富士山と茶畑が同時に見られる絶景撮影スポット。電線・防霜ファンを排除した景観保全により、遮るものなく富士山と緑の茶畑を撮影できる。早朝の霧の朝は幻想的な光景に。",
        "videos": [
            {"id": "al4M2UUoxnQ", "title": "茶畑と富士山撮影スポット4選（大渕笹場など）"},
            {"id": "o1XAavHIps0", "title": "富士山と茶畑の絶景 おおぶちお茶まつり2024"},
            {"id": "IJ3RhJwr7M8", "title": "【公式4K】白糸ノ滝 富士宮PV — 静岡富士山エリアの絶景"},
            {"id": "MehSQqzpri0", "title": "【公式4K】富士山本宮浅間大社 富士宮PV"},
        ],
        "shorts": [
            {"id": "al4M2UUoxnQ", "title": "大淵笹場 富士山×茶畑 撮影スポット"},
            {"id": "o1XAavHIps0", "title": "大淵笹場 茶畑と富士山"},
        ],
        "access": "新東名新富士IC・東名富士ICから車約10分",
        "hours": "見学自由",
        "holiday": "なし",
        "parking": "あり（無料）",
        "feature": "茶畑×富士山絶景・お茶体験・インスタ映え・無料",
        "lat": 35.173, "lng": 138.707,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN007000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220502/",
        "related": [
            ("fujisan-hongu", "静岡県 富士宮市", "富士山本宮浅間大社"),
            ("shiraito-falls", "静岡県 富士宮市", "白糸の滝"),
            ("asagiri-kogen", "静岡県 富士宮市", "朝霧高原"),
        ],
    },
    {
        "slug": "omuroyama",
        "name": "大室山",
        "area_label": "伊豆エリア",
        "location": "静岡県伊東市",
        "tag": "火山・リフト・絶景",
        "desc": "約4,000年前の噴火でできた標高580mのスコリア丘。リフトで山頂まで約6分で登れ、すり鉢状の火口を一周できる「お鉢めぐり」が人気。天気が良ければ富士山・伊豆七島まで見渡せる。",
        "videos": [
            {"id": "Q01y85gThoY", "title": "大室山/静岡県伊東市 360度の大絶景をリフトで手軽に楽しめる火山"},
            {"id": "18lHtFHCC-E", "title": "リフトでGO！歩いて登れない山【大室山 580m】伊豆半島ジオパーク 4K"},
            {"id": "eulEeOhj_ck", "title": "【伊豆リフト・ロープウェイ】これを観れば大室山の全貌わかります！"},
            {"id": "5KhjJ7PLDw0", "title": "大室山登山リフト4K PV"},
        ],
        "shorts": [
            {"id": "uwJi-QN4QLc", "title": "【伊東市】大室山登山リフト"},
            {"id": "OUmsJMBoV90", "title": "大室山 お鉢めぐり Mt.Omuro Climbing"},
        ],
        "access": "伊東駅からバス約30分 / 新東名長泉沼津ICから車約60分",
        "hours": "リフト 9:00〜17:15（季節変動）",
        "holiday": "荒天時リフト運休",
        "parking": "あり（無料）",
        "feature": "火山・リフト・お鉢めぐり・富士山絶景・アーチェリー",
        "lat": 34.898, "lng": 139.094,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN014000/",
        "tabelog": "https://tabelog.com/shizuoka/A2204/A220403/",
        "related": [
            ("jogasaki", "静岡県 伊東市", "城ヶ崎海岸"),
            ("izu-panorama", "静岡県 伊豆の国市", "伊豆パノラマパーク"),
            ("joren-falls", "静岡県 伊豆市", "浄蓮の滝"),
        ],
    },
    {
        "slug": "osezaki",
        "name": "大瀬崎",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市",
        "tag": "ダイビング・パワースポット",
        "desc": "ダイビングの聖地として全国から愛好家が集まる沼津市西浦の岬。「神池」は海から15mしか離れていないのに淡水という不思議な池。ビャクシンの古木が生い茂る「大瀬神社」も見どころ。",
        "videos": [
            {"id": "NlahQGN0hMs", "title": "沼津の大瀬崎にある不思議な神池を見に行く"},
            {"id": "rBZYtsiKL-U", "title": "ちょーキレイな絶景！大瀬崎でダイビングしてきましたよぉ！"},
            {"id": "YZ00iG85JM0", "title": "【大瀬崎のダイビング】知らないと損をする本当の魅力！"},
            {"id": "8GsreE8ts3M", "title": "4K60fps 西伊豆・大瀬崎ダイビング（湾内・一本松）"},
        ],
        "shorts": [
            {"id": "NlahQGN0hMs", "title": "大瀬崎 神池 海から15mの淡水池"},
            {"id": "k6TfT3S6xic", "title": "大瀬崎 ビーチダイビング"},
        ],
        "access": "JR沼津駅からバス約60分「大瀬崎」下車 / 沼津ICから車約35分",
        "hours": "見学自由（神池 6:00〜17:00）",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "ダイビング聖地・神池・大瀬神社・ビャクシン古木・富士山ビュー",
        "lat": 35.040, "lng": 138.800,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("lovelinevision", "静岡県 沼津市", "ラブライブ！聖地"),
            ("kanukiyama", "静岡県 沼津市", "香貫山"),
        ],
    },
    {
        "slug": "rakujuen",
        "name": "楽寿園",
        "area_label": "三島エリア",
        "location": "静岡県三島市",
        "tag": "公園・動物・歴史",
        "desc": "三島駅南口すぐの三島市立公園。約1万年前の富士山溶岩流「三島溶岩流」の上に広がり、天然記念物・小浜池を有する庭園が美しい。レッサーパンダ・カピバラ・アルパカなど動物も人気。",
        "videos": [
            {"id": "e2Xu-NM9fus", "title": "【三島観光】水の都 三島駅周辺を歩く 楽寿園 源兵衛川 三嶋大社"},
            {"id": "6C1pED0c_uM", "title": "静岡県「三島駅」周辺散策！美しすぎた水のエリアと歴史スポット"},
            {"id": "VDeA2w3b6Eo", "title": "三島観光おすすめ 水の都 三島の湧水散歩"},
            {"id": "M0vV9ZdDi34", "title": "vlog【静岡/三島市】三島スカイウォーク＆三嶋大社＆うなぎ"},
        ],
        "shorts": [
            {"id": "e2Xu-NM9fus", "title": "楽寿園 三島市立公園"},
            {"id": "ocK0ns9IZCo", "title": "三島散歩 水の郷"},
        ],
        "access": "JR三島駅から徒歩1分",
        "hours": "9:00〜17:00（最終入場16:30）",
        "holiday": "月曜（祝日の場合翌日）・年末年始",
        "parking": "なし（周辺駐車場利用）",
        "feature": "溶岩流庭園・小浜池・レッサーパンダ・カピバラ・アルパカ",
        "lat": 35.120, "lng": 138.910,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN012000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220505/",
        "related": [
            ("genbegawa", "静岡県 三島市", "源兵衛川"),
            ("mishima-taisha", "静岡県 三島市", "三嶋大社"),
            ("kakitagawa", "静岡県 清水町", "柿田川公園"),
        ],
    },
    {
        "slug": "senbonmatsubara",
        "name": "千本松原・千本浜",
        "area_label": "沼津エリア",
        "location": "静岡県沼津市",
        "tag": "松林・海岸・富士山",
        "desc": "狩野川河口から続く約7kmの松林「千本松原」と、沼津市街地に最も近い千本浜海岸。日本の白砂青松100選にも選定。富士山と駿河湾を望む絶景は夕暮れが特に美しい。",
        "videos": [
            {"id": "vszInLMcLXo", "title": "千本浜公園から見る富士山 沼津市 4K 2025.2.27"},
            {"id": "RcSTYM6PMAI", "title": "沼津旅行ひとり旅は絶景・グルメ最高すぎた！おすすめ絶景スポット"},
            {"id": "ko_WA-D-we4", "title": "静岡県【沼津観光VLOG】日帰りで手軽に海鮮グルメ・絶景満喫旅"},
            {"id": "ScIsMJ0HC8M", "title": "沼津港と三島周辺を散策！人気の観光スポットとグルメ旅"},
        ],
        "shorts": [
            {"id": "vszInLMcLXo", "title": "千本浜から見る富士山"},
            {"id": "RcSTYM6PMAI", "title": "沼津 絶景スポット"},
        ],
        "access": "JR沼津駅からバス約10分「千本浜公園」下車",
        "hours": "散策自由",
        "holiday": "なし",
        "parking": "あり（無料）",
        "feature": "白砂青松100選・富士山絶景・夕日・海水浴・サーフィン",
        "lat": 35.084, "lng": 138.840,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN011000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220501/",
        "related": [
            ("numazu-port", "静岡県 沼津市", "沼津港"),
            ("numazu-goyotei", "静岡県 沼津市", "沼津御用邸記念公園"),
            ("kanukiyama", "静岡県 沼津市", "香貫山"),
        ],
    },
    {
        "slug": "shiraito-falls",
        "name": "白糸の滝",
        "area_label": "富士山エリア",
        "location": "静岡県富士宮市",
        "tag": "滝・世界遺産",
        "desc": "富士山世界文化遺産の構成資産。高さ20m・幅150mにわたり数百本の細い滝が滴り落ちる光景が「白糸」の名の由来。隣接する「音止の滝」との対比も美しい。通年観光可能。",
        "videos": [
            {"id": "IJ3RhJwr7M8", "title": "【公式4K】白糸ノ滝 富士宮PV Long.ver"},
            {"id": "vqIj_HUZzNE", "title": "【公式360度VR 4K】白糸ノ滝 富士宮"},
            {"id": "36CYkJkF-GY", "title": "夏の白糸ノ滝 富士山世界遺産 静岡県富士宮市 4K 2022"},
            {"id": "MehSQqzpri0", "title": "富士山本宮浅間大社 富士宮PV — 近隣の世界遺産スポット"},
        ],
        "shorts": [
            {"id": "IJ3RhJwr7M8", "title": "白糸の滝 4K公式映像"},
            {"id": "vqIj_HUZzNE", "title": "白糸ノ滝 360度VR"},
        ],
        "access": "JR富士宮駅からバス約30分 / 新東名新富士ICから車約25分",
        "hours": "見学自由",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "富士山世界遺産・国の天然記念物・音止の滝・富士宮やきそば",
        "lat": 35.278, "lng": 138.565,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN007000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("fujisan-hongu", "静岡県 富士宮市", "富士山本宮浅間大社"),
            ("asagiri-kogen", "静岡県 富士宮市", "朝霧高原"),
            ("tanuki-lake", "静岡県 富士宮市", "田貫湖"),
        ],
    },
    {
        "slug": "tanuki-lake",
        "name": "田貫湖",
        "area_label": "富士山エリア",
        "location": "静岡県富士宮市",
        "tag": "湖・逆さ富士・キャンプ",
        "desc": "朝霧高原の中にある周囲約4kmの湖。水面に映る「逆さ富士」が有名で、4月20日・8月20日頃には「ダイヤモンド富士」も見られる。湖畔のキャンプ場は富士山ビューの絶好ロケーション。",
        "videos": [
            {"id": "9kvLzufr8fs", "title": "【公式4K】田貫湖 富士宮PV Long.ver"},
            {"id": "whMwfulu9GA", "title": "【静岡キャンプ場紹介】田貫湖キャンプ場を徹底解説 湖越しの富士山が絶景"},
            {"id": "m48-tmYm6Rc", "title": "【前編】富士山キャンプ in 田貫湖キャンプ場"},
            {"id": "DktMyljBd60", "title": "富士宮市朝霧高原 田貫湖 ダイヤモンド富士"},
        ],
        "shorts": [
            {"id": "t61Y_ULrDIg", "title": "田貫湖キャンプ場 富士山ビュー"},
            {"id": "9kvLzufr8fs", "title": "田貫湖 4K PV"},
        ],
        "access": "JR富士宮駅から車約25分 / 新東名新富士ICから車約40分",
        "hours": "見学自由（キャンプ場はチェックイン13:00〜）",
        "holiday": "なし",
        "parking": "あり（有料）",
        "feature": "逆さ富士・ダイヤモンド富士・キャンプ・ハイキング・野鳥",
        "lat": 35.316, "lng": 138.575,
        "jalan": "https://www.jalan.net/yado/area/pref22/areaN007000/",
        "tabelog": "https://tabelog.com/shizuoka/A2205/A220503/",
        "related": [
            ("asagiri-kogen", "静岡県 富士宮市", "朝霧高原"),
            ("shiraito-falls", "静岡県 富士宮市", "白糸の滝"),
            ("fumotoppara", "静岡県 富士宮市", "ふもとっぱら"),
        ],
    },
]


def generate_html(spot):
    name = spot["name"]
    location = spot["location"]
    tag = spot["tag"]
    desc = spot["desc"]
    videos = spot["videos"]
    shorts = spot["shorts"]
    access = spot["access"]
    hours = spot["hours"]
    holiday = spot["holiday"]
    parking = spot["parking"]
    feature = spot["feature"]
    lat = spot["lat"]
    lng = spot["lng"]
    jalan = spot["jalan"]
    tabelog = spot["tabelog"]
    related = spot["related"]

    yt_items = ""
    for v in videos:
        yt_items += f'        <div class="video-wrap">\n          <iframe src="https://www.youtube.com/embed/{v["id"]}" title="{v["title"]}" allowfullscreen loading="lazy"></iframe>\n          <div class="video-caption">{v["title"]}</div>\n        </div>\n'

    shorts_items = ""
    for s in shorts:
        shorts_items += f'        <div class="video-wrap-vertical">\n          <iframe src="https://www.youtube.com/embed/{s["id"]}" title="{s["title"]}" allowfullscreen loading="lazy"></iframe>\n        </div>\n'

    related_cards = ""
    for (rslug, rloc, rname) in related:
        related_cards += f'      <a href="../{rslug}/" class="spot-card"><div class="spot-card-body"><div class="spot-card-area">{rloc}</div><div class="spot-card-name">{rname}</div><div class="spot-card-cta" style="margin-top:8px;">動画を見る →</div></div></a>\n'

    map_embed = f"https://maps.google.com/maps?q={lat},{lng}&z=15&output=embed"

    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{name}｜SNS動画でリアルチェック — ドコリアル</title>
<meta name="description" content="{name}の{tag}をSNS動画でリアルにチェック。YouTube動画{len(videos)}本まとめ。{location}のリアルな雰囲気を行く前に確認できます。">
<link rel="stylesheet" href="../../css/style.css">
</head>
<body>

<header>
  <a href="../../" class="logo">ドコ<span>リアル</span></a>
  <nav>
    <a href="../../">トップ</a>
    <a href="../atami/">熱海</a>
    <a href="../shuzenji/">修善寺</a>
    <a href="../mishima/">三島</a>
  </nav>
</header>

<div class="spot-hero">
  <div class="spot-hero-inner">
    <div class="breadcrumb"><a href="../../">トップ</a> › {spot["area_label"]}</div>
    <h1>{name}</h1>
    <div class="spot-hero-meta">
      <span>📍 {location}</span>
      <span>🏷️ {tag}</span>
      <span>▶ YouTube {len(videos)}本 / Shorts {len(shorts)}本</span>
    </div>
  </div>
</div>

<div class="spot-content">

  <div class="ad-slot">【広告】Google AdSense</div>

  <p class="reveal" style="margin-bottom:32px;color:#555;line-height:1.9;">
    {desc}
  </p>

  <div class="video-section reveal">
    <div class="video-section-title">📱 SNS動画でリアルチェック</div>

    <div class="platform-tabs">
      <button class="platform-tab active" data-platform="all">すべて</button>
      <button class="platform-tab" data-platform="youtube">▶ YouTube</button>
      <button class="platform-tab" data-platform="shorts">▶ Shorts</button>
    </div>

    <div class="platform-group" data-platform="youtube">
      <div class="platform-label yt">▶ YouTube</div>
      <div class="video-grid">
{yt_items}      </div>
    </div>

    <div class="platform-group" data-platform="shorts">
      <div class="platform-label shorts">▶ YouTube Shorts</div>
      <div class="video-grid-vertical">
{shorts_items}      </div>
    </div>

  </div>

  <div class="affiliate-section reveal">
    <h3>{name}周辺に泊まる・予約する</h3>
    <p>宿泊・観光の予約はこちらから</p>
    <div class="affiliate-btns">
      <a href="{jalan}" class="btn-affiliate btn-jalan" target="_blank" rel="noopener">🏨 じゃらんで宿を探す</a>
      <a href="{tabelog}" class="btn-affiliate btn-tabelog" target="_blank" rel="noopener">🍽 食べログで店を探す</a>
    </div>
  </div>

  <div class="info-section reveal">
    <div class="video-section-title">📌 基本情報</div>
    <table class="info-table">
      <tr><th>場所</th><td>{location}</td></tr>
      <tr><th>アクセス</th><td>{access}</td></tr>
      <tr><th>営業時間</th><td>{hours}</td></tr>
      <tr><th>定休日</th><td>{holiday}</td></tr>
      <tr><th>駐車場</th><td>{parking}</td></tr>
      <tr><th>見どころ</th><td>{feature}</td></tr>
    </table>
  </div>

  <div style="text-align:center;margin:32px 0;" class="reveal">
    <iframe src="{map_embed}"
      width="100%" height="300" style="border:0;border-radius:12px;" allowfullscreen loading="lazy"></iframe>
  </div>

  <div class="ad-slot">【広告】Google AdSense</div>

  <div class="reveal" style="margin-top:48px;">
    <div class="video-section-title">他のスポットも見る</div>
    <div class="spots-grid" style="grid-template-columns:repeat(auto-fill,minmax(220px,1fr));">
{related_cards}    </div>
  </div>

</div>

<footer>
  <div class="footer-logo">ドコ<span>リアル</span></div>
  <div class="footer-links"><a href="../../">トップ</a><a href="#">プライバシーポリシー</a></div>
  <p>掲載動画・投稿はYouTubeの公式埋め込み機能を使用しています。</p>
  <p style="margin-top:8px;">&copy; 2026 ドコリアル</p>
</footer>

<script src="../../js/main.js"></script>
</body>
</html>
"""


def main():
    created = []
    skipped = []

    for spot in SPOTS:
        slug = spot["slug"]
        dir_path = os.path.join(BASE, "spots", slug)
        file_path = os.path.join(dir_path, "index.html")

        os.makedirs(dir_path, exist_ok=True)

        if os.path.exists(file_path):
            skipped.append(slug)
            print(f"skip: {slug}")
            continue

        html = generate_html(spot)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html)
        created.append(slug)
        print(f"created: {slug} — {spot['name']}")

    print(f"\n完了: {len(created)}件作成 / {len(skipped)}件スキップ")


if __name__ == "__main__":
    main()
