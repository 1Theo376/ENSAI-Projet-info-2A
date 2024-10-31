from dao.utilisateur_dao import UtilisateurDao
from business_object.manga import Manga
from dao.manga_dao import MangaDao
from business_object.utilisateur import Utilisateur


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
<<<<<<< HEAD
            liste = [j.titre for j in res]
            sous_liste = liste[n:n + 8]
            return sous_liste if sous_liste else f"Aucun manga trouvé pour l'indice {n}."
        return print(f"Aucun manga trouvé pour le titre '{titre}'.")
=======
            return [j.titre for j in res]
        return f"Aucun manga trouvé pour le titre '{titre}'."
>>>>>>> cfcf791e9a7cc5162e49de334f98625bb06693b1

    def recherche_utilisateur(self, pseudo, n):
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
            liste = [j.pseudo for j in res]
            sous_liste = liste[n:n + 8]
            return sous_liste if sous_liste else f"Aucun manga trouvé pour l'indice {n}."
        return print(f"Aucun utilisateur trouvé pour le pseudo '{pseudo}'.")
