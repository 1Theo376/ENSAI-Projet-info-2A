from InquirerPy import inquirer
from vues.profil_utilisateur_vue import EcranDuProfilVue
from vues.session import Session


class CollectionCoherenteVue(VueAbstraite):
    """Vue de l'écran de collection coherente
    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    print("\n" + "-" * 50 + "\nÉcran du Profil\n" + "-" * 50 + "\n")

    choix = inquirer.select(
        message="Faites votre choix :",
        choices=[
            "Supprimer un manga",
            "Supprimer la collection",
            "Retour vers l'écran précédent",
            "Retour vers l'écran d'acceuil",
        ],
    ).execute()

    match choix:
        case "Supprimer un manga":
            pass

        case "Supprimer la collection":
            pass

        case "Retour vers l'écran précédent":
            return EcranDuProfilVue

        case "Retour veers l'écran d'acceuil":
            Session().deconnexion()
            from vues.accueil.accueil_vue import AccueilVue
