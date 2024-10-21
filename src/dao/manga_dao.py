import logging


from dao.db_connection import DBConnection
from manga import Manga


class MangaDao:
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
                auteurs=res["auteurs"],
                themes=res["themes"],
                genre=res["genre"],
            )
        return manga

    def lister_tous(self) -> list[Manga]:
        """lister tous les mangas

        Parameters
        ----------
        None

        Returns
        -------
        liste_joueurs : list[Joueur]
            renvoie la liste de tous les joueurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM manga;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_manga = []

        if res:
            for row in res:
                manga = Manga(
                    id_manga=res["id_manga"],
                    titre=res["titre"],
                    synopsis=res["synopsis"],
                    auteurs=res["auteurs"],
                    themes=res["themes"],
                    genre=res["genre"],
                )

                liste_manga.append(manga)

        return liste_manga
