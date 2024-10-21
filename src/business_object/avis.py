class Avis:
    """
    Définition de la classe avis

    Parameters:
    ----------------
    id_avis : int
        Identifiant lié à l'avis

    texte : str
        Contenu de l'avis
    """

    def __init__(self, id_avis: int, texte: str):
        self.id_avis = id_avis
        self.texte = texte

    def __str__(self):
        """
        Retourne le contenu de l'avis

        Returns : str
        """
        return f"Avis ID: {self.id_avis}, Texte : {self.texte}"
