import pytest
from unittest.mock import MagicMock
from unittest.mock import patch
from dao.utilisateur_dao import UtilisateurDao
from business_object.utilisateur import Utilisateur
from utils.securite import hash_password
from dao.manga_dao import MangaDao

liste_utilisateurs = [
    Utilisateur(pseudo="huy", mdp="1234Azer"),
    Utilisateur(pseudo="aze", mdp="0000Poiu"),
    Utilisateur(pseudo="vert", mdp="abcd1Ruy"),
]

@pytest.fixture(scope="function", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"POSTGRES_SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        MangaDao().inserer_mangas("testmangas.json")
        yield


@pytest.fixture(scope="function", autouse=True)
def utilisateur_test():
    """Crée un joueur pour les tests"""
    for user in liste_utilisateurs:
        UtilisateurDao().creer(user)

    return liste_utilisateurs


def test_creer_ok():
    """Création de Utilisateur réussie"""

    # GIVEN
    utilisateur = Utilisateur(pseudo="hy", mdp="HuYT7894")

    # WHEN
    creation_ok = UtilisateurDao().creer(utilisateur)

    # THEN
    assert creation_ok
    assert utilisateur.id


def test_creer_ko():
    """Création de Utilisateur échouée (pseudo incorrect)"""

    # GIVEN
    utilisateur = Utilisateur(pseudo=12, mdp="u")

    # WHEN
    utilisateur = UtilisateurDao().creer(utilisateur)
    # THEN
    assert not utilisateur


def test_lister_tous(utilisateur_test):
    #GIVEN

    # WHEN
    utilisateurs = UtilisateurDao().lister_tous()
    # THEN
    assert isinstance(utilisateurs, list)
    for u in utilisateurs:
        assert isinstance(u, Utilisateur)
    assert len(utilisateurs) >= 3


def test_se_connecter_oui(utilisateur_test):
    # GIVEN
    pseudo = "huy"
    mdp = "1234Azer"
    # WHEN
    utilisateur = UtilisateurDao().se_connecter(pseudo, mdp)
    # THEN
    assert isinstance(utilisateur, Utilisateur)


def test_se_connecter_non(utilisateur_test):
    # GIVEN
    pseudo = "queeny"
    mdp = "1234Azer"
    # WHEN
    utilisateur = UtilisateurDao().se_connecter(pseudo, mdp)
    # THEN
    assert not utilisateur


def test_rechercher_tous_pseudo(utilisateur_test):
    # GIVEN
    recherche_pseudo = "e"
    # WHEN
    utilisateurs = UtilisateurDao().rechercher_tous_pseudo(recherche_pseudo)
    # THEN
    assert len(utilisateurs) == 2


def test_recherche_id_par_pseudo(utilisateur_test):
    # GIVEN
    id_utilisateur = liste_utilisateurs[0].id
    pseudo_utilisateur = liste_utilisateurs[0].pseudo
    # WHEN
    id = UtilisateurDao().recherche_id_par_pseudo(pseudo_utilisateur)
    # THEN
    assert id_utilisateur == id


def test_recherche_pseudo_par_id(utilisateur_test):
    # GIVEN
    id_utilisateur = liste_utilisateurs[0].id
    pseudo_utilisateur = liste_utilisateurs[0].pseudo
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo






if __name__ == "__main__":
    pytest.main([__file__])
