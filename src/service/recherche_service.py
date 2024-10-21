from dao.joueur_dao import JoueurDao
from manga import Manga
from manga_dao import MangaDao
from utilisateur import Utilisateur


class RechercheService:
    """Classe"""

    def recherche_manga_par_titre(self, titre: str) -> Manga:
        """Recherche un manga par son titre
        Parameters
        ----------
        titre : str

        Returns
        -------
        manga : Manga
            renvoie le manga recherché"""
        res = self.manga_dao.trouver_mang_par_titre(titre)
        if not res:
            print(f"Aucun manga trouvé pour le titre '{titre}'.")
            return None
        return res

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
        res = self.dao.Joueur_dao.lister_tous()
        for pers in res:
            if pers[pseudo] == pseudo:
                return pers
            else:
                print(f"Aucun utilisateur trouvé pour le pseudo '{pseudo}'.")
        return pers
