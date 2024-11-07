import logging

from vues.session import Session
from dao.db_connection import DBConnection
from business_object.CollectionCoherente import CollectionCoherente
from business_object.manga import Manga


class CollectionCoherenteDAO:
    """Classe contenant les méthodes pour accéder aux collections du joueur"""

    # def trouver_par_id(self, id_collection) -> CollectionCoherente:
    #    """trouver une collectionr grace à son id
    #
    #    Parameters
    #    ----------
    #    id_collection : int
    #        numéro id de la collection que l'on souhaite trouver
    #
    #       Returns
    #       -------
    #       Colection : CollectionCoherente
    #           renvoie la collection que l'on cherche par id
    #       """
    #       try:
    #          with DBConnection().connection as connection:
    #               with connection.cursor() as cursor:
    #                   cursor.execute(
    #                      "SELECT id_utilisateur, titre_collection, description_collection "
    #                       "  FROM collection_coherente                      "
    #                       " JOIN association_manga_collection_coherente u
    # sing(id_collec_coherente)"
    #                      "JOIN manga using(id_manga)"
    #                       " WHERE id_collection = %(id)s;  ",
    #                       {"id": id_collection},
    #                   )
    #                  res = cursor.fetchone()
    #       except Exception as e:
    #           logging.info(e)
    #           raise
    #
    #       Collection = None
    #      if res:
    #           Collection = CollectionCoherente(
    #                id_collection_coherente=res["id_collection"],
    #               titre_collection=res["titre_collection"],
    #               desc_collection=res["desc_collection"],
    #               Liste_manga=None,
    #
    #      return Collection

    def supprimer_collection(self, CollectionC: CollectionCoherente) -> bool:
        """Suppression d'une collection coherente dans la base de données

        Parameters
        ----------


        Returns
        -------
            True si la collection a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer la collection d'un utilisateur
                    cursor.execute(
                        "DELETE FROM collection_coherente                  "
                        " WHERE id_collec_coherente=%(id)s      ",
                        {"id": CollectionC.id_collection},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def creer_collection(self, CollectionC: CollectionCoherente) -> bool:
        """Creation d'une collectiopn coherente dans la base de données

        Parameters
        ----------


        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO CollectionCoherente(id_utilisateur, titre_collection, description_collection) VALUES"
                        "(%(id_utilisateur)s, %(titre)s, %(desc)s) "
                        "  RETURNING id_collec_coherente; ",
                        {
                            "id_utilisateur": Session().utilisateur.id,
                            "titre": CollectionC.titre_collection,
                            "desc": CollectionC.desc_collection,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            CollectionC.id = res["id_collec_coherente"]
            created = True

        return created

    def supprimer_manga(self, CollectionC: CollectionCoherente, MangaC: Manga) -> bool:
        """Suppression d'un manga d'une collection coherente

        Parameters
        ----------


        Returns
        -------
            True si le manga a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le manga d'une collection
                    cursor.execute(
                        "DELETE FROM association_manga_collection_coherente                 "
                        " WHERE (id_collec_coherente=%(id_collec_coherente)s and id_manga=%(idm)s ",
                        {
                            "id_collec_coherente": CollectionC.id_collectioncoherente,
                            "idm": MangaC.id_manga,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0

    def ajouter_manga(self, CollectionC: CollectionCoherente, MangaC: Manga) -> bool:
        """Ajout d'un manga dans une collection coherente

        Parameters
        ----------


        Returns
        -------
        created : bool
            True si la création est un succès
            False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO association_manga_collection_coherente(id_collec_coherente, id_manga) VALUES"
                        "(%(idc)s, %(idm)s) "
                        "  RETURNING id_collec_coherente, id_manga; ",
                        {"idc": CollectionC.id_collectioncoherente, "idm": MangaC.id_manga},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            CollectionC.id = res["id_collec_coherente"]
            MangaC.id_manga = res["id_manga"]
            created = True

        return created
