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

    def nb_volume_manga(self, nom):
        """trouver le nombre de volumes d'un manga avec son nom

        Parameters
        ----------
        nom : str
            nom du manga

           Returns
           -------
           volumes : int
               renvoie le nombre de volumes du manga
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT volumes                   "
                        "FROM manga                                 "
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
        """Trouve le manga possédé d'un utilisateur à partir de son nom
        Parameters
        ----------
        titre : str
            titre du manga
        id_collec_phys : int
            identifiant unique de la collection physique
        Returns
        -------
        manga_possede : MangaPossede
            renvoie le manga possédé de l'utilisateur
        """
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
            liste.append(elt["num_manquant"])
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

    def ajouter_num_manquant(self, num_manquant) -> bool:  # à voir
        """Ajout des numéros manquants d'un manga possédé dans la base de données
        Parameters
        ----------
        num_manquant : int
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
                        "INSERT INTO num_manquant(num_manquant) VALUES "
                        "(%(num_manquant)s) "
                        "  RETURNING id_num_manquant ; ",
                        {
                            "num_manquant": num_manquant,
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
        created = False
        if res:
            return res["id_num_manquant"]
        return created

    def ajouter_ass_num_manquant(
        self, id_manga_p, id_num_manquant
    ) -> bool:  # fusionner les deux fonctions ???
        """Ajout des numéro manquants d'un manga possédé dans la base de données
        Parameters
        ----------
        id_manga_p : int
            identifiant unique du manga possédé
        id_num_manquant : int
            identifiant unique des numéro manquants
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
                        "INSERT INTO association_manga_num_manquant(id_manga_p,id_num_manquant) "
                        " VALUES (%(id_manga_p)s,%(id_num_manquant)s) "
                        "  RETURNING id_manga_p, id_num_manquant; ",
                        {"id_num_manquant": id_num_manquant, "id_manga_p": id_manga_p},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
        created = False
        if res:
            created = True
        return created

    def trouver_manga_possede_id(self, id_p):
        """Trouve le manga possédé à partir de son identifiant
        Parameters
        ----------
        id_p : int
            identifiant unique du manga possédé
        Returns
        -------
        manga_possede : MangaPossede
            renvoie le manga possédé
        """
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
            liste.append(elt["num_manquant"])
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

    def trouver_id_num_manquant_id(self, id_p):
        """trouve les numéro manquants d'un manga possédé dans la base de données
        Parameters
        ----------
        id_p : int
            identifiant unique du manga possédé
        Returns
        -------
        list : list[int]
            liste des numéros manquants d'un manga possédé
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_num_manquant FROM num_manquant as mq            "
                        "left join association_manga_num_manquant using(id_num_manquant)      "
                        "left join manga_possede using(id_manga_p)                "
                        "WHERE id_manga_p = %(id_manga_p)s;                   ",
                        {"id_manga_p": id_p},
                    )
                    res2 = cursor.fetchall()
                    logging.info(f"Résultats de la recherche : {res2}")
        except Exception as e:
            logging.info(e)
            raise
        liste = []
        for elt in res2:
            liste.append(elt["id_num_manquant"])
        logging.info(f"Liste des numéros manquants : {liste}")
        return liste

    def supprimer_num_manquant(self, idnm) -> bool:
        """Suppression d'un numéro manquant dans la base de donnée

        Parameters
        ----------
        idnm : int
            identifiant unique du numéro manquant

        Returns
        -------
        True si le numéro manquant a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le manga d'une collection
                    cursor.execute(
                        "DELETE FROM num_manquant                 "
                        " WHERE id_num_manquant = %(idnm)s ;",
                        {
                            "idnm": idnm,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise
        return res > 0
