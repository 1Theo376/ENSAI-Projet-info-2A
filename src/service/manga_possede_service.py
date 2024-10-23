from dao.utilisateur_dao import Utilisateur
from manga_possede import MangaPossede
from manga_possede_dao import MangaPossedeDAO
from business_object.utilisateur import Utilisateur


class MangaPossedeService:
    """Classe"""

    def creer_manga_possede(self, id_manga_p, manga, num_dernier_acquis, num_manquant, statut) -> bool:
        """Création d'un manga possédé"""
        nouveau_manga_p = MangaPossede(
            id_manga_p=id_manga_p,
            manga=manga,
            num_dernier_acquis=num_dernier_acquis,
            num_manquant=num_manquant,
            statut=statut
        )
        return nouveau_manga_p if self.dao.MangaPossedeDAO.ajouter_manga_p(nouveau_manga_p) else None

    def modifier_num_dernier_acquis(self, manga: MangaPossede, nouveau_num):
        manga.num_dernier_acquis = nouveau_num
        return manga.num_dernier_acquis if self.dao.MangaPossedeDAO.modifier_num_dernier_acquis(manga.num_dernier_acquis) else None

    def modifier_num_manquant(self, manga: MangaPossede, num_manquant, num_acquis):
        manga.num_manquant.remove(num_acquis)
        return manga.num_manquant if self.dao.MangaPossedeDAO.ajouter_num_manquant(manga.num_manquant) else None

    def modifier_statut(self, manga: MangaPossede, statut):
        manga.statut = statut
        return manga.statut if self.dao.MangaPossedeDAO.modifier_statut(manga.statut) else None
