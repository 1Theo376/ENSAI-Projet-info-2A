-----------------------------------------------------
-- Numero manquant
-----------------------------------------------------
DROP TABLE IF EXISTS num_manquant CASCADE ;
CREATE TABLE num_manquant(
    id_num_manquant SERIAL PRIMARY KEY,
    num_manquant INT
);
