import pytest
from unittest.mock import patch
from business_object.utilisateur import Utilisateur
from business_object.avis import Avis
from business_object.manga import Manga
from dao.manga_dao import MangaDao
from service.avis_service import AvisService


@pytest.fixture(scope="module", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"POSTGRES_SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        MangaDao().inserer_mangas("testmangas.json")
        yield


# Objets
avis = Avis(id_avis=1, texte="j'adore ce livre")
manga = Manga(id_manga=1, titre="Naruto", synopsis="synopsis", auteur="auteur",
              themes="thèmes", genre="genre")
utilisateur = Utilisateur(id=1, pseudo="huz1y", mdp="1234Azer")

@patch('dao.avis_dao.AvisDAO.creer_avis', return_value=True)
def test_rediger_avis_oui(patch):
    """Test de création d'un avis"""
    # GIVEN

    # WHEN
    res = AvisService().rediger_avis("ce livre est super", 1, 1, 1)
    # THEN
    assert res


@patch('dao.avis_dao.AvisDAO.creer_avis', return_value=False)
def test_rediger_avis_non(patch):
    """Test de création d'un avis"""
    # GIVEN

    # WHEN
    res = AvisService().rediger_avis("ce livre est super", 1, 1, 1)
    # THEN
    assert not res


@patch('dao.avis_dao.AvisDAO.supprimer_avis', return_value=True)
def test_supprimer_avis_oui(patch):
    """Test de suppression d'un avis"""
    # GIVEN

    # WHEN
    res = AvisService().supprimer_avis(avis)
    # THEN
    assert res


@patch('dao.avis_dao.AvisDAO.supprimer_avis', return_value=False)
def test_supprimer_avis_non(patch):
    """Test de suppression d'un avis"""
    # GIVEN

    # WHEN
    res = AvisService().supprimer_avis(avis)
    # THEN
    assert not res


@patch('dao.avis_dao.AvisDAO.recuperer_avis_utilisateur',
       return_value=([avis], [manga.id_manga]))
def test_recuperer_avis_utilisateur_oui(patch):
    """Test de récupération de l'avis d'un utilisateur"""
    # GIVEN
    id_utilisateur = 1
    # WHEN
    res = AvisService().recuperer_avis_utilisateur(id_utilisateur)
    # THEN
    assert res


@patch('dao.avis_dao.AvisDAO.recuperer_avis_utilisateur',
       return_value=([], []))
def test_recuperer_avis_utilisateur_non(patch):
    """Test de récupération de l'avis d'un utilisateur"""
    # GIVEN
    id_utilisateur = 1
    # WHEN
    res = AvisService().recuperer_avis_utilisateur(id_utilisateur)
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
