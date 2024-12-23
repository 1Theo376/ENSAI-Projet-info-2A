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

    def __init__(self, texte: str, note: int, id_avis=None):
        """Initialise un nouvel objet Avis"""
        self.id_avis = id_avis
        self.texte = texte
        self.note = note

    def __str__(self):
        """Retourne le contenu de l'avis"""
        return f"Avis : {self.texte}, Note : {self.note}"
