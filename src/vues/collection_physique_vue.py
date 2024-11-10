from vues.vue_abstraite import VueAbstraite
from InquirerPy import inquirer
from vues.session import Session
from service.recherche_service import RechercheService


class CollectionPhysiqueVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        collec = RechercheService().recherche_collec_phys_par_id(Session().utilisateur.id)

        if not collec:
            print("Aucune collection trouvée")
            from vues.profil_utilisateur_vue import EcranDuProfilVue
            return EcranDuProfilVue().choisir_menu()

        print(
            "\n"
            + "-" * 50
            + f"\n votre Collection physique : {collec.titre_collection} \n"
            + "-" * 50
            + "\n"
        )

        choix = inquirer.select(
            message="Que voulez vous faire dans votre collection Physique : ",
            choices=[
                "Consulter/Modifier les mangas de la collection",
                "Modifier titre de la collection",
                "Modifier description de la collection",
                "Retour au menu précédent",
            ],
        ).execute()
        if choix == "Consulter/Modifier les mangas de la collection":
            pass
        if choix == "Modifier titre de la collection":
            pass
        if choix == "Modifier description de la collection":
            pass
        if choix == "Retour au menu précédent":
            from vues.profil_utilisateur_vue import EcranDuProfilVue
            return EcranDuProfilVue().choisir_menu()
