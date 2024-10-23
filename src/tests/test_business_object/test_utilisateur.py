from business_object.utilisateur import Utilisateur
import pytest


@pytest.fixture
def utilisateur():
    return Utilisateur(1, "mdp1", "pseudo1")
