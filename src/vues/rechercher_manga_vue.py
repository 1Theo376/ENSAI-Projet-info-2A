from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao


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
                choix2 = RechercheService().recherche_manga_par_t(titre)
                choix2.append("Retour au menu précédent")
                if choix2:
                    choix3 = inquirer.select(
                                            message="Choisissez un manga : ",
                                            choices=choix2,
                                            ).execute()
                    if choix3 == "Retour au menu précédent":
                        from vues.menu_utilisateur_vue import MenuUtilisateurVue

                        return MenuUtilisateurVue()
                    manga = MangaDao.trouver_manga_par_titre(choix3)
                    choix4 = inquirer.select(
                                            message="Faites votre choix : ",
                                            choices=["Ajouter à une collection", "Afficher les informations du manga", "Consulter les avis", "Ajouter un avis", "Retour au menu précédent", "Retour vers l'écran d'accueil"],
                                            ).execute()
                    match choix4:
                        case "Ajouter à une collection":
                            pass
                        case "Afficher les informations du manga":
                            print("\n" + "-" * 50 + "\nInformation du manga\n" + "-" * 50 + "\n")
                            print("\n" + "-" * 50 + "\n" + manga.titre + "\n" + "-" * 50 + "\n")
                            print("\n" + "-" * 50 + "\n" + manga.synopsis + "\n" + "-" * 50 + "\n")
                            #print("\n" + "-" * 50 + "\n" + manga.auteur + "\n" + "-" * 50 + "\n")
                            #print("\n" + "-" * 50 + "\n" + manga.themes + "\n" + "-" * 50 + "\n")
                            #print("\n" + "-" * 50 + "\n" + manga.genre + "\n" + "-" * 50 + "\n")
                            choix5 = inquirer.select(
                                                    message="Faites votre choix : ",
                                                    choices=["Retour au menu précédent"],
                                                    ).execute()
                            if choix5:
                                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                                return MenuUtilisateurVue()
                        case "Consulter les avis":
                            pass
                        case "Ajouter un avis":
                            pass
                        case "Retour au menu précédent":
                            from vues.recherche_vue import RechercheVue

                            return RechercheVue()
                        case "Retour vers l'écran d'accueil":
                            from vues.menu_utilisateur_vue import MenuUtilisateurVue

                            return MenuUtilisateurVue()
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
