-----------------------------------------------------
-- Theme
-----------------------------------------------------
DROP TABLE IF EXISTS theme CASCADE ;
CREATE TABLE theme(
    id_theme    SERIAL PRIMARY KEY,
    theme_name       TEXT
);