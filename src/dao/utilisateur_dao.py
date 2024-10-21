import logging


from dao.db_connection import DBConnection
from utilisateur import Utilisateur


class UtilisateurDao():
    """Classe contenant les méthodes pour accéder aux Utilisateurs de la base de données"""

    def creer(self, user) -> bool:
        """Creation d'un utilisateur dans la base de données

        Parameters
        ----------
        user : utilisateur

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

    def modifier(self, utilisateur) -> bool:
        """Modification d'un utilisateur dans la base de données
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

"""
    def trouver_par_id(self, id) -> Utilisateur:
        trouver un joueur grace à son id

        Parameters
        ----------
        id : int
            numéro id de l'utilisateur que l'on souhaite trouver

        Returns
        -------
        user : Utilisateur
            renvoie l'utilisateur que l'on cherche par id

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                           "
                        "  FROM utilisateur                      "
                        " WHERE id = %(id)s;  ",
                        {"id": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        utilisateur = None
        if res:
            utilisateur = Utilisateur(
                id=res["id"],
                mdp=res["mdp"],
                pseudo=res["pseudo"],
            )

        return utilisateur
"""

    def lister_tous(self) -> list[Utilisateur]:
        """lister tous les joueurs

        Parameters
        ----------
        None

        Returns
        -------
        liste_utilisateur : list[Joueur]
            renvoie la liste de tous les utilisateurs dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT *                              "
                        "  FROM utilisateur;                        "
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_utilisateur = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    id=row["id"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"],
                )

                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs

    def supprimer(self, utilisateur) -> bool:
        """Suppression d'un utilisateur dans la base de données

        Parameters
        ----------
        utilisateur : Utilisateur
            utilisateur à supprimer de la base de données

        Returns
        -------
            True si le utilisateur a bien été supprimé
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer le compte d'un utilisateur
                    cursor.execute(
                        "DELETE FROM utilisateur                  "
                        " WHERE id=%(id)s      ",
                        {"id": utilisateur.id},
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
