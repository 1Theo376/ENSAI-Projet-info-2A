from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from service.avis_service import AvisService
from vues.session import Session


class ConsulterAvisMangaVuerecherche(VueAbstraite):
    def choisir_menu(self, choixm):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = RechercheService().trouver_manga_par_titre(choixm)

        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")

        n = 0
        m = 8
        if not AvisService().recuperer_avis_manga(manga.id_manga):
            print(f"Aucun avis trouvé pour le manga '{manga.titre}'.")
            from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

            return SelectionMangaVuerecherche().choisir_menu(choixm)
        liste_avis, liste_pseudo = AvisService().recuperer_avis_manga(manga.id_manga)
        longueur_tot = len(liste_avis)
        while n >= 0:
            choix2 = [
                "Afficher la page suivante",
                "Afficher la page précédente",
                "Signaler un avis",
                "Retour au menu précédent",
            ]
            for i in range(n, min(longueur_tot, n + m)):
                print(
                    "\n"
                    + "-" * 50
                    + f"\nUtilisateur: {liste_pseudo[i]}\n{i} : {liste_avis[i].texte} \n Note : {liste_avis[i].note}\n"
                    + "-" * 50
                    + "\n"
                )
            if n + m >= longueur_tot:
                choix2.remove("Afficher la page suivante")

            if n == 0:
                choix2.remove("Afficher la page précédente")

            if AvisService().AvisUtilisateurMangaExistant(Session().utilisateur.id, manga.id_manga):
                choix2.extend(["Modifier votre avis sur ce manga"])

            choix3 = inquirer.select(message="Choisissez une action :", choices=choix2).execute()

            if choix3 == "Modifier votre avis sur ce manga":
                n = -1
                nouvel_avis = input(
                    f"Entrez votre nouvel avis sur le manga {choixm} "
                    "(si aucun changement appuyez sur Entrée) : "
                )
                nouvelle_note = inquirer.select(
                    message="Donnez une nouvelle note à ce manga:",
                    choices=[1, 2, 3, 4, 5],
                ).execute()
                if len(nouvel_avis.strip()) == 0:
                    AvisService().modifier_avis(
                        AvisService().recuperer_avis_user_et_manga(
                            RechercheService().trouver_manga_par_titre(choixm).id_manga,
                            Session().utilisateur.id,
                        ),
                        (
                            AvisService()
                            .recuperer_avis_user_et_manga(
                                RechercheService().trouver_manga_par_titre(choixm).id_manga,
                                Session().utilisateur.id,
                            )
                            .texte,
                        ),
                        nouvelle_note,
                    )

                else:
                    AvisService().modifier_avis(
                        AvisService().recuperer_avis_user_et_manga(
                            RechercheService().trouver_manga_par_titre(choixm).id_manga,
                            Session().utilisateur.id,
                        ),
                        nouvel_avis,
                        nouvelle_note,
                    )
                return ConsulterAvisMangaVuerecherche().choisir_menu(choixm)

            if choix3 == "Retour au menu précédent":
                n = -1
                from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

                return SelectionMangaVuerecherche().choisir_menu(choixm)
            if choix3 == "Signaler un avis":
                signalement = inquirer.text(message="Quel numéro? ").execute()
                AvisService().creer_signalement(
                    Session().utilisateur.id,
                    liste_avis[int(signalement)].id_avis,
                    "Contenu offensant",
                )
            elif choix3 == "Afficher la page suivante":
                n += m
            elif choix3 == "Afficher la page précédente":
                n = max(0, n - m)
