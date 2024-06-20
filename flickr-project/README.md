# Flickr Data Collection

このプロジェクトは、SNS の画像拡散にコミュニティが及ぼす影響を調査する前段階として、 Flickr からデータを収集し、MySQL データベースに保存することを目的として開発されました。

## Project Behavior

1. MySQL に FlickrAPI から収集したデータを保存するテーブル、クエリを作成します。
2. 写真情報の取得＆保存
   FlickrAPI で人気順にソートされた写真情報を取得します。
   作成されたテーブル photo に写真情報を保存します。
3. 写真投稿ユーザー情報の取得＆保存
   テーブル photo から、画像を投稿した全てのユーザー ID を取得します。
   FlickrAPI でユーザー情報を取得します。
   作成されたテーブル user にユーザー情報を保存します。
4. 写真コメント情報の取得＆保存
   テーブル photo から、投稿された写真 ID を取得します。
   FlickrAPI でそれぞれの投稿に対する全てのコメント情報を取得します。
   作成されたテーブル comment にコメント情報を保存します。
5. 写真コメントユーザー情報の取得＆保存
   テーブル comment から、コメントを投稿した全てのユーザー ID を取得します。
   FlickrAPI でユーザー情報とユーザーが過去に投稿した画像を取得します。
   作成されたテーブル user にユーザー情報を保存します。
6. 写真 favorite 情報の取得＆保存
   テーブル photo から、投稿された写真 ID を取得します。
   FlickrAPI でそれぞれの投稿に対する全ての favorite 情報を取得します。
   作成されたテーブル favorite に favorite 情報を保存します。
7. 写真 favorite ユーザー情報の取得＆保存
   テーブル favorite から、favorite を押した全てのユーザー ID を取得します。
   FlickrAPI でユーザー情報とユーザーが過去に投稿した画像を取得します。
   作成されたテーブル user にユーザー情報を保存します。

## Project Structure

- `/scripts` :Python スクリプト用ディレクトリ
- `/config` : 設定ファイルのディレクトリ

## Setup

1. 必要なパッケージをインストールします。:

   ```sh
   pip install -r requirements.txt
   ```

2. `config/config.py`で detabase と API キーを設定します。

3. create_tables_sql script を実行します。:
   ```sh
   scripts/create_tables_sql.py
   ```
4. insert script を実行します。:
   ```sh
   scripts/insert.py
   ```
5. cheak_abd_skip script を実行します。:
   ```sh
   scripts/cheak_abd_skip.py
   ```
6. last_processed script を実行します。:
   ```sh
   scripts/last_processed.py
   ```
7. main script を実行します。:

   ```sh
   scripts/main.py
   ```

## Requirements

- Python 3.8+
- MySQL
