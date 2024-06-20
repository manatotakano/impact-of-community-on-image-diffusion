def create_database_and_tables(db_config):
    # データベース作成
    conn = mysql.connector.connect(
        host=db_config["host"],
        user=db_config["user"],
        password=db_config["password"]
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS flickr_SQL")
    cursor.close()
    conn.close()

    # MySQLに再接続
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # テーブル作成のクエリ
    create_table_queries = [
        """
        CREATE TABLE IF NOT EXISTS photo (
            id INT AUTO_INCREMENT PRIMARY KEY,
            photo_id VARCHAR(255) NOT NULL,
            owner_id VARCHAR(255) NOT NULL,
            title VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            dateupload INT NOT NULL,
            views INT NOT NULL,
            count_faves INT NOT NULL,
            tags TEXT NOT NULL,
            latitude DOUBLE NOT NULL,
            longitude DOUBLE NOT NULL,
            url_n VARCHAR(255) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS user (
            id INT AUTO_INCREMENT PRIMARY KEY,
            user_id VARCHAR(255) NOT NULL,
            username VARCHAR(255) NOT NULL,
            location VARCHAR(255),
            description TEXT,
            firstdatetaken TEXT,
            firstdate INT,
            photos_count INT,
            photo_id VARCHAR(255),
            title VARCHAR(255),
            tags TEXT,
            url_n VARCHAR(255)
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS favorite (
            id INT AUTO_INCREMENT PRIMARY KEY,
            owner_id VARCHAR(255) NOT NULL,
            photo_id VARCHAR(255) NOT NULL,
            user_id VARCHAR(255) NOT NULL,
            favedate INT NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS comment (
            id INT AUTO_INCREMENT PRIMARY KEY,
            owner_id VARCHAR(255) NOT NULL,
            photo_id VARCHAR(255) NOT NULL,
            user_id VARCHAR(255) NOT NULL,
            datecreate INT NOT NULL,
            comment_content TEXT NOT NULL
        )
        """
    ]

    for query in create_table_queries:
        cursor.execute(query)

    cursor.close()
    conn.close()