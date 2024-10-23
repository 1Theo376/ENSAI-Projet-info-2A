import pytest 
from business_object.CollectionCoherente import CollectionCoherente
from business_object.manga import Manga


@pytest.fixture
def mangas():
    return [Manga(id_manga=1, titre="Naruto", synopsis="ninja ", auteurs=["Masashi Kishimoto"], themes=["Aventure"], genre="Shonen"),
        Manga(id_manga=2, titre="One Piece", synopsis="pirate", auteurs=["Eiichiro Oda"], themes=["Aventure"], genre="Shonen"),
        Manga(id_manga=3, titre="Bleach", synopsis="jeune homme", auteurs=["Tite Kubo"], themes=["Fantastique"], genre="Shonen")]

@pytest.fixture
def colection_coherente():
    return CollectionCoherente(id_collection_physique=1,
        titre_collection="Collection Shonen",
        description_collection="Une collection des meilleurs mangas Shonen",
        liste_manga=mangas)
