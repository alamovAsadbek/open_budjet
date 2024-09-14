import threading

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
    def get_appeals(self, status: str, data_id: int = None) -> list or None:
        active_season = self.get_active_season()
        if active_season is None or active_season is False:
            print(color_text('Active season not found!', 'yellow'))
            return False
        if data_id is None:
            query = '''
            select a.id          as a_id,
               a.name        as a_name,
               a.status      as a_status,
               a.description as a_description,
               a.price       as a_price,
               c.name        as category_name,
               r.name        as region_name,
               d.name        as districts_name,
               s.name        as season_name,
               s.status      as season_status,
               s.created_at  as season_created,
               u.first_name  as u_first_name,
               u.last_name   as u_last_name,
               u.email       as u_email,
               a.seasons_id  as a_seasons_id
            FROM appeals a
                     inner join categories c on c.ID = a.CATEGORY_ID
                     inner join districts d on a.DISTRICTS_ID = d.ID
                     inner join regions r on d.REGION_ID = r.ID
                     inner join SEASONS S on S.ID = a.SEASONS_ID
                     inner join users u on u.ID = a.USER_ID
            where s.status = 'appeal'
              and a.seasons_id = %s
              and a.status = %s;
            '''
            param = (active_season['id'], status)
            return execute_query(query, param, fetch='all')
        query = '''
                    select a.id          as a_id,
                       a.name        as a_name,
                       a.status      as a_status,
                       a.description as a_description,
                       a.price       as a_price,
                       c.name        as category_name,
                       r.name        as region_name,
                       d.name        as districts_name,
                       s.name        as season_name,
                       s.status      as season_status,
                       s.created_at  as season_created,
                       u.first_name  as u_first_name,
                       u.last_name   as u_last_name,
                       u.email       as u_email,
                       a.seasons_id  as a_seasons_id
                    FROM appeals a
                             inner join categories c on c.ID = a.CATEGORY_ID
                             inner join districts d on a.DISTRICTS_ID = d.ID
                             inner join regions r on d.REGION_ID = r.ID
                             inner join SEASONS S on S.ID = a.SEASONS_ID
                             inner join users u on u.ID = a.USER_ID
                    where s.status = 'appeal'
                      and a.seasons_id = %s
                      and a.status = %s
                      and a.id = %s
                    '''
        param = (active_season['id'], status, data_id)
        return execute_query(query, param, fetch='one')

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
                                display_keys=['Appeal ID', 'Appeal Name', 'Appeal Description', 'Appeal Price (uzs)',
                                              'Appeal Status', 'User first_name', 'User last_name', 'User email',
                                              'Category name', 'Region name', 'District name', 'Season name'],
                                data=get_appeals)
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def rejecting_appeals(self) -> bool:
        print(color_text('Waiting...', 'cyan'))
        self.show_appeals(status='cancellation')
        return True

    @log_decorator
    def approved_appeals(self) -> bool:
        print(color_text('Waiting...', 'cyan'))
        self.show_appeals(status='approved')
        return True

    @log_decorator
    def accepting_application(self) -> bool:
        print(color_text('Waiting...', 'cyan'))
        self.show_appeals(status='wait')
        appeal_id: int = int(input('Appeal ID or enter 0 to exit: ').strip())
        if appeal_id == 0:
            return False
        print(color_text('Checked...', 'cyan'))
        get_appeals = self.get_appeals(status='wait', data_id=appeal_id)
        if get_appeals is False or get_appeals is None:
            print(color_text('Appeals not found!', 'yellow'))
            return False
        print(
            f"\n{color_text('Appeal ID: ', 'blue')} {appeal_id}\n"
            f"{color_text('Appeal Name: ', 'blue')} {get_appeals['a_name']}\n"
            f"{color_text('Appeal Description: ', 'blue')}{get_appeals['a_description']}\n"
            f"{color_text('Appeal price: ', 'blue')}{get_appeals['a_price']}\n"
            f"{color_text('Appeal status: ', 'blue')}{get_appeals['a_status']}\n"
            f"{color_text('User first_name: ', 'blue')} {get_appeals['u_first_name']}\n"
            f"{color_text('User last_name: ', 'blue')} {get_appeals['u_last_name']}\n"
            f"{color_text('User email: ', 'blue')} {get_appeals['u_email']}\n"
            f"{color_text('Category name: ', 'blue')} {get_appeals['category_name']}\n"
            f"{color_text('Region name: ', 'blue')} {get_appeals['region_name']}\n"
            f"{color_text('District name: ', 'blue')} {get_appeals['districts_name']}\n"
            f"{color_text('Season name: ', 'blue')} {get_appeals['season_name']}\n")
        while True:
            print(f"{color_text('1. Confirmation', 'green')}\t\t{color_text('2. Cancellation', 'red')}")
            choose_menu: int = int(input("Choose menu: ").strip())
            if choose_menu == 1:
                get_appeals['a_status'] = 'approved'
                print(color_text('Approved', 'green'))
            elif choose_menu == 2:
                get_appeals['a_status'] = 'cancellation'
                print(color_text('Canceled', 'yellow'))
            else:
                print(color_text('Invalid option!', 'yellow'))
                continue
            break
        query = '''
        UPDATE appeals SET status = %s WHERE id = %s;
        '''
        param = (get_appeals['a_status'], appeal_id)
        threading.Thread(target=execute_query, args=(query, param)).start()
        return True
