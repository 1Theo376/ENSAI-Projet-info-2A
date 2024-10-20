-----------------------------------------------------
-- Manga
-----------------------------------------------------
DROP TABLE IF EXISTS manga CASCADE ;
CREATE TABLE manga(
    id_manga    SERIAL PRIMARY KEY,
    titre      TEXT,
    synopsis          TEXT
);