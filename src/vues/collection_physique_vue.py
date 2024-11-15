from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.manga_dao import MangaDao
from dao.manga_possede_dao import MangaPossedeDao
import logging


class CollectionPhysiqueVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        choix = [
                "Consulter/Modifier les mangas de la collection",
                "Consulter la description de la collection",
                "Modifier titre de la collection",
                "Modifier description de la collection",
                "Retour au menu précédent"
            ]

        if not CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id).Liste_manga :
            choix.remove("Consulter/Modifier les mangas de la collection")

        choix3 = inquirer.select(
            message="Que voulez vous faire dans votre collection Physique : ",
            choices=choix
        ).execute()
        if choix3 == "Consulter/Modifier les mangas de la collection":

            liste_titre = []
            for manga in (
                CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id)
            ).Liste_manga:
                liste_titre.append(MangaDao().trouver_manga_par_id(manga.idmanga).titre)
            choix4 = inquirer.select(
                message="Selectionnez un manga de votre collection : ",
                choices=liste_titre,
            ).execute()
            return self.choisir_menu_bis(choix4)

        if choix3 == "Consulter la description de la collection":
            description = (
                CollectionPhysiqueDAO()
                .trouver_collec_phys_id_user(Session().utilisateur.id)
                .description_collection
            )
            print(print("\n" + "-" * 50 + "\n" + description + "\n" + "-" * 50 + "\n"))
            return self.choisir_menu()

        if choix3 == "Modifier titre de la collection":
            id_collection = (
                CollectionPhysiqueDAO()
                .trouver_collec_phys_id_user(Session().utilisateur.id)
                .id_collectionphysique
            )
            nouveau_titre = inquirer.text(message="Entrer le nouveau titre : ").execute()
            CollectionPhysiqueDAO().modifier_titre(id_collection, nouveau_titre)
            print("\n" + "Titre modifié." + "\n")
            return self.choisir_menu()
        if choix3 == "Modifier description de la collection":
            id_collection = (
                CollectionPhysiqueDAO()
                .trouver_collec_phys_id_user(Session().utilisateur.id)
                .id_collectionphysique
            )
            nouvelle_desc = inquirer.text(message="Entrer la nouvelle description : ").execute()
            CollectionPhysiqueDAO().modifier_desc(id_collection, nouvelle_desc)
            print("\n" + "Description modifiée." + "\n")
            return self.choisir_menu()
        if choix3 == "Retour au menu précédent":
            from vues.profil_utilisateur_vue import EcranDuProfilVue

            return EcranDuProfilVue()

    def choisir_menu_bis(self, choix4):
        choix5 = inquirer.select(
            message=f"Que voulez-vous faire avec le manga {choix4}: ",
            choices=[
                "Afficher les informations du manga",
                "Modifier les tomes possédés",
                "Consulter son avis sur ce manga",
                "Retirer le manga de la collection",
                "Retour au menu précédent",
            ],
        ).execute()
        if choix5 == "Afficher les informations du manga":
            print(MangaDao().trouver_manga_par_titre(choix4))
            print(
                MangaPossedeDao().trouver_manga_possede_collecphys(
                    choix4,
                    (
                        CollectionPhysiqueDAO().trouver_collec_phys_id_user(
                            Session().utilisateur.id
                        )
                    ).id_collectionphysique,
                )
            )
            print(f"Nombre de volumes possédés : {MangaPossedeDao().nb_volume_manga(choix4)}")
            return self.choisir_menu_bis(choix4)
        if choix5 == "Retirer le manga de la collection":
            from service.collection_physique_service import Collection_physique_service

            Collection_physique_service().supprimer_mangaposs(
                CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id),
                MangaPossedeDao().trouver_manga_possede_collecphys(
                    choix4,
                    (
                        CollectionPhysiqueDAO().trouver_collec_phys_id_user(
                            Session().utilisateur.id
                        )
                    ).id_collectionphysique,
                ),
            )
            return self.choisir_menu()

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

        if choix5 == "Modifier les tomes possédés":
            mangap = MangaPossedeDao().trouver_manga_possede_collecphys(
                    choix4,
                    (
                        CollectionPhysiqueDAO().trouver_collec_phys_id_user(
                            Session().utilisateur.id
                        )
                    ).id_collectionphysique,
                )
            num_manquant = mangap.num_manquant
            manga = MangaDao().trouver_manga_par_titre(choix4)
            liste_id_num_manquant = MangaPossedeDao().trouver_id_num_manquant_id(mangap.id_manga_p)
            logging.info(f"nummanq = {liste_id_num_manquant}")
            for elt in num_manquant:
                MangaPossedeDao().supprimer_num_manquant(liste_id_num_manquant[0])
            liste_id_num_manquant = MangaPossedeDao().trouver_id_num_manquant_id(mangap.id_manga_p)
            logging.info(f"nummanq = {liste_id_num_manquant}")
            volume_manga = MangaPossedeDao().nb_volume_manga(manga.titre)
            nb_volumes_poss = int(
                                    inquirer.text(message="Entrez le nombre de volumes possédés du manga : ").execute()
                                )
            if volume_manga:
                if nb_volumes_poss > volume_manga:
                    print("Nombre incorrect")
                    return self.choisir_menu_bis(choix4)
            volumes_poss = []
            while nb_volumes_poss != 0:
                num_vol = inquirer.text(
                            message="Entrez le numéro des volumes possédés du manga : "
                        ).execute()
                if "-" in num_vol:
                    a = int(num_vol.split("-")[0])
                    b = int(num_vol.split("-")[1])
                    if a < 1 or b < 1 or (nb_volumes_poss-(b-a+1)) < 0:
                        if volume_manga:
                            if a > volume_manga or b > volume_manga:
                                print("Erreur")
                                return self.choisir_menu_bis(choix4)
                        print("Erreur")
                        return self.choisir_menu_bis(choix4)
                    for i in range(a, b+1):
                        volumes_poss.append(i)
                    nb_volumes_poss = nb_volumes_poss-(b-a+1)
                else:
                    num = int(num_vol)
                    if volume_manga:
                        if num > volume_manga:
                            print("Erreur")
                            return self.choisir_menu_bis(choix4)
                    volumes_poss.append(num)
                    nb_volumes_poss -= 1
            logging.info(f"vol:{volumes_poss}")
            if volume_manga:
                num_manquant = [i for i in range(1, volume_manga+1)]
                for elt in volumes_poss:
                    num_manquant.remove(elt)
            logging.info(f"manq:{num_manquant}")
            if volume_manga:
                for elt in num_manquant:
                    MangaPossedeDao().ajouter_ass_num_manquant(mangap.id_manga_p, MangaPossedeDao().ajouter_num_manquant(elt))
            return self.choisir_menu_bis(choix4)