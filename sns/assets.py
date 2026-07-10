# -*- coding: utf-8 -*-
"""
自前ブランド画像/動画の生成（第三者写真を使わず、ロゴ＋テキストのみ＝著作権クリーン）。
- make_card       : 1080x1080  Instagram用
- make_vertical   : 1080x1920  TikTok / YouTube Shorts用
- make_slideshow  : 上記縦カードから数秒のmp4（ffmpegでゆっくりズーム）
Pillow が無い/フォントが無い環境では None を返し、呼び出し側でスキップする。
"""
import os, re, subprocess

BRAND_BG   = (26, 26, 46)     # navy #1A1A2E
BRAND_ACC  = (255, 107, 74)   # coral #FF6B4A
WHITE      = (245, 245, 245)

FONT_CANDIDATES = [
    "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc",
    "/usr/share/fonts/opentype/noto/NotoSansCJKjp-Bold.otf",
    "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc",
    "/System/Library/Fonts/Supplemental/Hiragino Sans GB.ttc",
    "/Library/Fonts/NotoSansCJKjp-Bold.otf",
]

def _font(size):
    from PIL import ImageFont
    for p in FONT_CANDIDATES:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                continue
    return None

def _draw_card(row, W, H, out):
    try:
        from PIL import Image, ImageDraw
    except ImportError:
        return None
    f_name  = _font(int(W * 0.075))
    f_small = _font(int(W * 0.032))
    f_logo  = _font(int(W * 0.040))
    if not f_name:
        return None  # 日本語フォント無し → スキップ

    img = Image.new("RGB", (W, H), BRAND_BG)
    d = ImageDraw.Draw(img)
    # 上下のアクセントバー
    d.rectangle([0, 0, W, int(H * 0.012)], fill=BRAND_ACC)
    d.rectangle([0, H - int(H * 0.012), W, H], fill=BRAND_ACC)
    # ロゴ
    d.text((int(W * 0.07), int(H * 0.09)), "ドコリアル", font=f_logo, fill=BRAND_ACC)
    # エリア・ジャンル
    meta = "　".join([x for x in [row.get("area"), row.get("genre")] if x])
    d.text((int(W * 0.07), int(H * 0.09) + int(W * 0.06)), meta, font=f_small, fill=(180, 180, 200))
    # スポット名（カードは括弧内を省いてスッキリ表示）
    name = re.sub(r"[（(][^）)]*[）)]", "", row["name"]).strip() or row["name"]
    lines, line = [], ""
    maxch = 9 if W <= H else 16
    for ch in name:
        if len(line) >= maxch:
            lines.append(line); line = ""
        line += ch
    if line:
        lines.append(line)
    y = int(H * 0.34)
    for ln in lines[:4]:
        d.text((int(W * 0.07), y), ln, font=f_name, fill=WHITE)
        y += int(W * 0.09)
    # 下部コピー
    d.text((int(W * 0.07), H - int(H * 0.16)), "行く前に、リアルを見よう。", font=f_small, fill=WHITE)
    d.text((int(W * 0.07), H - int(H * 0.16) + int(W * 0.05)), "dokoriaru.com", font=f_small, fill=BRAND_ACC)
    img.save(out, quality=90)
    return out

def make_card(row, out):        return _draw_card(row, 1080, 1080, out)
def make_vertical(row, out):    return _draw_card(row, 1080, 1920, out)

def make_slideshow(row, out_mp4, seconds=6):
    """縦カード→ゆっくりズームのmp4。ffmpeg必須。生成できなければNone。"""
    base = out_mp4.replace(".mp4", "_frame.jpg")
    if not make_vertical(row, base):
        return None
    if not subprocess.run(["which", "ffmpeg"], capture_output=True).returncode == 0:
        return None
    zoom = (f"zoompan=z='min(zoom+0.0009,1.15)':d={seconds*30}:"
            f"s=1080x1920:fps=30")
    cmd = ["ffmpeg", "-y", "-loop", "1", "-i", base, "-vf", zoom,
           "-c:v", "libx264", "-t", str(seconds), "-pix_fmt", "yuv420p", out_mp4]
    if subprocess.run(cmd, capture_output=True).returncode == 0:
        return out_mp4
    return None
