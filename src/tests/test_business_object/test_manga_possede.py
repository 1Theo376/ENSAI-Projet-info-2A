from business_object.manga_possede import MangaPossede
from manga import Manga
import pytest


@pytest.fixture
def manga():
    return Manga(id_manga_p=1, manga=manga, num_dernier_acquis=3, statut="En cours")


@pytest.fixture
def mnga_possede():
    return MangaPossede(id_manga_p=1, manga=manga, num_dernier_acquis=3, statut="En cours")


@pytest.fixture
def manga_test_str(manga_possede):
    result = str(manga_possede)
    assert result == (
        "MangaPossede(id_manga_p=1, "
        "manga=Naruto, "
        "num_dernier_acquis=3, "
        "num_manquant=[1, 2, 3, 4, 5], "
        "statut='En cours')"
    )
