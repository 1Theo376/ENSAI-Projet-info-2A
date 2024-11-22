from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from dao.manga_dao import MangaDao


class SelectionMangaVuerecherche(VueAbstraite):
    def choisir_menu(self, choix):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = MangaDao().trouver_manga_par_titre(choix)
        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")
        choix4 = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Ajouter à une collection",
                "Afficher les informations du manga",
                "Consulter les avis",
                "Ajouter un avis",
                "Chercher un autre manga",
                "Retour vers l'écran d'accueil",
            ],
        ).execute()

        match choix4:
            case "Ajouter à une collection":
                from vues.AjouterMangaCollec import AjouterMangaCollecVuerecherche

                return AjouterMangaCollecVuerecherche().choisir_menu(choix)
            case "Afficher les informations du manga":
                print("\n" + "-" * 50 + "\n" + manga.titre + "\n" + "-" * 50 + "\n")
                print("Synopsis: " + manga.synopsis + "\n")
                print("Auteur: " + manga.auteur + "\n")
                print("Thèmes: " + manga.themes + "\n")
                print("Genre: " + manga.genre + "\n")
                return self.choisir_menu(choix)
            case "Consulter les avis":
                from vues.ConsulterAvisVue import ConsulterAvisMangaVuerecherche

                return ConsulterAvisMangaVuerecherche().choisir_menu(choix)
            case "Ajouter un avis":
                from vues.AjouterAvisVue import AjouterAvisVuerecherche

                return AjouterAvisVuerecherche().choisir_menu(choix)
            case "Chercher un autre manga":
                from vues.rechercher_manga_vue import RechercheMangaVue

                return RechercheMangaVue().choisir_menu()
            case "Retour vers l'écran d'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue().choisir_menu()
