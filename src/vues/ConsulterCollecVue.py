from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
from dao.utilisateur_dao import UtilisateurDao


class CollectionCoherenteVueRecherche(VueAbstraite):
    def choisir_menu(self, choix3):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        id_utilisateur = UtilisateurDao().recherche_id_par_pseudo(choix3)
        choix = RechercheService().recherche_collec_cohe_par_id(id_utilisateur)

        if not choix:
            print("Aucune collection trouvée")
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()

        choix.extend(["Retour au menu précédent", "Afficher la page suivante"])

        choix2 = inquirer.select(
            message="Choisissez une collection : ",
            choices=choix,
        ).execute()

        if choix2 == "Retour au menu précédent":
            from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue
            return RechercheUtilisateurVue()

        elif choix2 == "Afficher la page suivante":
            pass

        choix3 = inquirer.select(
            message="Que voulez vous faire  : ",
            choices=[
                "Consulter les mangas de la collection",
                "Retour au menu précédent",
            ],
        ).execute()
        if choix3 == "Consulter les mangas de la collection":
            pass
        if choix3 == "Retour au menu précédent":
            from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue
            return RechercheUtilisateurVue()
