from business_object import Avis
import pytest


@pytest.fixture
def test_avis_creation():
    id_avis = 1
    texte = "Excellent manga"
    avis = Avis(id_avis, texte)
    assert avis.id_avis == id_avis
    assert avis.texte == texte


@pytest.fixture
def test_avis_str():
    avis = Avis(1, "Un manga captivant")
    result = str(avis)
    assert result == "Avis 1: Un manga captivant"
