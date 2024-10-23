from business_object.manga_possede import MangaPossede
from manga import Manga
import pytest

@pytest.fixture
def manga():
    return Manga(id_manga_p=1, manga=manga, num_dernier_acquis=3, statut="En cours")

