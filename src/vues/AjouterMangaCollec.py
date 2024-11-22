from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao
from service.avis_service import AvisService
from vues.session import Session
import logging
from dao.avis_dao import AvisDAO
from dao.utilisateur_dao import UtilisateurDao
from service.collection_coherente_service import CollectionCoherenteService
from service.collection_physique_service import Collection_physique_service
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.collection_physique_dao import CollectionPhysiqueDAO


class AjouterMangaCollecVuerecherche(VueAbstraite):
    def choisir_menu(self, choix3):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = MangaDao().trouver_manga_par_titre(choix3)
        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")

        id_utilisateur = Session().utilisateur.id
        choix = []
        listecolleccohe = []
        if RechercheService().recherche_collec_cohe_par_id(id_utilisateur):
            listecolleccohe = RechercheService().recherche_collec_cohe_par_id(id_utilisateur)
        logging.info(f"listecolleccohe type: {type(listecolleccohe)}, contenu: {listecolleccohe}")

        collection_physique = RechercheService().recherche_collec_phys_par_id(
            Session().utilisateur.id
        )
        logging.info(f"collection_physique type: , contenu: {collection_physique}")

        if RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id):
            choix.append(collection_physique.titre_collection)
            logging.info(f"Contenu de `choix` après ajout de collection_physique: {choix}")

        listecollections = choix + listecolleccohe
        logging.info(f"listecollections: {listecollections}")

        if not listecollections:
            print("Aucune collection trouvée")
            from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

            return SelectionMangaVuerecherche().choisir_menu(choix3)

        choices = []
        for i in range(len(listecollections)):
            if isinstance(listecollections[i], str):
                if RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id):
                    if listecollections[i] == collection_physique.titre_collection:
                        option = f"Dans votre collection physique : {listecollections[0]}"
                        logging.info(f"Ajout de l'option physique : {option}")
                        choices.append(option)
                    else:
                        option2 = f"Dans votre collection cohérente : {listecollections[i]}"
                        logging.info(f"Ajout de l'option cohérente : {option2}")
                        choices.append(option2)
                else:
                    option2 = f"Dans votre collection cohérente : {listecollections[i]}"
                    logging.info(f"Ajout de l'option cohérente : {option2}")
                    choices.append(option2)

        choices.extend(["Retour au menu précédent", "Retour vers l'écran d'accueil"])
        logging.info(f"Choices avant inquirer: {choices}")

        choixp = inquirer.select(
            message="Dans quelle collection ?",
            choices=choices,
        ).execute()

        if choixp == "Retour au menu précédent":
            from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

            return SelectionMangaVuerecherche().choisir_menu(choix3)
        elif choixp == "Retour vers l'écran d'accueil":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()
        else:
            nom = choixp.split(" : ")[1].strip()
            collec = choixp.split(" : ")[0].strip()
            logging.info(f"Nom de la collection choisi: {nom}")
            if collec == "Dans votre collection physique":
                if nom == collection_physique.titre_collection:
                    collection = CollectionPhysiqueDAO().trouver_collec_phys_nom(nom)
                    for i in collection.Liste_manga:
                        if i.titre == choix3:
                            from vues.Selection_manga_vue_recherche import (
                                SelectionMangaVuerecherche,
                            )

                            print("\n")
                            print(f"Ce manga est déjà présent dans la collection {nom}.")
                            return SelectionMangaVuerecherche().choisir_menu(choix3)
                    from vues.AjouterMangaPossCollPhys import AjouterMangaPossCollPhys

                    return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
            else:
                collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(nom, id_utilisateur)
                logging.info(f"Collection cohérente trouvée : {nom}, {collection}")
                logging.info(f"collection.Liste_manga : {collection.Liste_manga}")
                for i in collection.Liste_manga:
                    if i.titre == choix3:
                        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

                        print("\n" + f"Ce manga est déjà présent dans la collection {nom}.")
                        return SelectionMangaVuerecherche().choisir_menu(choix3)

                CollectionCoherenteService().ajouter_manga(
                    collection.id_collectioncoherente, manga.id_manga
                )
                from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

                print("\n" + f"Manga ajouté dans la collection {nom}.")
                return SelectionMangaVuerecherche().choisir_menu(choix3)
