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


def test_creer_compte_ok():
    """Test de la création d'un compte utilisateur"""
    # GIVEN
    pseudo, mdp = "buy", "1234Azer"
    UtilisateurDao.creer = MagicMock(return_value=True)
    # WHEN
    utilisateur = UtilisateurService().creer_compte(pseudo, mdp)
    # THEN
    assert utilisateur.pseudo == pseudo


def test_creer_compte_false():
    """Test de la création d'un compte utilisateur"""
    # GIVEN
    pseudo, mdp = "art", "1234Azer"
    UtilisateurDao.creer = MagicMock(return_value=False)
    # WHEN
    utilisateur = UtilisateurService().creer_compte(pseudo, mdp)
    # THEN
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


def test_se_connecter_oui():
    """Test de la connexion d'un utilisateur"""

    # GIVEN
    pseudo, mdp = "huy", "1234Azer"
    UtilisateurDao().se_connecter = MagicMock(return_value=True)
    # WHEN
    res = UtilisateurService().se_connecter(pseudo, mdp)
    # THEN
    assert res


def test_se_connecter_non():
    """Test de la connexion d'un utilisateur"""

    # GIVEN
    pseudo, mdp = "huy", "1234Azer"
    UtilisateurDao().se_connecter = MagicMock(return_value=False)
    # WHEN
    res = UtilisateurService().se_connecter(pseudo, mdp)
    # THEN
    assert not res


def test_supprimer_compte_oui():
    """Test de la suppression d'un compte utilisateur"""
    # GIVEN

    UtilisateurDao().supprimer = MagicMock(return_value=True)

    # WHEN
    res = UtilisateurService().supprimer_compte(Utilisateur(pseudo="huy", mdp="1234Azer"))

    # THEN
    assert res


def test_supprimer_compte_non():
    """Test de la suppression d'un compte utilisateur"""
    # GIVEN
    UtilisateurDao().supprimer = MagicMock(return_value=False)

    # WHEN
    res = UtilisateurService().supprimer_compte(Utilisateur(pseudo="aze", mdp="0000Poiu"))

    # THEN
    assert not res



if __name__ == "__main__":
    import pytest

    pytest.main([__file__])