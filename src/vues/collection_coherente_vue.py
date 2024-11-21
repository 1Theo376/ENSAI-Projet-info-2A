from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService
import logging


class CollectionCoherenteVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        listecollections = RechercheService().recherche_collec_cohe_par_id(Session().utilisateur.id)
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
                from vues.profil_utilisateur_vue import EcranDuProfilVue

                return EcranDuProfilVue()
            elif choix3 == "Afficher la page suivante":
                n += m
            elif choix3 == "Afficher la page précédente":
                n = max(0, n - m)
            else:
                from vues.manga_collection_cohe import MangaCollectionCoherenteVue

                return MangaCollectionCoherenteVue().choisir_menu(choix2)
