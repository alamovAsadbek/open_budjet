import threading

from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
from main_files.database.db_setting import execute_query, get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserAppealPageUser:
    @log_decorator
    def get_category(self):
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
    def send_request(self):
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
        INSERT INTO appeals (name, description, price, user_id, category_id, region_id, seasons_id, district_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        '''
        params = (title, description, price, active_user['id'], get_category['id'], get_region['id'],
                  active_season['id'], get_district['id'])
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(color_text('Sent request', 'green'))
        return True
