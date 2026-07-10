# -*- coding: utf-8 -*-
"""
各SNSへの投稿関数。すべて (status, detail) を返す:
  status = "ok" | "skip"（キー未設定）| "error"
環境変数(GitHub Secrets)が無い媒体は自動でskip → キーを足した媒体から順に稼働。
外部ライブラリはこの中でだけimportする（未インストールでも他媒体は動く）。
"""
import os, json, time
import urllib.request, urllib.parse

def _env(*names):
    vals = [os.environ.get(n, "").strip() for n in names]
    return vals if all(vals) else None

# ---------------- X (旧Twitter) ----------------
def post_x(caption, card_path=None, **_):
    creds = _env("X_API_KEY", "X_API_SECRET", "X_ACCESS_TOKEN", "X_ACCESS_SECRET")
    if not creds:
        return ("skip", "X_* キー未設定")
    try:
        import tweepy
        ck, cs, at, ats = creds
        media_ids = None
        if card_path and os.path.exists(card_path):
            auth = tweepy.OAuth1UserHandler(ck, cs, at, ats)
            api = tweepy.API(auth)
            media_ids = [api.media_upload(card_path).media_id_string]
        client = tweepy.Client(consumer_key=ck, consumer_secret=cs,
                               access_token=at, access_token_secret=ats)
        r = client.create_tweet(text=caption, media_ids=media_ids)
        return ("ok", str(r.data.get("id")))
    except Exception as e:
        return ("error", f"{type(e).__name__}: {e}")

# ---------------- Threads (Meta) ----------------
def post_threads(caption, card_url=None, **_):
    creds = _env("THREADS_USER_ID", "THREADS_TOKEN")
    if not creds:
        return ("skip", "THREADS_* キー未設定")
    uid, token = creds
    base = f"https://graph.threads.net/v1.0/{uid}"
    try:
        params = {"access_token": token, "text": caption}
        if card_url:
            params.update({"media_type": "IMAGE", "image_url": card_url})
        else:
            params["media_type"] = "TEXT"
        cid = _post_json(f"{base}/threads", params)["id"]
        time.sleep(3)  # コンテナ処理待ち
        pid = _post_json(f"{base}/threads_publish",
                         {"access_token": token, "creation_id": cid})["id"]
        return ("ok", str(pid))
    except Exception as e:
        return ("error", f"{type(e).__name__}: {e}")

# ---------------- Instagram (Graph API) ----------------
def post_instagram(caption, card_url=None, **_):
    creds = _env("IG_USER_ID", "IG_TOKEN")
    if not creds:
        return ("skip", "IG_* キー未設定")
    if not card_url:
        return ("skip", "IGは公開画像URLが必須（カード未生成）")
    uid, token = creds
    base = f"https://graph.facebook.com/v21.0/{uid}"
    try:
        cid = _post_json(f"{base}/media",
                         {"access_token": token, "image_url": card_url, "caption": caption})["id"]
        time.sleep(5)
        pid = _post_json(f"{base}/media_publish",
                         {"access_token": token, "creation_id": cid})["id"]
        return ("ok", str(pid))
    except Exception as e:
        return ("error", f"{type(e).__name__}: {e}")

# ---------------- TikTok (Content Posting API) ----------------
def post_tiktok(caption, video_path=None, **_):
    creds = _env("TIKTOK_TOKEN")
    if not creds:
        return ("skip", "TIKTOK_TOKEN 未設定")
    if not (video_path and os.path.exists(video_path)):
        return ("skip", "動画未生成（ffmpeg/フォント要）")
    token = creds[0]
    try:
        # 監査前アプリは下書き(インボックス)投稿まで。監査後にDirect Post可。
        init = _post_json(
            "https://open.tiktokapis.com/v2/post/publish/inbox/video/init/",
            None, headers={"Authorization": f"Bearer {token}",
                           "Content-Type": "application/json"},
            body=json.dumps({"source_info": {
                "source": "FILE_UPLOAD",
                "video_size": os.path.getsize(video_path),
                "chunk_size": os.path.getsize(video_path),
                "total_chunk_count": 1}}).encode())
        upload_url = init["data"]["upload_url"]
        with open(video_path, "rb") as f:
            data = f.read()
        req = urllib.request.Request(upload_url, data=data, method="PUT",
            headers={"Content-Type": "video/mp4",
                     "Content-Range": f"bytes 0-{len(data)-1}/{len(data)}"})
        urllib.request.urlopen(req, timeout=120)
        return ("ok", "draft:" + init["data"].get("publish_id", "uploaded"))
    except Exception as e:
        return ("error", f"{type(e).__name__}: {e}")

# ---------------- YouTube (Data API v3) ----------------
def post_youtube(meta, video_path=None, **_):
    creds = _env("YT_CLIENT_ID", "YT_CLIENT_SECRET", "YT_REFRESH_TOKEN")
    if not creds:
        return ("skip", "YT_* キー未設定")
    if not (video_path and os.path.exists(video_path)):
        return ("skip", "動画未生成（ffmpeg/フォント要）")
    cid, cs, rt = creds
    try:
        from google.oauth2.credentials import Credentials
        from googleapiclient.discovery import build
        from googleapiclient.http import MediaFileUpload
        c = Credentials(None, refresh_token=rt, client_id=cid, client_secret=cs,
                        token_uri="https://oauth2.googleapis.com/token")
        yt = build("youtube", "v3", credentials=c)
        body = {"snippet": {"title": meta["title"][:100], "description": meta["description"],
                            "categoryId": "19"},
                "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False}}
        req = yt.videos().insert(part="snippet,status", body=body,
                                 media_body=MediaFileUpload(video_path))
        return ("ok", req.execute().get("id"))
    except Exception as e:
        return ("error", f"{type(e).__name__}: {e}")

# ---------------- helper ----------------
def _post_json(url, params, headers=None, body=None):
    if params is not None:
        data = urllib.parse.urlencode(params).encode()
        req = urllib.request.Request(url, data=data)
    else:
        req = urllib.request.Request(url, data=body)
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode())

POSTERS = {
    "x": post_x, "threads": post_threads, "instagram": post_instagram,
    "tiktok": post_tiktok, "youtube": post_youtube,
}
