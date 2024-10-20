-----------------------------------------------------
-- Manga physique
-----------------------------------------------------
DROP TABLE IF EXISTS manga_physique CASCADE ;
CREATE TABLE manga_physique(
    id_manga_physique SERIAL PRIMARY KEY,
    id_manga INT,
    num_dernier_acquis INT,
    statut CHAR,
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE
);
