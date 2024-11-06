import pytest
from dao.manga_possede_dao import MangaPossedeDao
from business_object.manga_possede import MangaPossede
from business_object.manga import Manga
from unittest.mock import patch, MagicMock


@pytest.fixture
def mock_manga():
    return Manga(id_manga=1, titre="Naruto", synopsis="Ninja adventure", auteur="Masashi Kishimoto",
                 themes=["Aventure", "Action"], genre="Shonen")


@pytest.fixture
def mock_manga_possede(mock_manga):
    return MangaPossede(id_manga_p=1, manga=mock_manga, num_dernier_acquis=10, statut="en cours")


@pytest.fixture
def manga_possede_dao():
    return MangaPossedeDao()


@patch("dao.db_connection.DBConnection")
def test_ajouter_manga_p(mock_db, manga_possede_dao, mock_manga_possede):
    mock_db_instance = mock_db.return_value
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.fetchone.return_value = {"id_manga_p": 1}
    mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
    mock_db_instance.connection.__enter__.return_value = mock_connection

    result = manga_possede_dao.ajouter_manga_p(mock_manga_possede)

    mock_cursor.execute.assert_called_once_with(
        "INSERT INTO manga_possede (id_manga_p, id_manga, num_dernier_acquis, num_manquant) VALUES"
        "(%(id_manga_p)s, %(id_manga)s, %(num_dernier_acquis)s, %(num_manquant)s) "
        "  RETURNING id_manga_p; ",
        {
            "id_manga": mock_manga_possede.manga.id_manga,
            "id_manga_p": mock_manga_possede.id_manga_p,
            "num_dernier_acquis": mock_manga_possede.num_dernier_acquis,
            "num_manquant": mock_manga_possede.num_manquant,
        },
    )
    assert result is True


@patch("dao.db_connection.DBConnection")
def test_modifier_num_dernier_acquis(mock_db, manga_possede_dao, mock_manga_possede):
    mock_db_instance = mock_db.return_value
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_cursor.rowcount = 1
    mock_connection.cursor.return_value.__enter__.return_value = mock_cursor
    mock_db_instance.connection.__enter__.return_value = mock_connection

    utilisateur = MagicMock()
    utilisateur.pseudo = "user123"
    utilisateur.mdp = "password"
    utilisateur.id = 1

    result = manga_possede_dao.modifier_num_dernier_acquis(utilisateur)

    mock_cursor.execute.assert_called_once_with(
        "UPDATE utilisateur SET pseudo = %(pseudo)s, mdp = %(mdp)s WHERE id = %(id)s;",
        {
            "pseudo": utilisateur.pseudo,
            "mdp": utilisateur.mdp,
            "id": utilisateur.id,
        },
    )
    assert result is True
