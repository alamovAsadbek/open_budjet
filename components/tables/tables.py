from main_files.database.db_setting import execute_query
from main_files.decorator.decorator_func import log_decorator


class Tables:
    @log_decorator
    def create_users_table(self) -> bool:
        query = '''
        CREATE TABLE IF NOT EXISTS users (
        ID BIGSERIAL PRIMARY KEY,
        FIRST_NAME VARCHAR(255) NOT NULL,
        LAST_NAME VARCHAR(255) NOT NULL,
        EMAIL VARCHAR(255) NOT NULL UNIQUE,
        PASSWORD VARCHAR(255) NOT NULL,
        IS_LOGIN BOOLEAN NOT NULL DEFAULT FALSE,
        CREATED_AT TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_categories_table(self) -> bool:
        query = '''
        CREATE TABLE IF NOT EXISTS categories (
        ID BIGSERIAL PRIMARY KEY,
        NAME VARCHAR(255) NOT NULL,
        STATUS BOOLEAN NOT NULL DEFAULT TRUE
        )
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_regions_table(self) -> bool:
        query = '''
        CREATE TABLE IF NOT EXISTS regions
        (
            ID   BIGSERIAL PRIMARY KEY,
            NAME VARCHAR(255) NOT NULL
        );
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_districts_table(self) -> bool:
        pass

    @log_decorator
    def create_appeals_table(self) -> bool:
        pass
