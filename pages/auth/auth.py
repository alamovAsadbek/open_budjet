import threading

from components.tables.tables import Tables
from main_files.decorator.decorator_func import log_decorator


class Auth:
    def __init__(self):
        self.__tables = Tables()

    @log_decorator
    def create_tables(self):
        self.__tables.create_users_table()
        threading.Thread(target=self.__tables.create_categories_table).start()

    @log_decorator
    def login(self):
        pass

    @log_decorator
    def logout(self):
        self.create_tables()
        return True

    @log_decorator
    def register(self):
        pass
