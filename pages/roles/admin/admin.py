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
