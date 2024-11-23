from business_object.avis import Avis
from dao.avis_dao import AvisDAO
import logging
from dao.manga_dao import MangaDao
from dao.utilisateur_dao import UtilisateurDao


class AvisService:
    """Classe contenant les méthodes de service des avis"""

    def rediger_avis(self, texte: str, id_avis: int, id_user: int, id_manga: int, note: int):
        """Création d'un avis dans la base de données à partir de ses attributs"""

        if not texte or len(texte.strip()) == 0:
            raise ValueError("Ce n'est pas une description")

        nouvel_avis = Avis(id_avis=id_avis, texte=texte, note=note)
        logging.info(f"Avis : {nouvel_avis}")
        return nouvel_avis if AvisDAO().creer_avis(nouvel_avis, id_user, id_manga) else None

    def supprimer_avis(self, avis: Avis):
        """Supprimer l'avis"""
        return AvisDAO().supprimer_avis(avis)

    def recuperer_avis_utilisateur(self, id_utilisateur: int):
        """Récupère tous les avis de l'utilisateur"""
        liste_avis, liste_manga = AvisDAO().recuperer_avis_utilisateur(id_utilisateur)
        liste_titre_mangas = []
        for i in liste_manga:
            manga = MangaDao().trouver_manga_par_id(i)
            liste_titre_mangas.append(manga.titre)
        if liste_avis:
            return liste_avis, liste_titre_mangas
        return None

    def recuperer_avis_manga(self, id_manga: int):
        """Récupère tous les avis sur le manga"""
        liste_avis, liste_user = AvisDAO().recuperer_avis_manga(id_manga)
        liste_pseudo = []
        for elt in liste_user:
            liste_pseudo.append(UtilisateurDao().recherche_pseudo_par_id(elt))

        if not liste_avis:
            return None

        return liste_avis, liste_pseudo

    def recuperer_avis_user_manga(self, id_manga: int, id_utilisateur: int ):
        """Récupère l'avis de l'utilisateur sur le manga"""
        avis = AvisDAO().recuperer_avis_user_et_manga(id_manga, id_utilisateur)
        if avis:
            return avis
        return None

    def modifier_avis(self, avis: Avis, nouveau_texte: str) -> bool:
        return AvisDAO().modifier_avis(avis, nouveau_texte)

    def AvisUtilisateurMangaExistant(self, id_utilisateur: int, id_manga: int):
        return AvisDAO().AvisUtilisateurMangaExistant(id_utilisateur, id_manga)

    def creer_signalement(self, id_user: int, id_avis: int, motif: str):
        return AvisDAO().creer_signalement(id_user, id_avis, motif)

    def liste_signalement(self):
        return AvisDAO().liste_signalement()

    def supprimer_signalement(self, id_signalement: int):
        return AvisDAO().supprimer_signalement(id_signalement)
