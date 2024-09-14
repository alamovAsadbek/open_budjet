from main_files.database.db_setting import get_active_user


class UserProfile:
    def __init__(self):
        self.__active_user = get_active_user()
