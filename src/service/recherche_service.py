from dao.joueur_dao import JoueurDao
from manga import Manga
from dao.manga_dao import MangaDao
from utilisateur import Utilisateur


class RechercheService:
    """Classe """

    def recherche_manga_par_titre(self, titre: str) -> Manga:
        

    def recherche_utilisateur(self, pseudo):
        """Recherche les utilisateurs par leurs pseudo
        """
        res = self.joueur_dao.lister_tous()
        for pers in res:
            if pers[pseudo] == pseudo:
                return pers
            else:
                print(f"Aucun utilisateur trouvé pour le pseudo '{pseudo}'.")

