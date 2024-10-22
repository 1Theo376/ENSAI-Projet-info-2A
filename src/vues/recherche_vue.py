from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite


class RechercheVue(VueAbstraite):
    """Vue qui affiche les recherches que peut faire l'utilisateur
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
            pass

        case "Rechercher un utilisateur":
            pass

        case "Retour vers le menu principal":
            pass
