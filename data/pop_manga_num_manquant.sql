DROP TABLE IF EXISTS association_manga_num_manquant CASCADE ;
CREATE TABLE association_manga_num_manquant(
    id_manga_p  INTEGER,
    id_num_manquant INTEGER,
    PRIMARY KEY (id_manga_p, id_num_manquant),
    FOREIGN KEY (id_manga_p) REFERENCES manga_possede(id_manga_p) ON DELETE CASCADE,
    FOREIGN KEY (id_num_manquant) REFERENCES num_manquant(id_num_manquant) ON DELETE CASCADE
);
