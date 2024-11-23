from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.avis_service import AvisService
from service.utilisateur_service import UtilisateurService
import logging
from vues.session import Session


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

        id_utilisateur = UtilisateurService().recherche_id_par_pseudo(choix3)
        if not AvisService().recuperer_avis_utilisateur(id_utilisateur):
            print("Cet utilisateur n'a aucun avis.\n")
            from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue

            return RechercheUtilisateurVue().choisir_menu_bis(choix3)
        print("\n" + "-" * 50 + f"\nAvis de l'utilisateur {choix3} \n" + "-" * 50 + "\n")
        liste_avis, liste_titre = AvisService().recuperer_avis_utilisateur(id_utilisateur)
        n = 0
        m = 8
        sous_liste_avis, sous_liste_titre, longueur_tot = (
            liste_avis[n : n + m],
            liste_titre[n : n + m],
            len(liste_avis),
        )

        while n >= 0:
            sous_liste_avis, sous_liste_titre, longueur_tot = (
                liste_avis[n : n + m],
                liste_titre[n : n + m],
                len(liste_avis),
            )
            logging.info(f"avis : {sous_liste_avis}")
            choix2 = [
                "Afficher la page suivante",
                "Afficher la page précédente",
                "Signaler un avis",
                "Retour au menu précédent",
            ]
            for i in range(n, min(len(liste_avis), n + m)):
                print(
                    "\n"
                    + "-" * 50
                    + f"\nManga: {sous_liste_titre[i]}\n {i+n} : {sous_liste_avis[i].texte} \n Note : {sous_liste_avis[i].note} \n"
                    + "-" * 50
                    + "\n"
                )
            if n + m >= longueur_tot:
                choix2.remove("Afficher la page suivante")

            if n == 0:
                choix2.remove("Afficher la page précédente")

            choix4 = inquirer.select(message="Choisissez une action :", choices=choix2).execute()

            if choix4 == "Retour au menu précédent":
                n = -1
                from vues.rechercher_utilisateur_vue import RechercheUtilisateurVue

                return RechercheUtilisateurVue().choisir_menu_bis(choix3)

            if choix4 == "Signaler un avis":
                signalement = inquirer.text(message="Quel numéro? ").execute()
                AvisService().creer_signalement(
                    Session().utilisateur.id,
                    liste_avis[int(signalement)].id_avis,
                    "Contenu offensant",
                )
            elif choix4 == "Afficher la page suivante":
                n += m
            elif choix4 == "Afficher la page précédente":
                n = max(0, n - m)
