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
        if not self.show_all_categories():
            return False
        category_id: int = int(input("Enter category id or type 0 to exit: ").strip())
        if category_id == 0:
            print("Exit")
            return True
        print(color_text("Waiting...", color='cyan', is_bold=True))
        query = '''
        SELECT * FROM categories WHERE id=%s;
        '''
        result_get = execute_query(query, (category_id,), fetch='one')
        if result_get is None:
            print(color_text("Category not found", color='yellow', is_bold=True))
            return False
        print(f"\nCategory ID: {result_get['id']}\nCategory name: {result_get['name']}\n")
        name: str = input("Enter category new name: ").strip()
        query = '''
        UPDATE categories SET name=%s WHERE id=%s;
        '''
        threading.Thread(target=execute_query, args=(query, (name, result_get['id']))).start()
        print(color_text("Category updated successfully", color='green', is_bold=True))
        return True

    @log_decorator
    def show_all_categories(self) -> bool:
        print(color_text("Waiting...", color='cyan'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'],
                                display_keys=['ID', "Name"])
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def delete_category(self) -> bool:
        if not self.show_all_categories():
            return False
        category_id: int = int(input("Enter category id or type 0 to exit: ").strip())
        if category_id == 0:
            print("Exit")
            return True
        print(color_text("Waiting...", color='cyan'))
        query = '''
        SELECT * FROM categories WHERE id=%s;
        '''
        result_get = execute_query(query, (category_id,), fetch='one')
        if result_get is None:
            print(color_text("Category not found", color='yellow', is_bold=True))
            return False
        print(f"\nCategory ID: {result_get['id']}\nCategory name: {result_get['name']}\n")
        confirm_delete: str = input("Are you sure you want to delete this category? (y/n): ").strip().lower()
        if confirm_delete == 'y':
            query = '''
            DELETE FROM categories WHERE id=%s;
            '''
            threading.Thread(target=execute_query, args=(query, (category_id,))).start()
            print(color_text("Deleting category successfully", color='green', is_bold=True))
        elif confirm_delete == 'n':
            print(color_text("Deleting category not found", color='magenta', is_bold=True))
        else:
            print(color_text("Wrong input", color='yellow', is_bold=True))
        return True
