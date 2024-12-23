from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
import logging
from service.collection_physique_service import Collection_physique_service
from business_object.manga_possede import MangaPossede
from service.manga_possede_service import MangaPossedeService


class AjouterMangaPossCollPhys(VueAbstraite):
    def choisir_menu(self, choix3, collection):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = RechercheService().trouver_manga_par_titre(choix3)
        logging.info(f"id: {manga.id_manga}")
        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")
        volume_manga = MangaPossedeService().nb_volume_manga(manga.titre)
        res = ""
        while not res.isdigit():
            res = inquirer.text(
                message="Entrez le nombre de volumes possédés du manga : "
            ).execute()
            if not res.isdigit():
                print("Valeur incorrecte, entrez un nombre !")
        nb_volumes_poss = int(res)
        if volume_manga:
            if nb_volumes_poss > volume_manga:
                print(f"Nombre incorrect. Ce manga possède {volume_manga} volumes.")
                return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
        volumes_poss = []
        while nb_volumes_poss != 0:
            num_vol = inquirer.text(
                message=(
                    "Entrez les numéros des volumes possédés du manga, "
                    "vous pouvez les écrires sous la forme a-b: "
                )
            ).execute()

            while True:
                if "-" in num_vol:
                    parts = num_vol.split("-")
                    if len(parts) == 2 and all(part.strip().isdigit() for part in parts):
                        if int(parts[0]) > int(parts[1]):
                            print("la tranche doit être de forme a-b avec a < b !")
                        elif (
                            int(parts[0]) not in volumes_poss and int(parts[1]) not in volumes_poss
                        ):
                            break
                        else:
                            print("Vous avez déja enregistré un des volumes")
                    else:
                        print(
                            "Valeur incorrecte pour la tranche, "
                            "entrez sous la forme a-b avec des nombres."
                        )

                elif num_vol.isdigit():
                    if int(num_vol) not in volumes_poss:
                        break
                    else:
                        print("Vous avez déja enregistré ce volume")
                else:
                    print(
                        "Valeur incorrecte, entrez un nombre ou une tranche valide "
                        "sous la forme a-b."
                    )
                num_vol = inquirer.text(
                    message=(
                        "Entrez les numéros des volumes possédés du manga, "
                        "vous pouvez les écrire sous la forme a-b: "
                    )
                ).execute()

            if "-" in num_vol:
                a = int(num_vol.split("-")[0])
                b = int(num_vol.split("-")[1])
                if a < 1 or b < 1 or (nb_volumes_poss - (b - a + 1)) < 0:
                    if volume_manga:
                        if a > volume_manga or b > volume_manga:
                            print("Erreur")
                            return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
                    print("Erreur")
                    return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
                for i in range(a, b + 1):
                    volumes_poss.append(i)
                nb_volumes_poss = nb_volumes_poss - (b - a + 1)
            else:
                num = int(num_vol)
                if volume_manga:
                    if num > volume_manga:
                        print("Erreur")
                        return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
                volumes_poss.append(num)
                nb_volumes_poss -= 1
        logging.info(f"vol:{volumes_poss}")
        if volume_manga:
            num_manquant = [i for i in range(1, volume_manga + 1)]
            logging.info(f"manq: {num_manquant}")
            for elt in volumes_poss:
                num_manquant.remove(elt)
            logging.info(f"manq:{num_manquant}")
        res2 = ""
        while not res2.isdigit():
            res2 = inquirer.text(
                message="Entrez le numéro du dernier volume acquis du manga : "
            ).execute()
            if not res2.isdigit():
                print("Valeur incorrecte, entrez un nombre !")
        num_dernier_acquis = int(res2)
        if num_dernier_acquis not in volumes_poss:
            if volume_manga:
                if num_dernier_acquis > volume_manga:
                    print("Erreur")
                    return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
            print("Erreur")
            return AjouterMangaPossCollPhys().choisir_menu(choix3, collection)
        Statut = inquirer.select(
            message="Quel est votre statut de lecture ?",
            choices=[
                "En cours",
                "Abandonné",
                "Terminé",
            ],
        ).execute()
        mangap = MangaPossede(
            idmanga=manga.id_manga, num_dernier_acquis=num_dernier_acquis, statut=Statut
        )
        logging.info(f"idm = {manga.id_manga}, num = {num_dernier_acquis}, statut = {Statut},")
        MangaPossedeService().ajouter_manga_p(mangap)
        if volume_manga:
            for elt in num_manquant:
                MangaPossedeService().ajouter_ass_num_manquant(
                    mangap.id_manga_p, MangaPossedeService().ajouter_num_manquant(elt)
                )
        Collection_physique_service().ajouter_mangaposs(
            collection.id_collectionphysique, mangap.id_manga_p
        )
        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

        return SelectionMangaVuerecherche().choisir_menu(choix3)
