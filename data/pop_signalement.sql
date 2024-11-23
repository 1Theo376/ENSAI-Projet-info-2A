-----------------------------------------------------
-- Signalement
-----------------------------------------------------
DROP TABLE IF EXISTS signalement CASCADE ;
CREATE TABLE signalement (
    id_signalement SERIAL PRIMARY KEY,
    id_utilisateur INT ,
    id_avis INT ,
    date_signalement TIMESTAMP DEFAULT NOW(),
    motif TEXT ,
    statut VARCHAR(50) DEFAULT 'En attente',
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (id_avis) REFERENCES avis(id_avis) ON DELETE CASCADE
);