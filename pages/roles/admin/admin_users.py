from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.decorator.decorator_func import log_decorator


class AdminUsersPageAdmin:
    @log_decorator
    def show_all_users(self):
        pass

    @log_decorator
    def update_users(self) -> bool:
        print(color_text('Waiting...', 'cyan'))
        pagination = Pagination(table_name='users', table_keys=['id', 'first_name', 'last_name', 'email', 'created_at'],
                                display_keys=['ID', 'First name', 'Last name', 'Email', 'Registered'])
        if not pagination.page_tab():
            return False
