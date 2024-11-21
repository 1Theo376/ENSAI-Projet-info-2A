import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from dao.utilisateur_dao import UtilisateurDao
from business_object.utilisateur import Utilisateur


liste_utilisateurs = [
    Utilisateur(pseudo="huy", mdp="1234Azer"),
    Utilisateur(pseudo="aze", mdp="0000Poiu"),
    Utilisateur(pseudo="vert", mdp="abcd1Ruy"),
]

@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    """
    with patch.dict("os.environ", {"SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        yield
    """


def test_creer_ok():
    """Création de Joueur réussie"""

    # GIVEN
    utilisateur = Utilisateur(pseudo="huy", mdp="HuYT7894")

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert creation_ok
    assert joueur.id_joueur


def test_creer_ko():
    """Création de Joueur échouée (age et mail incorrects)"""

    # GIVEN
    utilisateur = Utilisateur(pseudo="kio", mdp="AuYT7894")

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert not creation_ok
