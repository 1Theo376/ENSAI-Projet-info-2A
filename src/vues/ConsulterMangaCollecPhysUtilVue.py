from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from service.utilisateur_service import UtilisateurService
import logging
from service.collection_physique_service import Collection_physique_service
from service.recherche_service import RechercheService
from service.avis_service import AvisService


class ConsulterMangaCollecPhysUtilVUe(VueAbstraite):
    def choisir_menu(self, choixu, choixc):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        id_utilisateur = UtilisateurService().recherche_id_par_pseudo(choixu)
        liste_titre = []
        for manga in (
            Collection_physique_service().trouver_collec_phys_id_user(id_utilisateur)
        ).Liste_manga:
            liste_titre.append(RechercheService().trouver_manga_par_id(manga.idmanga).titre)
        if liste_titre == []:
            print("Cette collection ne contient pas de mangas")
            from vues.ConsulterCollecVue import CollectionCoherenteVueRecherche

            return CollectionCoherenteVueRecherche().choisir_menu(choixu)
        logging.info(f"liste: {liste_titre}")
        liste_titre.append("Retour au menu précédent")
        choix4 = inquirer.select(
            message="Selectionnez un manga de votre collection : ",
            choices=liste_titre,
        ).execute()

        if choix4 == "Retour au menu précédent":
            from vues.ConsulterCollecVue import CollectionCoherenteVueRecherche

            return CollectionCoherenteVueRecherche().choisir_menu(choixu)

        else:
            n = 0
            manga = RechercheService().trouver_manga_par_titre(choix4)
            if AvisService().recuperer_avis_utilisateur(id_utilisateur):
                liste_avis, liste_titre = AvisService().recuperer_avis_utilisateur(id_utilisateur)
                for i in range(0, len(liste_titre)):
                    if liste_titre[i] == manga.titre:
                        n = i

            print("\n" + "-" * 50 + "\nInformation du manga\n" + "-" * 50 + "\n")
            print("Titre: " + manga.titre + "\n")
            print("Synopsis: " + manga.synopsis + "\n")
            print("Auteur: " + manga.auteur + "\n")
            print("Thèmes: " + manga.themes + "\n")
            print("Genre: " + manga.genre + "\n")

            if n != 0:
                print(
                    "\n"
                    + "-" * 50
                    + f"\nManga: {liste_titre[n]}\n{liste_avis[n].texte} \n"
                    + "-" * 50
                    + "\n"
                )
            return self.choisir_menu(choixu, choixc)
