# ドコリアル SNS自動投稿システム

155スポットを弾に、毎日 JST 8:00 / 19:00 に各SNSへ**完全自動投稿**する仕組み。
太田さんの作業は「初回のアカウント作成＋APIキー登録」だけ。以降は無人で回ります。

## 仕組み
```
GitHub Actions (cron 1日2回)
  → build_queue.py   155スポットから投稿データ生成
  → post.py          ローテーションで本日分を選択 → キャプション生成 → 各SNSへ投稿
  → state.json       ローテ位置を自動記録（次回は続きから）
```
- **キーを登録した媒体だけ**が自動で稼働（未登録は自動スキップ）。1媒体ずつ足せる。
- **フィード投稿（X/Threads/Instagram）**：ロゴ＋テキストの自前ブランドカード（`cards/`）＝第三者写真不使用で著作権クリーン。`https://dokoriaru.com/sns/cards/{slug}.jpg` で公開（IG/Threadsが参照）。
- **Short動画（TikTok/YouTube Shorts）**：`video.py` が自動生成。
  - Wikimedia Commonsの**その場所の実写**（CC/パブリックドメインのみ・出典を概要欄へ自動記載）
  - **AI音声ナレーション**（edge-tts / ja-JP-NanamiNeural・キー不要）＋フレーズ実測の**同期字幕**を焼き込み
  - 冒頭フック＋スポット名＋ブランドEndカード。実写が乏しいスポットはブランドカードで代替。

## 太田さんの作業：APIキーを GitHub Secrets に登録
リポジトリ **ota1014/doko-real** → Settings → Secrets and variables → Actions → New repository secret
下表の名前で登録すれば、その媒体が翌回から自動投稿を開始します。

### X（旧Twitter）★最優先・完全自動対応
1. @dokoriaru 等でアカウント作成
2. https://developer.x.com で開発者登録 → App作成 → 権限を **Read and Write** に
3. 以下4つを取得して登録：
   - `X_API_KEY` / `X_API_SECRET`（API Key/Secret）
   - `X_ACCESS_TOKEN` / `X_ACCESS_SECRET`（Access Token/Secret）

### Threads ★完全自動対応・無料
1. Instagram/Threadsアカウント作成（下のIGと共通でOK）
2. https://developers.facebook.com でMetaアプリ作成 → Threads API追加
3. 取得して登録：`THREADS_USER_ID` / `THREADS_TOKEN`（長期トークン）

### Instagram ★プロアカウント必須
1. Instagramを**プロ（ビジネス/クリエイター）**に切替 → Facebookページと連携
2. Metaアプリで `instagram_content_publish` 権限を有効化（アプリ審査が必要）
3. 取得して登録：`IG_USER_ID` / `IG_TOKEN`

### TikTok ▲下書きまで自動（本公開はアプリ審査後）
1. @dokoriaru でアカウント作成
2. https://developers.tiktok.com でアプリ作成 → Content Posting API有効化
3. 取得して登録：`TIKTOK_TOKEN`
   - ※審査前は「下書き（インボックス）」までの自動化。アプリ審査を通すと自動本公開に切替可能。

### YouTube Shorts ▲自前スライドショー動画を自動生成して投稿
1. ドコリアルのYouTubeチャンネル作成
2. Google Cloudで YouTube Data API v3 有効化 → OAuth同意画面 → クライアント作成
3. リフレッシュトークンを取得して登録：`YT_CLIENT_ID` / `YT_CLIENT_SECRET` / `YT_REFRESH_TOKEN`

## 動作確認・運用
- 手動テスト：Actions タブ → 「ドコリアル SNS自動投稿」→ Run workflow → dry_run=true（実投稿せずキャプション確認）
- 投稿頻度の変更：`sns/config.json` の `posts_per_run`、cron時刻は `.github/workflows/sns-auto.yml`
- 文言・ハッシュタグ調整：`sns/captions.py`／カードの見た目：`sns/assets.py`
- スポット追加時：`python3 sns/build_queue.py && python3 sns/build_cards.py` で弾とカードを最新化

## 現実的な期待値
自動投稿は初速が遅く（新規アカウントはフォロワー週数人〜）、SNS単体で集客が跳ねる例は稀です。
**主力はSEO（155ページ）、SNSは回遊導線と指名検索の底上げ**という位置づけが現実的。
まずX＋Threads（月¥0）で基盤を作り、反応を見てInstagram/TikTok/Shortsへ拡張するのが費用対効果的です。
