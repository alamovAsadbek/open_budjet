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
    STATUS        VARCHAR(255) NULL DEFAULT 'not_started',
    CREATED_AT    TIMESTAMP    NULL DEFAULT CURRENT_TIMESTAMP,
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
    STATUS      VARCHAR(255) NULL DEFAULT 'wait',
    FOREIGN KEY (SEASONS_ID) REFERENCES seasons (ID) ON DELETE CASCADE,
    FOREIGN KEY (CATEGORY_ID) REFERENCES categories (ID) ON DELETE CASCADE,
    FOREIGN KEY (USER_ID) REFERENCES users (ID) ON DELETE CASCADE
);

-- votes tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS votes
(
    ID         BIGSERIAL PRIMARY KEY,
    USER_ID    BIGINT    NOT NULL,
    APPEAL_ID  BIGINT    NOT NULL,
    CREATED_AT TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (USER_ID) REFERENCES users (ID) ON DELETE CASCADE,
    FOREIGN KEY (APPEAL_ID) REFERENCES appeals (ID) ON DELETE CASCADE
);

-- regionlarni qo'shib olish uchun query
INSERT INTO regions(NAME)
VALUES ('Andijon viloyati'),
       ('Buxoro viloyati'),
       ('Jizzax viloyati'),
       ('Qashqadaryo viloyati'),
       ('Navoiy viloyati'),
       ('Namangan viloyati'),
       ('Samarqand viloyati'),
       ('Surxondaryo viloyati'),
       ('Sirdaryo viloyati'),
       ('Toshkent shahri'),
       ('Toshkent viloyati'),
       ('Farg`ona viloyati'),
       ('Xorazm viloyati'),
       ('Qoraqalpog`iston Respublikasi');

