import os
# photo_searchの再開位置を取得する関数
def get_last_processed_page():
    progress_file = "progress_photo_search.txt"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return int(f.read().strip())
    return 1  # 初回は1ページ目から
# photo_searchの再開位置を保存する関数
def save_last_processed_page(page):
    progress_file = "progress_photo_search.txt"
    with open(progress_file, "w") as f:
        f.write(str(page))
# people_getInfoの再開位置を取得する関数
def get_last_processed_owner_id():
    progress_file = "progress_owner_id.txt"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return f.read().strip()
# people.getInfoの再開位置を保存する関数
def save_last_processed_owner_id(owner_id):
    progress_file = "progress_owner_id.txt"
    with open(progress_file, "w") as f:
        f.write(str(owner_id))
    return None
# comment_searchの再開位置を取得する関数
def get_last_processed_comment_photo_id():
    progress_file = "progress_comment_photo_id.txt"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return f.read().strip()
    return None
# comment_searchの再開位置を保存する関数
def save_last_processed_comment_photo_id(photo_id):
    progress_file = "progress_comment_photo_id.txt"
    with open(progress_file, "w") as f:
        f.write(str(photo_id))
# people.getInfo(コメント)の再開位置を取得する関数
def get_last_processed_author():
    progress_file = "progress_author.txt"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return f.read().strip()
    return None
# people.getInfo(コメント)の再開位置を保存する関数
def save_last_processed_author(author):
    progress_file = "progress_author.txt"
    with open(progress_file, "w") as f:
        f.write(str(author))
# favorite_searchの再開位置を取得する関数
def get_last_processed_favorite_photo_id():
    progress_file = "progress_favorite_photo_id.txt"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return f.read().strip()
    return None
# favorite_searchの再開位置を保存する関数
def save_last_processed_favorite_photo_id(photo_id):
    progress_file = "progress_favorite_photo_id.txt"
    with open(progress_file, "w") as f:
        f.write(str(photo_id))
# people.getInfo(favorite)の再開位置を取得する関数
def get_last_processed_favorite_id():
    progress_file = "progress_favorite_id.txt"
    if os.path.exists(progress_file):
        with open(progress_file, "r") as f:
            return f.read().strip()
    return None
# people.getInfo(favorite)の再開位置を保存する関数
def save_last_processed_favorite_id(favorite_id):
    progress_file = "progress_favorite_id.txt"
    with open(progress_file, "w") as f:
        f.write(str(favorite_id))
