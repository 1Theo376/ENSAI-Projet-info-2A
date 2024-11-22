import pytest
from dao.manga_possede_dao import MangaPossedeDao
from business_object.manga_possede import MangaPossede
from business_object.manga import Manga
from unittest.mock import patch, MagicMock
from business_object.collection_phys import Collection_physique
from business_object.utilisateur import Utilisateur
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.utilisateur_dao import UtilisateurDao
from dao.manga_dao import MangaDao

utilisateur1 = Utilisateur("Testuser", "Barte8755")
UtilisateurDao().creer(utilisateur1)
manga1 = MangaDao().trouver_manga_par_id(1)

mangap = MangaPossede(idmanga=1, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours")

collecphysique = Collection_physique(
    id_collectionphysique=0,
    titre_collection="TestCollec",
    description_collection="Description test",
)
CollectionPhysiqueDAO().creer_collectionphys(collecphysique, utilisateur1.id)


def test_ajouter_manga_p():
    # GIVEN
    mangap = MangaPossede(
        idmanga=1, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours"
    )
    # WHEN
    res = MangaPossedeDao().ajouter_manga_p(mangap)
    # THEN
    assert res


def test_nb_volume_manga():
    # GIVEN
    nom = "Monster"  # il y a 18 tomes dans ce manga
    # WHEN
    volumes = MangaPossedeDao().nb_volume_manga(nom)
    # THEN
    assert volumes == 18


def test_trouver_manga_possede_collecphys():
    # GIVEN
    titre = manga1.titre
    # WHEN
    mangap2 = MangaPossedeDao().trouver_manga_possede_collecphys(
        titre, collecphysique.id_collectionphysique
    )
    # THEN
    assert mangap.num_dernier_acquis == mangap2.num_dernier_acquis


def test_trouver_id_num_manquant_id():  # difficile
    # GIVEN
    idp = mangap.id_manga_p
    # WHEN
    liste_id_num_manquant = MangaPossedeDao().trouver_id_num_manquant_id(idp)
    # THEN
    assert liste_id_num_manquant


def test_ajouter_num_manquant():
    # GIVEN
    num_manquant1 = 5
    # WHEN
    res = MangaPossedeDao().ajouter_num_manquant(num_manquant1)
    # THEN
    assert res


def test_ajouter_ass_num_manquant():  # à revoir
    # GIVEN
    liste_id_num_manquant = MangaPossedeDao().trouver_id_num_manquant_id(idp)
    # WHEN
    res = MangaPossedeDao().ajouter_ass_num_manquant(mangap.id_manga_p, liste_id_num_manquant[0])
    # THEN
    assert res


def test_trouver_manga_possede_id():
    # GIVEN
    idp = mangap.id_manga_p
    # WHEN
    mangap3 = MangaPossedeDao().trouver_manga_possede_id(idp)
    # THEN
    assert mangap.num_dernier_acquis == mangap3.num_dernier_acquis


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
