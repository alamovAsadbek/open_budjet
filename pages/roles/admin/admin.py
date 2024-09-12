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
    def create_new_season(self):
        pass

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
    # /category menu
