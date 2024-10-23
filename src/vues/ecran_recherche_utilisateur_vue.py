from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session

from service.recherche_service import RechercheService


class EcranRechercheUtilisateurVue(VueAbstraite):
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

        print("\n" + "-" * 50 + "\nProfil de lutilisateur sélectionné\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=["Consulter les collections", "Consullter les avis", "Retour au menu précédent", "Retour vers l'écran d'accueil"],
        ).execute()

        match choix:
            case "Consulter les collections":
                pass
            case "Consullter les avis":
                pass
            case "Retour au menu précédent":
                pass
            case "Retour vers l'écran d'accueil":
                pass
