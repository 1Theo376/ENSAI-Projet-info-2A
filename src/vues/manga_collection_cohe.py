from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.manga_dao import MangaDao


class MangaCollectionCoherenteVue(VueAbstraite):
    def choisir_menu(self, choix2):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
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

            liste_titre = []
            for manga in (CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2)).Liste_manga:
                liste_titre.append(manga.titre)
            choix4 = inquirer.select(
                message="Selectionnez un manga de votre collection : ",
                choices=liste_titre,
            ).execute()
            return self.choisir_menu_bis(choix2, choix4)

        if choix3 == "Modifier titre de la collection":
            pass
        if choix3 == "Modifier description de la collection":
            pass
        if choix3 == "Retour au menu précédent":
            from vues.collection_coherente_vue import CollectionCoherenteVue

            return CollectionCoherenteVue()

    def choisir_menu_bis(self, choix2, choix4):
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
            return self.choisir_menu_bis(choix2, choix4)

        if choix5 == "Afficher les informations du manga":
            print(MangaDao().trouver_manga_par_titre(choix4))
            return self.choisir_menu_bis(choix2, choix4)

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
            return self.choisir_menu_bis(choix2, choix4)
        if choix5 == "Retour au menu précédent":
            return self.choisir_menu(choix2)
