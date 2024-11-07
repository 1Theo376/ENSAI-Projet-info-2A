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

        print(
            "\n"
            + "-" * 50
            + f"\n votre Collection physique : {collec.titre_collection} \n"
            + "-" * 50
            + "\n"
        )

        if not collec:
            print(f"Aucune collection trouvée")
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()

        choix = inquirer.select(
            message="Que voulez vous faire dans votre collection Physique : ",
            choices=[
                "Consulter les mangas de la collection",
                "Modifier titre de la collection",
                "Modifier description de la collection",
                "Retour au menu précédent",
            ],
        ).execute()
        if choix == "Consulter/Modifier les mangas et leurs avis de la collection":
            pass
        if choix == "Modifier titre de la collection":
            pass
        if choix == "Modifier description de la collection":
            pass
        if choix == "Retour au menu précédent":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()
