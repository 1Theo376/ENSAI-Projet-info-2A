-----------------------------------------------------
-- Avis
-----------------------------------------------------
DROP TABLE IF EXISTS avis CASCADE;
CREATE TABLE avis(
    id_avis SERIAL PRIMARY KEY,
    id_utilisateur INTEGER,
    id_manga INTEGER,
    texte TEXT,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga)
);
