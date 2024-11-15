from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
from dao.utilisateur_dao import UtilisateurDao
import logging
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.manga_dao import MangaDao


class ConsulterMangaCollecPhysUtilVUe(VueAbstraite):
    def choisir_menu(self, choixu, choixc):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        id_utilisateur = UtilisateurDao().recherche_id_par_pseudo(choixu)
        liste_titre = []
        for manga in (CollectionPhysiqueDAO().trouver_collec_phys_id_user(Session().utilisateur.id)).Liste_manga:
            liste_titre.append(MangaDao().trouver_manga_par_id(manga.idmanga).titre)
        liste_titre.append("Retour au menu précédent")
        choix4 = inquirer.select(
            message="Selectionnez un manga de votre collection : ",
            choices=liste_titre,
        ).execute()
        if choix4 == "Retour au menu précédent":
            from vues.ConsulterCollecVue import CollectionCoherenteVueRecherche
            return CollectionCoherenteVueRecherche().choisir_menu(choixu)
        else:
            manga = MangaDao().trouver_manga_par_titre(choix4)
            print("\n" + "-" * 50 + "\nInformation du manga\n" + "-" * 50 + "\n")
            print("Titre: " + manga.titre + "\n")
            print("Synopsis: " + manga.synopsis + "\n")
            print("Auteur: " + manga.auteur + "\n")
            print("Thèmes: " + manga.themes + "\n")
            print("Genre: " + manga.genre + "\n")
            self.choisir_menu(choixu, choixc)
