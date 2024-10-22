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
                    res = cursor.fetchone
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

    def rechercher_manga_par_titre(self, titre):
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
                        "Select titre",
                        "From manga",
                        "Where titre LIKE '%(titre)%' ",
                        {"titre": titre},
                    )
                    res = cursor.fetchone
        except Exception as e:
            logging.info(e)
            raise
        liste_manga = []
        if res:
            liste_manga = [res[titre]]
        return liste_manga
