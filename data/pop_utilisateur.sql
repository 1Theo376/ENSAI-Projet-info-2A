-----------------------------------------------------
-- Joueur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur    SERIAL PRIMARY KEY,
    pseudo       VARCHAR(30) UNIQUE,
    mdp          VARCHAR(256)
);