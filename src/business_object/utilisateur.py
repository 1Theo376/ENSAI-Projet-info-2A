class Utilisateur:
    """
    Calsse représentant un Utilisateur.

    Attributs
    ----------
    id : int
        Identifiant unique de l'utilisateur

    pseudo: str
        Pseudo de l'utilisateur

    mdp: str
        mot de passe de l'utilisateur

    """

    def __init__(self, id: int, pseudo: str, mdp: str):
        """Initialise un objet Utilisateur"""
        self.id = id
        self.mdp = mdp
        self.pseudo = pseudo
