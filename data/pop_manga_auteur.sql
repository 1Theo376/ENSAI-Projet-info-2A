DROP TABLE IF EXISTS association_manga_auteur CASCADE ;
CREATE TABLE association_manga_auteur(
    id_manga  INTEGER,
    id_auteur INTEGER,
    PRIMARY KEY (id_manga, id_auteur),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_auteur) REFERENCES auteur(id_auteur) ON DELETE CASCADE
);