-- DISTRICTS larni qo'shib olish uchun query
INSERT INTO "districts" ("region_id", "name")
VALUES (1, 'Marxamat tumani'),
       (1, 'Andijon tumani'),
       (1, 'Baliqchi tumani'),
       (1, 'Bo`z tumani'),
       (1, 'Buloqboshi tumani'),
       (1, 'Izboskan tumani'),
       (1, 'Ulug`nor tumani'),
       (1, 'Qo`rg`ontepa tumani'),
       (1, 'Asaka tumani'),
       (1, 'Paxtaobod tumani'),
       (1, 'Jalolquduq tumani'),
       (1, 'Oltinkol tumani'),
       (1, 'Xojaobod tumani'),
       (1, 'Shahrixon tumani'),
       (1, 'Andijon shahri'),
       (1, 'Xonobod shahri'),
       (2, 'Olot tumani'),
       (2, 'Buxoro tumani'),
       (2, 'Vobkent tumani'),
       (2, 'Kogon tumani'),
       (2, 'Qorakol tumani'),
       (2, 'Qorovulbozor tumani'),
       (2, 'Peshku tumani'),
       (2, 'Romitan tumani'),
       (2, 'Shofirkon tumani'),
       (2, 'Jondor tumani'),
       (2, 'Buxoro shahri'),
       (2, 'Kogon shahri'),
       (2, 'Gijduvon tumani'),
       (3, 'Dostlik tumani'),
       (3, 'Zomin tumani'),
       (3, 'Zarbdor tumani'),
       (3, 'Mirzachol tumani'),
       (3, 'Forish tumani'),
       (3, 'Arnasoy tumani'),
       (3, 'Baxmal tumani'),
       (3, 'Gallaorol tumani'),
       (3, 'Yangiobod tumani'),
       (3, 'Jizzax shahri'),
       (3, 'Paxtakor tumani'),
       (3, 'Zafarobod tumani'),
       (3, 'Sharof Rashidov tumani'),
       (4, 'Muborak tumani'),
       (4, 'Kasbi tumani'),
       (4, 'Guzor tumani'),
       (4, 'Dehqonobod tumani'),
       (4, 'Qamashi tumani'),
       (4, 'Qarshi shahri'),
       (4, 'Chiroqchi tumani'),
       (4, 'Shahrisabz tumani'),
       (4, 'Yakkabog tumani'),
       (4, 'Qarshi tumani'),
       (4, 'Koson tumani'),
       (4, 'Kitob tumani'),
       (4, 'Mirishkor tumani'),
       (4, 'Nishon tumani'),
       (4, 'Shahrisabz shahri'),
       (5, 'Konimex tumani'),
       (5, 'Qiziltepa tumani'),
       (5, 'Navbahor tumani'),
       (5, 'Karmana tumani'),
       (5, 'Nurota tumani'),
       (5, 'Uchquduq tumani'),
       (5, 'Xatirchi tumani'),
       (5, 'Navoiy shahri'),
       (5, 'Tomdi tumani'),
       (5, 'Zarafshon shahri'),
       (6, 'Mingbuloq tumani'),
       (6, 'Kosonsoy tumani'),
       (6, 'Namangan tumani'),
       (6, 'Norin tumani'),
       (6, 'Pop tumani'),
       (6, 'Toraqorgon tumani'),
       (6, 'Uychi tumani'),
       (6, 'Uchqorgon tumani'),
       (6, 'Chortoq tumani'),
       (6, 'Chust tumani'),
       (6, 'Namangan shahri'),
       (6, 'Yangiqorgon tumani'),
       (7, 'Qoshrabot tumani'),
       (7, 'Samarqand shahri'),
       (7, 'Ishtixon tumani'),
       (7, 'Kattaqorgon tumani'),
       (7, 'Oqdaryo tumani'),
       (7, 'Bulungur tumani'),
       (7, 'Jomboy tumani'),
       (7, 'Narpay tumani'),
       (7, 'Pastdargom tumani'),
       (7, 'Paxtachi tumani'),
       (7, 'Samarqand tumani'),
       (7, 'Nurobod tumani'),
       (7, 'Urgut tumani'),
       (7, 'Tayloq tumani'),
       (7, 'Payariq tumani'),
       (7, 'Kattaqorgon shahri'),
       (8, 'Oltinsoy tumani'),
       (8, 'Angor tumani'),
       (8, 'Boysun tumani'),
       (8, 'Denov tumani'),
       (8, 'Qumqorgon tumani'),
       (8, 'Qiziriq tumani'),
       (8, 'Sariosiyo tumani'),
       (8, 'Termiz tumani'),
       (8, 'Uzun tumani'),
       (8, 'Sherobod tumani'),
       (8, 'Shorchi tumani'),
       (8, 'Termiz shahri'),
       (8, 'Muzrabot tumani'),
       (8, 'Jarqorgon tumani'),
       (9, 'Mirzaobod tumani'),
       (9, 'Sirdaryo tumani'),
       (9, 'Oqoltin tumani'),
       (9, 'Boyovut tumani'),
       (9, 'Guliston tumani'),
       (9, 'Sayxunobod tumani'),
       (9, 'Sardoba tumani'),
       (9, 'Shirin shahri'),
       (9, 'Yangiyer shahri'),
       (9, 'Xovos tumani'),
       (9, 'Guliston shahri'),
       (10, 'Yunusobod tumani'),
       (10, 'Uchtepa tumani'),
       (10, 'Bektemir tumani'),
       (10, 'Mirzo Ulugbek tumani'),
       (10, 'Mirobod tumani'),
       (10, 'Olmazor tumani'),
       (10, 'Sirgali tumani'),
       (10, 'Yakkasaroy tumani'),
       (10, 'Chilonzor tumani'),
       (10, 'Yashnobod tumani'),
       (10, 'Shayxontohur tumani'),
       (11, 'Boka tumani'),
       (11, 'Oqqorgon tumani'),
       (11, 'Ohangaron tumani'),
       (11, 'Bekobod tumani'),
       (11, 'Bostonliq tumani'),
       (11, 'Zangiota tumani'),
       (11, 'Qibray tumani'),
       (11, 'Parkent tumani'),
       (11, 'Ortachirchiq tumani'),
       (11, 'Chinoz tumani'),
       (11, 'Yangiyol tumani'),
       (11, 'Yuqorichirchiq tumani'),
       (11, 'Pskent tumani'),
       (11, 'Olmaliq shahri'),
       (11, 'Angren shahri'),
       (11, 'Chirchiq shahri'),
       (11, 'Quyichirchiq tumani'),
       (11, 'Toshkent tumani'),
       (11, 'Nurafshon shahri'),
       (11, 'Bekobod shahri'),
       (11, 'Ohangaron shahri'),
       (11, 'Yangiyol shahri'),
       (12, 'Quva tumani'),
       (12, 'Dangara tumani'),
       (12, 'Sox tumani'),
       (12, 'Oltiariq tumani'),
       (12, 'Qoshtepa tumani'),
       (12, 'Bogdod tumani'),
       (12, 'Buvayda tumani'),
       (12, 'Beshariq tumani'),
       (12, 'Uchkoprik tumani'),
       (12, 'Rishton tumani'),
       (12, 'Toshloq tumani'),
       (12, 'Ozbekiston tumani'),
       (12, 'Fargona tumani'),
       (12, 'Furqat tumani'),
       (12, 'Yozyovon tumani'),
       (12, 'Fargona shahri'),
       (12, 'Qoqon shahri'),
       (12, 'Quvasoy shahri'),
       (12, 'Margilon shahri'),
       (13, 'Hazorasp tumani'),
       (13, 'Yangiariq tumani'),
       (13, 'Yangibozor tumani'),
       (13, 'Xonqa tumani'),
       (13, 'Xiva tumani'),
       (13, 'Urganch shahri'),
       (13, 'Shovot tumani'),
       (13, 'Bogot tumani'),
       (13, 'Gurlan tumani'),
       (13, 'Qoshkopir tumani'),
       (13, 'Urganch tumani'),
       (13, 'Xiva shahri'),
       (14, 'Beruniy tumani'),
       (14, 'Qoraozak tumani'),
       (14, 'Kegeyli tumani'),
       (14, 'Qongirot tumani'),
       (14, 'Qanlikol tumani'),
       (14, 'Moynoq tumani'),
       (14, 'Shumanay tumani'),
       (14, 'Ellikkala tumani'),
       (14, 'Nukus shahri'),
       (14, 'Amudaryo tumani'),
       (14, 'Nukus tumani'),
       (14, 'Taxtakopir tumani'),
       (14, 'Tortkol tumani'),
       (14, 'Xojayli tumani'),
       (14, 'Chimboy tumani'),
       (14, 'Taxiatosh tumani');


-- Yangi category qo'shish uchun query
INSERT INTO categories (name) VALUES ('%s');


-- categoryini update qilish uchun query
UPDATE categories SET name='%s' WHERE id='%s';

-- category ni uchirish uchun query
DELETE FROM categories WHERE id='%s';