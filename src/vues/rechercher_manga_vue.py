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
                longueur, sous_liste, longueur_tot = RechercheService().recherche_manga_par_t2(titre, n, m, a)
                logging.info(f"longueur : {longueur}")
                res_entier = longueur // m
                res_reste = longueur % m

                if not RechercheService().recherche_manga_par_t2(titre, n, m, a):
                    print(f"Aucun manga trouvé pour le titre '{titre}'.")
                    choix2 = ["Retour au menu précédent"]
                    choix3 = inquirer.select(
                        message="Faites votre choix : ",
                        choices=choix2
                        ).execute()

                while n >= 0:
                    longueur, sous_liste, longueur_tot = RechercheService().recherche_manga_par_t2(titre, n, m, a)
                    choix2 = sous_liste
                    logging.info(f"choix2 : {choix2}")

                    choix2.extend(["Afficher la page suivante", "Retour au menu précédent"])

                    if (res_entier == 0 and res_reste == 0) or longueur_tot <= 8:
                        choix2.remove("Afficher la page suivante")

                    if res_entier != (longueur // m):
                        choix2.extend(["Afficher la page précédente"])
                        res_entier += 1

                    choix3 = inquirer.select(
                        message="Choisissez un manga : ",
                        choices=choix2,
                    ).execute()

                    if choix3 == "Retour au menu précédent":
                        from vues.recherche_vue import RechercheVue
                        return RechercheVue().choisir_menu()

                    elif choix3 == "Afficher la page suivante":
                        if res_entier != 0:
                            n = n + m
                            res_entier -= 1
                        if res_entier == 0 and res_reste != 0:
                            n = n + m
                            a = res_reste - m

                    else:
                        n = -1
                        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                        return SelectionMangaVuerecherche().choisir_menu(choix3)

                # Retour à l'accueil si aucune option choisie
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue()
