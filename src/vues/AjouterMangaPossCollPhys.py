from InquirerPy import inquirer
from vues.vue_abstraite import VueAbstraite
from service.recherche_service import RechercheService
from dao.manga_dao import MangaDao
from service.avis_service import AvisService
from vues.session import Session
import logging
from dao.avis_dao import AvisDAO
from dao.utilisateur_dao import UtilisateurDao
from service.collection_coherente_service import CollectionCoherenteService
from service.collection_physique_service import Collection_physique_service
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.collection_physique_dao import CollectionPhysiqueDAO
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao


class AjouterMangaPossCollPhys(VueAbstraite):
    def choisir_menu(self, choix3, collection):
        """Choix du menu suivant de l'utilisateur

        Return
        ------
        vue
            Retourne la vue choisie par l'utilisateur dans le terminal
        """
        manga = MangaDao().trouver_manga_par_titre(choix3)
        logging.info(f"id: {manga.id_manga}")
        print("\n" + "-" * 50 + "\nManga :", manga.titre, " \n" + "-" * 50 + "\n")

        id_utilisateur = Session().utilisateur.id
        nb_volumes_poss = int(
            inquirer.text(message="Entrez le nombre de volumes possédés du manga : ").execute()
        )
        volumes_poss = []
        for i in range(0, nb_volumes_poss):
            volumes_poss.append(
                int(
                    inquirer.text(
                        message="Entrez le numéro des volumes possédés du manga : "
                    ).execute()
                )
            )
        num_dernier_acquis = int(
            inquirer.text(message="Entrez le numéro du dernier volume acquis du manga : ").execute()
        )
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
        MangaPossedeDao().ajouter_manga_p(mangap)
        Collection_physique_service().ajouter_mangaposs(
            collection.id_collectionphysique, mangap.id_manga_p
        )
        from vues.Selection_manga_vue_recherche import SelectionMangaVuerecherche

        return SelectionMangaVuerecherche().choisir_menu(choix3)
