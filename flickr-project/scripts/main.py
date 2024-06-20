
# MySQLデータベース、テーブル作成
create_database_and_tables(db_config)

# Flickr API設定
flickr = FlickrAPI(key, secret, format="parsed-json")

# 取得画像枚数の設定(per_page=任意の枚数)
per_page = 1000
if per_page < 500:
    n_page = 1
else:
    n_page = math.floor(per_page/500) + 1
    per_page = math.floor(per_page / n_page)

# photos.searchの再開位置を取得
start_page = get_last_processed_page()

# 写真情報の取得とデータベースへの挿入
for i in range(n_page):
    response = flickr.photos.search(per_page=per_page,page=i+1,media="photos",sort="interestingness-desc",safe_search=1,extras="views,count_faves,description,date_upload,owner_name,geo,tags,url_n")
    main_photo_count=i+1
    print(f"{main_photo_count}番目の人気写真")
    time.sleep(1)
    # MySQLに接続
    try:
        conn = mysql.connector.connect(**db_config)
        photos = response["photos"]["photo"]
        for photo in photos:
          photo_id = photo["id"]
          owner_id = photo["owner"]
          title = photo["title"]
          description = photo["description"]['_content']
          dateupload = int(photo["dateupload"])
          views = int(photo["views"])
          count_faves = int(photo["count_faves"])
          tags = photo["tags"]
          latitude = float(photo["latitude"])
          longitude = float(photo["longitude"])
          url_n = photo["url_n"]

          # 検索したいphoto_idの値
          search_photo_id = photo_id

          # ユーザーIDが存在しない場合にのみ以降の処理を実行する
          if not check_and_skip_photo_id(conn, search_photo_id):
             insert_data_photo(photo_id, owner_id, title, description, dateupload, views, count_faves, tags, latitude, longitude, url_n)

    finally:
        conn.close()
    # ユーザー情報の取得とデータベースへの挿入
    try:
        # MySQLに接続
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        cursor = conn.cursor()

        # データを取得するクエリ
        query = "SELECT owner_id, photo_id, title, tags, url_n FROM photo"
        cursor.execute(query)
        # 結果をすべてリストに格納
        results = cursor.fetchall()

        last_processed_owner_id = get_last_processed_owner_id()
        skip = last_processed_owner_id is not None

        for (owner_id, photo_id, title, tags, url_n) in results:
            if skip:
                if owner_id == last_processed_owner_id:
                    skip = False
                continue

            try:
                # 検索したいuser_idの値
                search_user_id = owner_id

                # ユーザーIDが存在しない場合にのみ以降の処理を実行する
                if not check_and_skip_user_id(conn, search_user_id):
                    # 写真投稿ユーザ情報
                    response = flickr.people.getInfo(user_id=owner_id)
                    time.sleep(1)
                    person = response["person"]
                    username = person["username"]["_content"]
                    location = person.get("location", {}).get("_content", "None")
                    description = person["description"]["_content"]
                    firstdatetaken = person["photos"]["firstdatetaken"]["_content"]
                    firstdate = int(person["photos"]["firstdate"]["_content"])
                    photos_count = int(person["photos"]["count"]["_content"])

                    insert_data_user(owner_id, username, location, description, firstdatetaken, firstdate, photos_count, photo_id, title, tags, url_n)

                # 進捗を保存
                save_last_processed_owner_id(owner_id)

            except Exception as e:
                # エラー発生時に進捗を保存
                save_last_processed_owner_id(owner_id)
                print(f"Error processing owner_id {owner_id}: {e}")
                continue

    finally:
        cursor.close()
        conn.close()
    # コメント情報の取得とデータベースへの挿入
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        cursor = conn.cursor()

        # データを取得するクエリ
        query = "SELECT photo_id, owner_id FROM photo"
        cursor.execute(query)
        # 結果をすべてリストに格納
        results = cursor.fetchall()
        last_processed_comment_photo_id = get_last_processed_comment_photo_id()
        skip = last_processed_comment_photo_id is not None

        for (photo_id, owner_id) in results:
            if skip:
                if photo_id == last_processed_comment_photo_id:
                    skip = False
                continue

            try:
                # 写真コメントユーザ取得
                response = flickr.photos.comments.getList(photo_id=photo_id)
                time.sleep(1)
                # commentsキーの存在を確認し、コメントがあるかどうかをチェック
                if "comments" in response and "comment" in response["comments"]:
                    comments = response["comments"]["comment"]
                    for comment in comments:
                        author = comment["author"]
                        datecreate = int(comment["datecreate"])
                        comment_content = comment["_content"]

                    insert_data_comment(owner_id, photo_id, author, datecreate, comment_content)

                # 進捗を保存
                save_last_processed_comment_photo_id(photo_id)

            except Exception as e:
                # エラー発生時に進捗を保存
                save_last_processed_comment_photo_id(photo_id)
                print(f"Error processing photo_id {photo_id}: {e}")
                continue

    finally:
        cursor.close()
        conn.close()
    # コメントユーザー情報の取得とデータベースへの挿入
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        cursor = conn.cursor()

        # データを取得するクエリ
        query = "SELECT user_id FROM comment"
        cursor.execute(query)
        # 結果をすべてリストに格納
        results = cursor.fetchall()
        last_processed_author = get_last_processed_author()
        skip = last_processed_author is not None

        for (user_id) in results:
            if skip:
                if user_id == last_processed_author:
                    skip = False
                continue

            try:
                # 検索したいuser_idの値
                search_user_id = user_id

                # ユーザーIDが存在しない場合にのみ以降の処理を実行する
                if not check_and_skip_user_id(conn, search_user_id):
                    # 写真コメントユーザ情報
                    response = flickr.people.getInfo(user_id=search_user_id)
                    time.sleep(1)
                    person = response["person"]
                    username = person["username"]["_content"]
                    location = person.get("location", {}).get("_content", "None")
                    description = person["description"]['_content']
                    firstdatetaken = person.get("firstdatetaken", {}).get("_content", "None")
                    firstdate = int(person.get("firstdate", {}).get("_content", 0))
                    photos_count = int(person["photos"]["count"]['_content'])

                    response = flickr.people.getPhotos(user_id=search_user_id, per_page=1, extras="tags,url_n")
                    time.sleep(1)
                    photos = response.get("photos", {})
                    first_photo = photos.get("photo", [{}])[0]
                    photo_id = first_photo.get("id", "None")
                    title = first_photo.get("title", "None")
                    tags = first_photo.get("tags", "None")
                    url_n = first_photo.get("url_n", "None")

                    insert_data_user(search_user_id, username, location, description, firstdatetaken, firstdate, photos_count, photo_id, title, tags, url_n)

                # 進捗を保存
                save_last_processed_author(search_user_id)

            except Exception as e:
                # エラー発生時に進捗を保存
                save_last_processed_author(search_user_id)
                print(f"Error processing author {search_user_id}: {e}")
                continue

    finally:
        cursor.close()
        conn.close()
    # favorite情報取得とデータベースへの挿入
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        cursor = conn.cursor()

        # データを取得するクエリ
        query = "SELECT photo_id, owner_id, count_faves FROM photo"
        cursor.execute(query)
        # 結果をすべてリストに格納
        results = cursor.fetchall()
        last_processed_favorite_photo_id = get_last_processed_favorite_photo_id()
        skip = last_processed_favorite_photo_id is not None

        for (photo_id, owner_id, count_faves) in results:
            if skip:
                if photo_id == last_processed_favorite_photo_id:
                    skip = False
                continue

            try:
                loop = count_faves // 50 + 1
                # 写真お気に入りユーザ取得
                for i in range(loop):
                    response = flickr.photos.getFavorites(per_page=50, page=i+1, photo_id=photo_id)
                    time.sleep(1)
                    photo = response["photo"]
                    for person in photo["person"]:
                        favorite_id = person["nsid"]
                        favedate = int(person["favedate"])
                        insert_data_favorite(owner_id, photo_id, favorite_id, favedate)

                # 進捗を保存
                save_last_processed_favorite_photo_id(photo_id)

            except Exception as e:
                # エラー発生時に進捗を保存
                save_last_processed_favorite_photo_id(photo_id)
                print(f"Error processing photo_id {photo_id}: {e}")
                continue

    finally:
        cursor.close()
        conn.close()
     # favoriteユーザー情報の取得とデータベースへの挿入
    try:
        conn = mysql.connector.connect(
            host=db_config["host"],
            user=db_config["user"],
            password=db_config["password"],
            database=db_config["database"]
        )
        cursor = conn.cursor()

        # データを取得するクエリ
        query = "SELECT user_id FROM favorite"
        cursor.execute(query)
        # 結果をすべてリストに格納
        results = cursor.fetchall()
        last_processed_favorite_id = get_last_processed_favorite_id()
        skip = last_processed_favorite_id is not None

        for (user_id) in results:
            if skip:
                if user_id == last_processed_favorite_id:
                    skip = False
                continue

            try:
                # 検索したいuser_idの値
                search_user_id = user_id

                # ユーザーIDが存在しない場合にのみ以降の処理を実行する
                if not check_and_skip_user_id(conn, search_user_id):
                    # 写真お気に入りユーザ情報
                    response = flickr.people.getInfo(user_id=search_user_id)
                    time.sleep(1)
                    person = response["person"]
                    username = person["username"]["_content"]
                    location = person.get("location", {}).get("_content", "None")
                    description = person["description"]["_content"]
                    firstdatetaken = person.get("firstdatetaken", {}).get("_content", "None")
                    firstdate = int(person.get("firstdate", {}).get("_content", 0))
                    photos_count = int(person["photos"]["count"]["_content"])

                    response = flickr.people.getPhotos(user_id=search_user_id, per_page=1, extras="tags,url_n")
                    time.sleep(1)
                    photos = response.get("photos", {})
                    first_photo = photos.get("photo", [{}])[0]
                    photo_id = first_photo.get("id", "None")
                    title = first_photo.get("title", "None")
                    tags = first_photo.get("tags", "None")
                    url_n = first_photo.get("url_n", "None")

                    insert_data_user(search_user_id, username, location, description, firstdatetaken, firstdate, photos_count, photo_id, title, tags, url_n)

                # 進捗を保存
                save_last_processed_favorite_id(search_user_id)

            except Exception as e:
                # エラー発生時に進捗を保存
                save_last_processed_favorite_id(search_user_id)
                print(f"Error processing favorite_id {search_user_id}: {e}")
                continue

    finally:
        cursor.close()
        conn.close()