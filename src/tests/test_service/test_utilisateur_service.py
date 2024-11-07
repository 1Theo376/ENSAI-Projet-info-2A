import pytest
from unittest.mock import MagicMock
from service.utilisateur_service import UtilisateurService
from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
from utils.securite import hash_password


@pytest.fixture
def utilisateur_service():
    """Fixture pour créer une instance du service UtilisateurService avec un mock du DAO"""
    service = UtilisateurService()
    service.dao = MagicMock()  # Remplacer l'instance DAO par un mock
    return service


@pytest.fixture
def utilisateur():
    """Fixture pour créer une instance d'Utilisateur"""
    return Utilisateur(id=1, pseudo="testuser", mdp="hashedpassword")


def test_pseudo_deja_utilise(utilisateur_service):
    """Test de la méthode pseudo_deja_utilise"""
    # Préparer le mock pour la méthode lister_tous
    utilisateur_service.dao.lister_tous.return_value = [Utilisateur(id=1, pseudo="testuser", mdp="hashedpassword")]

    # Tester le cas où le pseudo existe déjà
    result = utilisateur_service.pseudo_deja_utilise("testuser")
    assert result is True  # Le pseudo est déjà utilisé

    # Tester le cas où le pseudo n'existe pas
    result = utilisateur_service.pseudo_deja_utilise("newuser")
    assert result is False  # Le pseudo n'est pas encore utilisé


def test_creer_compte(utilisateur_service):
    """Test de la création d'un compte utilisateur"""
    # Préparer le mock pour la méthode creer
    utilisateur_service.dao.creer.return_value = True

    # Tester la création d'un utilisateur
    result = utilisateur_service.creer_compte("newuser", "password123")

    # Vérification
    assert result is not None  # L'utilisateur doit être créé
    utilisateur_service.dao.creer.assert_called_once()


def test_se_connecter(utilisateur_service):
    """Test de la connexion d'un utilisateur"""
    # Préparer le mock pour la méthode se_connecter
    utilisateur_service.dao.se_connecter.return_value = Utilisateur(id=1, pseudo="testuser", mdp="hashedpassword")

    # Tester la connexion avec des informations valides
    result = utilisateur_service.se_connecter("testuser", "password123")
    assert result is not None  # L'utilisateur doit être retourné
    utilisateur_service.dao.se_connecter.assert_called_once()


def test_se_connecter_invalide(utilisateur_service):
    """Test de la connexion d'un utilisateur avec un mot de passe incorrect"""
    # Préparer le mock pour la méthode se_connecter
    utilisateur_service.dao.se_connecter.return_value = None

    # Tester la connexion avec un mot de passe incorrect
    result = utilisateur_service.se_connecter("testuser", "wrongpassword")
    assert result is None  # Aucun utilisateur retourné pour des informations incorrectes


def test_supprimer_compte(utilisateur_service, utilisateur):
    """Test de la suppression d'un compte utilisateur"""
    # Préparer le mock pour la méthode supprimer
    utilisateur_service.dao.supprimer.return_value = True

    # Tester la suppression de l'utilisateur
    result = utilisateur_service.supprimer_compte(utilisateur)

    # Vérification
    assert result is True  # Le compte doit être supprimé
    utilisateur_service.dao.supprimer.assert_called_once()


def test_modifier_compte(utilisateur_service, utilisateur):
    """Test de la modification d'un compte utilisateur"""
    # Préparer le mock pour la méthode modifier
    utilisateur_service.dao.modifier.return_value = True

    # Tester la modification du compte
    utilisateur.mdp = "newpassword123"
    result = utilisateur_service.modifier_compte(utilisateur)

    # Vérification
    assert result is not None  # L'utilisateur doit être retourné après la modification
    utilisateur_service.dao.modifier.assert_called_once()
