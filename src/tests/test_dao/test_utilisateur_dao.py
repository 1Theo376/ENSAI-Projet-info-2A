import pytest
from unittest.mock import patch
from dao.utilisateur_dao import UtilisateurDao
from business_object.utilisateur import Utilisateur


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        yield


@pytest.fixture
def utilisateur_dao():
    return UtilisateurDao()


@pytest.fixture
def utilisateur_test():
    return Utilisateur(id=None, pseudo="TestUser", mdp="password123")


def test_creer(utilisateur_dao, utilisateur_test):
    """Test de la création d'un utilisateur"""
    assert utilisateur_dao.creer(utilisateur_test) == True
    assert utilisateur_test.id is not None


def test_modifier(utilisateur_dao, utilisateur_test):
    """Test de la modification d'un utilisateur existant"""
    utilisateur_test.pseudo = "UpdatedUser"
    assert utilisateur_dao.modifier(utilisateur_test) == True


def test_se_connecter(utilisateur_dao, utilisateur_test):
    """Test de la connexion d'un utilisateur"""
    user = utilisateur_dao.se_connecter(utilisateur_test.pseudo, utilisateur_test.mdp)
    assert user is not None
    assert user.pseudo == utilisateur_test.pseudo


def test_lister_tous(utilisateur_dao):
    """Test de la récupération de tous les utilisateurs"""
    utilisateurs = utilisateur_dao.lister_tous()
    assert isinstance(utilisateurs, list)
    assert len(utilisateurs) > 0


def test_supprimer(utilisateur_dao, utilisateur_test):
    """Test de la suppression d'un utilisateur"""
    assert utilisateur_dao.supprimer(utilisateur_test) == True


def test_supprimer_tous(utilisateur_dao):
    """Test de la suppression de tous les utilisateurs"""
    assert utilisateur_dao.supprimer_tous() == True
    assert len(utilisateur_dao.lister_tous()) == 0
