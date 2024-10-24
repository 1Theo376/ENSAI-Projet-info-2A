from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from vues.collection_coherente_vue import CollectionCoherenteVue
from vues.collection_physique_vue import CollectionPhysiqueVue
from vues.avis_utilisateur_vue import MenuAvis
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.utilisateur_dao import UtilisateurDao


class EcranDuProfilVue(VueAbstraite):
    """Vue de l'écran du profil

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

        print("\n" + "-" * 50 + "\nÉcran du Profil\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix :",
            choices=[
                "Consulter mes collections cohérentes",
                "Consulter ma collection physique",
                "Consulter ses avis",
                "Créer une collection cohérente",
                "Créer une collection physique",
                "Retour vers l'écran d'acceuil",
                "Supprimer mon compte",
            ],
        ).execute()

        match choix:
            case "Consulter mes collections cohérentes":
                return CollectionCoherenteVue()

            case "Consulter ma collection physique":
                return CollectionPhysiqueVue()

            case "Consulter ses avis":
                return MenuAvis()

            case "Créer une collection cohérente":
                test = CollectionPhysiqueDAO()
                test.créer_collectionpys()
                print("\nCollection physique créée")
                return CollectionPhysiqueVue()

            case "Créer une collection physique":
                test2 = CollectionCoherenteDAO()
                test2.créer_collection_cohérente()
                print("\nCollection cohérente créée")
                return CollectionCoherenteVue()

            case "Retour vers l'écran d'acceuil":
                Session().deconnexion()
                from vues.accueil.accueil_vue import AccueilVue

                return AccueilVue()

            case "Supprimer mon compte":
                user = Session().utilisateur
                user.supprimer()
                return AccueilVue()
