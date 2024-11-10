from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao
from service.avis_service import AvisService
from vues.session import Session
import logging


class SelectionMangaVuerecherche(VueAbstraite):
    def choisir_menu(self, choix3):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = MangaDao().trouver_manga_par_titre(choix3)
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
                SelectionMangaVuerecherche().choisir_menu(choix3)
            case "Consulter les avis":
                from vues.ConsulterAvisVue import ConsulterAvisMangaVuerecherche
                return ConsulterAvisMangaVuerecherche().choisir_menu(choix3)
            case "Ajouter un avis":
                from vues.AjouterAvisVue import AjouterAvisVuerecherche
                return AjouterAvisVuerecherche().choisir_menu(choix3)
            case "Retour au menu précédent":
                from vues.recherche_vue import RechercheVue
                return RechercheVue()
            case "Retour vers l'écran d'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue()
