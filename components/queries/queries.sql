-- users tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS users
(
    ID
               BIGSERIAL
        PRIMARY
            KEY,
    FIRST_NAME
               VARCHAR(255) NOT NULL,
    LAST_NAME  VARCHAR(255) NOT NULL,
    EMAIL      VARCHAR(255) NOT NULL UNIQUE,
    PASSWORD   VARCHAR(255) NOT NULL,
    IS_LOGIN   BOOLEAN      NOT NULL DEFAULT FALSE,
    CREATED_AT TIMESTAMP    NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- categories tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS categories
(
    ID
           BIGSERIAL
        PRIMARY
            KEY,
    NAME
           VARCHAR(255) NOT NULL,
    STATUS BOOLEAN      NOT NULL DEFAULT TRUE
);

-- userlarni logout qilish uchun query
UPDATE users
SET is_login= FALSE;

-- user kiritgan emailni tekshirish, yani mavjudmi yoki yoqligini
SELECT *
FROM USERS
WHERE email = 'alamovasad55@gmail.com';

-- Login uchun query
SELECT *
FROM USERS
WHERE email = '% s'
  and password = '% s';

-- regions tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS regions
(
    ID   BIGSERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL
);

-- districts tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS districts
(
    ID        BIGSERIAL PRIMARY KEY,
    NAME      VARCHAR(255) NOT NULL,
    REGION_ID BIGINT       NOT NULL,
    FOREIGN KEY (REGION_ID) REFERENCES regions (ID) ON DELETE CASCADE
);

--Seasons tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS SEASONS
(
    ID            BIGINT PRIMARY KEY,
    NAME          VARCHAR(255) NOT NULL,
    CATEGORIES_ID jsonb,
    REGION_ID     BIGINT       NOT NULL,
    DISTRICTS_ID  BIGINT       NOT NULL,
    STATUS        VARCHAR(255) NOT NULL DEFAULT 'not_started',
    CREATED_AT    TIMESTAMP    NULL     DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (REGION_ID) REFERENCES regions (ID) ON DELETE CASCADE,
    FOREIGN KEY (DISTRICTS_ID) REFERENCES districts (ID) ON DELETE CASCADE
);

-- Appeals tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS appeals
(
    ID          BIGSERIAL PRIMARY KEY,
    NAME        VARCHAR(255) NOT NULL,
    DESCRIPTION TEXT         NOT NULL,
    PRICE       BIGINT       NOT NULL,
    USER_ID     BIGINT       NOT NULL,
    CATEGORY_ID BIGINT       NOT NULL,
    SEASONS_ID  BIGINT       NOT NULL,
    FOREIGN KEY (SEASONS_ID) REFERENCES seasons (ID) ON DELETE CASCADE,
    FOREIGN KEY (CATEGORY_ID) REFERENCES categories (ID) ON DELETE CASCADE,
    FOREIGN KEY (USER_ID) REFERENCES users (ID) ON DELETE CASCADE
)