from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminSeasonsPageAdmin:
    @log_decorator
    def check_seasons(self):
        pass

    @log_decorator
    def get_categories(self):
        query = '''
        SELECT * FROM categories;
        '''
        result_get = execute_query(query, fetch='all')
        return result_get

    @log_decorator
    def create_seasons(self):
        pass
