from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from service.avis_service import AvisService
from service.recherche_service import RechercheService
from dao.utilisateur_dao import UtilisateurDao
import logging


class AvisRechercheUtilisateurVue(VueAbstraite):
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

    def choisir_menu(self, choix3):
        """Choix du menu suivant de l'utilisateur

        Returns
        -------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nRecherche d'un utilisateur\n" + "-" * 50 + "\n")
        id_utilisateur = UtilisateurDao().recherche_id_par_pseudo(choix3)
        liste_avis, liste_titre = AvisService().recuperer_avis_utilisateur(id_utilisateur)
        n = 0
        m = 8
        sous_liste_avis, sous_liste_titre, longueur_tot = liste_avis[n:n+m], liste_titre[n: n+m], len(liste_avis)

        while n >= 0:
            sous_liste_avis, sous_liste_titre, longueur_tot = liste_avis[n:n+m], liste_titre[n: n+m], len(liste_avis)
            choix2 = ["Afficher la page suivante","Afficher la page précédente", "Retour au menu précédent"]
            for i in range(n, n+m):
                print(
                    "\n" + "-" * 50 + f"\n{sous_liste_avis[i]} Titre: {sous_liste_titre[i]}\n" + "-" * 50 + "\n"
                    )
            if n + m >= longueur_tot:
                choix2.remove("Afficher la page suivante")

            if n == 0:
                choix2.remove("Afficher la page précédente")

            choix3 = inquirer.select(message="Choisissez une action :", choices=choix2).execute()

            if choix3 == "Retour au menu précédent":
                n = -1
                from vues.recherche_vue import RechercheVue
                return RechercheVue().choisir_menu()
            elif choix3 == "Afficher la page suivante":
                n += m
            elif choix3 == "Afficher la page précédente":
                n = max(0, n - m)
