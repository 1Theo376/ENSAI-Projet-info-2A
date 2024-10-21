import logging


from dao.db_connection import DBConnection
from CollectionCoherente import CollectionCoherente


class CollectionDAO():
    """Classe contenant les méthodes pour accéder aux collections du joueur"""

    def trouver_par_id(self, id_collection) -> CollectionCoherente:
        """trouver une collectionr grace à son id

        Parameters
        ----------
        id_collection : int
            numéro id de la collection que l'on souhaite trouver

        Returns
        -------
        Colection : CollectionCoherente
            renvoie la collection que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM CollectionCoherente                      "
                        " WHERE id_collection = %(id)s;  ",
                        {"id": id_collection},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        Collection = None
        if res:
            Collection = CollectionCoherente(
                id_collection_coherente=res["id_collection"],
                titre_collection=res["titre_collection"],
                desc_collection=res["desc_collection"],
            )

        return Collection

    def supprimer(self, CollectionCoherente) -> bool:
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
                        "DELETE FROM CollectionCoherente                  "
                        " WHERE id=%(id)s      ",
                        {"id": CollectionCoherente.id_collection},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0
