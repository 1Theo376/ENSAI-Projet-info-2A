-----------------------------------------------------
-- Collection physique
-----------------------------------------------------
DROP TABLE IF EXISTS collection_physique CASCADE ;
CREATE TABLE collection_physique(
    id_collec_physique SERIAL PRIMARY KEY,
    titre_collection CHAR,
    description_collection CHAR,
    statut CHAR
);
