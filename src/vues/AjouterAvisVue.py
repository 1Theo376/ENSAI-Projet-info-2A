from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.avis_service import AvisService
from vues.session import Session
import logging
from service.recherche_service import RechercheService


class AjouterAvisVuerecherche(VueAbstraite):
    def choisir_menu(self, choix3):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = RechercheService().trouver_manga_par_titre(choix3)
        if AvisService().AvisUtilisateurMangaExistant(Session().utilisateur.id, manga.id_manga):
            from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

            print("\n" * 30)
            print("Vous avez déjà donné un avis sur ce manga.")
            return SelectionMangaVuerecherche().choisir_menu(choix3)
        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")
        avis = inquirer.text(message="Entrer votre avis sur ce manga : ").execute()
        note = inquirer.select(
            message="Donnez une note à ce manga:",
            choices=[0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
        ).execute()
        aviscreer = AvisService().rediger_avis(
            texte=avis,
            id_user=Session().utilisateur.id,
            id_manga=manga.id_manga,
            id_avis=None,
            note=note
        )
        logging.info(f"id:{Session().utilisateur.id} et manga:{manga.id_manga}")
        logging.info(f"Avis : {aviscreer}")
        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

        print("\n" * 30)
        print("Avis crée avec succès")
        return SelectionMangaVuerecherche().choisir_menu(choix3)
