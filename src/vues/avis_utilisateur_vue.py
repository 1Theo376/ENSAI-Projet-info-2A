from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from dao.manga_dao import MangaDao
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

        liste_avis, liste_titre = AvisService().recuperer_avis_utilisateur(Session().utilisateur.id)
        choices = []
        for i in range(len(liste_avis)):
            option = f"titre : {liste_titre[i]} | Avis: {liste_avis[i]}"
            choices.append(option)
        choices.extend(["Retour au menu précédent", "Retour vers l'écran d'accueil"])
        choix_utilisateur = inquirer.select(
            message="Choisissez un avis : ", choices=choices
        ).execute()
        if choix_utilisateur != "Retour au menu précédent" and choix_utilisateur != "Retour au menu précédent":
            titre = choix_utilisateur.split("titre : ")[1].split(" |")[0].strip()
            id_manga = (MangaDao().trouver_manga_par_titre(titre)).id_manga
            avis = AvisService().recuperer_avis_user_manga(id_manga, Session().utilisateur.id)
            choix2 = inquirer.select(
                message="Faites votre choix : ",
                choices=["Modifier l'avis", "Supprimer l'avis", "Retour au menu précédent"],
            ).execute()
            match choix2:
                case "Modifier l'avis":
                    from dao.avis_dao import AvisDAO

                    nouvel_avis = input(f"Entrez votre nouvel avis sur le manga {titre} : ")
                    AvisDAO().modifier_avis(avis, nouvel_avis)
                    return MenuAvis()
                case "Supprimer l'avis":
                    print("Avis supprimé avec succés")
                    AvisService().supprimer_avis(avis)
                    return MenuAvis()

                case "Retour au menu précédent":
                    return MenuAvis()

        if choix_utilisateur == "Retour au menu précédent":
            from vues.profil_utilisateur_vue import EcranDuProfilVue

            return EcranDuProfilVue()

        if choix_utilisateur == "Retour vers l'écran de Menu":
            from vues.menu_utilisateur_vue import MenuUtilisateurVue

            return MenuUtilisateurVue()
