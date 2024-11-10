from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao


class CollectionCoherenteVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        choix = RechercheService().recherche_collec_cohe_par_id(Session().utilisateur.id)

        if not choix:
            print(f"Aucune collection trouvée")
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue().choisir_menu()

        choix.extend(["Retour au menu précédent", "Afficher la page suivante"])

        choix2 = inquirer.select(
            message="Choisissez une collection : ",
            choices=choix,
        ).execute()

        if choix2 == "Retour au menu précédent":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()

        elif choix2 == "Afficher la page suivante":
            pass

        choix3 = inquirer.select(
            message="Que voulez vous faire dans votre collection Cohérente : ",
            choices=[
                "Consulter/Modifier les mangas de la collection",
                "Modifier titre de la collection",
                "Modifier description de la collection",
                "Retour au menu précédent",
            ],
        ).execute()
        if choix3 == "Consulter/Modifier les mangas de la collection":
            from dao.collection_coherente_dao import CollectionCoherenteDAO

            liste_titre = []
            for manga in (CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2)).Liste_manga:
                liste_titre.append(manga.titre)
            choix4 = inquirer.select(
                message="Selectionnez un manga de votre collection : ",
                choices=liste_titre,
            ).execute()

            choix5 = inquirer.select(
                message=f"Que voulez-vous faire avec le manga {choix4}: ",
                choices=[
                    "Afficher les informations du manga",
                    "Consulter son avis sur ce manga",
                    "Retirer le manga de la collection",
                    "Retour au menu précédent",
                ],
            ).execute()
            if choix5 == "Retirer le manga de la collection":
                from service.collection_coherente_service import CollectionCoherenteService

                CollectionCoherenteService().supprimer_mangaposs(
                    CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2),
                    MangaDao().trouver_manga_par_titre(choix4),
                )
                return CollectionCoherenteVue()

            if choix5 == "Afficher les informations du manga":
                print(MangaDao().trouver_manga_par_titre(choix4))
                return CollectionCoherenteVue()

            if choix5 == "Consulter son avis sur ce manga":
                pass

            if choix5 == "Retour au menu précédent":
                return CollectionCoherenteVue()

        if choix3 == "Modifier titre de la collection":
            pass
        if choix3 == "Modifier description de la collection":
            pass
        if choix3 == "Retour au menu précédent":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()
