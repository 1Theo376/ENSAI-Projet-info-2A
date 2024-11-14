import logging

from dao.db_connection import DBConnection
from business_object.manga_possede import MangaPossede


class MangaPossedeDao:
    """classe MangaDao"""

    def ajouter_manga_p(self, mangap) -> bool:
        """Ajout d'un manga possédé dans la base de données

        Parameters
        ----------
        manga : MangaPossede

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
                        "INSERT INTO manga_possede(id_manga, num_dernier_acquis, statut) VALUES"
                        "(%(id_manga)s, %(num_dernier_acquis)s, %(statut)s) "
                        "  RETURNING id_manga_p; ",
                        {
                            "id_manga": mangap.idmanga,
                            "num_dernier_acquis": mangap.num_dernier_acquis,
                            "statut": mangap.statut,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            mangap.id_manga_p = res["id_manga_p"]
            created = True

        return created

    def modifier_num_dernier_acquis(self, utilisateur) -> bool:
        """Modification du dernier tome acquis dans la base de données
        Parameters
        ----------
        utilisateur : Utilisateur

        Returns
        -------
        created : bool
            True si la modification est un succès
            False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE utilisateur                                      "
                        "   SET pseudo      = %(pseudo)s,                   "
                        "       mdp         = %(mdp)s,                      "
                        " WHERE id = %(id)s;                  ",
                        {
                            "pseudo": utilisateur.pseudo,
                            "mdp": utilisateur.mdp,
                            "id": utilisateur.id,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    def nb_volume_manga(self, nom):
        """trouver une collection grâce à son nom

        Parameters
        ----------
        nom : str
            nom de la collection cohérente

           Returns
           -------
           collection : CollectionCoherente
               renvoie la collection cohérente correspondant au nom
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT volumes                   "
                        "FROM manga                                                     "
                        " WHERE titre = %(titre)s;                                ",
                        {"titre": nom},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        if res:
            volumes = res["volumes"]
        return volumes

    def trouver_manga_possede_collecphys(self, titre, id_collec_phys):
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_manga_p, id_manga, num_dernier_acquis, statut                "
                        "FROM manga_possede                                                      "
                        "left join manga using(id_manga)      "
                        "left join association_manga_collection_physique using(id_manga_p)      "
                        "left join collection_physique using(id_collec_physique)                "
                        "WHERE id_collec_physique = %(id_collec_physique)s                  "
                        "AND manga.titre = %(titre)s ;                   ",
                        {"id_collec_physique": id_collec_phys, "titre": titre},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT num_manquant FROM num_manquant as mq            "
                        "left join association_manga_num_manquant using(id_num_manquant)      "
                        "left join manga_possede using(id_manga_p)                "
                        "WHERE id_manga_p = %(id_manga_p)s;                   ",
                        {"id_manga_p": res["id_manga_p"]},
                    )
                    res2 = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise
        liste = []
        for elt in res2:
            liste.append(res2["num_manquant"])
        manga_possede = None
        if res:
            manga_possede = MangaPossede(
                id_manga_p=res["id_manga_p"],
                idmanga=res["id_manga"],
                num_dernier_acquis=res["num_dernier_acquis"],
                statut=res["statut"],
                num_manquant=liste,
            )
        return manga_possede

        def trouver_manga_possede_id(self, id_p):
            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT id_manga_p, id_manga, num_dernier_acquis, statut                "
                            "FROM manga_possede                                                      "
                            "WHERE id_manga_p = %(id_manga_p)s                  ",
                            {"id_manga_p": id_p},
                        )
                        res = cursor.fetchone()
            except Exception as e:
                logging.info(e)
                raise
            try:
                with DBConnection().connection as connection:
                    with connection.cursor() as cursor:
                        cursor.execute(
                            "SELECT num_manquant FROM num_manquant as mq            "
                            "left join association_manga_num_manquant using(id_num_manquant)      "
                            "left join manga_possede using(id_manga_p)                "
                            "WHERE id_manga_p = %(id_manga_p)s;                   ",
                            {"id_manga_p": res["id_manga_p"]},
                        )
                        res2 = cursor.fetchall()
            except Exception as e:
                logging.info(e)
                raise
            liste = []
            for elt in res2:
                liste.append(res2["num_manquant"])
            manga_possede = None
            if res:
                manga_possede = MangaPossede(
                    id_manga_p=res["id_manga_p"],
                    idmanga=res["id_manga"],
                    num_dernier_acquis=res["num_dernier_acquis"],
                    statut=res["statut"],
                    num_manquant=liste,
                )
            return manga_possede
