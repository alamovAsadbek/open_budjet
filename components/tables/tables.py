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
        query = '''
        CREATE TABLE IF NOT EXISTS districts
        (
            ID        BIGSERIAL PRIMARY KEY,
            NAME      VARCHAR(255) NOT NULL,
            REGION_ID BIGINT       NOT NULL,
            FOREIGN KEY (REGION_ID) REFERENCES regions (ID) ON DELETE CASCADE
        );
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_seasons_table(self) -> bool:
        query = '''
        CREATE TABLE IF NOT EXISTS SEASONS
        (
            ID            BIGINT PRIMARY KEY,
            NAME          VARCHAR(255) NOT NULL,
            CATEGORIES_ID jsonb,
            STATUS        VARCHAR(255) NULL DEFAULT 'not_started',
            CREATED_AT    TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP
        );
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_appeals_table(self) -> bool:
        query = '''
        CREATE TABLE IF NOT EXISTS appeals
        (
            ID          BIGSERIAL PRIMARY KEY,
            NAME        VARCHAR(255) NOT NULL,
            DESCRIPTION TEXT         NOT NULL,
            PRICE       BIGINT       NOT NULL,
            USER_ID     BIGINT       NOT NULL,
            CATEGORY_ID BIGINT       NOT NULL,
            REGION_ID   BIGINT      NOT NULL,
            DISTRICTS_ID BIGINT       NOT NULL,
            SEASONS_ID  BIGINT       NOT NULL,
            STATUS      VARCHAR(255) NULL DEFAULT 'wait',
            FOREIGN KEY (SEASONS_ID) REFERENCES seasons (ID) ON DELETE CASCADE,
            FOREIGN KEY (CATEGORY_ID) REFERENCES categories (ID) ON DELETE CASCADE,
            FOREIGN KEY (USER_ID) REFERENCES users (ID) ON DELETE CASCADE,
            FOREIGN KEY (REGION_ID) REFERENCES regions (ID) ON DELETE CASCADE,
            FOREIGN KEY (DISTRICTS_ID) REFERENCES districts (ID) ON DELETE CASCADE
        );
        '''
        execute_query(query)
        return True

    @log_decorator
    def create_votes_table(self) -> bool:
        query = '''
        CREATE TABLE IF NOT EXISTS votes
        (
            ID         BIGSERIAL PRIMARY KEY,
            USER_ID    BIGINT    NOT NULL,
            APPEAL_ID  BIGINT    NOT NULL,
            CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (USER_ID) REFERENCES users (ID) ON DELETE CASCADE,
            FOREIGN KEY (APPEAL_ID) REFERENCES appeals (ID) ON DELETE CASCADE
        )
        '''
        execute_query(query)
        return True
