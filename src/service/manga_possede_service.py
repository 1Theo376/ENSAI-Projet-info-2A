from dao.utilisateur_dao import Utilisateur
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDAO
from business_object.utilisateur import Utilisateur


class MangaPossedeService:
    """Classe"""

    def creer_manga_possede(
        self, id_manga_p, manga: MangaPossede, num_dernier_acquis, num_manquant, statut
    ) -> bool:
        """Création d'un manga possédé"""
        nouveau_manga_p = MangaPossede(
            id_manga_p=id_manga_p,
            manga=manga,
            num_dernier_acquis=num_dernier_acquis,
            num_manquant=num_manquant,
            statut=statut,
        )
        if self.dao.MangaPossedeDAO.ajouter_manga_p(nouveau_manga_p):
            return nouveau_manga_p
        else:
            None

    def modifier_num_dernier_acquis(self, manga: MangaPossede, nouveau_num):
        """Modification du dernier numéro acquis d'un manga possédé"""
        manga.num_dernier_acquis = nouveau_num
        if self.dao.MangaPossedeDAO.modifier_num_dernier_acquis(manga.num_dernier_acquis):
            return manga.num_dernier_acquis
        else:
            None

    def modifier_num_manquant(self, manga: MangaPossede, num_manquant, num_acquis):
        """Modification des numéros manquants des tomes d'un manga possédé"""
        manga.num_manquant.remove(num_acquis)
        if self.dao.MangaPossedeDAO.ajouter_num_manquant(manga.num_manquant):
            return manga.num_manquant
        else:
            None

    def modifier_statut(self, manga: MangaPossede, statut):
        """Modification du statut de lecture du manga possédé"""
        manga.statut = statut
        if self.dao.MangaPossedeDAO.modifier_statut(manga.statut):
            return manga.statut
        else:
            None
