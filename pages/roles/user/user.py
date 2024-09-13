from main_files.decorator.decorator_func import log_decorator
from pages.roles.user.user_appeal import UserAppealPageUser


class User:
    def __init__(self):
        self.__appeals_menu = UserAppealPageUser()

    # appeals menu

    @log_decorator
    def send_request(self) -> bool:
        self.__appeals_menu.send_request()
        return True

    @log_decorator
    def my_request(self) -> bool:
        pass
    # / appeals menu
