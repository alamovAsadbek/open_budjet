from components.color_text.color_text import color_text
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class UserSeason:
    @log_decorator
    def get_active_season(self):
        query = '''
        SELECT * FROM seasons WHERE status='vote';
        '''
        result = execute_query(query, fetch='one')
        return result

    @log_decorator
    def voting_user(self):
        get_active_season = self.get_active_season()
        if get_active_season is None:
            print(color_text('Active season not found', 'yellow'))
            return False
