-----------------------------------------------------
-- Collection physique
-----------------------------------------------------
DROP TABLE IF EXISTS collection_physique CASCADE ;
CREATE TABLE collection_physique(
    id_collec_physique SERIAL PRIMARY KEY,
    id_utilisateur INT, 
    titre_collection TEXT,
    description_collection TEXT, 
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE
);
