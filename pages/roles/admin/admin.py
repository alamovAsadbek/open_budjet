from main_files.decorator.decorator_func import log_decorator
from pages.roles.admin.admin_appeals import AdminAppealsPageAdmin
from pages.roles.admin.admin_categories import AdminCategoryPageAdmin
from pages.roles.admin.admin_seasons import AdminSeasonsPageAdmin
from pages.roles.admin.admin_users import AdminUsersPageAdmin


class Admin:
    def __init__(self):
        self.__season_menu = AdminSeasonsPageAdmin()
        self.__appeals_menu = AdminAppealsPageAdmin()
        self.__categories_menu = AdminCategoryPageAdmin()
        self.__users_menu = AdminUsersPageAdmin()

    # season menu
    @log_decorator
    def create_new_season(self) -> bool:
        self.__season_menu.create_seasons()
        return True

    @log_decorator
    def update_season_status(self) -> bool:
        self.__season_menu.update_status()
        return True

    @log_decorator
    def show_all_seasons(self) -> bool:
        self.__season_menu.show_all_seasons()
        return True

    @log_decorator
    def show_statistics(self) -> bool:
        self.__season_menu.show_all_statistics()
        return True

    # / season menu

    # category menu

    @log_decorator
    def create_new_category(self) -> bool:
        self.__categories_menu.create_category()
        return True

    @log_decorator
    def show_all_categories(self) -> bool:
        self.__categories_menu.show_all_categories()
        return True

    @log_decorator
    def update_category(self) -> bool:
        self.__categories_menu.update_category()
        return True

    @log_decorator
    def delete_category(self) -> bool:
        self.__categories_menu.delete_category()
        return True

    # /category menu

    # users menu
    @log_decorator
    def show_all_users(self) -> bool:
        self.__users_menu.show_all_users()
        return True

    @log_decorator
    def update_users(self) -> bool:
        self.__users_menu.update_user()
        return True

    @log_decorator
    def delete_user(self) -> bool:
        self.__users_menu.delete_user()
        return True

    # / users menu

    # appeals menu

    @log_decorator
    def rejecting_appeals(self) -> bool:
        self.__appeals_menu.rejecting_appeals()
        return True

    @log_decorator
    def approved_appeals(self):
        self.__appeals_menu.approved_appeals()
        return True

    @log_decorator
    def accepting_application(self):
        self.__appeals_menu.accepting_application()
        return True
    # / appeals menu
