from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from service.recherche_service import RechercheService
from dao.utilisateur_dao import UtilisateurDao
from service.collection_physique_service import Collection_physique_service
import logging


class CollectionCoherenteVueRecherche(VueAbstraite):
    def choisir_menu(self, choixu):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        id_utilisateur = UtilisateurDao().recherche_id_par_pseudo(choixu)
        choix = []
        listecolleccohe = []
        if RechercheService().recherche_collec_cohe_par_id(id_utilisateur):
            listecolleccohe = RechercheService().recherche_collec_cohe_par_id(id_utilisateur)
        logging.info(f"listecolleccohe type: {type(listecolleccohe)}, contenu: {listecolleccohe}")

        collection_physique = RechercheService().recherche_collec_phys_par_id(id_utilisateur)
        logging.info(f"collection_physique type: , contenu: {collection_physique}")

        if RechercheService().recherche_collec_phys_par_id(id_utilisateur):
            choix.append(collection_physique.titre_collection)
            logging.info(f"Contenu de `choix` après ajout de collection_physique: {choix}")

        listecollections = choix + listecolleccohe
        logging.info(f"listecollections: {listecollections}")

        if listecollections == []:
            print("Aucune collection trouvée \n")
            from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue

            return RechercheUtilisateurVue().choisir_menu_bis(choixu)
        n, m = 0, 8
        sous_liste, longueur_tot = listecollections[n : n + m], len(listecollections)
        while n >= 0:
            sous_liste, longueur_tot = listecollections[n : n + m], len(listecollections)
            choix2 = sous_liste + [
                "Afficher la page suivante",
                "Afficher la page précédente",
                "Retour au menu précédent",
            ]
            logging.info(f"util:{sous_liste}")
            if n + m >= longueur_tot:
                choix2.remove("Afficher la page suivante")

            if n == 0:
                choix2.remove("Afficher la page précédente")

            choix3 = inquirer.select(
                message="Choisissez une collection :", choices=choix2
            ).execute()

            if choix3 == "Retour au menu précédent":
                from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu_bis(choixu)
            elif choix3 == "Afficher la page suivante":
                n += m
            elif choix3 == "Afficher la page précédente":
                n = max(0, n - m)
            else:
                choix4 = inquirer.select(
                    message="Que voulez vous faire  : ",
                    choices=[
                        "Consulter les mangas de la collection",
                        "Retour au menu précédent",
                    ],
                ).execute()
                if choix4 == "Consulter les mangas de la collection":
                    if (
                        Collection_physique_service().trouver_collec_phys_id_user(
                            UtilisateurDao().recherche_id_par_pseudo(choixu)
                        )
                        is not None
                    ):
                        if choix3 == collection_physique.titre_collection:
                            from vues.ConsulterMangaCollecPhysUtilVue import (
                                ConsulterMangaCollecPhysUtilVUe,
                            )

                            return ConsulterMangaCollecPhysUtilVUe().choisir_menu(choixu, choix3)
                        else:
                            from vues.ConsulterMangaCollecVueUtilisateur import (
                                ConsulterMangaCollecCoheUtilVUe,
                            )

                            return ConsulterMangaCollecCoheUtilVUe().choisir_menu(choixu, choix3)
                    else:
                        from vues.ConsulterMangaCollecVueUtilisateur import (
                            ConsulterMangaCollecCoheUtilVUe,
                        )

                        return ConsulterMangaCollecCoheUtilVUe().choisir_menu(choixu, choix3)

                if choix4 == "Retour au menu précédent":
                    from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue

                    return RechercheUtilisateurVue()
