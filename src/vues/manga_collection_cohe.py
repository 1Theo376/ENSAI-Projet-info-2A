from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.manga_dao import MangaDao
import logging


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
                "Consulter la description de la collection",
                "Modifier le titre de la collection",
                "Modifier la description de la collection",
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

        if choix3 == "Consulter la description de la collection":
            description = CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2).desc_collection
            print(print("\n" + "-"*50 + "\n" + description + "\n" + "-"*50 + "\n"))
            return self.choisir_menu(choix2)

        if choix3 == "Modifier le titre de la collection":
            id_collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2).id_collectioncoherente
            nouveau_titre = inquirer.text(message="Entrer le nouveau titre : ").execute()
            CollectionCoherenteDAO().modifier_titre(id_collection, nouveau_titre)
            print("\n" + "Titre modifié." + "\n")
            return self.choisir_menu(choix2)

        if choix3 == "Modifier la description de la collection":
            id_collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2).id_collectioncoherente
            nouvelle_desc = inquirer.text(message="Entrer la nouvelle description : ").execute()
            CollectionCoherenteDAO().modifier_desc(id_collection, nouvelle_desc)
            print("\n" + "Description modifiée." + "\n")
            return self.choisir_menu(choix2)

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
