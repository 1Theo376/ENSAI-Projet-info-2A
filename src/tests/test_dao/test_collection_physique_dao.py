import pytest
from unittest.mock import patch, MagicMock
from dao.collection_physiquedao import CollectionPhysiqueDAO
from business_object.collection_phys import Collection_physique
from business_object.manga_possede import MangaPossede


@pytest.fixture
def mock_db_connection():
    """Mock pour DBConnection."""
    with patch("dao.collection_physiquedao.DBConnection") as mock_db:
        yield mock_db


@pytest.fixture
def collection_physique():
    """Fixture pour une instance de Collection_physique."""
    return Collection_physique(
        id_collectionphysique=1,
        titre_collection="Ma Collection",
        desc_collection="Description de la collection"
    )


@pytest.fixture
def manga_possede():
    """Fixture pour une instance de MangaPossede."""
    return MangaPossede(
        id_mangapossede=10,
        num_dernier_acquis=5,
        num_manquant=[2, 4],
        statut="En cours"
    )


def test_supprimer_collectionphys(mock_db_connection, collection_physique):
    """Test de la méthode supprimer_collectionphys."""
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1  # Simule une suppression réussie
    mock_db_connection.return_value.connection.cursor.return_value = mock_cursor

    dao = CollectionPhysiqueDAO()
    result = dao.supprimer_collectionphys(collection_physique)

    mock_cursor.execute.assert_called_once_with(
        "DELETE FROM collection_physique WHERE id_collec_coherente=%(id)s",
        {"id": collection_physique.id_collectionphysique}
    )
    assert result is True


def test_creer_collectionphys(mock_db_connection, collection_physique):
    """Test de la méthode creer_collectionphys."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {"id_collec_physique": 1}  # Simule un ID renvoyé
    mock_db_connection.return_value.connection.cursor.return_value = mock_cursor

    dao = CollectionPhysiqueDAO()
    result = dao.creer_collectionphys(collection_physique)

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO collection_physique (id_collec_physique, titre_collection, description_collection) "
        "VALUES (%(id)s, %(titre)s, %(desc)s) RETURNING id_collec_physique;",
        {
            "id": collection_physique.id_collectionphysique,
            "titre": collection_physique.titre_collection,
            "desc": collection_physique.desc_collection,
        }
    )
    assert result is True
    assert collection_physique.id_collectionphysique == 1


def test_supprimer_mangaposs(mock_db_connection, collection_physique, manga_possede):
    """Test de la méthode supprimer_mangaposs."""
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1  # Simule une suppression réussie
    mock_db_connection.return_value.connection.cursor.return_value = mock_cursor

    dao = CollectionPhysiqueDAO()
    result = dao.supprimer_mangaposs(collection_physique, manga_possede)

    mock_cursor.execute.assert_called_once_with(
        "DELETE FROM association_manga_collection_physique "
        "WHERE (id_collec_physique=%(id_collec_physique)s and id_manga_physique=%(idm)s",
        {
            "id_collec_physique": collection_physique.id_collectionphysique,
            "idm": manga_possede.id_mangapossede,
        }
    )
    assert result is True


def test_ajouter_mangaposs(mock_db_connection, collection_physique, manga_possede):
    """Test de la méthode ajouter_mangaposs."""
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {
        "id_collec_physique": collection_physique.id_collectionphysique,
        "id_manga_physique": manga_possede.id_mangapossede
    }
    mock_db_connection.return_value.connection.cursor.return_value = mock_cursor

    dao = CollectionPhysiqueDAO()
    result = dao.ajouter_mangaposs(collection_physique, manga_possede)

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO association_manga_collection_physique(id_collec_physique, id_manga_physique) VALUES "
        "(%(idc)s, %(idm)s) RETURNING id_collec_physique, id_manga_physique;",
        {
            "idc": collection_physique.id_collectionphysique,
            "idm": manga_possede.id_mangapossede,
        }
    )
    assert result is True
    assert collection_physique.id_collectionphysique == mock_cursor.fetchone.return_value["id_collec_physique"]
    assert manga_possede.id_mangapossede == mock_cursor.fetchone.return_value["id_manga_physique"]
