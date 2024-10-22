DROP TABLE IF EXISTS association_mp_num_manquant CASCADE ;
CREATE TABLE association_mp_num_manquant(
    id_manga_physique  INTEGER,
    id_num_manquant INTEGER,
    PRIMARY KEY (id_manga_physique, id_num_manquant),
    FOREIGN KEY (id_manga_physique) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_num_manquant) REFERENCES num_manquant(id_num_manquant) ON DELETE CASCADE
);
