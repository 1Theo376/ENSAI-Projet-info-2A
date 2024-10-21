from dao.joueur_dao import JoueurDao
from manga import Manga
from dao.manga_dao import MangaDao
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
            renvoie le manga recherché
        """
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
