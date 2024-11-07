-----------------------------------------------------
-- Manga physique
-----------------------------------------------------
DROP TABLE IF EXISTS manga_possede CASCADE ;
CREATE TABLE manga_possede(
    id_manga_p SERIAL PRIMARY KEY,
    id_manga INT,
    num_dernier_acquis INT,
    statut TEXT,
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE
);
