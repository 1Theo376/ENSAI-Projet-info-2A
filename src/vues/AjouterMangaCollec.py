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
        id_utilisateur = UtilisateurDao().recherche_id_par_pseudo(Session().utilisateur.id)
        choix = []
        listecolleccohe = RechercheService().recherche_collec_cohe_par_id(id_utilisateur)
        if RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id):
            choix.append(RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id))
        listecollections = choix+listecolleccohe
        if not listecollections:
            print("Aucune collection trouvée")
            from vues.menu_utilisateur_vue import MenuUtilisateurVue
            return MenuUtilisateurVue()
        choices = []
        for i in range(len(listecollections)):
            if listecollections[0] == RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id):
                choix.append(RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id))
                option = f"Dans votre collection physique : {listecollections[0]}"
                choices.append(option)
            else:
                option2 = f"Dans votre collection cohérente : {listecollections[i]}"
                choices.append(option2)
        choices.extend(["Retour au menu précédent", "Retour vers l'écran d'accueil"])
        choixp = inquirer.select(
                            message="Dans quelle collection?",
                            choices=choices,
                        ).execute()
        if choixp == "Retour au menu précédent":
            pass
        if choixp == "Retour vers l'écran d'accueil":
            pass
        else:
            if choixp == listecollections[0]:
                nom = choix.split(": ")[1]
                collection = CollectionPhysiqueDAO().trouver_collec_phys_nom(nom)
                Collection_physique_service().ajouter_mangaposs(collection.id_collectioncoherente, manga.id_manga)
                from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche
                return SelectionMangaVuerecherche().choisir_menu(choix3)
            else:
                nom = choix.split(": ")[1]
                collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(nom)
                CollectionCoherenteService().ajouter_mangaposs(collection.id_collectioncoherente, manga.id_manga)