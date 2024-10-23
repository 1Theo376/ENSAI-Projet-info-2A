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
                pseudo.append("Retour au menu précdent")
                if RechercheService.recherche_utilisateur(pseudo):
                    choix = inquirer.select(
                                            message="Choisissez un utilisateur : ",
                                            choices=pseudo,
                                            ).execute()
                    if choix == "Retour au menu précdent":
                        from view.menu_joueur_vue import MenuJoueurVue

                        return MenuJoueurVue()

                #from view.menu_joueur_vue import MenuJoueurVue

                #pokemons_str = f"Liste des pokemons du type {choix} :\n\n"
                #pokemons_str += str(pokemon_client.get_all_pokemon_by_types(choix))
                #return MenuJoueurVue(pokemons_str)
            case "Retour au menu précédent":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
