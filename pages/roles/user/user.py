from main_files.decorator.decorator_func import log_decorator
from pages.roles.user.user_appeal import UserAppealPageUser
from pages.roles.user.user_season import UserSeason


class User:
    def __init__(self):
        self.__appeals_menu = UserAppealPageUser()
        self.__season_menu = UserSeason()

    # appeals menu

    @log_decorator
    def send_request(self) -> bool:
        self.__appeals_menu.send_request()
        return True

    @log_decorator
    def my_request(self) -> bool:
        self.__appeals_menu.my_request()
        return True

    # / appeals menu

    # season menu

    @log_decorator
    def voting_appeal(self) -> bool:
        self.__season_menu.voting_user()
        return True

    # /season menu
