from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from service.avis_service import AvisService


class MenuAvis(VueAbstraite):
    """Vue du menu des avis

    Attributes
    ----------
    message=''
        str

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """

    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nMenu Avis\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=[
                "Accéder à ses avis",
                "Modifier un avis",
                "Supprimer un avis",
                "Retour au menu précédent",
                "Retour vers l'écran d'accueil",
            ],
        ).execute()

        match choix:
            case "Accéder à ses avis":
                from service.avis_service import AvisService

                liste_avis, liste_titre = AvisService().recuperer_avis_utilisateur(
                    Session().utilisateur.id
                )
                choices = []
                for i in range(len(liste_avis)):
                    option = f"titre : {liste_titre[i]} | Avis: {liste_avis[i]}"
                    choices.append(option)
                choix_utilisateur = inquirer.select(
                    message="Faites votre choix : ", choices=choices
                ).execute()

                choix2 = inquirer.select(
                    message="Faites votre choix : ", choices=["Modifier l'avis", "Supprimer l'avis"]
                ).execute()
                match choix2:
                    case "Modifier l'avis":
                        # Ici, on doit encore implémenter la logique pour modifier un avis
                        print("La fonctionnalité de modification n'est pas encore implémentée.")
                    case "Supprimer un avis":
                        from service.avis_service import AvisService

                        AvisService.supprimer_avis()

            case "Retour au menu précédent":
                from profil_utilisateur_vue import EcranDuProfilVue

                return EcranDuProfilVue()

            case "Retour vers l'écran de Menu":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                return MenuUtilisateurVue()

    def afficher_avis(self):
        """Affiche les avis de l'utilisateur avec pagination"""

        # Récupérer l'ID utilisateur depuis la session
        id_utilisateur = Session().get_utilisateur_id()
        avis_service = AvisService()

        # Commence par afficher les avis avec pagination
        avis_service.afficher_avis_pagination(id_utilisateur)

        # Menu de pagination interactif après affichage
        while True:
            choix2 = inquirer.select(
                message="Faites votre choix :",
                choices=[
                    "Lire les 5 avis suivants",
                    "Retourner au meu des avis",
                ],
            ).execute()

            if choix2 == "Lire les 5 avis suivants":
                # Incrémente la page actuelle et continue l'affichage
                avis_service.afficher_avis_pagination(id_utilisateur, page_suivante=True)
            elif choix2 == "Retourner au menu des avis":
                from vues.avis_utilisateur_vue import MenuAvis

                return MenuAvis()
