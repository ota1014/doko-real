# -*- coding: utf-8 -*-
"""
Short動画（1080x1920）を自動生成。テキストはPillowでPNG化→ffmpeg overlayで合成するため
drawtext/libass 非依存（環境を選ばず動く）。
 - Wikimedia実写（CC/PD・出典付き）でKen-Burnsスライドショー
 - edge-tts AI音声ナレーション＋単語タイミングから字幕（フレーズ単位でPNG焼き込み）
 - 冒頭フック＋スポット名ロワーサード＋ブランドEndカード
戻り値: (mp4パス, 出典テキスト) / 不可なら (None, "")
"""
import os, re, json, tempfile, asyncio, subprocess
import assets, wiki

VOICE, RATE = "ja-JP-NanamiNeural", "+8%"
W, H = 1080, 1920

def _fontpath():
    for p in assets.FONT_CANDIDATES:
        if os.path.exists(p):
            return p
    return None

def _dur(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nk=1:nw=1", path], capture_output=True, text=True)
    try: return float(r.stdout.strip())
    except: return 0.0

def narration_script(row):
    blurb = re.sub(r"（[^）]*）", "", row.get("blurb", ""))
    sents = [s for s in re.split(r"[。！]", blurb) if s.strip()][:2]
    name = re.sub(r"[（(][^）)]*[）)]", "", row["name"]).strip() or row["name"]
    return f"行く前に見て。{name}、{row.get('area','')}。{'。'.join(sents)}。実際の雰囲気はSNS動画でチェック。ドコリアルで、行く前にリアルを見よう。"

# ---------- ナレーション＋字幕キュー ----------
# 日本語のedge-ttsはWordBoundaryを返さないため、フレーズ単位で個別合成して尺を実測し、
# 字幕タイミングを自前構築する（正確な同期字幕）。
def _split_phrases(script, maxlen=15):
    out = []
    for seg in re.split(r"[。、！]", script):
        seg = seg.strip()
        while len(seg) > maxlen:
            cut = seg[:maxlen]; out.append(cut); seg = seg[maxlen:]
        if seg:
            out.append(seg)
    return out

async def _synth_one(text, out):
    import edge_tts
    await edge_tts.Communicate(text, VOICE, rate=RATE).save(out)

def synth_phrases(script, work):
    """フレーズごとに合成→連結し、(narration.mp3, [(start,end,text)]) を返す。"""
    phrases = _split_phrases(script)
    mp3s, cues, t = [], [], 0.0
    for i, ph in enumerate(phrases):
        m = os.path.join(work, f"p{i}.mp3")
        try:
            asyncio.run(_synth_one(ph, m))
        except Exception:
            continue
        d = _dur(m)
        if d <= 0:
            continue
        mp3s.append(m); cues.append([t, t + d, ph]); t += d
    if not mp3s:
        return (None, [])
    lst = os.path.join(work, "alist.txt")
    open(lst, "w").write("".join(f"file '{m}'\n" for m in mp3s))
    full = os.path.join(work, "narr.mp3")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", full],
                   capture_output=True)
    return (full if os.path.exists(full) else None, cues)

# ---------- テキストPNG（Pillow） ----------
def _png_name(name, out):
    from PIL import Image, ImageDraw, ImageFont
    fp = _fontpath()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(fp, 58)
    tw = d.textlength(name, font=f); x = (W - tw) / 2; y = 1330
    d.rounded_rectangle([x-30, y-14, x+tw+30, y+84], radius=18, fill=(26, 26, 46, 200))
    d.rectangle([x-30, y-14, x-22, y+84], fill=(255, 107, 74, 255))
    d.text((x, y), name, font=f, fill=(255, 255, 255, 255))
    img.save(out)

def _png_hook(text, out):
    from PIL import Image, ImageDraw, ImageFont
    fp = _fontpath()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(fp, 66)
    tw = d.textlength(text, font=f); x = (W - tw) / 2; y = 210
    d.rounded_rectangle([x-28, y-16, x+tw+28, y+92], radius=20, fill=(255, 107, 74, 235))
    d.text((x, y), text, font=f, fill=(255, 255, 255, 255))
    img.save(out)

def _png_sub(text, out):
    """箱付きテロップ（TikTok/バラエティ風）。半透明ダーク箱＋白太字＋縁取り。"""
    from PIL import Image, ImageDraw, ImageFont
    fp = _fontpath()
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(img)
    f = ImageFont.truetype(fp, 58)
    tw = d.textlength(text, font=f)
    x = (W - tw) / 2; y = 1470
    pad_x, pad_y = 34, 18
    d.rounded_rectangle([x - pad_x, y - pad_y, x + tw + pad_x, y + 78 + pad_y],
                        radius=20, fill=(20, 20, 40, 205))
    d.text((x, y), text, font=f, fill=(255, 255, 255, 255),
           stroke_width=4, stroke_fill=(0, 0, 0, 255))
    img.save(out)

