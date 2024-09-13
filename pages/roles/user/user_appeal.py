import threading

from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query, get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserAppealPageUser:
    @log_decorator
    def get_category(self) -> bool or list:
        print(color_text('Waiting...', 'cyan'))
        print(color_text("Switch category", color='blue'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'],
                                display_keys=['ID', 'Name'])
        pagination.page_tab()
        category_id: int = int(input("Enter the category ID or enter 0 to exit: ").strip())
        if category_id == 0:
            return False
        print(color_text('Checked...', 'cyan'))
        query = '''
        SELECT * FROM categories WHERE ID=%s;
        '''
        result_get = execute_query(query, (category_id,), 'one')
        return result_get

    @log_decorator
    def switch_region(self) -> bool or list:
        print(color_text("Switch region", color='blue'))
        pagination = Pagination(table_name='regions', table_keys=['id', 'name'],
                                display_keys=["ID", "Region Name"])
        if not pagination.page_tab():
            print("Region not found")
            return False
        region_id: int = int(input("Enter region ID or enter 0 to exit: ").strip())
        if region_id == 0:
            return False
        print(color_text("Checked...", color='cyan'))
        query = '''
            SELECT * FROM regions WHERE id=%s;
            '''
        result_get = execute_query(query, (region_id,), fetch='one')
        return result_get

    @log_decorator
    def switch_district(self, region_id) -> bool or list:
        print(color_text("Switch district", color='blue'))
        query = '''
        SELECT d.id as d_id, d.name as d_name, r.name as r_name
         FROM districts d INNER JOIN regions r ON d.region_id=r.id 
        WHERE region_id=%s;
        '''
        result_get = execute_query(query, (region_id,), fetch='all')
        if result_get is None:
            return False
        pagination = Pagination(table_name='districts', table_keys=['d_id', 'r_name', 'd_name', ],
                                display_keys=['Districts ID', 'Region name', 'Districts name'], data=result_get)
        if not pagination.page_tab():
            print(color_text("District not found", 'yellow'))
            return False
        district_id: int = int(input("Enter district ID or enter 0 to exit: ").strip())
        if district_id == 0:
            return False
        print(color_text("Checked...", color='cyan'))
        query = '''
        SELECT * FROM districts WHERE id=%s;
        '''
        params = (district_id,)
        result_get = execute_query(query, params, fetch='one')
        return result_get

    @log_decorator
    def get_active_season(self):
        query = '''
        SELECT * FROM seasons WHERE status='appeal';
        '''
        result_get = execute_query(query, fetch='one')
        return result_get

    @log_decorator
    def get_my_request(self):
        query = '''
        SELECT a.id          as a_id,
           a.name        as a_name,
           a.description as a_description,
           a.price       as a_price,
           a.status      as a_status,
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
        WHERE a.user_id = '%s';
        '''
        params = (get_active_user()['id'],)
        return execute_query(query, params, fetch='all')

    @log_decorator
    def check_appeal(self):
        all_appeals = self.get_my_request()
        if all_appeals is None or len(all_appeals) == 0:
            return False
        for appeal in all_appeals:
            if appeal['season_status'] != 'end':
                return True
        return False

    @log_decorator
    def send_request(self):
        print(color_text("Waiting...", 'cyan'))
        if self.check_appeal() is True:
            print(color_text('You have an active appeal!', 'yellow'))
            return True
        active_user = get_active_user()
        active_season = self.get_active_season()
        if active_season is None or active_season is False:
            print(color_text('\nActive season not found', 'yellow'))
            return False
        get_category = self.get_category()
        if get_category is None or get_category is False:
            print(color_text('Category not found', 'red'))
            return False
        get_region = self.switch_region()
        if get_region is None or get_region is False:
            print(color_text('Region not found', 'red'))
            return False
        get_district = self.switch_district(get_region['id'])
        if get_district is None or get_district is False:
            print(color_text('District not found', 'red'))
            return False
        title: str = input("Enter title: ").strip()
        description: str = input("Enter description: ").strip()
        price: int = int(input("Enter price only number(uzs): ").strip())
        query = '''
        INSERT INTO appeals (name, description, price, user_id, category_id, region_id, seasons_id,  districts_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        params = (title, description, price, active_user['id'], get_category['id'], get_region['id'],
                  active_season['id'], get_district['id'])
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(color_text('Sent request', 'green'))
        return True

    @log_decorator
    def my_request(self) -> bool:
        print(color_text("Waiting...", 'cyan'))
        all_appeals = self.get_my_request()
        if all_appeals is None or len(all_appeals) == 0:
            print(color_text('Appeals not found', 'yellow'))
            return False
        pagination = Pagination(table_name='appeals',
                                table_keys=['a_id', 'a_name', 'a_description', 'a_price', 'a_status', 'category_name',
                                            'region_name', 'districts_name', 'season_name', 'season_status',
                                            'season_created'],
                                display_keys=['Appeals ID', 'Appeals Name', 'Appeals Description',
                                              'Appeals Price (uzs)' 'Appeal Status',
                                              'Category Name', 'Region Name', 'District Name', 'Season Status',
                                              'Season status', 'Season Created'], data=all_appeals)
        if not pagination.page_tab():
            return False
        return True
