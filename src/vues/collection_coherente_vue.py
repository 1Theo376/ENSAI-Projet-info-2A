from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService


class CollectionCoherenteVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'une collection\n" + "-" * 50 + "\n")
        choix = RechercheService().recherche_collec_cohe_par_id(Session().utilisateur.id)

        choix.extend(["Afficher la page suivante", "Retour au menu précédent"])

        choix2 = inquirer.select(
            message="Choisissez une collection : ",
            choices=choix,
        ).execute()

        if choix2 == "Retour au menu précédent":
            from vues.profil_utilisateur_vue import EcranDuProfilVue

            return EcranDuProfilVue()

        elif choix2 == "Afficher la page suivante":
            pass

        from vues.manga_collection_cohe import MangaCollectionCoherenteVue

        return MangaCollectionCoherenteVue().choisir_menu(choix2)
