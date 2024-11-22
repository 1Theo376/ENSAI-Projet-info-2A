from utils.securite import hash_password
from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
import logging


class UtilisateurService:
    """Classe contenant les méthodes de service des Utilisateurs"""

    def pseudo_deja_utilise(self, pseudo) -> bool:
        """Vérifie si le pseudo est déjà utilisé
        Retourne True si le pseudo existe déjà en BDD"""
        utilisateurs = UtilisateurDao().lister_tous()
        return pseudo in [j.pseudo for j in utilisateurs]

    def creer_compte(self, pseudo, mdp) -> Utilisateur:
        """Création d'un utilisateur à partir de ses attributs"""
        nouveau_utilisateur = Utilisateur(id=None, pseudo=pseudo, mdp=hash_password(mdp, pseudo))
        logging.info(
            f"Mot de passe haché : {nouveau_utilisateur.mdp} "
            f"(length: {len(nouveau_utilisateur.mdp)})"
        )

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

    def recherche_id_par_pseudo(self, pseudo):
        return UtilisateurDao().recherche_id_par_pseudo(pseudo)
