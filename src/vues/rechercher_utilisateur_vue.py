from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session

from service.utilisateur_service import UtilisateurService


class RechercheUtilisateurVue(VueAbstraite):
    """Vue du menu de l'utilisateur

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Utilisateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Consulter ses collections",
                "Consulter ses avis",
                "Retour au menu précédent",
                "Retour au menu d'accueil",
            ],
        ).execute()

        match choix:
            case "Consulter ses collections":
                pass

            case "Consulter ses avis":
                pass

            case "Retour au menu précédent":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue()

            case "Retour au menu d'accueil":
                Session().deconnexion()
                from vues.accueil.accueil_vue import AccueilVue
                return AccueilVue()
