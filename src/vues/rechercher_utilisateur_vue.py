from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session

from service.recherche_service import RechercheService


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

        print("\n" + "-" * 50 + "\nRecherche d'un utilisateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=["Entrer le pseudo de l'utilisateur recherché", "Retour au menu précédent"],
        ).execute()

        match choix:
            case "Entrer le pseudo de l'utilisateur recherché":
                pseudo = inquirer.text(message="Entrer le pseudo : ").execute()
                if RechercheService().recherche_utilisateur(pseudo):
                    pass
            case "Retour au menu précédent":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
