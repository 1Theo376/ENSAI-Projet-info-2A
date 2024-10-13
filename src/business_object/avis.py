class Avis:
    """
    Définition de la classe avis

    Attributs:
    ----------------
    id_avis : int
        Identifiant lié à l'avis

    texte : str
        Contenu de l'avis
    """
    self.id_avis = id_avis
    self.texte = texte

    def __init__(self, id_avis:int, texte: str):
        """
        Retourne le contenu de l'avis

        Retour : str
        """  
        return f"Avis ID: {self.id_avis}, Texte : {self.texte}"

#test test