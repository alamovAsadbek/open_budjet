from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Tables:
    @log_decorator
    def create_users_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS users (
        ID INTEGER PRIMARY KEY,
        FIRST_NAME VARCHAR(255) NOT NULL,
        LAST_NAME VARCHAR(255) NOT NULL,
        EMAIL VARCHAR(255) NOT NULL,
        PASSWORD VARCHAR(255) NOT NULL,
        IS_LOGIN BOOLEAN NOT NULL DEFAULT FALSE,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_categories_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS categories (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        STATUS BOOLEAN NOT NULL DEFAULT TRUE
        )
        '''
        execute_query(query)
        return True
