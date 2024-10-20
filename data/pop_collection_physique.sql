-----------------------------------------------------
-- Collection physique
-----------------------------------------------------
DROP TABLE IF EXISTS collection_physique CASCADE ;
CREATE TABLE collection_physique(
    id_collec_coherente INT PRIMARY KEY,
    id_manga INT FOREIGN KEY REFERENCES Manga(id_manga),
    titre_collection CHAR,
    description_collection CHAR,
    statut CHAR
);
