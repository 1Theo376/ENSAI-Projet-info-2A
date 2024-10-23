from dao.utilisateur_dao import UtilisateurDao
from business_object.manga import Manga
from dao.manga_dao import MangaDao
from business_object.utilisateur import Utilisateur


class RechercheService:
    """Classe"""

    def recherche_manga_par_t(self, titre: str) -> Manga:
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
            return [j.titre for j in res]
        return print(f"Aucun utilisateur trouvé pour le pseudo '{titre}'.")

    def recherche_utilisateur(self, pseudo):
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
            return [j.pseudo for j in res]
        return print(f"Aucun utilisateur trouvé pour le pseudo '{pseudo}'.")
