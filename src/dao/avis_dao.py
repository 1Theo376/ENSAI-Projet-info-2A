import logging


from dao.db_connection import DBConnection
from business_object.avis import Avis


class AvisDAO:
    def creer_avis(self, avis, id_user, id_manga) -> bool:
        """Créer un nouvel avis dans la base de données

        Parameters
        ----------
        avis : Avis
            L'avis à créer

        Returns
        -------
        created : bool
            True si la création est un succès, False sinon
        """
        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO avis(id_utilisateur, id_manga, texte) VALUES "
                        "(%(id_utilisateur)s, %(id_manga)s, %(texte)s) RETURNING id_avis;",
                        {
                            "id_utilisateur": id_user,
                            "id_manga": id_manga,
                            "texte": avis.texte,
                        },
                    )
                    res = cursor.fetchone()
                    connection.commit()  # Commit pour confirmer l'insertion

        except Exception as e:
            logging.error(f"Erreur lors de l'insertion de l'avis : {e}")
            connection.rollback()
            return False

        created = False
        if res:
            avis.id_avis = res["id_avis"]
            created = True

        return created

    def trouver_avis_par_id(self, id_avis) -> Avis:
        """
        permet de trouver un avis à l'aide de son id

        Parameters
        -----------
        id_avis : int
            Identifiant de l'avis

        Returns
        --------
            avis ou None
            Renvoie l'avis que l'on cherche par id ou une None si l'avis n'existe pas
        """
        avis = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                           "
                        " FROM avis                      "
                        " WHERE id_avis = %(id_avis)s;  ",
                        {"id_avis": id_avis},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        if res:
            avis = Avis(id_avis=res["id_avis"], texte=res["texte"])

        return avis

    def trouver_avis_par_titre_manga(self, titre) -> Avis:
        """
        permet de trouver un avis à l'aide de son id

        Parameters
        -----------
        id_avis : int
            Identifiant de l'avis

        Returns
        --------
            avis ou None
            Renvoie l'avis que l'on cherche par id ou une None si l'avis n'existe pas
        """
        avis = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "select id_avis, texte                                   "
                        "from manga left join avis using(id_manga)      "
                        "where titre = %(titre)s;                         ",
                        {"titre": titre},
                    )
                    res = cursor.fetchall()

        except Exception as e:
            logging.info(e)
            raise

        liste_avis = []

        if res:
            for row in res:
                avis = Avis(id_avis=row["id_avis"], texte=row["texte"])
                liste_avis.append(avis)

        return avis

    def supprimer_avis(self, avis) -> bool:
        """Suppression d'un avis dans la base de données

        Parameters
        -----------
            avis : Avis

        Returns
        ---------
            True si l'avis a bien été supprimé, false sinon
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM avis                           "
                        "WHERE id_avis= %(id_avis)s                      ",
                        {"id_avis": avis.id_avis},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def modifier_avis(self, avis) -> bool:
        """Modification d'un avis dans la base de données
        Parameters
        ----------
        avis : Avis

        Returns
        -------
        True si l'avis a bien été modifié, False sinon
        """

        res = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE avis                                     "
                        "SET texte = %(texte)s,                        "
                        "   WHERE id_avis      = %(id_avis)s,        ",
                        {
                            "texte": avis.texte,
                            "id_avis": avis.id_avis,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

            return res == 1

    def consulter_avis(self, id_avis):
        """Consultation de l'avis voulu
        Parameters
        ----------
        id_avis : int

        Returns
        --------
        Avis ou None
        """

        Avis = None

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                       "
                        "FROM avis                      "
                        "WHERE id_avis = %(id_avis)s,     ",
                        {"id_avis": id_avis},
                    )
                    res = cursor.fetchone()

                    if res:
                        avis = Avis(id_avis=res["id_avis"], texte=res["texte"])

        except Exception as e:
            logging.info(e)
            raise

        return avis

    def recuperer_avis_utilisateur(self, id_utilisateur):
        """Récupère tous les avis d'un utilisateur"""
        avis_liste = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM avis WHERE id_utilisateur = %(id_utilisateur)s ORDER BY id_avis;",
                        {"id_utilisateur": id_utilisateur},
                    )
                    result = cursor.fetchall()
                    for row in result:
                        avis = Avis(id_avis=row["id_avis"], texte=row["texte"])
                        avis2 = [avis]+[row["id_manga"]]
                        avis_liste.append(avis2)
        except Exception as e:
            logging.info(e)
            raise
        return avis_liste

    def recuperer_avis_manga(self, id_manga):
        avis_liste = []
        liste_manga =[]
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM avis WHERE id_manga = %(id_manga)s ORDER BY id_avis;",
                        {"id_manga": id_manga},
                    )
                    result = cursor.fetchall()
                    for row in result:
                        avis = Avis(id_avis=row["id_avis"], texte=row["texte"])
                        avis_liste.append(avis)
                        liste_manga.append(row["id_manga"])
        except Exception as e:
            logging.info(e)
            raise
        return avis_liste, liste_manga
