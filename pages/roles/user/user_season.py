from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
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
    def switch_category(self):
        print(color_text('Switch category', 'magenta'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'], display_keys=['ID', 'Name'])
        if not pagination.page_tab():
            return False
        category_id: int = int(input("Enter the category ID: ").strip())
        query = '''
        SELECT * FROM categories WHERE id=%s;
        '''
        return execute_query(query, (category_id,), fetch='one')

    @log_decorator
    def switch_appeal(self, season_id):
        query = '''
        SELECT a.id          as a_id,
           a.name        as a_name,
           a.description as a_description,
           a.price       as a_price,
           a.status      as a_status,
           c.name        as category_name,
           r.name        as region_name,
           d.name        as districts_name,
           s.id          as season_id,
           s.name        as season_name,
           s.status      as season_status,
           s.created_at  as season_created
        FROM appeals a
                 inner join categories c on c.ID = a.CATEGORY_ID
                 inner join districts d on a.DISTRICTS_ID = d.ID
                 inner join regions r on d.REGION_ID = r.ID
                 inner join SEASONS S on S.ID = a.SEASONS_ID
        WHERE a_status='accepted' and s.id = %s;
        '''
        params = (season_id,)
        return execute_query(query, params, fetch='all')

    @log_decorator
    def voting_user(self):
        get_active_season = self.get_active_season()
        if get_active_season is None:
            print(color_text('Active season not found', 'yellow'))
            return False
        print(f"\nSeason name: {get_active_season['name']}\nSeason status: {get_active_season['status']}\n")
        get_category = self.switch_category()
        if get_category is None or get_category is False:
            print(color_text('Category not found', 'yellow'))
            return False
