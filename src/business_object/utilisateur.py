from collection_physique import Collection_physique
from collec import Collection
import csv


class Utilisateur:
    """
    Définition de la classe Utilisateur.

    Attributs
    ----------
    id: str
        identifiant rentré par l'utilisateur

    mdp: str
        mot de passe rentré par l'utilisateur

    pseudo: str
        Pseudo rentré par l'utilisateur

    collec_phys: Collection_physique
        La collection physique de l'utilisateur
    """

    def __init__(self, id: str, mdp: str, pseudo: str):
        """
        Initialise une instance de Utilisateur
        """
        self.id = id
        self.mdp = mdp
        self.pseudo = pseudo
