class CollectionCohérenteVue(VueAbstraite):
    def choisir_menu(self):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        print("\n" + "-" * 50 + "\nRecherche d'un manga\n" + "-" * 50 + "\n")

        choix = inquirer.select(
            message="Faites votre choix : ",
            choices=["Choisissez votre Collection", "Retour au menu précédent"],
        ).execute()

        match choix:
            case "Entrer le titre du manga recherché":
                titre = inquirer.text(message="Entrer le titre : ").execute()
                n = 0
                while True:
                    choix2 = collection_coherente_service().créer_collectioncohe(titre, n)

                    if not choix2:
                        print(f"Aucun manga trouvé pour le titre '{titre}'.")
                        break

                    choix2.append(["Afficher la page suivante", "Retour au menu précédent"])

                    choix3 = inquirer.select(
                        message="Choisissez un manga : ",
                        choices=choix2,
                    ).execute()

                    if choix3 == "Retour au menu précédent":
                        from vues.menu_utilisateur_vue import MenuUtilisateurVue

                        return MenuUtilisateurVue()
                    else:
                        choix4 = inquirer.select(
                            message="Faites votre choix : ",
                            choices=[
                                "Ajouter à une collection",
                                "Afficher les informations du manga",
                                "Consulter les avis",
                                "Ajouter un avis",
                                "Retour au menu précédent",
                                "Retour vers l'écran d'accueil",
                            ],
                        ).execute()
                        match choix4:
                            case "Ajouter à une collection":
                                pass
                            case "Afficher les informations du manga":
                                print(
                                    "\n" + "-" * 50 + "\nInformation du manga\n" + "-" * 50 + "\n"
                                )
                                print("\n" + "-" * 50 + "\n" + manga.titre + "\n" + "-" * 50 + "\n")
                                print(
                                    "\n" + "-" * 50 + "\n" + manga.synopsis + "\n" + "-" * 50 + "\n"
                                )
                                print(
                                    "\n" + "-" * 50 + "\n" + manga.auteur + "\n" + "-" * 50 + "\n"
                                )
                                print(
                                    "\n" + "-" * 50 + "\n" + manga.themes + "\n" + "-" * 50 + "\n"
                                )
                                print("\n" + "-" * 50 + "\n" + manga.genre + "\n" + "-" * 50 + "\n")
                                choix5 = inquirer.select(
                                    message="Faites votre choix : ",
                                    choices=["Retour au menu précédent"],
                                ).execute()
                                if choix5:
                                    from vues.menu_utilisateur_vue import MenuUtilisateurVue

                                    return MenuUtilisateurVue()

                            case "Consulter les avis":
                                pass

                            case "Ajouter un avis":
                                texte = inquirer.text(
                                    message="Entrez votre avis sur ce manga : "
                                ).execute()
                                AvisService().rediger_avis(texte, id_avis=None)

                            case "Retour au menu précédent":
                                from vues.recherche_vue import RechercheVue

                                return RechercheVue()
                            case "Retour vers l'écran d'accueil":
                                from vues.menu_utilisateur_vue import MenuUtilisateurVue

                                return MenuUtilisateurVue()
                    from vues.menu_utilisateur_vue import MenuUtilisateurVue

                    return MenuUtilisateurVue()
