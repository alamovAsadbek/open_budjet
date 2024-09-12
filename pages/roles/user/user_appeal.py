from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class UserAppealPageUser:
    @log_decorator
    def get_category(self):
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'],
                                display_keys=['ID', 'Name'])
        pagination.page_tab()
        category_id: int = int(input("Enter the category ID: ").strip())
        print(color_text('Checked...', 'cyan'))

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
        if result_get is None:
            print("Region not found")
            return False
        return result_get

    @log_decorator
    def send_request(self):
        pass
