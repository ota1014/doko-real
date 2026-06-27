#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ドコリアル AdSense 対応: 各スポットページにオリジナルコンテンツを追加

処理内容:
  1. 全53スポットの index.html を走査
  2. 動画タイトル・キャプション・基本情報を抽出
  3. Claude API (claude-opus-4-8) で 500〜600字の紹介文を生成
  4. 既存の説明文を置き換え
  5. フッターのプライバシーポリシーリンクを修正
  6. git add . && git commit && git push

使い方:
  cd ~/Desktop/BeeBloom/09_新規事業/ドコリアル
  python3 add_content.py [--dry-run] [--slug <slug>]
"""

import os
import re
import sys
import glob
import time
import argparse
import subprocess
from bs4 import BeautifulSoup
import anthropic

SPOTS_DIR = os.path.join(os.path.dirname(__file__), "spots")
MODEL = "claude-opus-4-8"
MIN_CHARS = 400  # これ以上あるスポットはスキップ


def extract_info(html_path: str) -> dict:
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    h1 = soup.find("h1")
    name = h1.get_text(strip=True) if h1 else ""

    desc_p = soup.find("p", style=lambda s: s and "margin-bottom:32px" in s)
    existing_desc = desc_p.get_text(strip=True) if desc_p else ""

    iframes = soup.find_all("iframe", title=True)
    video_titles = [i["title"] for i in iframes if i.get("title")]

    captions = [div.get_text(strip=True) for div in soup.find_all("div", class_="video-caption")]

    location = ""
    for span in soup.find_all("span"):
        text = span.get_text()
        if "📍" in text:
            location = text.replace("📍", "").strip()
            break

    info_rows = {}
    table = soup.find("table", class_="info-table")
    if table:
        for tr in table.find_all("tr"):
            th = tr.find("th")
            td = tr.find("td")
            if th and td:
                info_rows[th.get_text(strip=True)] = td.get_text(strip=True)

    return {
        "name": name,
        "location": location,
        "existing_desc": existing_desc,
        "video_titles": video_titles,
        "captions": captions,
        "info": info_rows,
    }


def generate_description(info: dict, client: anthropic.Anthropic) -> str:
    video_lines = []
    for t in info["video_titles"][:5]:
        video_lines.append(f"・動画タイトル: {t}")
    for c in info["captions"][:5]:
        video_lines.append(f"・動画の説明文: {c}")

    info_lines = [f"{k}: {v}" for k, v in info["info"].items()]

    prompt = f"""以下の観光スポット情報をもとに、観光客向けの紹介文を日本語で500〜600文字で作成してください。

スポット名: {info['name']}
場所: {info['location']}

【SNS動画の内容（必ず参照してください）】
{chr(10).join(video_lines) if video_lines else '（情報なし）'}

【基本情報】
{chr(10).join(info_lines) if info_lines else '（情報なし）'}

【要件】
- 500〜600文字（日本語の文字数）で厳守すること
- 動画タイトル・動画説明文に記載された内容・見どころを具体的に盛り込む
- アクセス・おすすめシーズン・周辺スポットも自然に触れる
- 観光客が「行ってみたい」と感じる魅力的な文章にする
- HTMLタグ一切なし・プレーンテキストのみ
- 段落は1〜2段落（改行は最小限）
- 文字数を必ず確認してから出力すること"""

    response = client.messages.create(
        model=MODEL,
        max_tokens=1200,
        messages=[{"role": "user", "content": prompt}],
    )
    return response.content[0].text.strip()


def update_html(html_path: str, new_desc: str) -> bool:
    with open(html_path, encoding="utf-8") as f:
        content = f.read()

    original = content

    # 説明文の置き換え（正規表現でp要素の中身のみ差し替え）
    pattern = (
        r'(<p class="reveal" style="margin-bottom:32px;color:#555;line-height:1\.9;">)'
        r'\s*.*?\s*'
        r'(</p>)'
    )
    new_content = re.sub(
        pattern,
        rf'\1\n    {new_desc}\n  \2',
        content,
        flags=re.DOTALL,
    )

    # フッターのプライバシーポリシーリンク修正
    new_content = new_content.replace(
        '<a href="#">プライバシーポリシー</a>',
        '<a href="../../privacy/">プライバシーポリシー</a>',
    )

    if new_content == original:
        return False

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="生成のみ・ファイル書き込みなし")
    parser.add_argument("--slug", help="特定スポットのみ処理（例: numazu-port）")
    parser.add_argument("--no-push", action="store_true", help="git push しない")
    args = parser.parse_args()

    client = anthropic.Anthropic()

    if args.slug:
        pattern = os.path.join(SPOTS_DIR, args.slug, "index.html")
    else:
        pattern = os.path.join(SPOTS_DIR, "*/index.html")

    spot_files = sorted(glob.glob(pattern))
    if not spot_files:
        print(f"エラー: スポットファイルが見つかりません: {pattern}")
        sys.exit(1)

    print(f"対象スポット数: {len(spot_files)}")
    print(f"モデル: {MODEL}")
    if args.dry_run:
        print("※ dry-run モード（ファイル書き込みなし）")
    print()

    skipped = []
    updated = []
    errors = []

    for i, path in enumerate(spot_files):
        slug = os.path.basename(os.path.dirname(path))
        try:
            info = extract_info(path)
            current_len = len(info["existing_desc"])

            if current_len >= MIN_CHARS and not args.slug:
                print(f"[{i+1}/{len(spot_files)}] {slug}: スキップ（既存 {current_len}字）")
                skipped.append(slug)
                continue

            print(f"[{i+1}/{len(spot_files)}] {slug} 生成中... ", end="", flush=True)
            new_desc = generate_description(info, client)
            gen_len = len(new_desc)
            print(f"{gen_len}字")

            if args.dry_run:
                print(f"  プレビュー: {new_desc[:80]}...")
            else:
                changed = update_html(path, new_desc)
                if changed:
                    updated.append(slug)
                else:
                    print(f"  警告: HTML更新失敗（パターン不一致）")
                    errors.append(slug)

            # レート制限対策
            if i < len(spot_files) - 1:
                time.sleep(0.3)

        except Exception as e:
            print(f"  エラー: {e}")
            errors.append(slug)

    print(f"\n=== 完了 ===")
    print(f"更新: {len(updated)}件 / スキップ: {len(skipped)}件 / エラー: {len(errors)}件")
    if errors:
        print(f"エラースポット: {', '.join(errors)}")

    if not args.dry_run and updated and not args.no_push:
        print("\ngit commit & push 中...")
        repo_dir = os.path.dirname(__file__)
        subprocess.run(["git", "add", "."], cwd=repo_dir, check=True)
        subprocess.run(
            ["git", "commit", "-m", "コンテンツ拡充: AdSense再申請対応（全スポット紹介文を500字以上に更新）"],
            cwd=repo_dir,
            check=True,
        )
        subprocess.run(["git", "push"], cwd=repo_dir, check=True)
        print("✓ GitHub Pages にデプロイしました")
        print("URL: https://ota1014.github.io/doko-real/")


if __name__ == "__main__":
    main()
