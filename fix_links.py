#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
API不要の確定的修正:
  - 全スポットページ/トップ/静岡ページのフッターに 運営者情報・お問い合わせ を追加し、
    壊れたプライバシーリンク(href="#")を修正
  - sitemap.xml に about/ contact/ を追加
冪等（再実行しても重複しない）。
"""
import os
import re
import glob

BASE = os.path.dirname(os.path.abspath(__file__))


def footer_links(prefix: str) -> str:
    return (
        '<div class="footer-links">'
        f'<a href="{prefix}">トップ</a>'
        f'<a href="{prefix}about/">運営者情報</a>'
        f'<a href="{prefix}contact/">お問い合わせ</a>'
        f'<a href="{prefix}privacy/">プライバシーポリシー</a>'
        '</div>'
    )


def fix_file(path: str, prefix: str) -> bool:
    with open(path, encoding="utf-8") as f:
        c = f.read()
    orig = c
    c = re.sub(r'<div class="footer-links">.*?</div>', footer_links(prefix), c, count=1, flags=re.DOTALL)
    if c != orig:
        with open(path, "w", encoding="utf-8") as f:
            f.write(c)
        return True
    return False


def fix_sitemap() -> bool:
    path = os.path.join(BASE, "sitemap.xml")
    with open(path, encoding="utf-8") as f:
        c = f.read()
    if "dokoriaru.com/about/" in c:
        return False
    entries = (
        "  <url><loc>https://dokoriaru.com/about/</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>\n"
        "  <url><loc>https://dokoriaru.com/contact/</loc><changefreq>monthly</changefreq><priority>0.5</priority></url>\n"
    )
    c = c.replace("</urlset>", entries + "</urlset>")
    with open(path, "w", encoding="utf-8") as f:
        f.write(c)
    return True


def main():
    changed = 0
    # スポットページ（../../ 基準）
    for p in sorted(glob.glob(os.path.join(BASE, "spots", "*", "index.html"))):
        if fix_file(p, "../../"):
            changed += 1
    # トップ（./ 基準）
    for name in ["index.html"]:
        p = os.path.join(BASE, name)
        if os.path.exists(p) and fix_file(p, ""):
            changed += 1
    # 静岡ページ（../ 基準）
    p = os.path.join(BASE, "shizuoka", "index.html")
    if os.path.exists(p) and fix_file(p, "../"):
        changed += 1
    sm = fix_sitemap()
    print(f"フッター修正: {changed}ファイル / sitemap更新: {'あり' if sm else 'スキップ'}")


if __name__ == "__main__":
    main()
