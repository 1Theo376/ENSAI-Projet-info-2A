-----------------------------------------------------
-- Joueur
-----------------------------------------------------
DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur    INTEGER,
    pseudo       VARCHAR(256) UNIQUE,
    mdp          VARCHAR(256),
    PRIMARY KEY (id_utilisateur)
);
