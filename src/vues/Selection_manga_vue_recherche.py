from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from dao.manga_dao import MangaDao
import logging


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
                    "Retour au menu précédent",
                    "Retour vers l'écran d'accueil",
                    ],
        ).execute()

        match choix4:
            case "Ajouter à une collection":
                pass
            case "Afficher les informations du manga":
                print(
                    "\n" + "-" * 50 + "\nInformation du manga\n" + "-" * 50 + "\n"
                    )
                print("Titre: " + manga.titre + "\n")
                print("Synopsis: " + manga.synopsis + "\n")
                print("Auteur: " + manga.auteur + "\n")
                print("Thèmes: " + manga.themes + "\n")
                print("Genre: " + manga.genre + "\n")
                self.choisir_menu(choix)
            case "Consulter les avis":
                from vues.ConsulterAvisVue import ConsulterAvisMangaVuerecherche
                return ConsulterAvisMangaVuerecherche().choisir_menu(choix)
            case "Ajouter un avis":
                from vues.AjouterAvisVue import AjouterAvisVuerecherche
                return AjouterAvisVuerecherche().choisir_menu(choix)
            case "Retour au menu précédent":
                from vues.rechercher_manga_vue import RechercheMangaVue
                return RechercheMangaVue().choisir_menu()
            case "Retour vers l'écran d'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue().choisir_menu()
