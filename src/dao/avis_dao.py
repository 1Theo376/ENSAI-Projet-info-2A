import logging


from dao.db_connection import DBConnection
from avis import Avis


class AvisDAO:
    def creer_avis(self, avis) -> bool:
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
            with DBConnection() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO avis (id_avis, texte) VALUES "
                        "(%(id_avis)s, %(texte)s) RETURNING id_avis;",
                        {
                            "id_avis": avis.id_avis,
                            "texte": avis.texte,
                        },
                    )
                    res = cursor.fetchone()

        except Exception as e:
            logging.info(e)

        created = False
        if res:
            avis.id_avis = res["id"]
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
