-----------------------------------------------------
-- Collection cohérente
-----------------------------------------------------
DROP TABLE IF EXISTS collection_coherente CASCADE ;
CREATE TABLE collection_coherente(
    id_collec_coherente INT PRIMARY KEY,
    titre_collection CHAR,
    description_collection CHAR
);
