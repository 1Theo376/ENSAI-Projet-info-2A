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
