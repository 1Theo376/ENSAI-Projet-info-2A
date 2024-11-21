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
    with patch.dict("os.environ", {"SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        yield


def test_lister_tous_inclure_mdp_true():
    """Lister les Joueurs en incluant les mots de passe"""

    # GIVEN
    UtilisateurDao().lister_tous = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    res = JoueurService().lister_tous(inclure_mdp=True)

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert joueur.mdp is not None


def test_lister_tous_inclure_mdp_false():
    """Lister les Joueurs en excluant les mots de passe"""

    # GIVEN
    JoueurDao().lister_tous = MagicMock(return_value=liste_joueurs)

    # WHEN
    res = JoueurService().lister_tous()

    # THEN
    assert len(res) == 3
    for joueur in res:
        assert not joueur.mdp