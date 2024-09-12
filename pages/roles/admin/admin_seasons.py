from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminSeasonsPageAdmin:
    @log_decorator
    def check_seasons(self):
        pass

    @log_decorator
    def get_categories(self):
        query = '''
        SELECT * FROM categories WHERE status=TRUE;
        '''
        result_get = execute_query(query, fetch='all')
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
        result_get = execute_query(query, (region_id,))
        if result_get is None:
            print("Region not found")
            return False
        return result_get

    @log_decorator
    def create_seasons(self):
        print(color_text('Waiting...', color='cyan'))
        print(color_text('Check out the first categories to create a new season. Then the categories cannot be changed',
                         color='yellow', is_bold=True))
        all_categories = self.get_categories()
        if all_categories is None or len(all_categories) == 0:
            print(color_text('There are no categories', color='yellow', is_bold=True))
            return False
        print(all_categories)
