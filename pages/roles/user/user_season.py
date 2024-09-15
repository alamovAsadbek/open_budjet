import threading

from components.color_text.color_text import color_text
from components.email_sender.email_sender import EmailSender
from components.pagination.pagination import Pagination
from components.random_password.generate_password import generate_password
from main_files.database.db_setting import execute_query, get_active_user
from main_files.decorator.decorator_func import log_decorator


class UserSeason:
    def __init__(self):
        self.__email_sender = EmailSender()

    @log_decorator
    def get_active_season(self):
        query = '''
        SELECT * FROM seasons WHERE status='vote';
        '''
        result = execute_query(query, fetch='one')
        return result

    @log_decorator
    def switch_category(self) -> bool or list:
        print(color_text('Switch category', 'magenta'))
        pagination = Pagination(table_name='categories', table_keys=['id', 'name'], display_keys=['ID', 'Name'])
        if not pagination.page_tab():
            return False
        category_id: int = int(input("Enter the category ID or type 0 to exit: ").strip())
        print(color_text('Waiting...', 'cyan'))
        if category_id == 0:
            return False
        query = '''
        SELECT * FROM categories WHERE id=%s;
        '''
        return execute_query(query, (category_id,), fetch='one')

    @log_decorator
    def switch_appeal_all(self, season_id: int, category_id: int):
        query = '''
        SELECT a.id          as a_id,
           a.name        as a_name,
           a.description as a_description,
           a.price       as a_price,
           a.status      as a_status,
           c.id          as category_id,
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
        WHERE a.status='approved' and s.id = %s and c.id = %s;
        '''
        params = (season_id, category_id)
        return execute_query(query, params, fetch='all')

    @log_decorator
    def switch_appeal(self, data: list):
        pagination = Pagination(table_name='appeals',
                                table_keys=['a_id', 'a_name', 'a_description', 'a_price', 'a_status',
                                            'category_name', 'region_name', 'districts_name',
                                            'season_name'],
                                display_keys=['Appeal ID', 'Appeal Name', 'Appeal Description', 'Appeal Price (uzs)',
                                              'Appeal Status', 'Category name', 'Region name', 'District name',
                                              'Season name'],
                                data=data)
        if not pagination.page_tab():
            return None
        appeal_id: int = int(input("Enter the appeal ID or type 0 to exit: ").strip())
        if appeal_id == 0:
            return None
        query = '''
        SELECT * FROM appeals WHERE id=%s;
        '''
        params = (appeal_id,)
        return execute_query(query, params, fetch='one')

    @log_decorator
    def check_vote(self, user_id: int):
        query = '''
        select *
        from votes v
                 inner join appeals a on a.ID = v.APPEAL_ID
                 inner join SEASONS S on S.ID = a.SEASONS_ID
        where s.STATUS != 'end'
          and v.user_id = %s;
        '''
        params = (user_id,)
        return execute_query(query, params, fetch='one')

    @log_decorator
    def confirm_vote(self, user_email: str) -> bool:
        print(color_text("A verification code has been sent to the mail. Mail: ", 'magenta'), user_email)
        confirm_code: int = generate_password()
        email_subject: str = 'Confirm Your Verification Code'
        email_body: str = f'Enter the verification code into the program and vote. Confirm password is {confirm_code}'
        threading.Thread(target=self.__email_sender.send_email, args=(email_subject, email_body, user_email)).start()
        number_of_attempts = 0
        while True:
            if number_of_attempts == 4:
                print(color_text('You are out of attempts. Please try again', 'red'))
                return False
            print(color_text('Number of Attempts: ', 'magenta'), number_of_attempts + 1)
            code: int = int(input("Enter the verification code: ").strip())
            if code == confirm_code:
                print(color_text('Confirm your verification code', 'green'))
                return True
            else:
                print(color_text('Please enter an incorrect number and try again', 'yellow'))
            number_of_attempts += 1

    @log_decorator
    def voting_user(self):
        print(color_text('Waiting...', 'cyan'))
        active_user = get_active_user()
        if self.check_vote(active_user['id']) is not None:
            print(color_text('You voted for this season!', 'yellow'))
            return False
        get_active_season = self.get_active_season()
        if get_active_season is None:
            print(color_text('Active season not found', 'yellow'))
            return False
        print(
            f"\n{color_text('Season name: ', 'blue')} {get_active_season['name']}\n"
            f"{color_text('Season status: ', 'blue')} {get_active_season['status']}\n")
        print(color_text('Waiting...', 'cyan'))
        get_category = self.switch_category()
        if get_category is None or get_category is False:
            print(color_text('Category not found', 'yellow'))
            return False
        get_appeals = self.switch_appeal_all(get_active_season['id'], get_category['id'])
        if get_appeals is None or get_appeals is False:
            print(color_text('Appeals not found', 'yellow'))
            return False
        switch_appeal = self.switch_appeal(get_appeals)
        if switch_appeal is None or switch_appeal is False:
            print(color_text('Appeal not found!', 'yellow'))
            return False
        if not self.confirm_vote(active_user['email']):
            return False
        query = '''
        INSERT INTO votes (user_id, appeal_id) VALUES (%s, %s);
        '''
        params = (active_user['id'], switch_appeal['id'])
        threading.Thread(target=execute_query, args=(query, params)).start()
        print(color_text('Your voted for this season!', 'green'))
        return True

    @log_decorator
    def get_my_votes(self):
        active_user = get_active_user()
        query = '''
                select s.name        as s_name,
               s.STATUS      as s_status,
               c.NAME        as c_name,
               a.NAME        as a_name,
               a.DESCRIPTION as a_description,
               r.name        as r_name,
               d.name        as d_name,
               v.id as v_id   
                from votes v
                         inner join appeals a on a.ID = v.APPEAL_ID
                         inner join SEASONS s on S.ID = a.SEASONS_ID
                         inner join categories c on c.ID = a.CATEGORY_ID
                         inner join regions r on a.REGION_ID = r.ID
                         inner join districts d on d.ID = a.DISTRICTS_ID
                where v.user_id = %s order by v.id desc;
        '''
        return execute_query(query, (active_user['id'],), fetch='all')

    @log_decorator
    def my_votes(self):
        print(color_text('Waiting...', 'cyan'))
        get_all_votes = self.get_my_votes()
        if get_all_votes is None or get_all_votes is False:
            print(color_text('You haven\'t voted yet', 'yellow'))
            return False
        pagination = Pagination(table_name='votes',
                                table_keys=['s_name', 's_status', 'c_name', 'a_name', 'a_description', 'r_name',
                                            'd_name'],
                                data=get_all_votes,
                                display_keys=['Season name', 'Season status', 'Category name', 'Appeal name',
                                              'Appeal description', 'Region name', 'District name'], is_sorted='v.id')
        if not pagination.page_tab():
            return False
        return True

    @log_decorator
    def get_statistics(self, season_id: int, category_id: int):
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
        GROUP BY a.id, a.name, a.description, a.price, a.status, c.id, c.name, 
        r.name, d.name, s.id, s.name, s.status, s.created_at
        ORDER BY vote_count DESC;
        '''
        params = (season_id, category_id,)
        return execute_query(query, params, fetch='all')

    @log_decorator
    def show_statistics(self) -> bool:
        get_active_season = self.get_active_season()
        if get_active_season is None:
            print(color_text('Active season not found', 'yellow'))
            return False
        print(
            f"\n{color_text('Season name: ', 'blue')} {get_active_season['name']}\n"
            f"{color_text('Season status: ', 'blue')} {get_active_season['status']}\n")
        print(color_text('Waiting...', 'cyan'))
        get_category = self.switch_category()
        if get_category is None or get_category is False:
            print(color_text('Category not found', 'yellow'))
            return False
        get_statistics = self.get_statistics(season_id=get_active_season['id'], category_id=get_category['id'])
        pagination = Pagination(table_name='votes', table_keys=[
            'a_id',
            'a_name',
            'a_description',
            'a_price',
            'a_status',
            'category_name',
            'region_name',
            'districts_name',
            'season_id',
            'season_name',
            'season_status',
            'season_created',
            'vote_count'], display_keys=['Appeal ID', 'Appeal name', 'Appeal description', 'Appeal price',
                                         'Appeal status', 'Category name', 'Region name', 'District name', 'Season ID',
                                         'Season name', 'Season status', 'Season created', 'Vote count'],
                                data=get_statistics)
        if not pagination.page_tab():
            return False
        return True