# ---------- 本体 ----------
def build_short(row, out_mp4):
    if not _fontpath():
        return (None, "")
    work = tempfile.mkdtemp(prefix="doko_")
    def wp(x): return os.path.join(work, x)
    name = re.sub(r"[（(][^）)]*[）)]", "", row["name"]).strip() or row["name"]

    # 1) ナレーション＋字幕（フレーズ単位で合成し尺を実測）
    try:
        mp3, cues = synth_phrases(narration_script(row), work)
    except Exception as e:
        print("  TTS失敗:", e); return (None, "")
    if not mp3:
        return (None, "")
    D = _dur(mp3)
    if D < 3: return (None, "")

    # 2) 実写取得（フォールバック多段）
    area = row.get("area", "")
    region = re.split(r"[市区町村]", area)[0] if area else ""
    genre = (row.get("genre", "") or "").split("・")[0]
    imgs = wiki.fetch_images_multi([name, area, region, f"{region} {genre}".strip()],
                                   n=5, out_dir=wp("w"))
    if len(imgs) >= 2:
        credits = "; ".join(sorted({f"{i['author']}({i['license']})" for i in imgs}))
        attribution = f"写真: Wikimedia Commons — {credits}"
    else:
        card = wp("card.jpg"); assets.make_vertical(row, card)
        imgs = [{"path": card}] if os.path.exists(card) else []
        attribution = ""
        if not imgs: return (None, "")

    # 3) ベーススライドショー（zoompanのみ・テキストなし）
    n = len(imgs); seg = max(2.6, D / n); parts = []
    # Ken-Burns: 1.4倍キャンバス内を1080x1920窓でパン。方向を画像ごとに変えて単調さを回避。
    # （zoompanは当環境で激遅のため、高速なcrop式アニメで実装）
    presets = [(0, 0.5, 1, 0.5), (0.5, 0, 0.5, 1), (1, 0.5, 0, 0.5), (0.5, 1, 0.5, 0)]
    for i, im in enumerate(imgs):
        out = wp(f"s{i}.mp4")
        sx, sy, ex, ey = presets[i % 4]
        vf = ("scale=1512:2688:force_original_aspect_ratio=increase,crop=1512:2688,"
              f"crop=1080:1920:x='(iw-1080)*({sx}+({ex}-{sx})*t/{seg:.2f})':"
              f"y='(ih-1920)*({sy}+({ey}-{sy})*t/{seg:.2f})',setsar=1,fps=30")
        subprocess.run(["ffmpeg", "-y", "-loop", "1", "-t", f"{seg:.2f}", "-i", im["path"],
                        "-vf", vf, "-r", "30", "-c:v", "libx264", "-preset", "veryfast",
                        "-pix_fmt", "yuv420p", out], capture_output=True)
        if os.path.exists(out): parts.append(out)
    endcard = wp("end.jpg")
    if assets.make_vertical(row, endcard):
        end = wp("end.mp4")
        subprocess.run(["ffmpeg", "-y", "-loop", "1", "-t", "3", "-i", endcard,
                        "-vf", "scale=1080:1920,setsar=1,fps=30", "-c:v", "libx264",
                        "-preset", "veryfast", "-pix_fmt", "yuv420p", end], capture_output=True)
        if os.path.exists(end): parts.append(end)
    if not parts: return (None, "")
    lst = wp("list.txt"); open(lst, "w").write("".join(f"file '{p}'\n" for p in parts))
    base = wp("base.mp4")
    subprocess.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", base],
                   capture_output=True)
    vlen = _dur(base)

    # 4) テキストPNG生成
    ov = []  # (png, enable)
    _png_name(name, wp("name.png")); ov.append((wp("name.png"), f"lt(t,{vlen-3:.2f})"))
    _png_hook(f"行く前に見て！", wp("hook.png")); ov.append((wp("hook.png"), "lt(t,2.6)"))
    for i, (s, e, t) in enumerate(cues):
        if e > vlen - 3: break
        _png_sub(t, wp(f"c{i}.png")); ov.append((wp(f"c{i}.png"), f"between(t,{s:.2f},{e:.2f})"))

    # 5) overlay合成＋音声
    inputs = ["-i", base, "-i", mp3]
    for png, _ in ov: inputs += ["-i", png]
    fc, cur = "", "0:v"
    for idx, (_, en) in enumerate(ov):
        nxt = f"v{idx}"
        fc += f"[{cur}][{idx+2}:v]overlay=0:0:enable='{en}'[{nxt}];"
        cur = nxt
    fc += f"[1:a]apad[a]"
    cmd = ["ffmpeg", "-y", *inputs, "-filter_complex", fc, "-map", f"[{cur}]", "-map", "[a]",
           "-shortest", "-r", "30", "-c:v", "libx264", "-preset", "veryfast",
           "-pix_fmt", "yuv420p", "-c:a", "aac", out_mp4]
    subprocess.run(cmd, capture_output=True)
    return (out_mp4 if os.path.exists(out_mp4) else None, attribution)

if __name__ == "__main__":
    import sys
    spots = json.load(open("spots_data.json", encoding="utf-8"))
    slug = sys.argv[1] if len(sys.argv) > 1 else "beppu-onsen"
    row = next(x for x in spots if x["slug"] == slug)
    p, attr = build_short(row, f"/tmp/short_{slug}.mp4")
    print("生成:", p, "| 長さ", round(_dur(p), 1) if p else "-", "秒")
    print("出典:", attr)
