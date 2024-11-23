from InquirerPy import inquirer
from service.avis_service import AvisService
from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from service.utilisateur_service import UtilisateurService
from dao.manga_dao import MangaDao
import logging


class SignalementVue(VueAbstraite):
    """Vue du menu de l'utilisateur

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

        print("\n" + "-" * 50 + "\nMenu Utilisateur\n" + "-" * 50 + "\n")

        signalements = AvisService().liste_signalement()
        logging.info(f"{signalements}")
        if not signalements:
            print("Aucun signalement en attente.")
            choix = inquirer.select(
                message="Que voulez-vous faire ?", choices=["Se déconnecter"]
            ).execute()
            if choix == "Se déconnecter":
                Session().deconnexion()
                from vues.accueil.accueil_vue import AccueilVue

                return AccueilVue()

        choix_signalements = []
        for signalement in signalements:
            avis = AvisService().recuperer_avis_user_et_manga(
                signalement["id_manga"],
                UtilisateurService().recherche_id_par_pseudo(signalement["pseudo"]),
            )
            manga = MangaDao().trouver_manga_par_id(signalement["id_manga"])
            choix_signalements.append(
                f"id signalement: {signalement['id_signalement']}, "
                f"Utilisateur: {signalement['pseudo']}, "
                f"texte avis: {avis.texte}, "
                f"Manga: {manga.titre}, "
                f"Motif: {signalement['motif']}, "
                f"Date : {signalement['date_signalement']}"
            )

        choix_signalements.append("Se déconnecter")
        choix = inquirer.select(message="Choisissez :", choices=choix_signalements).execute()

        if choix == "Retour au menu principal":
            Session().deconnexion()
            from vues.accueil.accueil_vue import AccueilVue

            return AccueilVue()
        print("\n" + "-" * 50 + "\nGestion du signalement\n" + "-" * 50 + "\n")
        signalement_choisi = signalements[choix_signalements.index(choix)]

        action = inquirer.select(
            message=f"Actions pour le signalement ID: {signalement_choisi['id_signalement']}:",
            choices=[
                "Supprimer le signalement",
                "Supprimer l'avis",
                "Retour à la liste des signalements",
            ],
        ).execute()

        match action:
            case "Supprimer l'avis":
                avis = AvisService().recuperer_avis_user_et_manga(
                    signalement_choisi["id_manga"],
                    UtilisateurService().recherche_id_par_pseudo(signalement_choisi["pseudo"]),
                )
                AvisService().supprimer_avis(avis)
                print("Avis supprimé")
                self.choisir_menu()

            case "Supprimer le signalement":
                AvisService().supprimer_signalement(signalement_choisi["id_signalement"])
                print("Signalement supprimé.")
                self.choisir_menu()

            case "Retour à la liste des signalements":
                self.choisir_menu()
