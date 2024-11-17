class Avis:
    """
    Classe Avis représentant un avis associé à un manga.

    Attributs:
    ----------------
    id_avis : int
        Identifiant unique de l'avis.

    texte : str
        Le contenu de l'avis.
    """

    def __init__(self, id_avis: int, texte: str):
        """Initialise un nouvel objet Avis"""
        self.id_avis = id_avis
        self.texte = texte

    def __str__(self):
        """Retourne le contenu de l'avis"""
        return f"{self.texte}"
