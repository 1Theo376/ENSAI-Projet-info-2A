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
                choix2 = RechercheService().recherche_utilisateur(pseudo)
                choix2.append("Retour au menu précédent")
                if choix2:
                    choix3 = inquirer.select(
                                            message="Choisissez un utilisateur : ",
                                            choices=choix2,
                                            ).execute()
                    if choix3 == "Retour au menu précédent":
                        from vues.menu_utilisateur_vue import MenuUtilisateurVue

                        return MenuUtilisateurVue()
                    choix4 = inquirer.select(
                                            message="Faites votre choix : ",
                                            choices=["Consulter les collections", "Consullter les avis", "Retour au menu précédent", "Retour vers l'écran d'accueil"],
                                            ).execute()
                    match choix4:
                        case "Consulter les collections":
                            pass
                        case "Consullter les avis":
                            pass
                        case "Retour au menu précédent":
                            from vues.recherche_vue import RechercheVue

                            return RechercheVue()
                        case "Retour vers l'écran d'accueil":
                            from vues.menu_utilisateur_vue import MenuUtilisateurVue

                            return MenuUtilisateurVue(message)
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
