from business_object.manga import Manga


class MangaPossede:
    """
    Classe représentant un manga possédé en vrai.

    Attributs :
    ----------
    id_manga_p : int
        identifiant unique du manga possédé
    manga : Manga
        La série de mangas
    num_dernier_acquis : int
        numéro du dernier tome acquis
    num_manquant : list(int)
        numéros de tomes manquantes
    """

    def __init__(
        self, idmanga: int, num_dernier_acquis: int, statut: str, num_manquant: list(int), id_manga_p=None
    ):
        """Initialise un nouvel objet MangaPossede"""
        self.id_manga_p = id_manga_p
        self.idmanga = idmanga
        self.num_dernier_acquis = num_dernier_acquis
        self.num_manquant = num_manquant
        self.statut = statut

    def __str__(self) -> str:
        """Retourne une représentation en chaîne de caractères du manga possédé."""
        return f"Numéro du dernier tome acquis: {self.num_dernier_acquis}, Numéro(s) manquant(s) : {self.num_manquant}, Statut: {self.statut}"
