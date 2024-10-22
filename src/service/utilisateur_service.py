# from tabulate import tabulate
from utils.accueil.securite import hash_password
from utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao


class UtilisateurService:
    """Classe contenant les méthodes de service des Utilisateurs"""

    def pseudo_deja_utilise(self, pseudo) -> bool:
        """Vérifie si le pseudo est déjà utilisé
        Retourne True si le pseudo existe déjà en BDD"""
        utilisateurs = UtilisateurDao().lister_tous()
        return pseudo in [j.pseudo for j in utilisateurs]

    def creer_compte(self, pseudo, mdp) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""
        nouveau_utilisateur = Utilisateur(
            pseudo=pseudo,
            mdp=hash_password(mdp, pseudo),
            id=id,
        )
        if self.pseudo_deja_utilise(nouveau_utilisateur.pseudo):
            raise ValueError("Ce pseudo est déjà utilisé, veuillez en choisir un autre")

        return nouveau_utilisateur if UtilisateurDao().creer(nouveau_utilisateur) else None

    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """Se connecter à partir de pseudo et mdp"""
        return UtilisateurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    def supprimer_compte(self, utilisateur) -> bool:
        """Supprimer le compte d'un utilisateur"""
        return UtilisateurDao().supprimer(utilisateur)

    def modifier_compte(self, utilisateur) -> Utilisateur:
        """Modification du compte d'un utilisateur"""
        utilisateur.mdp = hash_password(utilisateur.mdp, utilisateur.pseudo)
        return utilisateur if Utilisateur().modifier(utilisateur) else None
