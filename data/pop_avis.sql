-----------------------------------------------------
-- Avis
-----------------------------------------------------
DROP TABLE IF EXISTS avis CASCADE ;
CREATE TABLE avis(
    id_avis    SERIAL PRIMARY KEY,
    id_utilisateur   INTEGER FOREIGN KEY,
    id_manga          INTEGER FOREIGN KEY,
    texte     TEXT);