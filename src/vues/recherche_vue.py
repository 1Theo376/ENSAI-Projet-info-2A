from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite


class RechercheVue(VueAbstraite):
    """Vue qui affiche les recherches que peut faire l'utilisateur"""

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nMenu recherche\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Rechercher un manga",
                "Rechercher un utilisateur",
                "Retour vers le menu principal",
            ],
        ).execute()

        match choix:
            case "Rechercher un manga":
                from vues.rechercher_manga_vue import RechercheMangaVue
                return RechercheMangaVue()
            case "Rechercher un utilisateur":
                from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue()

            case "Retour vers le menu principal":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue
