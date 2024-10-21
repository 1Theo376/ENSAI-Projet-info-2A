-----------------------------------------------------
-- Collection coherente
-----------------------------------------------------
DROP TABLE IF EXISTS collection_coherente CASCADE ;
CREATE TABLE collection_coherente(
    id_collec_coherente SERIAL PRIMARY KEY,
    id_utilisateur INT,
    titre_collection CHAR,
    description_collection CHAR, 
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE
);
