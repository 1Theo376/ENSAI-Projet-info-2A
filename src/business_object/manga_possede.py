from manga import Manga


class MangaPossede:
    """
    Représente un manga avec ses informations de base
    """

    def __init__(self,
                 id_manga_p: int, manga: Manga, num_dernier_acquis: int,
                 num_manquant=None, statut: str):
        """

        Initialise un manga

    Parameters :
    ----------
    id_manga_p : int
        L'identifiant unique du manga possédé.
    manga : Manga
        La série de mangas
    num_dernier_acquis : int
        numéro du dernier tome acquis
    num_manquant : list(int)
        numéros de tomes manquantes
        """
        self.id_manga_p = id_manga_p
        self.manga = manga
        self.num_dernier_acquis = num_dernier_acquis
        self.num_manquant = list(range(1, manga.volume))
        self.statut = statut

    def __str__(self) -> str:
        """
        Retourne une représentation en chaîne de caractères du manga possédé.

        Return : str
        -------
            Une chaîne de caractères formatée contenant le titre,
            le numéro du dernier manga acquis et les numéros manquants.
        """
        return f"Titre: {self.manga.titre}, Numéro du dernier tome acquis: {self.num_dernier_acquis}, Numéro manquant: {self.num_manquant}, Statut: {self.statut}"
