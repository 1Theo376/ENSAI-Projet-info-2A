from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao


class CollectionCoherenteVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        choix = RechercheService().recherche_collec_cohe_par_id(Session().utilisateur.id)

        if not choix:
            print(f"Aucune collection trouvée")
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue().choisir_menu()

        choix.extend(["Retour au menu précédent", "Afficher la page suivante"])

        choix2 = inquirer.select(
            message="Choisissez une collection : ",
            choices=choix,
        ).execute()

        if choix2 == "Retour au menu précédent":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()

        elif choix2 == "Afficher la page suivante":
            pass

        from vues.manga_collection_cohe import MangaCollectionCoherenteVue

        return MangaCollectionCoherenteVue().choisir_menu(choix2)
