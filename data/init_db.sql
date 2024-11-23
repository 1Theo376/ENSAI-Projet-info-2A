DROP TABLE IF EXISTS auteur CASCADE ;
CREATE TABLE auteur(
    id_auteur    SERIAL PRIMARY KEY,
    name_auteur       TEXT
);

DROP TABLE IF EXISTS avis CASCADE;
CREATE TABLE avis(
    id_avis SERIAL PRIMARY KEY,
    id_utilisateur INTEGER,
    id_manga INTEGER,
    texte TEXT,
    note INTEGER,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga)
);

DROP TABLE IF EXISTS collection_coherente CASCADE ;
CREATE TABLE collection_coherente(
    id_collec_coherente SERIAL PRIMARY KEY,
    id_utilisateur INT,
    titre_collection TEXT,
    description_collection TEXT,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE
);

DROP TABLE IF EXISTS collection_physique CASCADE ;
CREATE TABLE collection_physique(
    id_collec_physique SERIAL PRIMARY KEY,
    id_utilisateur INT,
    titre_collection TEXT,
    description_collection TEXT,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE
);

DROP TABLE IF EXISTS genre CASCADE ;
CREATE TABLE genre(
    id_genre    SERIAL PRIMARY KEY,
    genre_name       TEXT
);

DROP TABLE IF EXISTS manga_possede CASCADE ;
CREATE TABLE manga_possede(
    id_manga_p SERIAL PRIMARY KEY,
    id_manga INT,
    num_dernier_acquis INT,
    statut TEXT,
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE
);

DROP TABLE IF EXISTS manga CASCADE ;
CREATE TABLE manga(
    id_manga    SERIAL PRIMARY KEY,
    titre      TEXT,
    volumes  INTEGER,
    publication TEXT,
    synopsis          TEXT
);

DROP TABLE IF EXISTS num_manquant CASCADE ;
CREATE TABLE num_manquant(
    id_num_manquant SERIAL PRIMARY KEY,
    num_manquant INT
);

DROP TABLE IF EXISTS theme CASCADE ;
CREATE TABLE theme(
    id_theme    SERIAL PRIMARY KEY,
    theme_name       TEXT
);

DROP TABLE IF EXISTS utilisateur CASCADE ;
CREATE TABLE utilisateur(
    id_utilisateur    SERIAL PRIMARY KEY,
    pseudo       VARCHAR(256) UNIQUE,
    mdp          VARCHAR(256)
);

DROP TABLE IF EXISTS association_manga_theme CASCADE ;
CREATE TABLE association_manga_theme(
    id_manga  INTEGER,
    id_theme INTEGER,
    PRIMARY KEY (id_manga, id_theme),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_theme) REFERENCES theme(id_theme) ON DELETE CASCADE
);

DROP TABLE IF EXISTS association_manga_auteur CASCADE ;
CREATE TABLE association_manga_auteur(
    id_manga  INTEGER,
    id_auteur INTEGER,
    PRIMARY KEY (id_manga, id_auteur),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_auteur) REFERENCES auteur(id_auteur) ON DELETE CASCADE
);

DROP TABLE IF EXISTS association_manga_collection_coherente CASCADE ;
CREATE TABLE association_manga_collection_coherente(
    id_manga  INTEGER,
    id_collec_coherente INTEGER,
    PRIMARY KEY (id_manga, id_collec_coherente),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_collec_coherente) REFERENCES collection_coherente(id_collec_coherente) ON DELETE CASCADE
);

DROP TABLE IF EXISTS association_manga_collection_physique CASCADE ;
CREATE TABLE association_manga_collection_physique(
    id_manga_p  INTEGER,
    id_collec_physique INTEGER,
    PRIMARY KEY (id_manga_p, id_collec_physique),
    FOREIGN KEY (id_manga_p) REFERENCES manga_possede(id_manga_p) ON DELETE CASCADE,
    FOREIGN KEY (id_collec_physique) REFERENCES collection_physique(id_collec_physique) ON DELETE CASCADE
);

DROP TABLE IF EXISTS association_manga_genre CASCADE ;
CREATE TABLE association_manga_genre(
    id_manga  INTEGER,
    id_genre INTEGER,
    PRIMARY KEY (id_manga, id_genre),
    FOREIGN KEY (id_manga) REFERENCES manga(id_manga) ON DELETE CASCADE,
    FOREIGN KEY (id_genre) REFERENCES genre(id_genre) ON DELETE CASCADE
);

DROP TABLE IF EXISTS association_manga_num_manquant CASCADE ;
CREATE TABLE association_manga_num_manquant(
    id_manga_p  INTEGER,
    id_num_manquant INTEGER,
    PRIMARY KEY (id_manga_p, id_num_manquant),
    FOREIGN KEY (id_manga_p) REFERENCES manga_possede(id_manga_p) ON DELETE CASCADE,
    FOREIGN KEY (id_num_manquant) REFERENCES num_manquant(id_num_manquant) ON DELETE CASCADE
);
