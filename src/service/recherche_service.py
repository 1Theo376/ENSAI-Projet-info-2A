from dao.joueur_dao import JoueurDao
from manga import Manga
from dao.manga_dao import MangaDao
from utilisateur import Utilisateur


class RechercheService:
    """Classe"""

    def recherche_manga_par_titre(self, titre: str) -> Manga:
<<<<<<< HEAD
        """Recherche un manga par son titre
        Parameters
        ----------
        titre : str

        Returns
        -------
        manga : Manga
            renvoie le manga recherché
        """
=======
<<<<<<< HEAD
        """Recherche les mangas par leurs titres

        """
=======
        """Recherche les mangas par leurs titres"""
>>>>>>> b0444b8e85aaea4cbe0c2a1d32daf5ad1b6f2ae8
>>>>>>> 749c84499c42003d1c26320a71d00f308c55f1e8
        res = self.dao.mangadao.lister_tous()
        for man in res:
            if man[titre] == titre:
                return man
            else:
                print(f"Aucun manga trouvé pour le titre '{titre}'.")

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
