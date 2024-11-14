import os
import logging
import dotenv

from unittest import mock

from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection

# from service.joueur_service import JoueurService


class ResetDatabase(metaclass=Singleton):
    """
    Reinitialisation de la base de données
    """

    @log
    def lancer(self, test_dao=False):
        """Lancement de la réinitialisation des données
        Si test_dao = True : réinitialisation des données de test"""
        if test_dao:
            mock.patch.dict(os.environ, {"POSTGRES_SCHEMA": "projet_info"}).start()
            sql_files = [
                "data/pop_utilisateur.sql",
                "data/pop_manga.sql",
                "data/pop_collection_coherente.sql",
                "data/pop_auteur.sql",
                "data/pop_avis.sql",
                "data/pop_collection_physique.sql",
                "data/pop_genre.sql",
                "data/pop_theme.sql",
                "data/pop_manga_auteur.sql",
                "data/pop_manga_genre.sql",
                "data/pop_manga_theme.sql",
                "data/pop_manga_possede.sql",
                "data/pop_manga_collection_physique.sql",
                "data/pop_manga_collection_coherente.sql",
                "data/pop_num_manquant.sql",
                "data/pop_manga_num_manquant.sql"
            ]
        else:
            mock.patch.dict(os.environ, {"POSTGRES_SCHEMA": "projet_info"}).start()
            sql_files = [
                "data/pop_utilisateur.sql",
                "data/pop_manga.sql",
                "data/pop_collection_coherente.sql",
                "data/pop_auteur.sql",
                "data/pop_avis.sql",
                "data/pop_collection_physique.sql",
                "data/pop_genre.sql",
                "data/pop_theme.sql",
                "data/pop_manga_auteur.sql",
                "data/pop_manga_genre.sql",
                "data/pop_manga_theme.sql",
                "data/pop_manga_possede.sql",
                "data/pop_manga_collection_physique.sql",
                "data/pop_manga_collection_coherente.sql",
                "data/pop_num_manquant.sql",
                "data/pop_manga_num_manquant.sql"
            ]

        dotenv.load_dotenv()

        schema = os.environ["POSTGRES_SCHEMA"]

        create_schema = f"DROP SCHEMA IF EXISTS {schema} CASCADE; CREATE SCHEMA {schema};"

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Exécuter la réinitialisation du schéma
                    cursor.execute(create_schema)

                    # Pour chaque fichier SQL dans la liste, on le lit et l'exécute
                    for file_path in sql_files:
                        with open(file_path, encoding="utf-8") as sql_file:
                            sql_as_string = sql_file.read()
                            cursor.execute(sql_as_string)
        except Exception as e:
            logging.info(e)
            raise


"""
        # Appliquer le hashage des mots de passe à chaque joueur
        joueur_service = JoueurService()
        for j in joueur_service.lister_tous(inclure_mdp=True):
            joueur_service.modifier(j)

        return True
"""

if __name__ == "__main__":
    ResetDatabase().lancer()
    ResetDatabase().lancer(True)
