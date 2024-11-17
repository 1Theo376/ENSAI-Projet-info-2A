from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from dao.manga_dao import MangaDao
from service.avis_service import AvisService
from vues.session import Session
import logging
from dao.avis_dao import AvisDAO


class ConsulterAvisMangaVuerecherche(VueAbstraite):
    def choisir_menu(self, choixm):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = MangaDao().trouver_manga_par_titre(choixm)

        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")

        n = 0
        m = 8
        liste_avis, liste_pseudo = AvisService().recuperer_avis_manga2(manga.id_manga)
        longueur_tot = len(liste_avis)
        if not AvisService().recuperer_avis_manga2(manga.id_manga):
            print(f"Aucun avis trouvé pour le manga '{manga.titre}'.")

        while n >= 0:

            sous_liste_avis, sous_liste_pseudo = liste_avis[n:n+m], liste_pseudo[n:n+m]

            choix2 = ["Afficher la page suivante", "Afficher la page précédente", "Retour au menu précédent"]
            for i in range(n, min(len(liste_avis), n+m)):
                print(
                    "\n" + "-" * 50 + f"\nManga: {sous_liste_pseudo[i]}\n{sous_liste_avis[i].texte} \n" + "-" * 50 + "\n"
                    )
            if n + m >= longueur_tot:
                choix2.remove("Afficher la page suivante")

            if n == 0:
                choix2.remove("Afficher la page précédente")

            if AvisDAO().AvisUtilisateurMangaExistant(Session().utilisateur.id, manga.id_manga):
                choix2.extend(["Modifier votre avis sur ce manga"])

            choix3 = inquirer.select(message="Choisissez une action :", choices=choix2).execute()

            if choix2 == "Modifier votre avis sur ce manga":
                n=-1
                pass

            if choix3 == "Retour au menu précédent":
                n = -1
                from vues.rechercher_manga_vue import RechercheMangaVue
                return RechercheMangaVue().choisir_menu()
            elif choix3 == "Afficher la page suivante":
                n += m
            elif choix3 == "Afficher la page précédente":
                n = max(0, n - m)
