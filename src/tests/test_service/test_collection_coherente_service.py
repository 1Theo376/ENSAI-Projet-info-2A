import pytest
from unittest.mock import MagicMock
from business_object.manga import Manga
from business_object.CollectionCoherente import CollectionCoherente
from service.collection_coherente_service import CollectionCoherenteService


@pytest.fixture
def collection_coherente_service():
    """Fixture pour créer une instance du service CollectionCoherenteService avec un mock du DAO"""
    service = CollectionCoherenteService()
    service.dao = MagicMock()  # Remplacer l'instance DAO par un mock
    return service


@pytest.fixture
def collection_coherente():
    """Fixture pour créer une instance de CollectionCoherente"""
    return CollectionCoherente(
        id_collectioncoherente=1,
        titre_collection="Ma Collection Coherente",
        desc_collection="Une collection cohérente de mangas",
        Liste_manga=[]
    )


@pytest.fixture
def manga():
    """Fixture pour créer un instance de Manga"""
    return Manga(
        id_manga=1,
        titre="Naruto",
        synopsis="L'histoire de Naruto",
        auteur=["Masashi Kishimoto"],
        themes=["Aventures", "Action", "Fantasie"],
        genre=["Action", "Aventure"],
    )


def test_creer_collectioncohe(collection_coherente_service):
    """Test de la création d'une collection cohérente"""
    # Mock du DAO
    collection_coherente_service.dao = MagicMock()
    collection_coherente_service.dao.creer_collectioncohe.return_value = True

    # Appel de la méthode du service
    result = collection_coherente_service.creer_collectioncohe("Ma Collection", "Description")

    # Vérifications
    assert result is not None  # La collection doit être créée
    collection_coherente_service.dao.creer_collectioncohe.assert_called_once()


def test_supprimer_collectioncohe(collection_coherente_service, collection_coherente):
    """Test de la suppression d'une collection cohérente"""
    # Préparer le mock pour la méthode DAO
    collection_coherente_service.dao.CollectionCoherenteDAO.supprimer_collection.return_value = True

    # Appeler la méthode du service
    result = collection_coherente_service.supprimer_collectioncohe(collection_coherente)

    # Vérification
    assert result is True  # La suppression doit être réussie
    collection_coherente_service.dao.CollectionCoherenteDAO.supprimer_collection.assert_called_once()


def test_ajouter_manga_possede(collection_coherente_service, collection_coherente, manga):
    """Test de l'ajout d'un manga possédé à une collection cohérente"""
    # Préparer le mock pour la méthode DAO
    collection_coherente_service.dao.CollectionCoherenteDAO.ajouter_manga.return_value = True

    # Appeler la méthode du service
    result = collection_coherente_service.ajouter_mangaposs(collection_coherente, manga)

    # Vérification
    assert result is collection_coherente  # La collection doit être mise à jour avec le manga
    collection_coherente_service.dao.CollectionCoherenteDAO.ajouter_manga.assert_called_once()


def test_supprimer_manga_possede(collection_coherente_service, collection_coherente, manga):
    """Test de la suppression d'un manga possédé d'une collection cohérente"""
    # Ajouter un manga à la collection avant de tester la suppression
    collection_coherente.Liste_manga.append(manga)

    # Préparer le mock pour la méthode DAO
    collection_coherente_service.dao.CollectionCoherenteDAO.supprimer_manga.return_value = True

    # Appeler la méthode du service
    result = collection_coherente_service.supprimer_mangaposs(collection_coherente, manga)

    # Vérification
    assert result is True  # Le manga doit être supprimé de la collection
    collection_coherente_service.dao.CollectionCoherenteDAO.supprimer_manga.assert_called_once()


def test_str(collection_coherente_service, collection_coherente, manga):
    """Test de la méthode __str__ pour afficher les mangas de la collection"""
    # Ajouter un manga à la collection
    collection_coherente.Liste_manga.append(manga)

    # Appeler la méthode __str__
    result = collection_coherente_service.__str__(collection_coherente)

    # Vérification
    assert "Voici les mangas présents dans cette collection" in result
    assert manga.titre in result

    # Tester avec une collection vide
    collection_coherente.Liste_manga.clear()
    result_empty = collection_coherente_service.__str__(collection_coherente)
    assert "La collection ne contient aucun manga." in result_empty
