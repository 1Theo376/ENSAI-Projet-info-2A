from dao.utilisateur_dao import UtilisateurDao
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao
from business_object.utilisateur import Utilisateur


class MangaPossedeService:
    """Classe"""

    def creer_manga_possede(
        self, idm, num_dernier_acquis, num_manquant, statut
    ) -> bool:
        """Création d'un manga possédé"""
        nouveau_manga_p = MangaPossede(
            idmanga=idm,
            num_dernier_acquis=num_dernier_acquis,
            statut=statut,
            num_manquant=num_manquant,
        )
        if MangaPossedeDao().ajouter_manga_p(mangap=nouveau_manga_p):
            return nouveau_manga_p
        else:
            None

    def modifier_num_manquant(self, mangap: MangaPossede, num_manquant):
        """Modification des numéros manquants des tomes d'un manga possédé"""
        if mangap.num_manquant:
            mangap.num_manquant.remove(mangap.num_manquant)
        listenummanquant = MangaPossedeDao().trouver_id_num_manquant_id(mangap.id_manga_p)
        for elt in listenummanquant:
            MangaPossedeDao().supprimer_num_manquant(elt)
        for elt in num_manquant:
            MangaPossedeDao().ajouter_num_manquant(elt)
            mangap.num_manquant.append(elt)
            return mangap.num_manquant
        else:
            None
