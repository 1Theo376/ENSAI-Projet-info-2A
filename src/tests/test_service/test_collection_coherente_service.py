import pytest
from unittest.mock import MagicMock, patch
from business_object.CollectionCoherente import CollectionCoherente
from business_object.manga import Manga
from dao.utilisateur_dao import UtilisateurDao
from dao.collection_coherente_dao import CollectionCoherenteDAO
from service.collection_coherente_service import CollectionCoherenteService
from service.utilisateur_service import UtilisateurService
from service.recherche_service import RechercheService


# Objets
collection = CollectionCoherente(1, "Matcha", "vert")
manga = Manga(1, "Naruto", "blabla", "Delemare, Jacques", "pouvoir", "action")


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.creer_collection', return_value=True)
def test_creer_collection_oui(patch):
    """Test de création d'une collection cohérente"""
    # GIVEN

    # WHEN
    res = CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", 5)
    # THEN
    assert res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.creer_collection', return_value=False)
def test_creer_collection_non(patch):
    """Test de création d'une collection cohérente"""
    # GIVEN

    # WHEN
    res = CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", 5)
    # THEN
    assert not res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.supprimer_collection', return_value=True)
def test_supprimer_collectioncohe_oui(patch):
    """Test de suppression d'une collection cohérente"""
    # GIVEN

    # WHEN
    res = CollectionCoherenteService().supprimer_collectioncohe(collection)
    # THEN
    assert res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.supprimer_collection', return_value=False)
def test_supprimer_collectioncohe_non(patch):
    """Test de suppression d'une collection cohérente"""
    # GIVEN

    # WHEN
    res = CollectionCoherenteService().supprimer_collectioncohe(collection)
    # THEN
    assert not res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.ajouter_manga', return_value=True)
def test_ajouter_mangaposs_oui(patch):
    """Test d'ajout d'un manga possédé dans une collection cohérente"""
    # GIVEN
    id_manga = 1
    # WHEN
    res = CollectionCoherenteService().ajouter_manga(collection.id_collectioncoherente, id_manga)
    # THEN
    assert res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.ajouter_manga', return_value=False)
def test_ajouter_mangaposs_non(patch):
    """Test d'ajout d'un manga possédé dans une collection cohérente"""
    # GIVEN
    id_manga = 1
    # WHEN
    res = CollectionCoherenteService().ajouter_manga(collection.id_collectioncoherente, id_manga)
    # THEN
    assert not res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.supprimer_manga', return_value=True)
def test_supprimer_mangaposs_oui(patch):
    """Test d'ajout d'un manga possédé dans une collection cohérente"""
    # GIVEN

    # WHEN
    res = CollectionCoherenteService().supprimer_mangaposs(collection, manga)
    # THEN
    assert res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.supprimer_manga', return_value=False)
def test_supprimer_mangaposs_non(patch):
    """Test d'ajout d'un manga possédé dans une collection cohérente"""
    # GIVEN

    # WHEN
    res = CollectionCoherenteService().supprimer_mangaposs(collection, manga)
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
