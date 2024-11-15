from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
from dao.utilisateur_dao import UtilisateurDao
import logging
from dao.collection_coherente_dao import CollectionCoherenteDAO


class ConsulterMangaCollecCoheUtilVUe(VueAbstraite):
    def choisir_menu(self, choixu, choic):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        id_utilisateur = UtilisateurDao().recherche_id_par_pseudo(choixu)
        liste_titre = []
        for manga in (CollectionCoherenteDAO().trouver_collec_cohe_nom(choixc, choixu)).Liste_manga:
            liste_titre.append(manga.titre)
        choix4 = inquirer.select(
            message="Selectionnez un manga de cette collection : ",
            choices=liste_titre,
        ).execute()
        pass