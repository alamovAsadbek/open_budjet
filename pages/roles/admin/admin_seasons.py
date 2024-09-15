import threading

from admin_categories import AdminCategoryPageAdmin
from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class AdminSeasonsPageAdmin:
    def __init__(self):
        self.__category_menu = AdminCategoryPageAdmin()

    @log_decorator
    def switch_districts(self) -> bool or list:
        print(color_text("Switch districts", color='blue'))
        query = '''
        select d.ID as d_id, d.name as d_name, r.NAME as r_name from districts d 
        inner join regions r on d.REGION_ID = r.ID;
        '''
        get_districts = execute_query(query, fetch='all')
        pagination = Pagination(table_name='districts', table_keys=['d_id', 'r_name', 'd_name'],
                                display_keys=["ID", "Region name", "Districts name"], data=get_districts)
        if not pagination.page_tab():
            print("District not found")
            return False
        district_id: int = int(input("Enter district ID: ").strip())
        print(color_text("Checked...", color='cyan'))
        query = '''
        SELECT * FROM districts WHERE ID=%s;
        '''
        result_get = execute_query(query, (district_id,), fetch='one')
        if result_get is None:
            print("District not found")
            return False
        return result_get

    @log_decorator
    def create_seasons(self):
        print(color_text('Waiting...', color='cyan'))
        print(color_text('Check out the first categories to create a new season. Then the categories cannot be changed',
                         color='yellow', is_bold=True))
        if self.get_active_seasons() is not None:
            print(color_text('\nThere is an active season', color='red'))
            return False
        name: str = input("Enter new season's name or type exit to exit: ").strip()
        if name.lower() == 'exit':
            return False
        query = '''
        INSERT INTO seasons (name) VALUES (%s);
        '''
        threading.Thread(target=execute_query, args=(query, (name,),)).start()
        print(color_text('Create Season', color='green'))
        return True

    @log_decorator
    def get_active_seasons(self):
        query = '''
                SELECT * FROM seasons WHERE status='not_started' or status='appeal' or status='vote';
        '''
        result_get = execute_query(query, fetch='one')
        return result_get

    @log_decorator
    def update_status(self) -> bool:
        print(color_text('Waiting...', color='cyan'))
        active_seasons = self.get_active_seasons()
        if active_seasons is None:
            print(color_text('\nThere is no active season', color='red'))
            return False
        print(f"\nSeason ID: {active_seasons['id']}\nSeason Name: {active_seasons['name']}\n"
              f"Status: {active_seasons['status']}\nCreated At: {active_seasons['created_at']}\n")
        while True:
            print(f"\n1. Pause\t2. Appeal\t3. Vote\t4. End")
            admin_input: int = int(input("Choose menu: ").strip())
            if admin_input == 1:
                status: str = 'not_started'
            elif admin_input == 2:
                status: str = 'appeal'
            elif admin_input == 3:
                status: str = 'vote'
            elif admin_input == 4:
                status: str = 'end'
            else:
                print(color_text('Wrong input', color='yellow'))
                continue
            query = '''
            UPDATE seasons SET status=%s WHERE ID=%s;
            '''
            params = (status, active_seasons['id'])
            threading.Thread(target=execute_query, args=(query, params,)).start()
            print(color_text('Updated Season', color='green'))
            return True

    @log_decorator
    def show_all_seasons(self) -> bool:
        print(color_text('Waiting...', color='cyan'))
        pagination = Pagination(table_name='seasons', table_keys=['id', 'name', 'status', 'created_at'],
                                display_keys=["ID", "Name", "Status", "Created at"], is_sorted='id')
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def switch_season(self) -> bool or list:
        print(color_text('Switch Season', color='magenta'))
        if not self.show_all_seasons():
            return False
        season_id: int = int(input("Enter season's ID: ").strip())
        query = '''
        SELECT * FROM seasons WHERE ID=%s;
        '''
        return execute_query(query, (season_id,), fetch='one')

    @log_decorator
    def switch_category(self) -> bool or list:
        print(color_text('Switch Category', color='magenta'))
        if not self.__category_menu.show_all_categories():
            return False
        category_id: int = int(input("Enter category ID: ").strip())
        query = '''
        SELECT * FROM categories WHERE ID=%s;
        '''
        return execute_query(query, (category_id,), fetch='one')

    @log_decorator
    def __get_statistics(self):
        get_season = self.switch_season()
        if get_season is None or get_season is False:
            print(color_text('\nSeason not found', color='red'))
            return False
        get_category = self.switch_category()
        if get_category is None or get_category is False:
            print(color_text('\nCategory not found', color='red'))
            return False
        query = '''
        SELECT a.id AS a_id,
           a.name AS a_name,
           a.description AS a_description,
           a.price AS a_price,
           a.status AS a_status,
           c.id AS category_id,
           c.name AS category_name,
           r.name AS region_name,
           d.name AS districts_name,
           s.id AS season_id,
           s.name AS season_name,
           s.status AS season_status,
           s.created_at AS season_created,
           COUNT(v.appeal_id) AS vote_count
        FROM appeals a
        INNER JOIN categories c ON c.ID = a.CATEGORY_ID
        INNER JOIN districts d ON a.DISTRICTS_ID = d.ID
        INNER JOIN regions r ON d.REGION_ID = r.ID
        INNER JOIN SEASONS s ON s.ID = a.SEASONS_ID
        LEFT JOIN votes v ON v.appeal_id = a.id
        WHERE a.status = 'approved'
          AND s.id = %s
          AND c.id = %s
        GROUP BY a.id, a.name, a.description, a.price, a.status, c.id, c.name, r.name, d.name, s.id, s.name, s.status, s.created_at
        ORDER BY v.id DESC
        '''
        if get_season['status'] == 'end':
            query += 'LIMIT 3'
        return execute_query(query, (get_season['id'], get_category['id']), fetch='all')

    @log_decorator
    def show_all_statistics(self) -> bool:
        get_statistics = self.__get_statistics()
        if get_statistics is None or get_statistics is False:
            print(color_text('\nSeason not found', color='red'))
            return False
