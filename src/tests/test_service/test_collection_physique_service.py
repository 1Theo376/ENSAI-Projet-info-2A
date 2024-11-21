import pytest
from unittest.mock import MagicMock
from dao.utilisateur_dao import UtilisateurDao
from dao.collection_physique_dao import CollectionPhysiqueDAO
from service.collection_physique_service import Collection_physique_service
from service.utilisateur_service import UtilisateurService
from service.recherche_service import RechercheService


def test_creer_collectionphys_oui():
    """Test de création d'une collection physique"""
    # GIVEN
    UtilisateurDao().creer = MagicMock(return_value=True)
    CollectionPhysiqueDAO().creer_collectionphys = MagicMock(return_value=True)

    UtilisateurService().creer_compte("manz1", "1234Azer")
    id = UtilisateurDao().recherche_id_par_pseudo("manz1")

    # WHEN
    res = Collection_physique_service().creer_collectionphys("pomme", "bleue", id)
    # THEN
    assert res


def test_creer_collectionphys_non():
    """Test de création d'une collection physique"""
    # GIVEN
    id = 1000
    # WHEN
    res = Collection_physique_service().creer_collectionphys("pomme", "bleue", id)
    # THEN
    assert not res


def test_supprimer_collectionphys_oui():
    """Test de suppression d'une collection physique"""
    # GIVEN
    Collection_physique_service().supprimer_collectionphys = MagicMock(return_value=True)
    id = UtilisateurDao().recherche_id_par_pseudo("manz1")
    collection = RechercheService().recherche_collec_phys_par_id(id)
    # WHEN
    res = Collection_physique_service().supprimer_collectionphys(collection.id_collectionphysique)
    # THEN
    assert res


def test_supprimer_collectionphys_non():
    """Test de suppression d'une collection physique"""
    # GIVEN
    id = 99
    # WHEN
    res = Collection_physique_service().supprimer_collectionphys(id)
    # THEN
    assert not res


def test_ajouter_mangaposs_oui():
    """Test d'ajout d'un manga possédé dans une collection physique"""
    # GIVEN
    CollectionPhysiqueDAO().creer_collectionphys = MagicMock(return_value=True)
    CollectionPhysiqueDAO().ajouter_mangaposs = MagicMock(return_value=True)

    id_util = UtilisateurDao().recherche_id_par_pseudo("manz1")
    Collection_physique_service().creer_collectionphys("pomme", "verte", id_util)
    id_coll = RechercheService().recherche_collec_phys_par_id(id_util).id_collectionphysique
    id_manga = 1

    # WHEN
    res = Collection_physique_service().ajouter_mangaposs(id_coll, id_manga)

    # THEN
    assert res


def test_ajouter_mangaposs_non():
    """Test d'ajout d'un manga possédé dans une collection physique"""
    # GIVEN
    CollectionPhysiqueDAO().creer_collectionphys = MagicMock(return_value=True)
    CollectionPhysiqueDAO().ajouter_mangaposs = MagicMock(return_value=True)

    id_util = UtilisateurDao().recherche_id_par_pseudo("manz1")
    Collection_physique_service().creer_collectionphys("pomme", "verte", id_util)
    id_coll = RechercheService().recherche_collec_phys_par_id(id_util).id_collectionphysique
    id_manga = 1000000000000

    # WHEN
    res = Collection_physique_service().ajouter_mangaposs(id_coll, id_manga)

    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
