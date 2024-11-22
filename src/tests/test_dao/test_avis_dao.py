import pytest
from unittest.mock import patch
from business_object.avis import Avis
from business_object.manga import Manga
from business_object.utilisateur import Utilisateur
from dao.utilisateur_dao import UtilisateurDao
from dao.avis_dao import AvisDAO
from dao.manga_dao import MangaDao


# Objets
avis = Avis(id_avis=1, texte="j'adore ce livre")
manga = Manga(id_manga=1, titre="Naruto", synopsis="synopsis", auteur="auteur",
              themes="thèmes", genre="genre")
utilisateur = Utilisateur(id=1, pseudo="huz1y", mdp="1234Azer")


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
    """Crée un utilisateur pour les tests"""
    return UtilisateurDao().creer(utilisateur)


def test_creer_avis_oui():
    """Création d'un avis dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    # WHEN
    res = AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # THEN
    assert res


def test_creer_avis_non():
    """Création d'un avis dans la base de données"""
    # GIVEN
    id_utilisateur = 9999
    id_manga = 1
    # WHEN
    res = AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # THEN
    assert not res


def test_supprimer_avis_oui():
    """Suppression d'un avis dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res = AvisDAO().supprimer_avis(avis)
    # THEN
    assert res


def test_recuperer_avis_utilisateur_oui():
    """Récupération des avis d'un utilisateur dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res = AvisDAO().recuperer_avis_utilisateur(id_utilisateur)
    # THEN
    assert res


def test_recuperer_avis_utilisateur_non():
    """Récupération des avis d'un utilisateur dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res1, res2 = AvisDAO().recuperer_avis_utilisateur(33)
    # THEN
    assert not res1
    assert not res2


def test_recuperer_avis_manga_oui():
    """Récupération des avis d'un manga dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res = AvisDAO().recuperer_avis_manga(id_manga)
    # THEN
    assert res


def test_recuperer_avis_manga_non():
    """Récupération des avis d'un manga dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res1, res2 = AvisDAO().recuperer_avis_manga(33)
    # THEN
    assert not res1
    assert not res2


def test_AvisUtilisateurMangaExistant_oui():
    """Vérifie si l'utilisateur a déjà rédigé un avis sur ce manga"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res = AvisDAO().AvisUtilisateurMangaExistant(id_utilisateur, id_manga)
    # THEN
    assert res


def test_AvisUtilisateurMangaExistant_non():
    """Vérifie si l'utilisateur a déjà rédigé un avis sur ce manga
    dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    # WHEN
    res = AvisDAO().AvisUtilisateurMangaExistant(id_utilisateur, id_manga)
    # THEN
    assert not res


def test_recuperer_avis_user_et_manga_oui():
    """Récupère l'avis de l' utilisateur sur ce manga dans la base
    de données"""
    # GIVEN
    id_utilisateur = 1
    id_manga = 1
    AvisDAO().creer_avis(avis, id_utilisateur, id_manga)
    # WHEN
    res = AvisDAO().recuperer_avis_user_et_manga(id_manga, id_utilisateur)
    # THEN
    assert res


if __name__ == "__main__":
    pytest.main([__file__])
