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
                m = 8
                a = 0
                if not RechercheService().recherche_manga_par_t2(titre, n, m, a):
                    print("\n" + f"Aucun manga trouvé pour le titre '{titre}'." + "\n")
                    choix2 = ["Retour au menu précédent"]
                    choix3 = inquirer.select(
                        message="Faites votre choix : ",
                        choices=choix2
                        ).execute()
                    if choix3 == "Retour au menu précédent":
                        from vues.recherche_vue import RechercheVue
                        return RechercheVue().choisir_menu()

                longueur, sous_liste, longueur_tot = RechercheService().recherche_manga_par_t2(titre, n, m, a)

                while n >= 0:
                    longueur, sous_liste, longueur_tot = RechercheService().recherche_manga_par_t2(titre, n, m, a)
                    choix2 = sous_liste + ["Afficher la page suivante","Afficher la page précédente", "Retour au menu précédent"]
                    logging.info(f"util:{sous_liste}")
                    if n + m >= longueur_tot:
                        choix2.remove("Afficher la page suivante")

                    if n == 0:
                        choix2.remove("Afficher la page précédente")

                    choix3 = inquirer.select(message="Choisissez un manga :", choices=choix2).execute()

                    if choix3 == "Retour au menu précédent":
                        from vues.recherche_vue import RechercheVue
                        return RechercheVue().choisir_menu()

                    elif choix3 == "Afficher la page suivante":
                        n += m

                    elif choix3 == "Afficher la page précédente":
                        n = max(0, n - m)

                    else:
                        n = -1
                        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                        return SelectionMangaVuerecherche().choisir_menu(choix3)

            case "Retour au menu précédent":
                from vues.recherche_vue import RechercheVue
                return RechercheVue().choisir_menu()

                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue()
