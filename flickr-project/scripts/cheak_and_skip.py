#user_idスキップチェック関数
def check_and_skip_user_id(connection, search_user_id):
    try:
        # カーソルを取得
        cursor = connection.cursor()

        # SQLクエリの実行
        query = """
        SELECT COUNT(*) AS count_user_id
        FROM user
        WHERE user_id = %s
        """
        cursor.execute(query, (search_user_id,))

        # 結果の取得
        result = cursor.fetchone()

        # カーソルをクローズ
        cursor.close()

        # ユーザーIDが存在する場合
        if result[0] > 0:
            print("既に登録されたUser IDのため、スキップ")
            return True
        else:
            return False  # ユーザーIDが存在しない場合

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return False  # エラーが発生した場合
#photo_idスキップチェック関数
def check_and_skip_photo_id(connection, search_photo_id):
    try:
        # カーソルを取得
        cursor = connection.cursor()

        # SQLクエリの実行
        query = """
        SELECT COUNT(*) AS count_photo_id
        FROM photo
        WHERE photo_id = %s
        """
        cursor.execute(query, (search_photo_id,))

        # 結果の取得
        result = cursor.fetchone()

        # カーソルをクローズ
        cursor.close()

        # ユーザーIDが存在する場合
        if result[0] > 0:
            print("既に登録されたphoto IDのため、スキップ")
            return True
        else:
            return False  # ユーザーIDが存在しない場合

    except mysql.connector.Error as err:
        print("Error: {}".format(err))
        return False  # エラーが発生した場合