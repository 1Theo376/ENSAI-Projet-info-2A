from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from service.collection_coherente_service import CollectionCoherenteService
from service.collection_physique_service import Collection_physique_service
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.collection_coherente_dao import CollectionCoherenteDAO
import logging


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

        choix = [
                "Consulter mes collections cohérentes",
                "Consulter ma collection physique",
                "Consulter ses avis",
                "Créer une collection cohérente",
                "Créer une collection physique",
                "Retour vers le menu précédent",
                "Supprimer mon compte",
            ]

        if not CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id):
            choix.remove("Consulter ma collection physique")

        if not CollectionCoherenteDAO().trouver_collec_cohe_id_user(Session().utilisateur.id):
            choix.remove("Consulter mes collections cohérentes")

        choix = inquirer.select(
            message="Faites votre choix :",
            choices=choix,
        ).execute()

        match choix:
            case "Consulter mes collections cohérentes":
                from vues.collection_coherente_vue import CollectionCoherenteVue
                return CollectionCoherenteVue()

            case "Consulter ma collection physique":
                from vues.collection_physique_vue import CollectionPhysiqueVue
                return CollectionPhysiqueVue()

            case "Consulter ses avis":
                from vues.avis_utilisateur_vue import MenuAvis
                return MenuAvis()

            case "Créer une collection cohérente":
                titre = inquirer.text(
                    message="Entrez le nom de la collection que vous voulez creer : "
                ).execute()
                desc = inquirer.text(message="Decrivez votre collection : ").execute()
                CollectionCoherenteService().creer_collectioncohe(titre, desc)
                return EcranDuProfilVue()

            case "Créer une collection physique":
                from service.recherche_service import RechercheService
                logging.info(f"Créer coll physique : {RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id)}")

                if RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id):
                    print("\n" + "Votre collection physique existe déjà." + "\n")
                    return self.choisir_menu()
                else:
                    titre = inquirer.text(
                        message="Entrez le nom de la collection que vous voulez creer : "
                    ).execute()
                    desc = inquirer.text(message="Decrivez votre collection : ").execute()
                    Collection_physique_service().creer_collectionphys(titre, desc)
                    return EcranDuProfilVue()

            case "Retour vers le menu précédent":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()

            case "Supprimer mon compte":
                from dao.utilisateur_dao import UtilisateurDao
                UtilisateurDao().supprimer(Session().utilisateur)
                Session().deconnexion()

                from vues.accueil.accueil_vue import AccueilVue
                return AccueilVue()
