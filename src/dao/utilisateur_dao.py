import logging
from dao.db_connection import DBConnection
from business_object.utilisateur import Utilisateur
from utils.log_decorator import log
from utils.singleton import Singleton


class UtilisateurDao(metaclass=Singleton):
    """Classe contenant les méthodes pour accéder aux Utilisateurs de la base de données"""

    @log
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
                        "INSERT INTO utilisateur(pseudo, mdp) VALUES"
                        "( %(pseudo)s, %(mdp)s) "
                        "  RETURNING id_utilisateur; ",
                        {"pseudo": user.pseudo, "mdp": user.mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        created = False
        if res:
            user.id = res["id_utilisateur"]
            created = True

        return created

    @log
    def supprimer(self, utilisateur) -> bool:
        """Suppression d'un utilisateur dans la base de données.

        Parameters
        ----------
        utilisateur : Utilisateur
            Utilisateur à supprimer de la base de données.

        Returns
        -------
        bool
            True si l'utilisateur a bien été supprimé, False sinon.
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    # Supprimer les enregistrements liés dans la table avis
                    cursor.execute(
                        "DELETE FROM avis WHERE id_utilisateur = %(id_utilisateur)s",
                        {"id_utilisateur": utilisateur.id},
                    )

                    # Supprimer l'utilisateur
                    cursor.execute(
                        "DELETE FROM utilisateur WHERE id_utilisateur = %(id_utilisateur)s",
                        {"id_utilisateur": utilisateur.id},
                    )

                    res = cursor.rowcount
        except Exception as e:
            logging.info(f"Erreur lors de la suppression : {e}")
            raise

        return res > 0

    @log
    def lister_tous(self) -> list[Utilisateur]:
        """lister tous les utilisateurs

        Parameters
        ----------
        None

        Returns
        -------
        liste_utilisateur : list[Utilisateur]
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

        liste_utilisateurs = []

        if res:
            for row in res:
                utilisateur = Utilisateur(
                    id=row["id_utilisateur"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"],
                )

                liste_utilisateurs.append(utilisateur)

        return liste_utilisateurs

    @log
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
                        "  FROM utilisateur                      "
                        " WHERE pseudo = %(pseudo)s         "
                        "   AND mdp = %(mdp)s;              ",
                        {"pseudo": pseudo, "mdp": mdp},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)

        user = None

        if res:
            user = Utilisateur(
                id=res["id_utilisateur"],
                pseudo=res["pseudo"],
                mdp=res["mdp"],
            )

        return user

    @log
    def rechercher_tous_pseudo(self, pseud) -> list[Utilisateur]:
        """rechercher des utilisateur à partir d'une chaîne de caractère

        Parameters
        ----------
        pseudo: int
            pseudo de l'utilisateur

        Returns
        -------
        liste_utilisateur : list[utIlisateur]
            renvoie la liste de tous les utilisateurs correspodants à la chaîne de caractère
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM utilisateur WHERE pseudo LIKE %(pseudo)s;",
                        {"pseudo": "%" + pseud + "%"},
                    )
                    res = cursor.fetchall()
        except Exception as e:
            logging.info(e)
            raise

        liste_utilisateurs = []
        logging.info(f"res de rechercher tous pseudo : {res}")
        if res:
            for row in res:
                utilisateur = Utilisateur(
                    id=row["id_utilisateur"],
                    pseudo=row["pseudo"],
                    mdp=row["mdp"],
                )
                if utilisateur:
                    liste_utilisateurs.append(utilisateur)
            return liste_utilisateurs
        return None

    @log
    def recherche_id_par_pseudo(self, pseudo):
        """recherche l'identifiant d'un utilisateur selon son pseudo

        Parameters
        ----------
        pseudo : str

        Returns
        -------
        id_utilisateur : int
            renvoie l'id_utilisateur dans la base de données
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id_utilisateur                  "
                        "FROM utilisateur                       "
                        "WHERE pseudo = %(pseudo)s;             ",
                        {"pseudo": pseudo},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        id_utilisateur = res["id_utilisateur"]

        return id_utilisateur

    def recherche_pseudo_par_id(self, id):
        """recherche le pseudo d'un utilisateur selon son id

        Parameters
        ----------
        id : int
            identifiant unique de l'utilisateur

        Returns
        -------
        pseudo : str
            renvoie le pseudo de l'utilisateur correspondant à l'id
        """

        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT pseudo                  "
                        "FROM utilisateur                       "
                        "WHERE id_utilisateur = %(id_utilisateur)s;             ",
                        {"id_utilisateur": id},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise

        pseudo = res["pseudo"]

        return pseudo
