import pytest
from dao.manga_dao import MangaDao
from unittest.mock import MagicMock
from unittest.mock import patch


@pytest.fixture(scope="function", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"POSTGRES_SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        MangaDao().inserer_mangas("testmangas.json")
        yield


def test_trouver_manga_par_id_oui():
    """Création de Utilisateur réussie"""

    # GIVEN
    manga_dao = MangaDao()

    # WHEN
    manga = manga_dao.trouver_manga_par_id(1)

    # THEN
    assert manga.id_manga == 1


def test_trouver_manga_par_id_non():
    """Création de Utilisateur réussie"""

    # GIVEN
    manga_dao = MangaDao()

    # WHEN
    manga = manga_dao.trouver_manga_par_id(-1)

    # THEN
    assert manga is None


def test_trouver_manga_par_titre_oui():
    """Création de Utilisateur réussie"""

    # GIVEN
    manga_dao = MangaDao()

    # WHEN
    manga = manga_dao.trouver_manga_par_titre("Naruto")

    # THEN
    assert manga.titre == "Naruto"


def test_trouver_manga_par_titre_non():
    """Création de Utilisateur réussie"""

    # GIVEN
    manga_dao = MangaDao()

    # WHEN
    manga = manga_dao.trouver_manga_par_titre("zghefdthete")

    # THEN
    assert manga is None


def test_rechercher_manga_par_titre_oui():
    """Création de Utilisateur réussie"""

    # GIVEN
    manga_dao = MangaDao()

    # WHEN
    mangas = manga_dao.rechercher_manga_par_titre("Monster")

    # THEN
    assert len(mangas) == 1


def test_rechercher_manga_par_titre_non():
    """Création de Utilisateur réussie"""

    # GIVEN
    manga_dao = MangaDao()

    # WHEN
    mangas = manga_dao.rechercher_manga_par_titre("guyrazfgbyuy")

    # THEN
    assert mangas is None


if __name__ == "__main__":
    pytest.main([__file__])