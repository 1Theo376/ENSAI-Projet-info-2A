import json
import logging
from utils.log_decorator import log
from utils.singleton import Singleton
from dao.db_connection import DBConnection
from business_object.manga import Manga


class MangaDao(metaclass=Singleton):
    """classe MangaDao"""

    def trouver_manga_par_id(self, id_manga) -> Manga:
        """Recherche et renvoie un manga par son id

        Parameters
        ---------
        id_manga: int
            numéro du manga qu'on veut rechercher

        Returns
        -------
        manga: Manga
            renvoie le manga
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "Select *",
                        "From manga",
                        "Where id_manga = %(id_manga)s ",
                        {"id_manga": id_manga},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        manga = None
        if res:
            manga = Manga(
                id_manga=res["id_manga"],
                titre=res["titre"],
                synopsis=res["synopsis"],
                auteur=res["auteur"],
                themes=res["themes"],
                genre=res["genre"],
            )
        return manga

    def trouver_manga_par_titre(self, titre):
        """Recherche et renvoie un manga par son titre

        Parameters
        ---------
        titre: str
            titre du manga qu'on veut rechercher

        Returns
        -------
        manga: Manga
            renvoie le manga
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "Select *",
                        "From manga",
                        "Where titre = %(titre)s ",
                        {"titre": titre},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        manga = None
        if res:
            manga = Manga(
                id_manga=res["id_manga"],
                titre=res["titre"],
                synopsis=res["synopsis"],
                auteur=res["auteur"],
                themes=res["themes"],
                genre=res["genre"],
            )
        return manga

    def rechercher_manga_par_titre(self, titr):
        """Recherche et renvoie un manga par son titre

        Parameters
        ---------
        titre: str
            titre du manga qu'on veut rechercher

        Returns
        -------
        liste_mangas : list[Manga]
           renvoie une liste de mangas correspondant au titre recherché
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_manga, titre, synopsis "
                        "FROM manga "
                        "WHERE titre LIKE %(titre)s;",
                        {"titre": "%" + titr + "%"},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_mangas = []

        if res:
            for row in res:
                manga = Manga(
                    id_manga=row["id_manga"],
                    titre=row["titre"],
                    synopsis=row["synopsis"],
                    auteur=None,
                    themes=None,
                    genre=None,
                )
                liste_mangas.append(manga)

        return liste_mangas

    @log
    def inserer_mangas(self, fichier):
        """Insère les mangas, les auteurs, les genres et les themes dans la base de données"""
        with open(fichier, "r", encoding="utf-8") as f:
            mangas_data = json.load(f)
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Réinitialiser les IDs
                    cursor.execute("TRUNCATE TABLE manga RESTART IDENTITY CASCADE;")
                    cursor.execute("TRUNCATE TABLE theme RESTART IDENTITY CASCADE;")
                    cursor.execute("TRUNCATE TABLE auteur RESTART IDENTITY CASCADE;")
                    cursor.execute("TRUNCATE TABLE genre RESTART IDENTITY CASCADE;")

                    # Dictionnaires pour vérfier les doublons des noms des thèmes/auteurs/genres
                    theme_id_map = {}
                    author_id_map = {}
                    genre_id_map = {}

                    # Insertion des mangas
                    for manga in mangas_data:
                        if not manga[0]:
                            continue
                        titre = manga[0]
                        volumes = manga[1]
                        publication = manga[3]["string"]
                        synopsis = manga[4]
                        cursor.execute(
                            "INSERT INTO manga(titre, volumes, publication, synopsis)"
                            "VALUES (%(titre)s, %(volumes)s, %(publication)s, %(synopsis)s)"
                            "RETURNING id_manga;",
                            {
                                "titre": titre,
                                "volumes": volumes,
                                "publication": publication,
                                "synopsis": synopsis,
                            },
                        )
                        manga_id = cursor.fetchone()["id_manga"]  # Récupérer l'id du manga inséré

                        # Gestion des auteurs
                        for author in manga[5]:
                            if author not in author_id_map:
                                cursor.execute(
                                    """
                                    INSERT INTO auteur (name_auteur)
                                    VALUES (%s)
                                    RETURNING id_auteur;
                                    """,
                                    (author,),
                                )
                                res = cursor.fetchone()["id_auteur"]
                                if res:
                                    author_id_map[author] = res

                            cursor.execute(
                                """
                                INSERT INTO association_manga_auteur(id_manga, id_auteur)
                                VALUES (%(id_manga)s, %(id_auteur)s);
                                """,
                                {
                                    "id_manga": manga_id,
                                    "id_auteur": author_id_map[author],
                                },
                            )

                        # Gestion des thèmes
                        for theme in manga[6]:
                            if theme not in theme_id_map:
                                cursor.execute(
                                    """
                                    INSERT INTO theme (theme_name)
                                    VALUES (%s)
                                    RETURNING id_theme;
                                    """,
                                    (theme,),
                                )
                                res = cursor.fetchone()["id_theme"]
                                if res:
                                    theme_id_map[theme] = res

                            cursor.execute(
                                """
                                INSERT INTO association_manga_theme(id_manga, id_theme)
                                VALUES (%(id_manga)s, %(id_theme)s);
                                """,
                                {
                                    "id_manga": manga_id,
                                    "id_theme": theme_id_map[theme],
                                },
                            )

                        # Gestion des genres
                        for genre in manga[7]:
                            if genre not in genre_id_map:
                                cursor.execute(
                                    """
                                    INSERT INTO genre (genre_name)
                                    VALUES (%s)
                                    RETURNING id_genre;
                                    """,
                                    (genre,),
                                )
                                res = cursor.fetchone()["id_genre"]
                                if res:
                                    genre_id_map[genre] = res
                            cursor.execute(
                                """
                                INSERT INTO association_manga_genre(id_manga, id_genre)
                                VALUES (%(id_manga)s, %(id_genre)s);
                                """,
                                {
                                    "id_manga": manga_id,
                                    "id_genre": genre_id_map[genre],
                                },
                            )

                # Commit les modifications après l'insertion
                connection.commit()

        except Exception as e:
            logging.error(f"Erreur lors de l'insertion des mangas : {e}")
            raise

    @log
    def supprimer_toutes_les_donnees(self) -> bool:
        """Suppression de tous les mangas, thèmes, auteurs et genres dans la base de données

        Returns
        -------
        bool
            True si des données ont bien été supprimées, False sinon
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer toutes les associations d'abord (pour respecter les contraintes de clé étrangère)
                    cursor.execute("DELETE FROM association_manga_auteur")
                    cursor.execute("DELETE FROM association_manga_theme")
                    cursor.execute("DELETE FROM association_manga_genre")

                    # Supprimer tous les mangas
                    cursor.execute("DELETE FROM manga")
                    manga_count = cursor.rowcount  # Nombre de mangas supprimés

                    # Supprimer tous les thèmes
                    cursor.execute("DELETE FROM theme")
                    theme_count = cursor.rowcount  # Nombre de thèmes supprimés

                    # Supprimer tous les auteurs
                    cursor.execute("DELETE FROM auteur")
                    auteur_count = cursor.rowcount  # Nombre d'auteurs supprimés

                    # Supprimer tous les genres
                    cursor.execute("DELETE FROM genre")
                    genre_count = cursor.rowcount  # Nombre de genres supprimés

        except Exception as e:
            logging.info(f"Erreur lors de la suppression des données : {e}")
            raise

        # Vérifier si au moins une table a été modifiée
        total_supprime = manga_count + theme_count + auteur_count + genre_count
        return total_supprime > 0


test = MangaDao()
test.supprimer_toutes_les_donnees()
test.inserer_mangas("mangas.json")
