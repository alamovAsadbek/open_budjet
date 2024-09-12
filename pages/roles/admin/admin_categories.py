import threading

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
        print("Category created successfully")
        return True

    @log_decorator
    def update_category(self) -> bool:
        pass

    @log_decorator
    def show_all_categories(self) -> bool:
        pass
