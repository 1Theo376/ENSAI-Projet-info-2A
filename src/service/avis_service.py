from business_object.avis import Avis
from dao.avis_dao import AvisDAO
import logging
from dao.manga_dao import MangaDao
from dao.utilisateur_dao import UtilisateurDao


class AvisService:
    """Classe contenant les méthodes de service des avis"""

    def rediger_avis(self, texte, id_avis, id_user, id_manga):
        """Rédaction d'un avis
        Parameters
        ----------
        texte : str

        Returns
        --------
        Avis rédigé
        """

        if not texte or len(texte.strip()) == 0:
            raise ValueError("Ce n'est pas une description")

        nouvel_avis = Avis(id_avis=id_avis, texte=texte)
        logging.info(f"Avis : {nouvel_avis}")
        return nouvel_avis if AvisDAO().creer_avis(nouvel_avis, id_user, id_manga) else None

    def supprimer_avis(self, avis):
        """Suppression d'un avis"""
        return AvisDAO().supprimer_avis(avis)

    def afficher_avis_pagination(self, id_utilisateur, page_suivante=False):
        """Affiche les avis d'un utilisateur avec pagination"""
        if page_suivante:
            self.current_page += 1
        avis_utilisateur = self.recuperer_avis_utilisateur(id_utilisateur)
        total_avis = len(avis_utilisateur)
        if total_avis == 0:
            print("Aucun avis disponible pour cet utilisateur.")
            return
        start_index = self.current_page * self.page_size
        end_index = min(start_index + self.page_size, total_avis)
        # Affichage des avis pour la page courante
        for i in range(start_index, end_index):
            print(f"{i + 1}. {avis_utilisateur[i]}")
        print(f"\nAffichage des avis {start_index + 1} à {end_index} sur {total_avis}.\n")

    def recuperer_avis_utilisateur(self, id_utilisateur):
        """Simule la récupération des avis d'un utilisateur"""
        # Simuler une liste d'avis pour l'exemple
        liste_avis, liste_manga = AvisDAO().recuperer_avis_utilisateur(id_utilisateur)
        liste_titre_mangas = []
        for i in liste_manga:
            logging.info(f"i : {i}")
            manga = MangaDao().trouver_manga_par_id(i)
            logging.info(f"manga : {manga.titre}")
            liste_titre_mangas.append(manga.titre)
        if liste_avis:
            return liste_avis, liste_titre_mangas
        return None

    def recuperer_avis_manga(self, id_manga):
        """Simule la récupération des avis d'un utilisateur"""
        # Simuler une liste d'avis pour l'exemple
        liste_avis, liste_user = AvisDAO().recuperer_avis_manga(id_manga)
        logging.info(f"liste_avis : {liste_avis}")
        logging.info(f"liste_user : {liste_user}")
        liste_pseudo = []
        for i in liste_user:
            logging.info(f"i : {i}")
            user = UtilisateurDao().recherche_pseudo_par_id(i)
            logging.info(f"manga : {user}")
            liste_pseudo.append(user)
        if liste_avis:
            return liste_avis, liste_pseudo
        return None

    def recuperer_avis_user_manga(self, id_manga, id_utilisateur):
        """Simule la récupération des avis d'un utilisateur"""
        avis = AvisDAO().recuperer_avis_user_et_manga(id_manga, id_utilisateur)
        if avis:
            return avis
        return None
