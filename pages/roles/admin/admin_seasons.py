from components.color_text.color_text import color_text
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
    def create_seasons(self):
        print(color_text('Waiting...', color='cyan'))
        all_categories = self.get_categories()
