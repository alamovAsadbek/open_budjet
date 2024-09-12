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
        self.show_all_categories()
        category_id: int = int(input("Enter category id: ").strip())
        print(color_text("Waiting...", color='cyan', is_bold=True))
        query = '''
        SELECT * FROM categories WHERE id=%s;
        '''
        result_get = execute_query(query, (category_id,))
        if result_get is None:
            print(color_text("Category not found", color='yellow', is_bold=True))

    @log_decorator
    def show_all_categories(self) -> bool:
        print(color_text("Waiting...", color='cyan'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'],
                                display_keys=['ID', "Name"])
        if not pagination.page_tab():
            return False
        return True
