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
                        "INSERT INTO manga_possede (id_manga, num_dernier_acquis, statut) VALUES"
                        "(%(id_manga)s, %(num_dernier_acquis)s, %(num_manquant)s) "
                        "  RETURNING id_manga_p; ",
                        {
                            "id_manga": mangap.idmanga,
                            "num_dernier_acquis": mangap.num_dernier_acquis,
                            "statut": mangap.statut
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
