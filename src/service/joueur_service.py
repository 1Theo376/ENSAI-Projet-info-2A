from tabulate import tabulate
from security import hash_password
from utilisateur import Utilisateur
from dao.joueur_dao import JoueurDao


class JoueurService:
    """Classe contenant les méthodes de service des Joueurs"""

    def creer(self, pseudo, mdp, age, mail, fan_pokemon) -> Utilisateur:
        """Création d'un joueur à partir de ses attributs"""

        nouveau_joueur = Utilisateur(
            pseudo=pseudo,
            mdp=hash_password(mdp, pseudo),
            id=id,
        )

        return nouveau_joueur if JoueurDao().creer(nouveau_joueur) else None

    def lister_tous(self, inclure_mdp=False) -> list[Utilisateur]:
        """Lister tous les joueurs
        Si inclure_mdp=True, les mots de passe seront inclus
        Par défaut, tous les mdp des joueurs sont à None
        """
        joueurs = JoueurDao().lister_tous()
        if not inclure_mdp:
            for j in joueurs:
                j.mdp = None
        return joueurs

    def trouver_par_id(self, id_joueur) -> Utilisateur:
        """Trouver un joueur à partir de son id"""
        return JoueurDao().trouver_par_id(id_joueur)

    def modifier(self, joueur) -> Utilisateur:
        """Modification d'un joueur"""

        joueur.mdp = hash_password(joueur.mdp, joueur.pseudo)
        return joueur if JoueurDao().modifier(joueur) else None

    def supprimer(self, joueur) -> bool:
        """Supprimer le compte d'un joueur"""
        return JoueurDao().supprimer(joueur)

    def afficher_tous(self) -> str:
        """Afficher tous les joueurs
        Sortie : Une chaine de caractères mise sous forme de tableau
        """
        entetes = ["pseudo", "age", "mail", "est fan de Pokemon"]

        joueurs = JoueurDao().lister_tous()

        joueurs_as_list = [j.as_list() for j in joueurs]

        str_joueurs = "-" * 100
        str_joueurs += "\nListe des joueurs \n"
        str_joueurs += "-" * 100
        str_joueurs += "\n"
        str_joueurs += tabulate(
            tabular_data=joueurs_as_list,
            headers=entetes,
            tablefmt="psql",
            floatfmt=".2f",
        )
        str_joueurs += "\n"

        return str_joueurs

    def se_connecter(self, pseudo, mdp) -> Utilisateur:
        """Se connecter à partir de pseudo et mdp"""
        return JoueurDao().se_connecter(pseudo, hash_password(mdp, pseudo))

    def pseudo_deja_utilise(self, pseudo) -> bool:
        """Vérifie si le pseudo est déjà utilisé
        Retourne True si le pseudo existe déjà en BDD"""
        joueurs = JoueurDao().lister_tous()
        return pseudo in [j.pseudo for j in joueurs]