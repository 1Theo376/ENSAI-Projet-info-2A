from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao


class MangaPossedeService:
    """Classe"""

    def creer_manga_possede(self, idm, num_dernier_acquis, num_manquant, statut) -> bool:
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
        mangap.num_manquant = []
        listenummanquant = MangaPossedeDao().trouver_id_num_manquant_id(mangap.id_manga_p)
        for elt in listenummanquant:
            MangaPossedeDao().supprimer_num_manquant(elt)
        for elt in num_manquant:
            if MangaPossedeDao().ajouter_num_manquant(elt):
                mangap.num_manquant.append(elt)
        return mangap.num_manquant

    def ajouter_manga_p(self, mangap) -> bool:
        return MangaPossedeDao().ajouter_manga_p(mangap)

    def nb_volume_manga(self, nom):
        return MangaPossedeDao().nb_volume_manga(nom)

    def trouver_manga_possede_collecphys(self, titre, id_collec_phys):
        return MangaPossedeDao().trouver_manga_possede_collecphys(titre, id_collec_phys)

    def ajouter_num_manquant(self, num_manquant) -> bool:
        return MangaPossedeDao().ajouter_num_manquant(num_manquant)

    def ajouter_ass_num_manquant(self, id_manga_p, id_num_manquant) -> bool:
        return MangaPossedeDao().ajouter_ass_num_manquant(id_manga_p, id_num_manquant)

    def trouver_id_num_manquant_id(self, id_p):
        return MangaPossedeDao().trouver_id_num_manquant_id(id_p)

    def supprimer_num_manquant(self, idnm) -> bool:
        return MangaPossedeDao().supprimer_num_manquant(idnm)
