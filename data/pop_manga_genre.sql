DROP TABLE IF EXISTS association_manga_genre CASCADE ;
CREATE TABLE association_manga_genre(
    id_manga  INTEGER,
    id_genre INTEGER,
    PRIMARY KEY (id_manga, id_genre),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_genre) REFERENCES genre(id_genre) ON DELETE CASCADE
);