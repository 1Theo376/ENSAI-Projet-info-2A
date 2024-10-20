DROP TABLE IF EXISTS association_manga_theme CASCADE ;
CREATE TABLE association_manga_theme(
    id_manga  INTEGER,
    id_theme INTEGER,
    PRIMARY KEY (id_manga, id_theme),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_theme) REFERENCES theme(id_theme) ON DELETE CASCADE
);