# -*- coding: utf-8 -*-
"""スポット1件から各SNS向けキャプションを生成する。プラットフォームごとに文字数・体裁を最適化。"""

# 先頭に付ける絵文字をジャンル語からゆるく選ぶ
GENRE_EMOJI = [
    ("温泉", "♨️"), ("キャンプ", "🏕"), ("富士山", "🗻"), ("動物", "🐾"), ("水族館", "🐬"),
    ("夜景", "🌃"), ("桜", "🌸"), ("紅葉", "🍁"), ("グルメ", "🍜"), ("海", "🌊"),
    ("滝", "💧"), ("神社", "⛩"), ("城", "🏯"), ("絶景", "✨"), ("公園", "🌳"),
]

def _emoji(row):
    g = (row.get("genre") or "") + (row.get("name") or "")
    for kw, e in GENRE_EMOJI:
        if kw in g:
            return e
    return "📍"

def _trim(s, n):
    s = (s or "").strip()
    return s if len(s) <= n else s[: n - 1].rstrip("、。・") + "…"

def for_x(row):
    """X: 日本語はおおむね全角=2でカウント。URL/ハッシュタグ込みで安全に収める。"""
    e = _emoji(row)
    tags = " ".join(row["hashtags"][:4])
    body = _trim(row["blurb"], 45)
    return f"{e}{row['name']}（{row['area']}）\n{body}\n\n▶ 動画でリアルチェック\n{row['url']}\n{tags}"

def for_threads(row):
    e = _emoji(row)
    tags = " ".join(row["hashtags"][:5])
    body = _trim(row["blurb"], 120)
    return f"{e}{row['name']}（{row['area']}）\n\n{body}\n\n▶ 行く前にSNS動画でリアルチェック👇\n{row['url']}\n\n{tags}"

def for_instagram(row):
    e = _emoji(row)
    tags = " ".join(row["hashtags"] + ["#国内旅行", "#旅行", "#お出かけスポット", "#dokoriaru"])
    body = _trim(row["blurb"], 150)
    return (f"{e}{row['name']}（{row['area']}）\n\n{body}\n\n"
            f"▶ 実際の雰囲気はSNS動画でチェック。\nプロフィールのリンク（@）からどうぞ✨\n\n{tags}")

def for_tiktok(row):
    tags = " ".join(row["hashtags"][:5] + ["#おすすめスポット", "#fyp"])
    return f"{_emoji(row)}{row['name']}の実際の雰囲気は？行く前に動画でチェック👀 {tags}"

def for_youtube(row):
    return {
        "title": f"{row['name']}｜行く前に見るリアル動画まとめ #shorts",
        "description": (f"{row['name']}（{row['area']}）の実際の雰囲気をチェック。\n"
                        f"詳しくは → {row['url']}\n\n{' '.join(row['hashtags'])} #shorts #国内旅行"),
    }

BUILDERS = {
    "x": for_x, "threads": for_threads, "instagram": for_instagram,
    "tiktok": for_tiktok, "youtube": for_youtube,
}
