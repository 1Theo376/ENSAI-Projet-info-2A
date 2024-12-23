from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from vues.session import Session
from service.recherche_service import RechercheService
from service.avis_service import AvisService
import logging


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
        n = 0
        m = 8
        while n >= 0:
            choix2 = []
            longueur_tot = len(liste_avis)

            for i in range(n, min(longueur_tot, n + m)):
                option = f"titre : {liste_titre[i]} | Avis: {liste_avis[i].texte} | Note: {liste_avis[i].note}"
                choix2.append(option)
            logging.info(f"option : {option}")
            choix2 = choix2 + [
                "Afficher la page suivante",
                "Afficher la page précédente",
                "Retour au menu précédent",
            ]
            if n + m >= longueur_tot:
                choix2.remove("Afficher la page suivante")

            if n == 0:
                choix2.remove("Afficher la page précédente")

            choix_utilisateur = inquirer.select(
                message="Choisissez un avis : ", choices=choix2
            ).execute()

            if choix_utilisateur == "Retour au menu précédent":
                n = -1
                from vues.profil_utilisateur_vue import EcranDuProfilVue

                return EcranDuProfilVue().choisir_menu()

            elif choix_utilisateur == "Afficher la page suivante":
                n += m
            elif choix_utilisateur == "Afficher la page précédente":
                n = max(0, n - m)
            else:
                n = -1
                titre = choix_utilisateur.split("titre : ")[1].split(" |")[0].strip()
                id_manga = (RechercheService().trouver_manga_par_titre(titre)).id_manga
                avis = AvisService().recuperer_avis_user_et_manga(
                    id_manga, Session().utilisateur.id
                )
                choix2 = inquirer.select(
                    message="Faites votre choix : ",
                    choices=["Modifier l'avis", "Supprimer l'avis", "Retour au menu précédent"],
                ).execute()
                match choix2:
                    case "Modifier l'avis":
                        nouvel_avis = input(
                            f"Entrez votre nouvel avis sur le manga {titre} "
                            "(si aucun changement appuyez sur Entrée) : "
                        )
                        nouvelle_note = inquirer.select(
                            message="Donnez une nouvelle note à ce manga:",
                            choices=[1, 2, 3, 4, 5],
                        ).execute()
                        if len(nouvel_avis.strip()) == 0:
                            AvisService().modifier_avis(
                                avis,
                                avis.texte,
                                nouvelle_note,
                            )

                        else:
                            AvisService().modifier_avis(
                                avis,
                                nouvel_avis,
                                nouvelle_note,
                            )

                        return MenuAvis()
                    case "Supprimer l'avis":
                        AvisService().supprimer_avis(avis)
                        from vues.profil_utilisateur_vue import EcranDuProfilVue

                        return EcranDuProfilVue().choisir_menu()

                    case "Retour au menu précédent":
                        return MenuAvis()

                if choix_utilisateur == "Retour au menu précédent":
                    from vues.profil_utilisateur_vue import EcranDuProfilVue

                    return EcranDuProfilVue().choisir_menu()
