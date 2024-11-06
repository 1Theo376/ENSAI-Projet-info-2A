import pytest
from unittest.mock import MagicMock
from business_object.manga_possede import MangaPossede
from business_object.collection_phys import CollectionPhysique
from service.collection_physique_service import CollectionPhysiqueService


@pytest.fixture
def collection_physique_service():
    """Fixture pour créer une instance du service CollectionPhysiqueService avec un mock du DAO"""
    service = CollectionPhysiqueService()
    service.dao = MagicMock()  # Remplacer l'instance DAO par un mock
    return service


@pytest.fixture
def collection_physique():
    """Fixture pour créer une instance de CollectionPhysique"""
    return CollectionPhysique(
        id_collection_physique=1,
        titre_collection="Ma Collection",
        desc_collection="Une collection de mangas",
        Liste_manga=[]
    )


@pytest.fixture
def manga_possede():
    """Fixture pour créer un MangaPossede"""
    return MangaPossede(
        id_manga_p=1,
        manga="Naruto",  # Par exemple
        num_dernier_acquis=5,
        num_manquant=[1, 2, 3],
        statut="A lire"
    )


def test_creer_collection_physique(collection_physique_service):
    """Test de la création d'une collection physique"""
    # Préparer le mock pour la méthode DAO
    collection_physique_service.dao.ajouter_collection_physique.return_value = True

    # Appeler la méthode du service
    result = collection_physique_service.creer_collection_physique(1, "Ma Collection", "Description")

    # Vérification
    assert result is not None  # Collection doit être créée
    collection_physique_service.dao.ajouter_collection_physique.assert_called_once()


def test_supprimer_collection_physique(collection_physique_service, collection_physique):
    """Test de la suppression d'une collection physique"""
    # Préparer le mock pour la méthode DAO
    collection_physique_service.dao.supprimer_collection_physique.return_value = True

    # Appeler la méthode du service
    result = collection_physique_service.supprimer_collection_physique(collection_physique)

    # Vérification
    assert result is True  # La suppression doit être réussie
    collection_physique_service.dao.supprimer_collection_physique.assert_called_once()


def test_ajouter_manga_possede(collection_physique_service, collection_physique, manga_possede):
    """Test de l'ajout d'un manga possédé à une collection physique"""
    # Préparer le mock pour la méthode DAO
    collection_physique_service.dao.ajouter_manga_possede.return_value = True

    # Appeler la méthode du service
    result = collection_physique_service.ajouter_manga_possede(collection_physique, manga_possede)

    # Vérification
    assert result is True  # Le manga doit être ajouté à la collection
    collection_physique_service.dao.ajouter_manga_possede.assert_called_once()


def test_supprimer_manga_possede(collection_physique_service, collection_physique, manga_possede):
    """Test de la suppression d'un manga possédé d'une collection physique"""
    # Ajouter un manga à la collection avant de tester la suppression
    collection_physique.Liste_manga.append(manga_possede)

    # Préparer le mock pour la méthode DAO
    collection_physique_service.dao.supprimer_manga_possede.return_value = True

    # Appeler la méthode du service
    result = collection_physique_service.supprimer_manga_possede(collection_physique, manga_possede)

    # Vérification
    assert result is True  # Le manga doit être supprimé de la collection
    collection_physique_service.dao.supprimer_manga_possede.assert_called_once()


def test_str(collection_physique_service, collection_physique, manga_possede):
    """Test de la méthode __str__ pour afficher les mangas de la collection"""
    # Ajouter un manga à la collection
    collection_physique.Liste_manga.append(manga_possede)

    # Appeler la méthode __str__
    result = collection_physique_service.__str__(collection_physique)

    # Vérification
    assert "Voici les mangas présents dans cette collection" in result
    assert manga_possede.manga in result

    # Tester avec une collection vide
    collection_physique.Liste_manga.clear()
    result_empty = collection_physique_service.__str__(collection_physique)
    assert "La collection ne contient aucun manga." in result_empty
