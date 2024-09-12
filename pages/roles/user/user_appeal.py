from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class UserAppealPageUser:
    @log_decorator
    def get_category(self):
        print(color_text('Waiting...', 'cyan'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'],
                                display_keys=['ID', 'Name'])
        pagination.page_tab()
        category_id: int = int(input("Enter the category ID or enter 0 to exit: ").strip())
        if category_id == 0:
            return False
        print(color_text('Checked...', 'cyan'))
        query = '''
        SELECT * FROM categories WHERE ID=%s;
        '''
        result_get = execute_query(query, (category_id,), 'one')
        return result_get

    @log_decorator
    def switch_region(self) -> bool or list:
        print(color_text("Switch region", color='blue'))
        pagination = Pagination(table_name='regions', table_keys=['id', 'name'],
                                display_keys=["ID", "Region Name"])
        if not pagination.page_tab():
            print("Region not found")
            return False
        region_id: int = int(input("Enter region ID: ").strip())
        print(color_text("Checked...", color='cyan'))
        query = '''
            SELECT * FROM regions WHERE id=%s;
            '''
        result_get = execute_query(query, (region_id,), fetch='one')
        return result_get

    @log_decorator
    def send_request(self):
        get_category = self.get_category()
        if get_category is None or get_category is False:
            print(color_text('Category not found', 'red'))
            return False
        get_region = self.switch_region()
        if get_region is None or get_region is False:
            print(color_text('Region not found', 'red'))
            return False
