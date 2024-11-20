import pytest
from unittest.mock import MagicMock
from service.utilisateur_service import UtilisateurService
from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
from utils.securite import hash_password

liste_utilisateurs = [
    Utilisateur(pseudo="huy", mdp="1234Azer"),
    Utilisateur(pseudo="aze", mdp="0000Poiu"),
    Utilisateur(pseudo="vert", mdp="abcd1Ruy"),
]

def test_creer_compte_ok(utilisateur_service):
    """Test de la création d'un compte utilisateur"""
    #GIVEN
    pseudo, mdp = "huy", "1234Azer"
    UtilisateurDao.creer = MagicMock(return_value=True)
    #WHEN
    
    #THEN
    assert

def test_pseudo_deja_utilise(utilisateur_service):
    """Test de la méthode pseudo_deja_utilise"""
    # GIVEN
    pseudo, mdp = "huy", "1234Azer"
    #WHEN
    UtilisateurDao.lister_tous =


def test_se_connecter(utilisateur_service):
    """Test de la connexion d'un utilisateur"""
    # Préparer le mock pour la méthode se_connecter
    utilisateur_service.dao.se_connecter.return_value = Utilisateur(
        id=1, pseudo="testuser", mdp="hashedpassword"
    )

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
