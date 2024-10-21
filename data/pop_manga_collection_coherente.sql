DROP TABLE IF EXISTS association_manga_collection_coherente CASCADE ;
CREATE TABLE association_manga_collection_coherente(
    id_manga  INTEGER,
    id_collec_coherente INTEGER,
    PRIMARY KEY (id_manga, id_collec_coherente),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_collec_coherente) REFERENCES collection_coherente(id_collec_coherente) ON DELETE CASCADE
);