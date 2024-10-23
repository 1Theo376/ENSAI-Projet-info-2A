import pytest
from business_object.manga import Manga


@pytest.fixture
def manga_instance():
    return Manga(
        id_manga=1,
        titre="One Piece",
        Synopsis="Un Manga sur les aventures de Monkey D. Luffy",
        auteurs="Eiichiro Oda",
        themes=["Aventures", "Action", "Fantasie"],
        genre="Shonen",
    )


@pytest.fixture
def test_str_method(manga_instance):
    expected_output = "One Piece (Shonen) - Un manga sur les aventures de Monkey D. Luffy. | Auteurs: Eiichiro Oda | Thèmes: Aventure, Action, Fantaisie"
    assert str(manga_instance) == expected_output
