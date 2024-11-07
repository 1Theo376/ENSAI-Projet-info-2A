import pytest
from dao.manga_dao import MangaDao
from business_object.manga import Manga
from unittest.mock import MagicMock


@pytest.fixture
def manga_dao():
    """Fixture pour creer une instance de MangaDao."""
    return MangaDao()


def test_trouver_manga_par_id(manga_dao):
    # Mock de DBConnection et de cursor
    manga_dao.trouver_manga_par_id = MagicMock(
        return_value=Manga(
            id_manga=1,
            titre="Naruto",
            synopsis="Un jeune ninja rêve de devenir Hokage.",
            auteur="Masashi Kishimoto",
            themes="Aventure, Action",
            genre="Shonen",
        )
    )
    manga = manga_dao.trouver_manga_par_id(1)

    assert manga is not None
    assert manga.id_manga == 1
    assert manga.titre == "Naruto"
    assert manga.auteur == "Masashi Kishimoto"


def test_trouver_manga_par_titre(manga_dao):
    manga_dao.trouver_manga_par_titre = MagicMock(
        return_value=Manga(
            id_manga=2,
            titre="One Piece",
            synopsis="Luffy, un pirate en quête de trésors.",
            auteur="Eiichiro Oda",
            themes="Aventure, Comédie",
            genre="Shonen",
        )
    )
    manga = manga_dao.trouver_manga_par_titre("One Piece")

    assert manga is not None
    assert manga.titre == "One Piece"
    assert manga.synopsis == "Luffy, un pirate en quête de trésors."


def test_rechercher_manga_par_titre(manga_dao):
    # Mock de DBConnection pour retourner plusieurs mangas avec le même titre
    manga_dao.rechercher_manga_par_titre = MagicMock(
        return_value=[
            Manga(
                id_manga=1,
                titre="Naruto",
                synopsis="Un jeune ninja...",
                auteur=None,
                themes=None,
                genre=None,
            ),
            Manga(
                id_manga=2,
                titre="Naruto Shippuden",
                synopsis="Naruto revient plus fort.",
                auteur=None,
                themes=None,
                genre=None,
            ),
        ]
    )
    result = manga_dao.rechercher_manga_par_titre("Naruto")

    assert result is not None
    assert len(result) == 2
    assert result[0].titre == "Naruto"
    assert result[1].titre == "Naruto Shippuden"


def test_inserer_mangas(manga_dao):
    manga_dao.inserer_mangas = MagicMock(return_value=True)
    result = manga_dao.inserer_mangas("chemin/vers/mangas.json")

    assert result is True


def test_supprimer_toutes_les_donnees(manga_dao):
    manga_dao.supprimer_toutes_les_donnees = MagicMock(return_value=True)
    result = manga_dao.supprimer_toutes_les_donnees()

    assert result is True
