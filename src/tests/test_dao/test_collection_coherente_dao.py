import pytest
from unittest.mock import patch
from dao.collection_coherente_dao import CollectionCoherenteDAO
from business_object.collection_coherente import CollectionCoherente
from business_object.manga import Manga


@pytest.fixture
def collection_dao():
    return CollectionCoherenteDAO()


@pytest.fixture
def collection_coherente():
    return CollectionCoherente(
        id_collectioncoherente=1,
        titre_collection="Ma Collection",
        desc_collection="Une collection d'anime populaire",
        Liste_manga=[]
    )


@pytest.fixture
def manga():
    return Manga(
        id_manga=1,
        titre="Naruto",
        synopsis="Un jeune ninja qui cherche à devenir Hokage.",
        auteur="Masashi Kishimoto",
        themes=["Aventure", "Action"],
        genre="Shonen"
    )


@patch("dao.db_connection.DBConnection")
def test_creer_collection(mock_db, collection_dao, collection_coherente):
    mock_connection = mock_db.return_value.connection
    mock_cursor = mock_connection.cursor.return_value
    mock_cursor.fetchone.return_value = {"id_collec_coherente": 1}

    created = collection_dao.creer_collection(collection_coherente)

    assert created
    assert collection_coherente.id_collectioncoherente == 1
    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchone.assert_called_once()


@patch("dao.db_connection.DBConnection")
def test_supprimer_collection(mock_db, collection_dao, collection_coherente):
    mock_connection = mock_db.return_value.connection
    mock_cursor = mock_connection.cursor.return_value
    mock_cursor.rowcount = 1

    result = collection_dao.supprimer_collection(collection_coherente)

    assert result is True
    mock_cursor.execute.assert_called_once()


@patch("dao.db_connection.DBConnection")
def test_ajouter_manga(mock_db, collection_dao, collection_coherente, manga):
    mock_connection = mock_db.return_value.connection
    mock_cursor = mock_connection.cursor.return_value
    mock_cursor.fetchone.return_value = {"id_collec_coherente": collection_coherente.id_collectioncoherente, "id_manga": manga.id_manga}
    created = collection_dao.ajouter_manga(collection_coherente, manga)

    assert created
    assert manga.id_manga == 1
    mock_cursor.execute.assert_called_once()
    mock_cursor.fetchone.assert_called_once()


@patch("dao.db_connection.DBConnection")
def test_supprimer_manga(mock_db, collection_dao, collection_coherente, manga):
    mock_connection = mock_db.return_value.connection
    mock_cursor = mock_connection.cursor.return_value
    mock_cursor.rowcount = 1

    result = collection_dao.supprimer_manga(collection_coherente, manga)

    assert result is True
    mock_cursor.execute.assert_called_once()
