import mysql.connector,os,sys,config
# プロジェクトのルートディレクトリを追加
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
db_config = config.db_config
# photoデータ挿入関数
def insert_data_photo(photo_id, owner_id, title, description, dateupload, views, count_faves, tags, latitude, longitude, url_n):
    try:
        # MySQLに接続
        conn = mysql.connector.connect(**db_config)

        # カーソルを取得
        cursor = conn.cursor()

        # データ挿入のクエリ
        insert_data_photo_query = """
        INSERT INTO photo (
            photo_id,
            owner_id,
            title,
            description,
            dateupload,
            views,
            count_faves,
            tags,
            latitude,
            longitude,
            url_n
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        # データ挿入
        photo_data = (photo_id, owner_id, title, description, dateupload, views, count_faves, tags, latitude, longitude, url_n)
        cursor.execute(insert_data_photo_query, photo_data)

        # 変更を確定
        conn.commit()
        cursor.close()
        conn.close()

        print("photoデータが正常に挿入されました。")

    except Exception as e:
        print("photoデータ挿入中にエラーが発生しました:", e)
# userデータ挿入関数
def insert_data_user(owner_id,username,location,description,firstdatetaken,firstdate,photos_count,photo_id,title,tags,url_n):
    try:
        # MySQLに接続
        conn = mysql.connector.connect(**db_config)

        # カーソルを取得
        cursor = conn.cursor()
        # データ挿入のクエリ

        insert_data_user_query = """
        INSERT INTO user (
          user_id,
          username,
          location,
          description,
          firstdatetaken,
          firstdate,
          photos_count,
          photo_id,
          title,
          tags,
          url_n
          )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
          """

        # データ挿入
        user_data = (owner_id,username,location,description,firstdatetaken,firstdate,photos_count,photo_id,title,tags,url_n)
        cursor.execute(insert_data_user_query, user_data)

        # 変更を確定
        conn.commit()
        cursor.close()
        conn.close()

        print("userデータが正常に挿入されました。")

    except Exception as e:
        print("userデータ挿入中にエラーが発生しました:", e)
# commentデータ挿入関数
def insert_data_comment(owner_id,photo_id,user_id,datecreate,comment_content):
    try:
        # MySQLに接続
        conn = mysql.connector.connect(**db_config)

        # カーソルを取得
        cursor = conn.cursor()
        # データ挿入のクエリ
        insert_data_comment_query = """
        INSERT INTO comment (
            owner_id,
            photo_id,
            user_id,
            datecreate,
            comment_content
             )
        VALUES (%s,%s,%s,%s,%s)
        """

        # データ挿入
        comment_data = (owner_id,photo_id,user_id,datecreate,comment_content)
        cursor.execute(insert_data_comment_query, comment_data)

        # 変更を確定
        conn.commit()
        cursor.close()
        conn.close()

        print("commentデータが正常に挿入されました。")

    except Exception as e:
        print("commentデータ挿入中にエラーが発生しました:", e)
# favoriteデータ挿入関数
def insert_data_favorite(owner_id,photo_id,user_id,favedate):
    try:
        # MySQLに接続
        conn = mysql.connector.connect(**db_config)

        # カーソルを取得
        cursor = conn.cursor()

        # データ挿入のクエリ
        insert_data_favorite_query = """
        INSERT INTO favorite (
            owner_id,
            photo_id,
            user_id,
            favedate
        )
        VALUES (%s,%s,%s,%s)
        """

        # データ挿入
        favorite_data = (owner_id,photo_id,user_id,favedate)
        cursor.execute(insert_data_favorite_query, favorite_data)

        # 変更を確定
        conn.commit()
        cursor.close()
        conn.close()

        print("favoriteデータが正常に挿入されました。")

    except Exception as e:
        print("favoriteデータ挿入中にエラーが発生しました:", e)

