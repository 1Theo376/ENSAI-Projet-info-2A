import logging
from dao.db_connection import DBConnection
from business_object.CollectionCoherente import CollectionCoherente
from business_object.manga import Manga
from dao.manga_dao import MangaDao


class CollectionCoherenteDAO:
    """Classe contenant les méthodes pour accéder aux collections du joueur"""

    def supprimer_collection(self, CollectionC: CollectionCoherente) -> bool:
        """Suppression d'une collection coherente dans la base de données

        Parameters
        ----------
        CollectionC: CollectionCoherente

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
                        " WHERE id_collec_coherente=%(id_collec_coherente)s      ",
                        {"id_collec_coherente": CollectionC.id_collectioncoherente},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def creer_collection(self, CollectionC: CollectionCoherente, idu: int) -> bool:
        """Creation d'une collectipn coherente dans la base de données

        Parameters
        ----------
        CollectionC: CollectionCoherente

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
                        "INSERT INTO collection_coherente(id_utilisateur, "
                        "titre_collection, description_collection) VALUES "
                        "(%(idu)s, %(titre)s, %(desc)s) "
                        "  RETURNING id_collec_coherente; ",
                        {
                            "idu": idu,
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
        CollectionC: CollectionCoherente

        MangaC: Manga

        Returns
        -------
        True si le manga a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM association_manga_collection_coherente                 "
                        " WHERE id_collec_coherente = %(id_collec_coherente)s AND "
                        " id_manga = %(id_manga)s ;",
                        {
                            "id_collec_coherente": CollectionC.id_collectioncoherente,
                            "id_manga": MangaC.id_manga,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0

    def ajouter_manga(self, idcollec: int, idmanga: int) -> bool:
        """Ajout d'un manga dans une collection coherente

        Parameters
        ----------
        idcollec: int

        idmanga: int

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
                        "INSERT INTO association_manga_collection_coherente( "
                        "id_collec_coherente, id_manga) VALUES"
                        "(%(idc)s, %(idm)s) "
                        "  RETURNING id_collec_coherente, id_manga; ",
                        {"idc": idcollec, "idm": idmanga},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            created = True

        return created

    def trouver_collec_cohe_id_user(self, id_utilisateur) -> CollectionCoherente:
        """trouver des collections grace à l'id de l'utilisateur

        Parameters
        ----------
        id_utilisateur : int
            numéro id de l'utilisateur

           Returns
           -------
           collections : List[CollectionCoherente]
               renvoie la liste de collection cohérente de l'utilisateur
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_collec_coherente, titre_collection, description_collection "
                        "  FROM collection_coherente                      "
                        " WHERE id_utilisateur = %(id_utilisateur)s;  ",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        collections = []
        if res:
            for elt in res:
                collections.append(
                    CollectionCoherente(
                        id_collectioncoherente=elt["id_collec_coherente"],
                        titre_collection=elt["titre_collection"],
                        desc_collection=elt["description_collection"],
                        Liste_manga=None,
                    )
                )
            return collections
        return None

    def trouver_collec_cohe_nom(self, nom, idu) -> CollectionCoherente:
        """trouver une collection grâce à son nom et à l'id de l'utilisateur

        Parameters
        ----------
        nom : str
            nom de la collection cohérente

        idu : int
            identifiant de l'utilisateur possédans la collection

           Returns
           -------
           collection : CollectionCoherente
               renvoie la collection cohérente correspondant au nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_collec_coherente, description_collection, id_manga "
                        "FROM collection_coherente         "
                        "LEFT JOIN association_manga_collection_coherente "
                        "USING(id_collec_coherente)  "
                        "LEFT JOIN manga USING(id_manga)       "
                        "WHERE titre_collection = %(titre_collection)s "
                        "and id_utilisateur = %(idu)s;                                ",
                        {"titre_collection": nom, "idu": idu},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        collection = None
        if res:
            L_mangas = []
            for elt in res:
                id = elt["id_collec_coherente"]
                desc = elt["description_collection"]
                if elt["id_manga"]:
                    L_mangas.append(MangaDao().trouver_manga_par_id(elt["id_manga"]))
            collection = CollectionCoherente(
                id_collectioncoherente=id,
                titre_collection=nom,
                desc_collection=desc,
                Liste_manga=L_mangas,
            )
        return collection

    def modifier_titre(self, id_collection: int, nouveau_titre: str) -> bool:
        """Modifier le titre d'une collection cohérente

        Parameters
        ----------
        id_collection : int
        identifiant de la collection

        nouveau_titre : str
        nouveau titre de la collection

        Returns
        -------
        True si la modification a bien été faite

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE collection_coherente                        "
                        "SET titre_collection = %(nouveau_titre)s           "
                        "WHERE id_collec_coherente = %(id_collection)s;     ",
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
        """Modifie la description d'une collection cohérente

        Parameters
        ----------
        id_collection : int
        identifiant de la collection

        nouvelle_desc : str
        nouvelle description de la collection

        Returns
        -------
        True si la modification a bien été faite

        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE collection_coherente                        "
                        "SET description_collection = %(nouvelle_desc)s           "
                        "WHERE id_collec_coherente = %(id_collection)s;     ",
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
