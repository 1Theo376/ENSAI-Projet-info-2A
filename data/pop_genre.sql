-----------------------------------------------------
-- Genre
-----------------------------------------------------
DROP TABLE IF EXISTS genre CASCADE ;
CREATE TABLE genre(
    id_genre    SERIAL PRIMARY KEY,
    genre_name       TEXT
);