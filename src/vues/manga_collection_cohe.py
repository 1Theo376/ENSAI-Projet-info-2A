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

        choix = [
            "Consulter/Modifier les mangas de la collection",
            "Consulter la description de la collection",
            "Modifier le titre de la collection",
            "Modifier la description de la collection",
            "Supprimer la collection",
            "Retour au menu précédent",
        ]

        choix3 = inquirer.select(
            message="Que souhaitez vous faire dans votre collection cohérente : ", choices=choix
        ).execute()
        logging.info(f"{choix2}, {Session().utilisateur.id}")
        if choix3 == "Consulter/Modifier les mangas de la collection":
            liste_titre = []
            for manga in (
                CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2, Session().utilisateur.id)
            ).Liste_manga:
                logging.info(f"{(CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2, Session().utilisateur.id)).Liste_manga}")
                liste_titre.append(manga.titre)
            if not liste_titre:
                print(
                    "\n"
                    + "La collection ne contient pas de mangas, \nvous pouvez en ajouter dans la section Recherche."
                    + "\n"
                )
                return self.choisir_menu(choix2)
            n, m = 0, 8
            while n >= 0:
                sous_liste, longueur_tot = liste_titre[n : n + m], len(liste_titre)
                choixmanga = sous_liste + [
                    "Afficher la page suivante",
                    "Afficher la page précédente",
                    "Retour au menu précédent",
                ]
                logging.info(f"util:{sous_liste}")
                if n + m >= longueur_tot:
                    choixmanga.remove("Afficher la page suivante")

                if n == 0:
                    choixmanga.remove("Afficher la page précédente")

                choix4 = inquirer.select(
                        message="Selectionnez un manga de votre collection : ",
                        choices=choixmanga,
                    ).execute()

                if choix4 == "Retour au menu précédent":
                    return self.choisir_menu(choix2)
                elif choix4 == "Afficher la page suivante":
                    n += m
                elif choix4 == "Afficher la page précédente":
                    n = max(0, n - m)
                else:
                    return self.choisir_menu_bis(choix2, choix4)

        if choix3 == "Consulter la description de la collection":
            description = (
                CollectionCoherenteDAO()
                .trouver_collec_cohe_nom(choix2, Session().utilisateur.id)
                .desc_collection
            )
            print("\n" + "-" * 50 + "\n" + description + "\n" + "-" * 50 + "\n")
            return self.choisir_menu(choix2)

        if choix3 == "Modifier le titre de la collection":
            logging.info(f"choix 2 : {choix2}")
            id_collection = (
                CollectionCoherenteDAO()
                .trouver_collec_cohe_nom(choix2, Session().utilisateur.id)
                .id_collectioncoherente
            )
            nouveau_titre = inquirer.text(message="Entrer le nouveau titre : ").execute()
            CollectionCoherenteDAO().modifier_titre(id_collection, nouveau_titre)
            print("\n" + "Titre modifié." + "\n")
            # nouveau_choix = CollectionCoherenteDAO().trouver_collec_cohe_nom(nouveau_titre, Session().utilisateur.id)
            return self.choisir_menu(nouveau_titre)

        if choix3 == "Modifier la description de la collection":
            id_collection = (
                CollectionCoherenteDAO()
                .trouver_collec_cohe_nom(choix2, Session().utilisateur.id)
                .id_collectioncoherente
            )
            nouvelle_desc = inquirer.text(message="Entrer la nouvelle description : ").execute()
            CollectionCoherenteDAO().modifier_desc(id_collection, nouvelle_desc)
            print("\n" + "Description modifiée." + "\n")
            return self.choisir_menu(choix2)

        if choix3 == "Supprimer la collection":
            CollectionCoherenteDAO().supprimer_collection(
                CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2, Session().utilisateur.id)
            )
            print("\n" + "Collection supprimée." + "\n")
            from vues.profil_utilisateur_vue import EcranDuProfilVue

            return EcranDuProfilVue()

        if choix3 == "Retour au menu précédent":
            from vues.collection_coherente_vue import CollectionCoherenteVue

            return CollectionCoherenteVue()

    def choisir_menu_bis(self, choix2, choix4):
        choix5 = inquirer.select(
            message=f"Que souhaitez vous faire avec le manga {choix4} : ",
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
                CollectionCoherenteDAO().trouver_collec_cohe_nom(choix2, Session().utilisateur.id),
                MangaDao().trouver_manga_par_titre(choix4),
            )
            return self.choisir_menu(choix2)

        if choix5 == "Afficher les informations du manga":
            manga = MangaDao().trouver_manga_par_titre(choix4)
            print("\n" + "-" * 50 + "\n" + manga.titre + "\n" + "-" * 50 + "\n")
            print("Synopsis: " + manga.synopsis + "\n")
            print("Auteur: " + manga.auteur + "\n")
            print("Thèmes: " + manga.themes + "\n")
            print("Genre: " + manga.genre + "\n")
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
                print("\n" + "Vous n'avez pas encore écrit d'avis sur ce manga." + "\n")
            return self.choisir_menu_bis(choix2, choix4)

        if choix5 == "Retour au menu précédent":
            return self.choisir_menu(choix2)