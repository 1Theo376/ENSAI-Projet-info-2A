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
            with self.connecter() as connection:
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
            with DBConnection().connexion as connexion:
                with connexion.cursor() as cursor:
                    cursor.execute(
                        " SELECT *                           "
                        " FROM Avis                      "
                        " WHERE id_avis = %(id_avis)s;  ",
                        {"id_avis": id_avis},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

            if res:
                avis = Avis(id_avis=res["id_avis"], texte=res["texte"])

        return Avis

    def supprimer_avis(self, Avis) -> bool:
        """Suppression d'un avis dans la base de données

        Parameters
        -----------
            True si l'avis a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor as cursor:
                    cursor.execute(
                        "DELETE FROM Avis                           "
                        "WHERE id_avis= %(id_avis)s                      ",
                        {"id_avis": Avis.id_avis},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def consulter_avis(self, id_avis):
        """ Permet de consulter un avis de la base de données

        Parameters
        ------------
            Avis ou None
            Affiche l'avis que l'on recherche, ou None sinon
        """

        try:
            with DBConnection().connexion as connection:
                with connection.cursor as cursor:
                    cursor.execute(
                        
                    )    