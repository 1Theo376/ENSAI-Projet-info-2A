from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.manga_dao import MangaDao


class CollectionPhysiqueVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        choix3 = inquirer.select(
            message="Que voulez vous faire dans votre collection Physique : ",
            choices=[
                "Consulter/Modifier les mangas de la collection",
                "Modifier titre de la collection",
                "Modifier description de la collection",
                "Retour au menu précédent",
            ],
        ).execute()
        if choix3 == "Consulter/Modifier les mangas de la collection":

            liste_titre = []
            for manga in (
                CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id)
            ).Liste_manga:
                liste_titre.append(manga.titre)
            choix4 = inquirer.select(
                message="Selectionnez un manga de votre collection : ",
                choices=liste_titre,
            ).execute()
            return self.choisir_menu_bis(choix4)

        if choix3 == "Modifier titre de la collection":
            pass
        if choix3 == "Modifier description de la collection":
            pass
        if choix3 == "Retour au menu précédent":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()

    def choisir_menu_bis(self, choix4):
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
                CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id),
                MangaDao().trouver_manga_par_titre(choix4),
            )
            return self.choisir_menu_bis(choix4)

        if choix5 == "Afficher les informations du manga":
            print(MangaDao().trouver_manga_par_titre(choix4))
            return self.choisir_menu_bis(choix4)

        if choix5 == "Consulter son avis sur ce manga":
            from service.avis_service import AvisService
            from dao.avis_dao import AvisDAO

            if AvisDAO().AvisUtilisateurMangaExistant(
                Session().utilisateur.id, MangaDao().trouver_manga_par_titre(choix4).id_manga
            ):
                print(
                    AvisService().recuperer_avis_user_manga(
                        MangaDao().trouver_manga_par_titre(choix4).id_manga,
                        Session().utilisateur.id,
                    )
                )
            else:
                print("Vous n'avez pas encore écrit d'avis sur ce manga. ")
            return self.choisir_menu_bis(choix4)
        if choix5 == "Retour au menu précédent":
            return self.choisir_menu()
