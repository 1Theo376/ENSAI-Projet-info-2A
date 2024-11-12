from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from dao.manga_dao import MangaDao
from service.avis_service import AvisService
from vues.session import Session
import logging
from dao.avis_dao import AvisDAO


class ConsulterAvisMangaVuerecherche(VueAbstraite):
    def choisir_menu(self, choix3):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = MangaDao().trouver_manga_par_titre(choix3)

        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")

        n = 0
        a = 0
        sous_liste, long, longueur_tot = AvisService().recuperer_avis_manga2(manga.id_manga, n, a)
        res_entier = long // 8
        res_reste = long % 8
        logging.info(f"sous_liste : {sous_liste}")
        logging.info(f"long : {long}")

        if AvisService().recuperer_avis_manga2(manga.id_manga, n, a) == "Aucun avis trouvé.":
            print(f"Aucun avis trouvé pour le manga '{manga.titre}'.")

        while n >= 0:

            sous_liste, long, longueur_tot = AvisService().recuperer_avis_manga2(manga.id_manga, n, a)

            choix = ["Retour au menu précédent", "Retour à l'accueil"]

            for i in sous_liste:
                print(f"{i[0]}\n{i[1]}\n")

            choix.extend(["Afficher la page suivante"])

            logging.info(f"long : {long}, res_entier : {res_entier}, res_reste : {res_reste}")

            if (res_entier == 0 and res_reste == 0) or longueur_tot <= 8:
                choix.remove("Afficher la page suivante")

            if AvisDAO().AvisUtilisateurMangaExistant(Session().utilisateur.id, manga.id_manga):
                choix.extend(["Modifier votre avis sur ce manga"])

            logging.info(f"choix : {choix}")

            choix2 = inquirer.select(
                        message="Faites votre choix : ",
                        choices=choix,
                    ).execute()

            if choix2 == "Retour au menu précédent":
                from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                return SelectionMangaVuerecherche().choisir_menu(choix3)

            if choix2 == "Retour à l'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue().choisir_menu()

            if choix2 == "Modifier votre avis sur ce manga":
                pass

            if choix2 == "Afficher la page suivante":
                if res_entier != 0:
                    n = n + 8
                    res_entier -= 1
                if res_entier == 0 and res_reste != 0:
                    n = n + 8
                    a = res_reste - 8

            else:
                n = n - 1


"""
        match choix2:
            case "Retour au menu précédent":
                from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                return SelectionMangaVuerecherche().choisir_menu(choix2)

            case "Retour à l'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue().choisir_menu()

            case "Modifier votre avis sur ce manga":
                pass
"""
