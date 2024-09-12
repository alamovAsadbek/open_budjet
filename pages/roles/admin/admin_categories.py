import threading

from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminCategoryPageAdmin:
    @log_decorator
    def create_category(self) -> bool:
        name: str = input("Enter category name: ").strip()
        query = '''
        INSERT INTO categories (name) VALUES (%s);
        '''
        threading.Thread(target=execute_query, args=(query, (name,))).start()
        print(color_text("Category created successfully", color='green', is_bold=True))
        return True

    @log_decorator
    def update_category(self) -> bool:
        pass

    @log_decorator
    def show_all_categories(self) -> bool:
        print(color_text("Waiting...", color='cyan'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'],
                                display_keys=['ID', "Name"])
        pagination.page_tab()
        return True
