import logging


from dao.db_connection import DBConnection
from utilisateur import Utilisateur


class JoueurDao():
    """Classe contenant les méthodes pour accéder aux Joueurs de la base de données"""

    def creer(self, user) -> bool:
        """Creation d'un joueur dans la base de données

        Parameters
        ----------
        user : Utilisateur

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
                        "INSERT INTO user(id, mdp, pseudo) VALUES"
                        "(%(id)s, %(mdp)s, %(pseudo)s) "
                        "  RETURNING id; ",
                        {
                            "id": user.id,
                            "mdp": user.mdp,
                            "pseudo": user.pseudo
                        },
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            user.id = res["id"]
            created = True

        return created

    def trouver_par_id(self, id) -> Utilisateur:
        """trouver un joueur grace à son id

        Parameters
        ----------
        id : int
            numéro id du joueur que l'on souhaite trouver

        Returns
        -------
        user : Utilisateur
            renvoie le joueur que l'on cherche par id
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM joueur                      "
                        " WHERE id = %(id)s;  ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        joueur = None
        if res:
            joueur = Utilisateur(
                id=res["id"],
                mdp=res["mdp"],
                pseudo=res["pseudo"],
            )

        return joueur

    def lister_tous(self) -> list[Utilisateur]:
        """lister tous les joueurs

        Parameters
        ----------
        None

        Returns
        -------
        liste_joueurs : list[Joueur]
            renvoie la liste de tous les joueurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM joueur;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_joueurs = []

        if res:
            for row in res:
                joueur = Utilisateur(
                    id=row["id"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"],
                )

                liste_joueurs.append(joueur)

        return liste_joueurs

    def modifier(self, joueur) -> bool:
        """Modification d'un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur

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
                        "UPDATE joueur                                      "
                        "   SET pseudo      = %(pseudo)s,                   "
                        "       mdp         = %(mdp)s,                      "
                        " WHERE id = %(id)s;                  ",
                        {
                            "pseudo": joueur.pseudo,
                            "mdp": joueur.mdp,
                            "id": joueur.id,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

        return res == 1

    def supprimer(self, joueur) -> bool:
        """Suppression d'un joueur dans la base de données

        Parameters
        ----------
        joueur : Joueur
            joueur à supprimer de la base de données

        Returns
        -------
            True si le joueur a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un joueur
                    cursor.execute(
                        "DELETE FROM joueur                  "
                        " WHERE id=%(id)s      ",
                        {"id": joueur.id},
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)
            raise

        return res > 0

    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """se connecter grâce à son pseudo et son mot de passe

        Parameters
        ----------
        pseudo : str
            pseudo du joueur que l'on souhaite trouver
        mdp : str
            mot de passe du joueur

        Returns
        -------
        joueur : Joueur
            renvoie le joueur que l'on cherche
        """
        res = None
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM joueur                      "
                        " WHERE pseudo = %(pseudo)s         "
                        "   AND mdp = %(mdp)s;              ",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        joueur = None

        if res:
            joueur = Utilisateur(
                pseudo=res["pseudo"],
                mdp=res["mdp"],
                id=res["id"],
            )

        return joueur
