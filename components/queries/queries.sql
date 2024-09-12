-- users tableni yaratish uchun query
CREATE TABLE IF NOT EXISTS categories
(
    ID
    BIGSERIAL
    PRIMARY
    KEY,
    NAME
    VARCHAR
(
    255
) NOT NULL,
    STATUS BOOLEAN NOT NULL DEFAULT TRUE
    );