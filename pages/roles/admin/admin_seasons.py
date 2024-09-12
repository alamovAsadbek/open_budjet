import threading

from components.color_text.color_text import color_text
from components.pagination.pagination import Pagination
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
    def switch_region(self) -> bool or list:
        print(color_text("Switch region", color='blue'))
        pagination = Pagination(table_name='regions', table_keys=['id', 'name'],
                                display_keys=["ID", "Region Name"])
        if not pagination.page_tab():
            print("Region not found")
            return False
        region_id: int = int(input("Enter region ID: ").strip())
        print(color_text("Checked...", color='cyan'))
        query = '''
        SELECT * FROM regions WHERE id=%s;
        '''
        result_get = execute_query(query, (region_id,), fetch='one')
        if result_get is None:
            print("Region not found")
            return False
        return result_get

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
        name: str = input("Enter new season's name or type exit to exit: ").strip()
        if name.lower() == 'exit':
            return False
        query = '''
        INSERT INTO seasons (name) VALUES (%s);
        '''
        threading.Thread(target=execute_query, args=(query, (name,),)).start()
        print(color_text('Create Season', color='green'))
        return True
