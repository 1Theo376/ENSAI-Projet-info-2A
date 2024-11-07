from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao
from service.avis_service import AvisService
from vues.session import Session
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

                    if not choix2:
                        print(f"Aucun manga trouvé pour le titre '{titre}'.")
                        break

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
                        manga = MangaDao().trouver_manga_par_titre(choix3)
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
                                print("\n" + "-" * 50 + "\n" + manga.titre + "\n" + "-" * 50 + "\n")
                                print(
                                    "\n" + "-" * 50 + "\n" + manga.synopsis + "\n" + "-" * 50 + "\n"
                                )
                                print(
                                    "\n" + "-" * 50 + "\n" + manga.auteur + "\n" + "-" * 50 + "\n"
                                )
                                print(
                                    "\n" + "-" * 50 + "\n" + manga.themes + "\n" + "-" * 50 + "\n"
                                )
                                print("\n" + "-" * 50 + "\n" + manga.genre + "\n" + "-" * 50 + "\n")
                                choix5 = inquirer.select(
                                    message="Faites votre choix : ",
                                    choices=["Retour au menu précédent"],
                                ).execute()
                                if choix5:
                                    from vues.menu_utilisateur_vue import MenuUtilisateurVue

                                    return MenuUtilisateurVue()
                            case "Consulter les avis":
                                liste_avis = AvisService().recuperer_avis_manga(manga.id_manga)
                                for i in range(len(liste_avis)):
                                    print("\n" + "-" * 50 + f"\n{liste_avis[i]}\n" + "-" * 50 + "\n")
                                choixavis = inquirer.select(
                                                    message="Faites votre choix : ",
                                                    choices=["Retour au menu précédent", "Retour à l'accueil"],
                                                        ).execute()
                                match choixavis:
                                    case "Retour au menu précédent":
                                        from vues.recherche_vue import RechercheVue

                                        return RechercheVue()
                                    case "Retour à l'accueil":
                                        from vues.menu_utilisateur_vue import MenuUtilisateurVue

                                        return MenuUtilisateurVue()
                            case "Ajouter un avis":
                                avis = inquirer.text(
                                    message="Entrer votre avis sur ce manga : "
                                ).execute()
                                aviscreer = AvisService().rediger_avis(
                                    texte=avis,
                                    id_user=Session().utilisateur.id,
                                    id_manga=manga.id_manga,
                                    id_avis=None,
                                )
                                logging.info(
                                    f"id:{Session().utilisateur.id} et manga:{manga.id_manga}"
                                )
                                logging.info(f"Avis : {aviscreer}")
                            case "Retour au menu précédent":
                                from vues.recherche_vue import RechercheVue

                                return RechercheVue()
                            case "Retour vers l'écran d'accueil":
                                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                                return MenuUtilisateurVue()

                # Retour à l'accueil si aucune option choisie
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
