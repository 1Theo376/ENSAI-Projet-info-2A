import pytest
from unittest.mock import MagicMock, patch
from dao.utilisateur_dao import UtilisateurDao
from dao.collection_physique_dao import CollectionPhysiqueDAO
from service.collection_physique_service import Collection_physique_service


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.creer_collectionphys', return_value=True)
def test_creer_collectionphys_oui(patch):
    """Test de création d'une collection physique"""
    # GIVEN

    # WHEN
    res = Collection_physique_service().creer_collectionphys("pomme", "bleue", 1)
    # THEN
    assert res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.creer_collectionphys', return_value=False)
def test_creer_collectionphys_non(patch):
    """Test de création d'une collection physique"""
    # GIVEN

    # WHEN
    res = Collection_physique_service().creer_collectionphys("pomme", "bleue", 1)
    # THEN
    assert not res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.supprimer_collectionphys', return_value=True)
def test_supprimer_collectionphys_oui(patch):
    """Test de suppression d'une collection physique"""
    # GIVEN
    id = 1
    # WHEN
    res = Collection_physique_service().supprimer_collectionphys(id)
    # THEN
    assert res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.supprimer_collectionphys', return_value=False)
def test_supprimer_collectionphys_non(patch):
    """Test de suppression d'une collection physique"""
    # GIVEN
    id = 1
    # WHEN
    res = Collection_physique_service().supprimer_collectionphys(id)
    # THEN
    assert not res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.ajouter_mangaposs', return_value=True)
def test_ajouter_mangaposs_oui(patch):
    """Test d'ajout d'un manga possédé dans une collection physique"""
    # GIVEN
    id_coll = 1
    id_manga = 2

    # WHEN
    res = Collection_physique_service().ajouter_mangaposs(id_coll, id_manga)

    # THEN
    assert res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.ajouter_mangaposs', return_value=False)
def test_ajouter_mangaposs_non(patch):
    """Test d'ajout d'un manga possédé dans une collection physique"""
    # GIVEN
    id_coll = 1
    id_manga = 2

    # WHEN
    res = Collection_physique_service().ajouter_mangaposs(id_coll, id_manga)

    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
