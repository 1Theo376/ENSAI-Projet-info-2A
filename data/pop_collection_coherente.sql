-----------------------------------------------------
-- Collection coherente
-----------------------------------------------------
DROP TABLE IF EXISTS collection_coherente CASCADE ;
CREATE TABLE collection_coherente(
    id_collec_coherente SERIAL PRIMARY KEY,
    titre_collection CHAR,
    description_collection CHAR
);
