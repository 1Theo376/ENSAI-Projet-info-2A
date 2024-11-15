import logging

from vues.session import Session
from dao.db_connection import DBConnection
from business_object.collection_phys import Collection_physique
from business_object.manga_possede import MangaPossede
from dao.manga_dao import MangaDao
from dao.manga_possede_dao import MangaPossedeDao


class CollectionPhysiqueDAO:
    """Classe contenant les méthodes pour accéder aux collections de l'utilisateur"""

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
        """Suppression d'une collection physique dans la base de données

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

    def creer_collectionphys(self, CollectionP: Collection_physique) -> bool:
        """Creation d'une collection physique dans la base de données

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
                        "INSERT INTO collection_physique (id_utilisateur, titre_collection, description_collection) VALUES"
                        "(%(id_utilisateur)s, %(titre)s, %(description_collection)s) "
                        "  RETURNING id_collec_physique; ",
                        {
                            "id_utilisateur": Session().utilisateur.id,
                            "titre": CollectionP.titre_collection,
                            "description_collection": CollectionP.description_collection,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            CollectionP.id = res["id_collec_physique"]
            created = True

        return created

    def supprimer_mangaposs(
        self, CollectionP: Collection_physique, MangaPoss: MangaPossede
    ) -> bool:
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
                        " WHERE (id_collec_physique = %(id_collec_physique)s and id_manga_p = %(id_manga_p)s)",
                        {
                            "id_collec_physique": CollectionP.id_collectionphysique,
                            "id_manga_p": MangaPoss.id_manga_p,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0

    def ajouter_mangaposs(self, idcoll: Collection_physique, idmanga: MangaPossede) -> bool:
        """Ajout d'un manga dans une collection

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
                        "INSERT INTO association_manga_collection_physique(id_collec_physique, id_manga_p) VALUES "
                        "(%(idc)s, %(idm)s) "
                        "  RETURNING id_collec_physique, id_manga_p; ",
                        {
                            "idc": idcoll,
                            "idm": idmanga,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            idcoll = res["id_collec_physique"]
            idmanga = res["id_manga_p"]
            created = True

        return created

    def trouver_collec_phys_id_user(self, id_utilisateur) -> Collection_physique:
        """trouver des collections grace à l'id de l'utilisateur

        Parameters
        ----------
        id_utilisateur : int
            numéro id de l'utilisateur

           Returns
           -------
           collections : List[Collection_physique]
               renvoie la liste de collection physique de l'utilisateur
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_collec_physique, titre_collection, description_collection, id_manga_p "
                        "FROM collection_physique                     "
                        "LEFT JOIN association_manga_collection_physique USING(id_collec_physique) "
                        "LEFT JOIN manga_possede USING(id_manga_p)        "
                        " WHERE id_utilisateur = %(id_utilisateur)s;  ",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        if not res:
            return None
        L_mangas = []
        id_collectionphysique = res[0]["id_collec_physique"]
        titre_collection = res[0]["titre_collection"]
        description_collection = res[0]["description_collection"]
        collection = None
        for elt in res:
            if elt["id_manga_p"]:
                manga_possede = MangaPossedeDao().trouver_manga_possede_id(elt["id_manga_p"])
                L_mangas.append(manga_possede)

        collection = Collection_physique(
            id_collectionphysique=id_collectionphysique,
            titre_collection=titre_collection,
            description_collection=description_collection,
            Liste_manga=L_mangas,
        )
        return collection

    def trouver_collec_phys_nom(self, nom):
        """trouver une collection grâce à son nom

        Parameters
        ----------
        nom : str
            nom de la collection physique

           Returns
           -------
           collection : CollectionPhysique
               renvoie la collection physique correspondant au nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_collec_physique, description_collection, id_manga_p                   "
                        "FROM collection_physique                                                     "
                        "LEFT JOIN association_manga_collection_physique USING(id_collec_physique)    "
                        "LEFT JOIN manga_possede Using(id_manga_p)                                               "
                        " WHERE titre_collection = %(titre_collection)s;                                ",
                        {"titre_collection": nom},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        collection = None
        if res:
            L_mangas = []
            for elt in res:
                id_c = elt["id_collec_physique"]
                desc = elt["description_collection"]
                if elt["id_manga_p"]:
                    L_mangas.append(MangaDao().trouver_manga_par_id(elt["id_manga_p"]))
                else:
                    L_mangas = []
            collection = Collection_physique(
                id_collectionphysique=id_c,
                titre_collection=nom,
                description_collection=desc,
                Liste_manga=L_mangas,
            )
        return collection

    def modifier_titre(self, id_collection: int, nouveau_titre: str) -> bool:
        """Modifier le titre d'une collection physique

        Parameters
        ----------
        id_collection : int
        identifiant de la collection

        nouveau_titre : str
        nouveau titre de la collection

        Returns
        -------

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE collection_physique                       "
                        "SET titre_collection = %(nouveau_titre)s           "
                        "WHERE id_collec_physique = %(id_collection)s;     ",
                        {
                            "id_collection": id_collection,
                            "nouveau_titre": nouveau_titre,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0

    def modifier_desc(self, id_collection: int, nouvelle_desc: str) -> bool:
        """Modifie la description d'une collection physique

        Parameters
        ----------
        id_collection : int
        identifiant de la collection

        nouvelle_desc : str
        nouvelle description de la collection

        Returns
        -------

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE collection_physique                       "
                        "SET description_collection = %(nouvelle_desc)s           "
                        "WHERE id_collec_physique = %(id_collection)s;     ",
                        {
                            "id_collection": id_collection,
                            "nouvelle_desc": nouvelle_desc,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0
