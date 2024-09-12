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