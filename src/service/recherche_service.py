from dao.utilisateur_dao import UtilisateurDao
from business_object.manga import Manga
from dao.manga_dao import MangaDao
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.collection_physique_dao import CollectionPhysiqueDAO
import logging


class RechercheService:
    """Classe"""

    def recherche_manga_par_t(self, titre: str, n: int) -> Manga:
        """Recherche un manga par son titre
        Parameters
        ----------
        titre : str

        Returns
        -------
        manga : Manga
            renvoie le manga recherché"""
        res = MangaDao().rechercher_manga_par_titre(titre)
        if res:
            liste = [j.titre for j in res]
            sous_liste = liste[n: n + 8]
            return sous_liste if sous_liste else None
        return None

    def recherche_manga_par_t2(self, titre: str, n: int, m, a) -> Manga:
        """Recherche un manga par son titre
        Parameters
        ----------
        titre : str

        Returns
        -------
        manga : Manga
            renvoie le manga recherché"""
        res = MangaDao().rechercher_manga_par_titre(titre)
        logging.info("recherche_manga_par_t2")
        if res:
            longueur_tot = len(res)
            liste = [j.titre for j in res]
            sous_liste = liste[n: n + m + a]
            longueur = len(sous_liste)
            return longueur, sous_liste, longueur_tot if sous_liste else None
        return None

    def recherche_utilisateur(self, pseudo, n, m, a):
        """Recherche un utilisateur par son pseudo
        Parameters
        ----------
        pseudo : str

        Returns
        -------
        utilisateur : Utilisateur
            renvoie l'utilisateur recherché
        """
        res = UtilisateurDao().rechercher_tous_pseudo(pseudo)
        if res:
            longueur_tot = len(res)
            liste = [j.pseudo for j in res]
            logging.info(f"liste={liste}")
            sous_liste = liste[n: n + m + a]
            longueur = len(sous_liste)
            return longueur, sous_liste, longueur_tot if sous_liste else None
        return None

    def recherche_collec_cohe_par_id(self, id):
        res = CollectionCoherenteDAO().trouver_collec_cohe_id_user(id)
        if res:
            liste = [collec.titre_collection for collec in res]
            return liste
        return None

    def recherche_collec_phys_par_id(self, id):
        res = CollectionPhysiqueDAO().trouver_collec_phys_id_user(id)
        if res:
            return res
        return None
