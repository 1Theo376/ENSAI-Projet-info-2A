DROP TABLE IF EXISTS association_manga_collection_physique CASCADE ;
CREATE TABLE association_manga_collection_physique(
    id_manga_p  INTEGER,
    id_collec_physique INTEGER,
    PRIMARY KEY (id_manga_p, id_collec_physique),
    FOREIGN KEY (id_manga_p) REFERENCES manga_possede(id_manga_p) ON DELETE CASCADE,
    FOREIGN KEY (id_collec_physique) REFERENCES collection_physique(id_collec_physique) ON DELETE CASCADE
);