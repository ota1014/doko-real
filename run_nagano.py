#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""長野エリア生成。"""
from add_region import run
from sync_nav import menu_items

CFG = {
    "region_slug": "nagano", "region_label": "長野エリア", "region_short": "長野",
    "spots_oneline": "善光寺・松本城・上高地・スノーモンキー・軽井沢",
    "nav_spots": [("zenkoji", "善光寺"), ("matsumoto-castle", "松本城")],
    "area_nav_html": menu_items(),
}

SPOTS = [
    {"slug": "zenkoji", "name": "善光寺", "area_label": "長野エリア",
     "location": "長野県長野市", "tag": "寺・パワースポット・参道",
     "desc": "「一生に一度は善光寺参り」と謳われる、約1400年の歴史を誇る長野市のシンボル。特定の宗派に属さない無宗派の寺院で、年間約700万人が参拝に訪れます。国宝の本堂は壮大で、真っ暗な回廊を手探りで進む「お戒壇巡り」が人気。本堂へ続く仲見世通りでは、おやきや七味、信州蕎麦などの食べ歩きや土産探しも楽しめる、信州随一の観光地です。",
     "videos": [{"id": "eo-bQpwdBac", "title": "【長野観光】年間700万人が訪れるパワースポット「善光寺」観光ガイド"},
                {"id": "u1t-d6abDIg", "title": "【長野】善光寺を120％楽しむ観光プラン お朝事＆仲見世通り食べ歩き"},
                {"id": "ega95yzIvV8", "title": "【善光寺】絶対におすすめ長野観光【長野県】"},
                {"id": "B798Du2ki4A", "title": "善光寺だけではない長野駅周辺の見どころを発見するぶらり旅"}],
     "shorts": [{"id": "9ACTnYZjcBU", "title": "善光寺仲見世通り食べ歩きの旅"},
                {"id": "kLdTeYV3P4k", "title": "善光寺へ歩く 長野の街並み"}],
     "access": "JR長野駅からバス約15分「善光寺大門」下車徒歩約5分", "hours": "参拝自由（お戒壇巡り等は時間あり）",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "国宝本堂・お戒壇巡り・仲見世通り・おやき・七味・無宗派・パワースポット",
     "lat": 36.6614, "lng": 138.1872, "kw_jp": "長野", "kw_en": "Zenkoji Nagano", "kw_book": "Nagano"},

    {"slug": "matsumoto-castle", "name": "松本城", "area_label": "長野エリア",
     "location": "長野県松本市", "tag": "城・国宝・絶景",
     "desc": "現存する五重六階の天守としては日本最古とされる国宝の名城。漆黒の下見板張りから「烏城（からすじょう）」とも呼ばれ、白と黒のコントラストが美しい姿が水堀に映ります。背後に北アルプスの山々を望むロケーションも絶景。天守内部の急な階段を上って最上階からの眺めも楽しめます。城下町の縄手通りや中町通りでの食べ歩き・街歩きも人気です。",
     "videos": [{"id": "L9JWV15P6Zo", "title": "【日帰り長野・松本城】魅力たっぷり大人の一人旅 観光・グルメ・城巡り"},
                {"id": "hdVlCdibAVM", "title": "松本市街地を散策 松本城でお勧めの観光アイテムを体験！信州観光"},
                {"id": "-WW5mxCWOtw", "title": "【長野／松本】国宝・松本城の美しさに圧倒！北アルプスが美しすぎた"},
                {"id": "Ki0gQYTe1Kk", "title": "国宝 松本城 4K ULTRA HD"}],
     "shorts": [{"id": "IS2ffCP5XMc", "title": "松本城観光となわて通りグルメ食べ歩き"},
                {"id": "4oKX2RFcsXw", "title": "松本城〜車で長野観光"}],
     "access": "JR松本駅から徒歩約15分、またはバス約7分「松本城・市役所前」下車", "hours": "8:30〜17:00（時季変動）",
     "holiday": "年末ほか", "parking": "周辺有料駐車場",
     "feature": "国宝天守・烏城・水堀の映り込み・北アルプス・城下町・縄手通り",
     "lat": 36.2384, "lng": 137.9690, "kw_jp": "松本", "kw_en": "Matsumoto Castle", "kw_book": "Matsumoto Nagano"},

    {"slug": "kamikochi", "name": "上高地", "area_label": "長野エリア",
     "location": "長野県松本市", "tag": "山岳・絶景・自然",
     "desc": "標高約1,500m、北アルプスの懐に抱かれた日本屈指の山岳景勝地。清流・梓川にかかる「河童橋」から望む穂高連峰の絶景は圧巻で、特別名勝・特別天然記念物に指定されています。大正池や明神池など神秘的な水辺、手つかずの自然を満喫できる散策路が整備され、ハイキングに最適。マイカー規制があり、バス・タクシーでアクセスする、自然保護された別天地です。",
     "videos": [{"id": "hNcWZ0M_hbg", "title": "4K映像 絶景「新緑の上高地 河童橋周辺 梓川と穂高連峰」"},
                {"id": "A2xowWCD6M4", "title": "【上高地 観光】大正池〜河童橋〜明神池まで 夏の早朝ハイキング"},
                {"id": "udo6KL8krRQ", "title": "【上高地】何度でも行きたくなる場所！上高地の美しさを100％満喫"},
                {"id": "IKk11EZi6Cg", "title": "上高地 夏8月の絶景 大正池〜河童橋まで散策（初心者向けルート）"}],
     "shorts": [{"id": "HeH7DnrVshc", "title": "【絶景】this is上高地 河童橋"},
                {"id": "88DyEZfl_4U", "title": "夏の旅 in 信州 上高地散策"}],
     "access": "松本電鉄・新島々駅からバス／マイカー規制のため沢渡・平湯からバス・タクシー", "hours": "散策自由（開山期間4月中旬〜11月中旬）",
     "holiday": "冬季閉山", "parking": "沢渡・平湯に駐車場（マイカー規制）",
     "feature": "河童橋・穂高連峰・梓川・大正池・明神池・特別名勝・ハイキング",
     "lat": 36.2502, "lng": 137.6383, "kw_jp": "上高地 松本", "kw_en": "Kamikochi Nagano", "kw_book": "Kamikochi Nagano"},

    {"slug": "jigokudani-monkey", "name": "地獄谷野猿公苑（スノーモンキー）", "area_label": "長野エリア",
     "location": "長野県山ノ内町", "tag": "動物・絶景・温泉",
     "desc": "世界で唯一、温泉に入るニホンザル「スノーモンキー」が見られることで世界的に有名なスポット。雪深い渓谷の温泉につかり、気持ちよさそうに目を閉じる猿たちの姿は、海外メディアでも紹介され、年間多くの外国人観光客が訪れます。とくに雪の積もる冬がベストシーズン。駐車場から遊歩道を約30分歩いてたどり着く、自然のなかの野生猿の楽園です。",
     "videos": [{"id": "2pqNx8JPzTA", "title": "世界で唯一！温泉に入る長野のサルを見る雪山散歩 地獄谷野猿公苑 SNOW MONKEY"},
                {"id": "P9-4GTEMVmI", "title": "【4K】雪見風呂楽しむニホンザル「スノーモンキー」山ノ内町 地獄谷野猿公苑"},
                {"id": "qWjDDbQIJ-Q", "title": "【4K】地獄谷野猿公苑のスノーモンキー"},
                {"id": "-o87vUh6Uq4", "title": "【地獄谷野猿公苑】世界で唯一猿が温泉に入るスノーモンキーパーク"}],
     "shorts": [{"id": "GXN00a_ccQc", "title": "世界でここだけ。温泉に入る野生の猿"},
                {"id": "1BGPxjJgHdg", "title": "地獄谷野猿公苑 Snow monkey 4K"}],
     "access": "長野電鉄・湯田中駅からバス＋徒歩約30分の遊歩道", "hours": "9:00〜16:00頃（時季変動）",
     "holiday": "なし（悪天候時は変動）", "parking": "あり",
     "feature": "温泉に入る野生猿・スノーモンキー・冬の絶景・渓谷の遊歩道",
     "lat": 36.7330, "lng": 138.4622, "kw_jp": "湯田中 渋温泉", "kw_en": "Jigokudani Snow Monkey Nagano", "kw_book": "Yamanouchi Nagano"},

    {"slug": "karuizawa", "name": "軽井沢", "area_label": "長野エリア",
     "location": "長野県軽井沢町", "tag": "高原リゾート・散策・グルメ",
     "desc": "明治時代から避暑地として愛されてきた、日本を代表する高原リゾート。緑豊かな別荘地に、おしゃれなカフェやレストラン、ショッピングモールが点在します。レトロな商店が並ぶ「旧軽井沢銀座通り」での食べ歩き、雲場池や白糸の滝の自然散策、軽井沢高原教会など見どころ多彩。サイクリングやアウトレットでの買い物も楽しめ、四季を通じて爽やかな滞在ができます。",
     "videos": [{"id": "79tgplC8-wQ", "title": "絶対行くべきおすすめスポット「旧軽井沢銀座通り商店街」食べ歩き観光"},
                {"id": "FFwNoKRaeIQ", "title": "【長野旅行vlog】軽井沢観光 絶景を巡るドライブ旅 鬼押出し園・白糸の滝・高原教会"},
                {"id": "f89rsHUREh0", "title": "【軽井沢】観光協会おすすめのモデルコースを実践してみた！"},
                {"id": "cPeLbpkIqcM", "title": "【軽井沢】グルメ＆観光 日帰り旅行"}],
     "shorts": [{"id": "JxrtrPdfpQA", "title": "11月上旬の旧軽井沢 地元民が解説"},
                {"id": "3breru_G6Lg", "title": "旧軽井沢の魅力たっぷりの散歩道"}],
     "access": "北陸新幹線・軽井沢駅すぐ／旧軽井沢へはバス・徒歩", "hours": "散策自由（店舗により異なる）",
     "holiday": "なし", "parking": "周辺有料駐車場",
     "feature": "旧軽井沢銀座・雲場池・白糸の滝・高原教会・アウトレット・避暑地",
     "lat": 36.3417, "lng": 138.6356, "kw_jp": "軽井沢", "kw_en": "Karuizawa Nagano", "kw_book": "Karuizawa Nagano"},

    {"slug": "narai-juku", "name": "奈良井宿", "area_label": "長野エリア",
     "location": "長野県塩尻市", "tag": "宿場町・町並み・歴史",
     "desc": "江戸時代の中山道・木曽路に栄えた、日本最長クラスの宿場町。約1kmにわたって格子戸の町家や旅籠が軒を連ね、まるで時代劇のセットのような江戸の風情が残ります。重要伝統的建造物群保存地区に指定され、映画やドラマのロケ地としても人気。木曽の漆器や五平餅、信州蕎麦などの食べ歩きや土産探しも楽しく、ノスタルジックな街道散策が満喫できます。",
     "videos": [{"id": "IBvIKXYcgm8", "title": "ノスタルジックな宿場町で食べ歩き 江戸時代の風情が残る「奈良井宿」"},
                {"id": "FWFB5ttf5kE", "title": "【奈良井宿観光モデルコース解説】中山道 木曽路 見どころを効率的に巡る"},
                {"id": "D9X3g93Z4EY", "title": "【長野観光】奈良井宿を観光 1kmにわたる日本最長の宿場町散策とグルメ"},
                {"id": "1D1-UVP0mz0", "title": "【木曽路・奈良井宿】日本最長の宿場町で蕎麦やパフェを堪能！"}],
     "shorts": [{"id": "8dP7ZVdZ6pA", "title": "鳥居峠を歩いてみた 奈良井宿〜薮原宿"},
                {"id": "ZJxtT5SlzeY", "title": "日本一長い宿場町 中山道「奈良井宿」を歩く"}],
     "access": "JR中央本線・奈良井駅から徒歩すぐ", "hours": "散策自由（店舗により異なる）",
     "holiday": "なし", "parking": "周辺駐車場",
     "feature": "中山道・木曽路・宿場町・格子戸の町家・漆器・五平餅・重要伝建地区",
     "lat": 35.9847, "lng": 137.8126, "kw_jp": "木曽 奈良井", "kw_en": "Narai juku Kiso Nagano", "kw_book": "Kiso Nagano"},
]

slugs = [(s["slug"], s["location"], s["name"]) for s in SPOTS]
for i, s in enumerate(SPOTS):
    s["related"] = [slugs[(i + j) % len(slugs)] for j in (1, 2, 3)]
    s["card_tag"] = s["tag"].split("・")[0]
CARD_DESC = {
    "zenkoji": "「一生に一度は善光寺参り」の信州随一の名刹。お戒壇巡りが人気。",
    "matsumoto-castle": "現存最古とされる五重六階の国宝天守。烏城の異名を持つ名城。",
    "kamikochi": "北アルプスの懐の山岳景勝地。河童橋から望む穂高連峰が絶景。",
    "jigokudani-monkey": "世界で唯一、温泉に入る野生のスノーモンキーが見られる。",
    "karuizawa": "明治から愛される高原リゾート。旧軽井沢銀座の食べ歩きも人気。",
    "narai-juku": "中山道・木曽路の日本最長クラスの宿場町。江戸の町並みが残る。",
}
for s in SPOTS:
    s["card_desc"] = CARD_DESC[s["slug"]]

if __name__ == "__main__":
    run(CFG, SPOTS)
