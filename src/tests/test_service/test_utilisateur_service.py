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
    utilisateur = UtilisateurService().creer_compte(pseudo, mdp)
    #THEN
    assert utilisateur.pseudo == pseudo


def test_creer_compte_false(utilisateur_service):
    """Test de la création d'un compte utilisateur"""
    #GIVEN
    pseudo, mdp = "huy", "1234Azer"
    UtilisateurDao.creer = MagicMock(return_value=False)
    #WHEN
    utilisateur = UtilisateurService().creer_compte(pseudo, mdp)
    #THEN
    assert utilisateur is None


def test_pseudo_deja_utilise_oui():
    """Le pseudo est déjà utilisé dans liste_joueurs"""

    # GIVEN
    pseudo = "huy"

    # WHEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert res


def test_pseudo_deja_utilise_non():
    """Le pseudo n'est pas utilisé dans liste_joueurs"""

    # GIVEN
    pseudo = "chaton"

    # WHEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)
    res = UtilisateurService().pseudo_deja_utilise(pseudo)

    # THEN
    assert not res


def test_lister_tous_inclure_mdp_true():
    """Lister les Joueurs en incluant les mots de passe"""

    # GIVEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert joueur.mdp is not None


def test_lister_tous_inclure_mdp_false():
    """Lister les Joueurs en excluant les mots de passe"""

    # GIVEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = UtilisateurService().lister_tous()

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert not joueur.mdp


def test_se_connecter(utilisateur_service):
    """Test de la connexion d'un utilisateur"""

    #GIVEN
    


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
