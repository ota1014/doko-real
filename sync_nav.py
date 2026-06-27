#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""トップ/各エリアページの『エリア』ドロップダウンを最新の掲載状況に同期する。"""
import os, re, glob

BASE = os.path.dirname(os.path.abspath(__file__))

LIVE = [("shizuoka", "🗾 静岡"), ("tokyo", "🗼 東京"), ("osaka", "🏯 大阪"),
        ("hokkaido", "🐻 北海道"), ("fukuoka", "🍜 福岡"), ("kyoto", "🌸 京都"),
        ("okinawa", "🌺 沖縄"), ("nagoya", "🏯 名古屋"), ("kanagawa", "⛩ 神奈川"),
        ("hiroshima", "🍁 広島")]
COMING = []

def menu_items():
    s = ""
    for slug, label in LIVE:
        s += f'        <a href="/{slug}/" class="nav-menu-item">{label} <span class="badge badge-live">掲載中</span></a>\n'
    if COMING:
        s += '        <div class="nav-menu-divider"></div>\n'
        for label in COMING:
            s += f'        <span class="nav-menu-item coming">{label} <span class="badge badge-soon">準備中</span></span>\n'
    return s

def sync(path):
    c = open(path, encoding="utf-8").read()
    # 『エリア』ボタン直後の nav-dropdown-menu の中身を差し替え
    pat = re.compile(r'(<button class="nav-btn">エリア\s*<span class="caret">▾</span></button>\s*<div class="nav-dropdown-menu">\n).*?(\n? *</div>\s*</div>\s*<div class="nav-dropdown">)', re.DOTALL)
    new = pat.sub(lambda m: m.group(1) + menu_items() + "      </div>\n    </div>\n    <div class=\"nav-dropdown\">", c, count=1)
    if new != c:
        open(path, "w", encoding="utf-8").write(new); return True
    # テーマ無しの単独ドロップダウン（エリアページ）用
    pat2 = re.compile(r'(<button class="nav-btn">エリア\s*<span class="caret">▾</span></button>\s*<div class="nav-dropdown-menu">\n).*?(\n? *</div>\s*</div>)', re.DOTALL)
    new = pat2.sub(lambda m: m.group(1) + menu_items() + "      </div>\n    </div>", c, count=1)
    if new != c:
        open(path, "w", encoding="utf-8").write(new); return True
    return False

def main():
    targets = ["index.html", "shizuoka/index.html", "tokyo/index.html",
               "osaka/index.html", "hokkaido/index.html", "fukuoka/index.html",
               "kyoto/index.html", "okinawa/index.html", "nagoya/index.html", "kanagawa/index.html"]
    done = []
    for t in targets:
        p = os.path.join(BASE, t)
        if os.path.exists(p) and sync(p):
            done.append(t)
    print("nav同期:", done)

if __name__ == "__main__":
    main()
