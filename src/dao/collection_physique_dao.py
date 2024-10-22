import logging


from dao.db_connection import DBConnection
from collection_phys import Collection_physique
from manga_possede import MangaPossede


class CollectionPhysiqueDAO():
    """Classe contenant les méthodes pour accéder aux collections du joueur"""

    # def trouver_par_idphys(self, id_collection) -> Collection_physique:
    #    """trouver une collectionr grace à son id
    #
    #        Parameters
    #        ----------
    #        id_collection : int
    #            numéro id de la collection que l'on souhaite trouver
    #
    #        Returns
    #        -------
    #        Colection : Collection_physique
    #            renvoie la collection que l'on cherche par id
    #        """
    #        try:
    #            with DBConnection().connection as connection:
    #                with connection.cursor() as cursor:
    #                    cursor.execute(
    #                        "SELECT *                           "
    #                        "  FROM collection_physique                     "
    #                        " WHERE id_collection = %(id)s;  ",
    #                        {"id": id_collection},
    #                    )
    #                    res = cursor.fetchone()
    #        except Exception as e:
    #           logging.info(e)
    #            raise
    #
    #        Collection = None
    #        if res:
    #            Collection = Collection_physique(
    #                id_collection_coherente=res["id_collection"],
    #                titre_collection=res["titre_collection"],
    #            desc_collection=res["desc_collection"],
    #        )
    #
    #    return Collection

    def supprimer_collectionphys(self, CollectionP: Collection_physique) -> bool:
        """Suppression d'une collection dans la base de données

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
                        "DELETE FROM collection_physique                  "
                        " WHERE id_collec_coherente=%(id)s      ",
                        {"id": CollectionP.id_collection},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def créer_collectionphys(self, CollectionP: Collection_physique) -> bool:
        """Creation d'un joueur dans la base de données

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
                        "INSERT INTO collection_physique (id_collec_coherente, titre_collection, description_collection) VALUES"
                        "(%(id)s, %(titre)s, %(desc)s) "
                        "  RETURNING id; ",
                        {
                            "id": CollectionP.id_collectionphysique,
                            "titre": CollectionP.titre_collection,
                            "desc": CollectionP.desc_collection
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            CollectionP.id = res["id"]
            created = True

        return created

    def supprimer_mangaposs(self, CollectionP: Collection_physique, MangaPoss: MangaPossede) -> bool:
        """Suppression d'un manga d'une collection

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
                        "DELETE FROM association_manga_collection_physique                 "
                        " WHERE (id_collec_coherente=%(id_collec_coherente)s and id_manga_physique=%(idm)s ",
                        {"id_collec_coherente": CollectionP.id_collectionphysique,
                         "idm": MangaPoss.id_mangapossede},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0

    def ajouter_mangaposs(self, CollectionP: Collection_physique, MangaPoss: MangaPossede) -> bool:
        """Ajout d'un manga dans une collection

        Parameters
        ----------
        user : Utilisateur

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
                        "INSERT INTO association_manga_collection_physique(id_collec_physique, id_manga_physique) VALUES"
                        "(%(idc)s, %(idm)s) "
                        "  RETURNING id_collec_physique, id_manga_physique; ",
                        {
                            "idc": CollectionP.id_collectioncoherente,
                            "idm": MangaPoss.id_mangapossede
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            CollectionP.id = res["id_collec_physique"]
            MangaPoss.id_mangapossede = res["id_manga_physique"]
            created = True

        return created
