from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
import logging


class RechercheMangaVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'un manga\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=["Entrer le titre du manga recherché", "Retour au menu précédent"],
        ).execute()

        match choix:
            case "Entrer le titre du manga recherché":
                titre = inquirer.text(message="Entrer le titre : ").execute()
                n = 0
                while True:
                    choix2 = RechercheService().recherche_manga_par_t(titre, n)
                    logging.info(f"choix2 : {choix2}")

                    if choix2 == "Aucun manga trouvé.":
                        logging.info(f"choix2 : {choix2}")
                        print(f"Aucun manga trouvé pour le titre '{titre}'.")
                        choix2 = ["Retour au menu précédent"]
                        choix3 = inquirer.select(
                            message="Faites votre choix : ",
                            choices=choix2,
                        ).execute()

                    else:
                        choix2.extend(["Retour au menu précédent", "Afficher la page suivante"])

                        choix3 = inquirer.select(
                            message="Choisissez un manga : ",
                            choices=choix2,
                        ).execute()

                    if choix3 == "Retour au menu précédent":
                        from vues.menu_utilisateur_vue import MenuUtilisateurVue
                        return MenuUtilisateurVue()

                    elif choix3 == "Afficher la page suivante":
                        n += 8

                    else:
                        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                        return SelectionMangaVuerecherche().choisir_menu(choix3)

                # Retour à l'accueil si aucune option choisie
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
