import pytest
from business_object.collection_phys import Collection_physique
from business_object.manga_possede import MangaPossede
from business_object.manga import Manga


@pytest.fixture
def manga():
    return Manga(
        id_manga=1,
        titre="Naruto",
        synopsis="Un ninja qui rêve de devenir Hokage",
        auteurs=["Masashi Kishimoto"],
        themes=["Aventure"],
        genre="Shonen",
        volume=72,
    )


@pytest.fixture
def manga_possede(manga):
    return MangaPossede(id_manga_p=1, manga=manga, num_dernier_acquis=72, statut="Complet")


@pytest.fixture
def test_manga_possede_creation(manga_possede):
    assert manga_possede.id_manga_p == 1
    assert manga_possede.manga.titre == "Naruto"
    assert manga_possede.num_dernier_acquis == 72
    assert manga_possede.num_manquant == list(range(1, 72))
    assert manga_possede.statut == "Complet"
