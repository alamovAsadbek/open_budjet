from main_files.database.db_setting import get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserProfile:
    def __init__(self):
        self.__active_user = get_active_user()

    @log_decorator
    def show_profile(self) -> bool:
        print(self.__active_user)
        return True
