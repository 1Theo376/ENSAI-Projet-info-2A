from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService


class RechercheMangaVue(VueAbstraite):
    """Vue qui affiche :

    """

    def choisir_menu(self):
        manga_recherche = inquirer.text(message="Entrez le manga recherché: ").execute()
        liste_manga_choix = RechercheService.recherche_manga_par_titre(manga_recherche)
        liste_manga_choix.append("Rechercher de nouveau")
        choix = inquirer.select(
            message="Choisissez un manga : ",
            choices=liste_manga_choix,
        ).execute()
        if choix == "Rechercher de nouveau":

            return RechercheMangaVue()

        else:
            pass
