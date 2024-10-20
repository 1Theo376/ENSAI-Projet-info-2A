-----------------------------------------------------
-- Auteur
-----------------------------------------------------
DROP TABLE IF EXISTS auteur CASCADE ;
CREATE TABLE auteur(
    id_auteur    SERIAL PRIMARY KEY,
    name_auteur       TEXT
);