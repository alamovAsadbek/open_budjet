import hashlib

from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminUsersPageAdmin:
    @log_decorator
    def show_all_users(self):
        pagination = Pagination(table_name='users', table_keys=['id', 'first_name', 'last_name', 'email', 'created_at'],
                                display_keys=['ID', 'First name', 'Last name', 'Email', 'Registered'])
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def update_user(self) -> bool:
        print(color_text('Waiting...', 'cyan'))
        if not self.show_all_users():
            return False
        user_id: int = int(input('Enter user ID: ').strip())
        print(color_text("Checked...", 'cyan'))
        query = '''
        SELECT * FROM users WHERE id=%s;
        '''
        result_get = execute_query(query, (user_id,), 'one')
        if result_get is None:
            print(color_text('User not found', 'yellow'))
            return False
        password = hashlib.sha256(input("Enter password").strip().encode('utf-8')).hexdigest()
