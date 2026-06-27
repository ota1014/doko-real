#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ドコリアル AdSense「有用性の低いコンテンツ」対策:
各スポットページに独自の解説記事（見どころ・アクセス・ベストシーズン・FAQ）を追加し、
thin content 判定を解消する。

処理内容:
  1. 全53スポットの spots/*/index.html を走査
  2. ページから名称・場所・動画タイトル/説明・基本情報を抽出
  3. Claude API (claude-opus-4-8) で構造化JSON（intro/highlights/access/season/tips/faq）を生成
  4. 独自解説ブロック（HTML）+ FAQPage構造化データ を動画セクションの直前に挿入
  5. フッターのリンクを修正（壊れたprivacy + about/contact 追加）
  6. 再実行しても二重挿入しない（マーカーで判定）

使い方:
  cd ~/Desktop/BeeBloom/09_新規事業/ドコリアル
  python3 enrich_spots.py [--dry-run] [--slug <slug>] [--no-push] [--limit N]
"""

import os
import re
import sys
import csv
import json
import glob
import time
import html
import argparse
import subprocess
from bs4 import BeautifulSoup
import anthropic

BASE = os.path.dirname(os.path.abspath(__file__))
SPOTS_DIR = os.path.join(BASE, "spots")
KEY_FILE = os.path.expanduser("~/.beebloom/07_Development/credentials/anthropic_key.txt")
ARTICLES_JSON = os.path.join(BASE, "articles.json")  # 手動執筆の本文を流し込む場合に使用
MODEL = "claude-opus-4-8"
MARKER = "<!-- enriched-article v1 -->"


def load_articles() -> dict:
    """articles.json があれば {slug: {intro, highlights, ...}} を返す。なければ空。"""
    if os.path.exists(ARTICLES_JSON):
        with open(ARTICLES_JSON, encoding="utf-8") as f:
            return json.load(f)
    return {}


def get_client() -> anthropic.Anthropic:
    """APIキーは環境変数優先、なければ認証ファイルから読む。"""
    key = os.environ.get("ANTHROPIC_API_KEY")
    if not key and os.path.exists(KEY_FILE):
        with open(KEY_FILE, encoding="utf-8") as f:
            key = f.read().strip()
    if not key:
        print("エラー: ANTHROPIC_API_KEY が見つかりません。")
        sys.exit(1)
    return anthropic.Anthropic(api_key=key)


def extract_info(soup: BeautifulSoup) -> dict:
    h1 = soup.find("h1")
    name = h1.get_text(strip=True) if h1 else ""

    location = ""
    for span in soup.find_all("span"):
        if "📍" in span.get_text():
            location = span.get_text().replace("📍", "").strip()
            break

    video_titles = [i["title"] for i in soup.find_all("iframe", title=True) if i.get("title")]
    captions = [d.get_text(strip=True) for d in soup.find_all("div", class_="video-caption")]

    info_rows = {}
    table = soup.find("table", class_="info-table")
    if table:
        for tr in table.find_all("tr"):
            th, td = tr.find("th"), tr.find("td")
            if th and td:
                info_rows[th.get_text(strip=True)] = td.get_text(strip=True)

    return {
        "name": name,
        "location": location,
        "video_titles": video_titles,
        "captions": captions,
        "info": info_rows,
    }


def generate_article(info: dict, client: anthropic.Anthropic) -> dict:
    video_lines = [f"・動画タイトル: {t}" for t in info["video_titles"][:6]]
    video_lines += [f"・動画の説明: {c}" for c in info["captions"][:6]]
    info_lines = [f"{k}: {v}" for k, v in info["info"].items()]

    prompt = f"""あなたは観光メディア「ドコリアル」の編集者です。以下の観光スポットについて、訪問計画に本当に役立つ独自の解説記事を作成してください。一般論や水増しの定型文は避け、このスポット固有の具体情報を盛り込みます。

スポット名: {info['name']}
場所: {info['location']}

【SNS動画から読み取れる現地の様子（参照）】
{chr(10).join(video_lines) if video_lines else '（情報なし）'}

【基本情報】
{chr(10).join(info_lines) if info_lines else '（情報なし）'}

以下のキーを持つJSONのみを出力してください（前後に説明文やコードフェンスを付けない）:
{{
  "intro": "このスポットの概要と魅力。250〜320字。",
  "highlights": "見どころ・楽しみ方を具体的に。250〜320字。",
  "access": "アクセス・行き方・駐車場・所要時間の実用情報。180〜240字。",
  "season": "ベストシーズン・訪れるおすすめの時間帯・混雑の傾向。180〜240字。",
  "tips": "知っておくと得する豆知識・周辺で合わせて回れるスポット。150〜220字。",
  "faq": [
    {{"q": "よくある質問1", "a": "回答（80〜140字）"}},
    {{"q": "よくある質問2", "a": "回答（80〜140字）"}},
    {{"q": "よくある質問3", "a": "回答（80〜140字）"}}
  ]
}}

要件:
- すべて日本語のプレーンテキスト（HTMLタグ禁止）。
- 事実が不確かな固有名詞・数値は断定せず一般的表現にとどめる。
- 文字数の目安を守る。JSONとして必ずパース可能な形式にする。"""

    resp = client.messages.create(
        model=MODEL,
        max_tokens=2500,
        messages=[{"role": "user", "content": prompt}],
    )
    text = resp.content[0].text.strip()
    # コードフェンスが付いた場合の除去
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text).strip()
    return json.loads(text)


def esc(s: str) -> str:
    return html.escape(s, quote=False)


def build_block(name: str, art: dict) -> str:
    # 見どころ（カード型: {title, body} の配列）
    hl_html = ""
    for h in art.get("highlights", []) or []:
        t = esc((h.get("title") or "").strip())
        b = esc((h.get("body") or "").strip())
        if t and b:
            hl_html += (
                f'\n      <div class="hl-item">'
                f'\n        <div class="hl-title">{t}</div>'
                f'\n        <div class="hl-body">{b}</div>'
                f'\n      </div>'
            )

    # 知っておきたいポイント（箇条書き配列）
    tips_html = ""
    for tip in art.get("tips", []) or []:
        tip = esc((tip or "").strip())
        if tip:
            tips_html += f'\n      <li>{tip}</li>'

    # FAQ
    faq_items = art.get("faq", []) or []
    faq_html = ""
    for item in faq_items:
        q = esc((item.get("q") or "").strip())
        a = esc((item.get("a") or "").strip())
        if q and a:
            faq_html += (
                f'\n      <div class="faq-item">'
                f'\n        <div class="faq-q">{q}</div>'
                f'\n        <div class="faq-a">{a}</div>'
                f'\n      </div>'
            )

    faq_ld = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": (item.get("q") or "").strip(),
                "acceptedAnswer": {"@type": "Answer", "text": (item.get("a") or "").strip()},
            }
            for item in faq_items
            if item.get("q") and item.get("a")
        ],
    }

    section = f"""  {MARKER}
  <article class="spot-article reveal">
    <div class="article-head">📖 {esc(name)}を訪れる前に｜編集部ガイド</div>
    <p class="article-lead">{esc((art.get('intro') or '').strip())}</p>

    <h3 class="article-h"><span>✨</span>見どころ・楽しみ方</h3>
    <div class="hl-list">{hl_html}
    </div>

    <div class="article-cols">
      <div class="article-col">
        <h3 class="article-h"><span>🚃</span>アクセス・所要時間</h3>
        <p>{esc((art.get('access') or '').strip())}</p>
      </div>
      <div class="article-col">
        <h3 class="article-h"><span>🗓️</span>ベストシーズン・時間帯</h3>
        <p>{esc((art.get('season') or '').strip())}</p>
      </div>
    </div>

    <h3 class="article-h"><span>💡</span>知っておきたいポイント</h3>
    <ul class="tips-list">{tips_html}
    </ul>

    <h3 class="article-h"><span>❓</span>よくある質問</h3>
    <div class="faq-list">{faq_html}
    </div>
  </article>
  <script type="application/ld+json">
{json.dumps(faq_ld, ensure_ascii=False, indent=2)}
  </script>
"""
    return section


def fix_footer(content: str) -> str:
    # 壊れた/不足しているフッターリンクを整える（スポットページは ../../ 基準）
    new_links = (
        '<div class="footer-links">'
        '<a href="../../">トップ</a>'
        '<a href="../../about/">運営者情報</a>'
        '<a href="../../contact/">お問い合わせ</a>'
        '<a href="../../privacy/">プライバシーポリシー</a>'
        '</div>'
    )
    content = re.sub(
        r'<div class="footer-links">.*?</div>',
        new_links,
        content,
        count=1,
        flags=re.DOTALL,
    )
    return content


def process(path: str, client, dry_run: bool, articles: dict) -> str:
    slug = os.path.basename(os.path.dirname(path))
    with open(path, encoding="utf-8") as f:
        content = f.read()

    if MARKER in content:
        return "skip"

    soup = BeautifulSoup(content, "html.parser")
    info = extract_info(soup)
    if not info["name"]:
        return "noname"

    # 手動執筆JSONがあればそれを優先（API課金不要）。なければAPIで生成。
    if slug in articles:
        art = articles[slug]
    else:
        if client is None:
            return "no-api-no-json"
        art = generate_article(info, client)
    block = build_block(info["name"], art)

    # 動画セクションの直前に挿入
    anchor = '<div class="video-section reveal">'
    if anchor not in content:
        return "noanchor"
    new_content = content.replace(anchor, block + "\n  " + anchor, 1)
    new_content = fix_footer(new_content)

    if new_content == content:
        return "nochange"

    if not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)
    return "ok"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--slug")
    p.add_argument("--no-push", action="store_true")
    p.add_argument("--no-api", action="store_true", help="APIを使わずarticles.jsonにある分のみ処理")
    p.add_argument("--limit", type=int, default=0)
    args = p.parse_args()

    articles = load_articles()
    if articles:
        print(f"articles.json 検出: {len(articles)}件の手動本文を使用")
    # 全スポット分の手動本文が揃っていればAPIは初期化しない
    spot_slugs = {os.path.basename(os.path.dirname(x))
                  for x in glob.glob(os.path.join(SPOTS_DIR, "*/index.html"))}
    need_api = bool(spot_slugs - set(articles.keys())) and not args.slug
    if args.slug and args.slug not in articles:
        need_api = True
    if args.no_api:
        need_api = False
    client = get_client() if need_api else None

    if args.slug:
        files = [os.path.join(SPOTS_DIR, args.slug, "index.html")]
    else:
        files = sorted(glob.glob(os.path.join(SPOTS_DIR, "*/index.html")))
    if args.limit:
        files = files[: args.limit]

    print(f"対象: {len(files)}件 / モデル: {MODEL}" + (" / dry-run" if args.dry_run else ""))
    ok, skip, err = [], [], []

    for i, path in enumerate(files):
        slug = os.path.basename(os.path.dirname(path))
        try:
            print(f"[{i+1}/{len(files)}] {slug} ... ", end="", flush=True)
            r = process(path, client, args.dry_run, articles)
            if r == "ok":
                print("追加")
                ok.append(slug)
            elif r == "skip":
                print("スキップ（既に追加済み）")
                skip.append(slug)
            else:
                print(f"警告: {r}")
                err.append(f"{slug}:{r}")
            if i < len(files) - 1:
                time.sleep(0.3)
        except Exception as e:
            print(f"エラー: {e}")
            err.append(f"{slug}:{e}")

    print(f"\n=== 完了 === 追加:{len(ok)} / スキップ:{len(skip)} / 問題:{len(err)}")
    if err:
        print("要確認:", "; ".join(err))

    if not args.dry_run and ok and not args.no_push:
        subprocess.run(["git", "add", "."], cwd=BASE, check=True)
        subprocess.run(
            ["git", "commit", "-m",
             "AdSense対策: 全スポットに独自解説記事+FAQ(構造化データ)を追加、運営者情報/お問い合わせページ新設"],
            cwd=BASE, check=True,
        )
        subprocess.run(["git", "push"], cwd=BASE, check=True)
        print("✓ GitHub Pages へデプロイ: https://dokoriaru.com/")


if __name__ == "__main__":
    main()
