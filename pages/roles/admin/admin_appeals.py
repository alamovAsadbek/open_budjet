from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminAppealsPageAdmin:
    @log_decorator
    def get_active_season(self):
        query = '''
        SELECT *
        FROM seasons
        WHERE status = 'appeal';
        '''
        return execute_query(query, fetch='one')

    @log_decorator
    def get_appeals(self, status):
        active_season = self.get_active_season()
        if active_season is None or active_season is False:
            print(color_text('Active season not found!', 'yellow'))
            return False
        query = '''
                            select a.id          as a_id,
                               a.name        as a_name,
                               a.status         as ,
                               a.description as a_description,
                               a.price       as a_price,
                               c.name        as category_name,
                               r.name        as region_name,
                               d.name        as districts_name,
                               s.name        as season_name,
                               s.status      as season_status,
                               s.created_at  as season_created,
                               u.first_name     as u_first_name,
                               u.last_name     as u_last_name,
                               u.email         as u_email
                            FROM appeals a
                                     inner join categories c on c.ID = a.CATEGORY_ID
                                     inner join districts d on a.DISTRICTS_ID = d.ID
                                     inner join regions r on d.REGION_ID = r.ID
                                     inner join SEASONS S on S.ID = a.SEASONS_ID
                                     inner join users u on u.ID = a.USER_ID
                            where s.status = 'appeal' and a.seasons_id=%s and a.status = %s;
                    '''
        param = (active_season['id'], status)
        return execute_query(query, param, fetch='all')

    @log_decorator
    def show_appeals(self, status):
        get_appeals = self.get_appeals(status=status)
        if get_appeals is False or get_appeals is None:
            print(color_text('Rejected appeals not found!', 'yellow'))
            return False
        pagination = Pagination(table_name='appeals',
                                table_keys=['a_id', 'a_name', 'a_description', 'a_price', 'a_status', 'u_first_name',
                                            'u_last_name', 'u_email', 'category_name', 'region_name', 'districts_name',
                                            'season_name'],
                                display_keys=['Appeal ID', 'Appeal Name', 'Appeal Description', 'Appeal Price',
                                              'Appeal Status', 'User first_name', 'User last_name', 'User email',
                                              'Category name', 'Region name', 'District name', 'Season name'],
                                data=get_appeals)
        if not pagination.page_tab():
            print("Rejecting appeals not found!", 'yellow')
            return False
        return True

    @log_decorator
    def rejecting_appeals(self) -> bool:
        self.show_appeals(status='rejected')
        return True

    @log_decorator
    def approved_appeals(self) -> bool:
        pass
