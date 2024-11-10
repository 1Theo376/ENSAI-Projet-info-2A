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
        for i in range(len(liste_avis)):
            print(
                "\n" + "-" * 50 + f"\n{liste_avis[i]} Titre: {liste_titre[i]}\n" + "-" * 50 + "\n"
                )
        choixavis = inquirer.select(
                                message="Faites votre choix : ",
                                choices=["Retour au menu précédent", "Retour à l'accueil"],
                                ).execute()
        match choixavis:
            case "Retour au menu précédent":
                from vues.recherche_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue()
            case "Retour à l'accueil":
                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                return MenuUtilisateurVue()
