from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from service.avis_service import AvisService
from service.recherche_service import RechercheService
from dao.utilisateur_dao import UtilisateurDao
import logging


class RechercheUtilisateurVue(VueAbstraite):
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

        Returns
        -------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """

        print("\n" + "-" * 50 + "\nRecherche d'un utilisateur\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=["Entrer le pseudo de l'utilisateur recherché", "Retour au menu précédent"],
        ).execute()

        match choix:
            case "Entrer le pseudo de l'utilisateur recherché":
                pseudo = inquirer.text(message="Entrer le pseudo : ").execute()
                n = 0
                m = 8
                a = 0
                longueur, sous_liste, longueur_tot = RechercheService().recherche_utilisateur(pseudo, n, m, a)
                logging.info(f"longueur : {longueur}")
                res_entier = longueur // m
                res_reste = longueur % m

                if not RechercheService().recherche_utilisateur(pseudo, n, m, a):
                    print(f"Aucun utilisateur trouvé pour le pseudo '{pseudo}'.")
                    choix2 = ["Retour au menu précédent"]
                    choix3 = inquirer.select(
                        message="Faites votre choix : ",
                        choices=choix2
                        ).execute()

                while n >= 0:
                    longueur, sous_liste, longueur_tot = RechercheService().recherche_utilisateur(pseudo, n, m, a)
                    choix2 = sous_liste

                    choix2.extend(["Afficher la page suivante", "Retour au menu précédent"])

                    if (res_entier == 0 and res_reste == 0) or longueur_tot <= 8:
                        choix2.remove("Afficher la page suivante")

                    if res_entier != (longueur // m):
                        choix2.extend(["Afficher la page précédente"])
                        res_entier += 1

                    choix3 = inquirer.select(
                        message="Choisissez un utilisateur : ",
                        choices=choix2,
                    ).execute()

                    if choix3 == "Retour au menu précédent":
                        from vues.menu_utilisateur_vue import MenuUtilisateurVue
                        return MenuUtilisateurVue().choisir_menu()

                    elif choix3 == "Afficher la page suivante":
                        if res_entier != 0:
                            n = n + m
                            res_entier -= 1
                        if res_entier == 0 and res_reste != 0:
                            n = n + m
                            a = res_reste - m

                    else:
                        n = -1
                        choix4 = inquirer.select(
                            message="Faites votre choix : ",
                            choices=[
                                "Consulter les collections",
                                "Consulter les avis",
                                "Retour au menu précédent",
                                "Retour vers l'écran d'accueil",
                            ],
                        ).execute()
                        match choix4:
                            case "Consulter les collections":
                                from vues.ConsulterCollecVue import CollectionCoherenteVueRecherche
                                return CollectionCoherenteVueRecherche().choisir_menu(choix3)

                            case "Consulter les avis":
                                from vues.AvisRechercheUtilisateurVue import (
                                    AvisRechercheUtilisateurVue,
                                )

                                return AvisRechercheUtilisateurVue().choisir_menu(choix3)
                            case "Retour au menu précédent":
                                from vues.recherche_vue import RechercheVue
                                return RechercheVue().choisir_menu()

                            case "Retour vers l'écran d'accueil":
                                from vues.menu_utilisateur_vue import MenuUtilisateurVue
                                return MenuUtilisateurVue("Bon retour")

        from vues.menu_utilisateur_vue import MenuUtilisateurVue

        return MenuUtilisateurVue()
