from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session

from service.utilisateur_service import UtilisateurService


class MenuUtilisateurVue(VueAbstraite):
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
                "Accéder à mon profil",
                "Accéder à la section recherche",
                "Se déconnecter",
            ],
        ).execute()

        match choix:
            case "Se déconnecter":
                Session().deconnexion()
                from vues.accueil.accueil_vue import AccueilVue

                return AccueilVue()

            case "Accéder à mon profil":
                pass
                # return MenuUtilisateurVue(Session().afficher())

            case "Accéder à la section recherche":
                from vues.recherche_vue import RechercheVue

                return RechercheVue()
