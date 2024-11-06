from InquirerPy import inquirer
import logging
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao
from service.avis_service import AvisService


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

                    choix2.extend(["Afficher la page suivante", "Retour au menu précédent"])

                    choix3 = inquirer.select(
                                            message="Choisissez un manga : ",
                                            choices=choix2,
                                            ).execute()

                    if choix3 == "Retour au menu précédent":
                        from vues.menu_utilisateur_vue import MenuUtilisateurVue

                        return MenuUtilisateurVue()
                    if choix3 and isinstance(choix3, str):
                        manga = MangaDao().trouver_manga_par_titre(choix3)
                    else:
                        print("Titre du manga invalide.")
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
                            print("\n" + "-" * 50 + "\nInformation du manga\n" + "-" * 50 + "\n")
                            print("\nTitre: " + manga.titre + "\n" + "-" * 50)
                            print("\nSynopsis:" + manga.synopsis + "\n" + "-" * 50)
                            print("\nAuteur: " + manga.auteur + "\n" + "-" * 50)
                            print("\nThèmes: " + manga.themes + "\n" + "-" * 50)
                            print("\nGenre: " + manga.genre + "\n" + "-" * 50)
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
                            texte = inquirer.text(
                                message="Entrez votre avis sur ce manga : "
                            ).execute()
                            AvisService().rediger_avis(texte, id_avis=None)

                        case "Retour au menu précédent":
                            from vues.recherche_vue import RechercheVue

                            return RechercheVue()
                        case "Retour vers l'écran d'accueil":
                            from vues.menu_utilisateur_vue import MenuUtilisateurVue

                            return MenuUtilisateurVue()
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()
