import logging
from dao.db_connection import DBConnection
from business_object.avis import Avis


class AvisDAO:
    "Classe contenant des méthodes relatives aux avis"
    def creer_avis(self, avis, id_user, id_manga) -> bool:
        """Création d'un avis dans la base de données

        Attributs
        ----------
        avis : Avis
            L'avis à creer

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

    def trouver_avis_par_id(self, id_avis) -> Avis:  ##???
        """
        Permet de trouver un avis à l'aide de son id

        Parameters
        -----------
        id_avis : int
            Identifiant unique de l'avis

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

    def trouver_avis_par_titre_manga(self, titre) -> Avis: #fonction étrange/ Returns à modifier ? on retourne une liste ou un avis ???§§!!!!!
        """
        permet de trouver un avis à l'aide du titre d'un manga

        Parameters
        -----------
        titre : str
            Titre du manga

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

    def modifier_avis(self, avis, nouveau_texte) -> bool:
        """Modification d'un avis dans la base de données
        Parameters
        ----------
        avis : Avis

        nouveau_texte: str
            le nouvel avis
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
                        "SET texte = %(texte)s                       "
                        "   WHERE id_avis = %(id_avis)s        ",
                        {
                            "texte": nouveau_texte,
                            "id_avis": avis.id_avis,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

            return res == 1

    def consulter_avis(self, id_avis):  #la même fonction au-dessus/ et à quoi elle sert concrétement???!!!
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

    def recuperer_avis_utilisateur(self, id_utilisateur):  #modifier la fonction : if...:... return None
        """Récupère tous les avis d'un utilisateur

        Parameters
        ----------
        id_utilisateur : int

        Returns
        --------
        avis_liste une liste des avis et liste_manga une liste des id_manga associés"""
        avis_liste = []
        liste_manga = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM avis WHERE id_utilisateur = %(id_utilisateur)s ORDER BY id_avis;",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
                    logging.info(f"res : {res}")
                    for row in res:
                        avis = Avis(id_avis=row["id_avis"], texte=row["texte"])
                        avis_liste.append(avis)
                        liste_manga.append(row["id_manga"])
        except Exception as e:
            logging.info(e)
            raise
        return avis_liste, liste_manga

    def recuperer_avis_manga(self, id_manga):
        """Récupère tous les avis sur un manga

        Parameters
        ----------
        id_manga : int

        Returns
        --------
        avis_liste une liste des avis et liste_user une liste des id_utilisateur associés"""
        avis_liste = []
        liste_user = []
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM avis WHERE id_manga = %(id_manga)s ORDER BY id_avis;",
                        {"id_manga": id_manga},
                    )
                    res = cursor.fetchall()
                    logging.info(f"res : {res}")
                    for row in res:
                        avis = Avis(id_avis=row["id_avis"],
                                    texte=row["texte"])
                        avis_liste.append(avis)
                        liste_user.append(row["id_utilisateur"])
        except Exception as e:
            logging.info(e)
            raise
        return avis_liste, liste_user

    def AvisUtilisateurMangaExistant(self, id_utilisateur, id_manga):  #peut-être plus util de vérfier si la fonction au-dessous retourne qqchose ou non
        """Vérifie si l'utilisateur a déjà fait un avis sur ce manga

         Parameters
        ----------
        id_manga : int

        id_utilisateur : int

        Returns
        --------
        True si il en a un, False sinon
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM avis WHERE id_utilisateur = %(id_utilisateur)s and id_manga =%(id_manga)s;",
                        {"id_utilisateur": id_utilisateur, "id_manga": id_manga},
                    )
                    res = cursor.fetchone()
        except Exception as e:
            logging.info(e)
            raise
        exist = False
        if res:
            exist = True
        return exist

    def recuperer_avis_user_et_manga(self, id_manga, id_utilisateur):  #bizarrement faite
        """Récupére l'avis de l' utilisateur sur ce manga

         Parameters
        ----------
        id_manga : int

        id_utilisateur : int

        Returns
        --------
        avis ou None #à modif
        """
        try:
            with DBConnection().connection as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT * FROM avis WHERE id_manga = %(id_manga)s "
                        "AND id_utilisateur = %(id_utilisateur)s; ",
                        {"id_manga": id_manga, "id_utilisateur": id_utilisateur},
                    )
                    result = cursor.fetchone()
                    if result:
                        avis = Avis(id_avis=result["id_avis"], texte=result["texte"])
                        return avis
        except Exception as e:
            logging.info(e)
            raise
