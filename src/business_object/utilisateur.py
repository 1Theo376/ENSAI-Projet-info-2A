class Utilisateur:
    """
    Définition de la classe Utilisateur.

    Attributs
    ----------
    id: int
        identifiant de l'utilisateur

    pseudo: str
        Pseudo de l'utilisateur

    mdp: str
        mot de passe de l'utilisateur

    """

    def __init__(self, pseudo: str, mdp: str):
        """
        Initialise une instance de Utilisateur
        """
        self.mdp = mdp
        self.pseudo = pseudo


# id manquant
