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
                        "INSERT INTO avis(id_utilisateur, id_manga, texte, note) VALUES "
                        "(%(id_utilisateur)s, %(id_manga)s, %(texte)s, %(note)s) RETURNING id_avis;",
                        {
                            "id_utilisateur": id_user,
                            "id_manga": id_manga,
                            "texte": avis.texte,
                            "note": avis.note,
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

    def modifier_avis(self, avis, nouveau_texte, nouvelle_note) -> bool:
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
                        "SET texte = %(texte)s, note = %(note)s    "
                        "   WHERE id_avis = %(id_avis)s        ",
                        {
                            "texte": nouveau_texte,
                            "id_avis": avis.id_avis,
                            "note": nouvelle_note,
                        },
                    )
                    res = cursor.rowcount
        except Exception as e:
            logging.info(e)

            return res == 1

    def recuperer_avis_utilisateur(self, id_utilisateur):
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
                        "SELECT * FROM avis WHERE id_utilisateur = %(id_utilisateur)s "
                        "ORDER BY id_avis;",
                        {"id_utilisateur": id_utilisateur},
                    )
                    res = cursor.fetchall()
                    logging.info(f"res : {res}")
                    for row in res:
                        avis = Avis(id_avis=row["id_avis"], texte=row["texte"], note=row["note"])
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
                        avis = Avis(id_avis=row["id_avis"], texte=row["texte"], note=row["note"])
                        avis_liste.append(avis)
                        liste_user.append(row["id_utilisateur"])
        except Exception as e:
            logging.info(e)
            raise
        return avis_liste, liste_user

    def AvisUtilisateurMangaExistant(self, id_utilisateur, id_manga):
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
                        "SELECT * FROM avis WHERE id_utilisateur = %(id_utilisateur)s "
                        "and id_manga =%(id_manga)s;",
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

    def recuperer_avis_user_et_manga(self, id_manga, id_utilisateur):
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
                        avis = Avis(
                            id_avis=result["id_avis"], texte=result["texte"], note=result["note"]
                        )
                        return avis
        except Exception as e:
            logging.info(e)
            raise
