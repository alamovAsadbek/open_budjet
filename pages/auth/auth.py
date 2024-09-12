import hashlib
import threading
import time

from components.tables.tables import Tables
from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__tables = Tables()
        self.__confirm_time = 0

    @log_decorator
    def create_tables(self) -> bool:
        self.__tables.create_users_table()
        threading.Thread(target=self.__tables.create_categories_table).start()
        return True

    @log_decorator
    def count_time(self) -> bool:
        for i in range(30):
            time.sleep(1)
            self.__confirm_time += 1
            yield True

    @log_decorator
    def login(self) -> bool:
        pass

    @log_decorator
    def logout(self) -> bool:
        self.create_tables()
        query = '''
               UPDATE users SET is_login=FALSE;
        '''
        execute_query(query)
        return True

    @log_decorator
    def register(self) -> bool:
        first_name: str = input('First name: ').strip()
        last_name: str = input('Last name: ').strip()
        email: str = input('Email: ').strip()
        password: str = hashlib.sha256(input('Password: ').encode('utf-8')).hexdigest()
        confirm_password: str = hashlib.sha256(input("Confirm password: ").strip().encode('utf-8')).hexdigest()
        while password != confirm_password:
            print('Passwords do not match!')
            password: str = hashlib.sha256(input('Password: ').encode('utf-8')).hexdigest()
            confirm_password: str = hashlib.sha256(password.encode('utf-8')).hexdigest()
        print(f"\nConfirm email: {email}\n")
        print("You will have 30 seconds to confirm your email")
