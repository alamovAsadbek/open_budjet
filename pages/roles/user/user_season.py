from components.color_text.color_text import color_text
from main_files.database.db_setting import execute_query, get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserSeason:
    @log_decorator
    def get_active_appeal(self):
        query = '''
        SELECT a.id          as a_id,
           a.name        as a_name,
           a.description as a_description,
           a.price       as a_price,
           c.name        as category_name,
           r.name        as region_name,
           d.name        as districts_name,
           s.name        as season_name,
           s.status      as season_status,
           s.created_at  as season_created
        FROM appeals a
                 inner join categories c on c.ID = a.CATEGORY_ID
                 inner join districts d on a.DISTRICTS_ID = d.ID
                 inner join regions r on d.REGION_ID = r.ID
                 inner join SEASONS S on S.ID = a.SEASONS_ID
        WHERE a.user_id = '%s' and s.status = 'vote';
        '''
        params = (get_active_user()['id'],)
        result = execute_query(query, params, fetch='one')
        return result

    @log_decorator
    def voting_user(self):
        get_active_appeal=self.get_active_appeal()
        if get_active_appeal is None:
            print(color_text(''))
