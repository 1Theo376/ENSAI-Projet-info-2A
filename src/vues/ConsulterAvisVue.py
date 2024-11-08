from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
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
        liste_avis, liste_user = AvisService().recuperer_avis_manga(manga.id_manga)
        for i in range(len(liste_avis)):
            print("\n" + "-" * 50 + f"\n Utilisateur : {liste_user[i]}\n Avis : {liste_avis[i]} \n" + "-" * 50 + "\n")
        choix = ["Retour au menu précédent", "Retour à l'accueil"]
        if AvisDAO().AvisUtilisateurMangaExistant(Session().utilisateur.id, manga.id_manga):
            choix.extend(["Souhaitez-vous modifier votre avis sur ce manga?"])
        choixavis = inquirer.select(
                                    message="Faites votre choix : ",
                                    choices=choix,
                                    ).execute()
        match choixavis:
            case "Retour au menu précédent":
                from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                return SelectionMangaVuerecherche().choisir_menu(choix3)

            case "Retour à l'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
            case "Souhaitez-vous modifier votre avis sur ce manga?":
                pass
