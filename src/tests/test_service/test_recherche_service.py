import pytest
from unittest.mock import patch, MagicMock
from business_object.utilisateur import Utilisateur
from business_object.CollectionCoherente import CollectionCoherente
from business_object.collection_phys import Collection_physique
from dao.utilisateur_dao import UtilisateurDao
from dao.manga_dao import MangaDao
from service.recherche_service import RechercheService


@pytest.fixture(scope="module", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"POSTGRES_SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        MangaDao().inserer_mangas("testmangas.json")
        yield


# Objets
liste_utilisateurs = [
    Utilisateur(pseudo="huz1y", mdp="1234Azer"),
    Utilisateur(pseudo="azez1", mdp="0000Poiu"),
    Utilisateur(pseudo="z1vert", mdp="abcd1Ruy"),
]

liste_collection_c = [CollectionCoherente(1, "Matcha", "vert")]
collection_p = Collection_physique(1, "Pelle", "bleue", [])


def test_recherche_manga_par_t_oui():
    """Test de recherche d'un manga par titre """
    # GIVEN
    titre = "monster"
    n, m, a = 0, 8, 0
    # WHEN
    longueur, sous_liste, longueur_tot = RechercheService().recherche_manga_par_t(titre, n, m, a)
    # THEN
    assert longueur == 1
    assert sous_liste == ["Monster"]
    assert longueur_tot == 1


def test_recherche_manga_par_t_non():
    """Test de recherche d'un manga par titre """
    # GIVEN
    titre = "rtrtt"
    n, m, a = 0, 8, 0
    # WHEN
    res = RechercheService().recherche_manga_par_t(titre, n, m, a)
    # THEN
    assert not res


def test_recherche_utilisateur_oui():
    """Test de recherche d'un utilisateur"""
    # GIVEN
    n, m, a = 0, 8, 0
    pseudo = "z1"
    UtilisateurDao().rechercher_tous_pseudo = MagicMock(return_value=liste_utilisateurs)

    # WHEN
    longueur, sous_liste, longueur_tot = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert longueur == 3
    assert sous_liste == ["huz1y", "azez1", "z1vert"]
    assert longueur_tot == 3


def test_recherche_utilisateur_non():
    """Test de recherche d'un utilisateur"""
    # GIVEN
    n, m, a = 0, 8, 0
    pseudo = "z1gg"
    UtilisateurDao().rechercher_tous_pseudo = MagicMock(return_value=None)

    # WHEN
    res = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert not res


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.trouver_collec_cohe_id_user', return_value=liste_collection_c)
def test_recherche_collec_cohe_par_id_oui(patch):
    """Test de recherche d'une collection cohérente par id d'utilisateur"""
    # GIVEN
    id = 1
    # WHEN
    res = RechercheService().recherche_collec_cohe_par_id(id)
    # THEN
    assert res == ["Matcha"]


@patch('dao.collection_coherente_dao.CollectionCoherenteDAO.trouver_collec_cohe_id_user', return_value=None)
def test_recherche_collec_cohe_par_id_non(patch):
    """Test de recherche d'une collection cohérente par id d'utilisateur"""
    # GIVEN
    id = 2
    # WHEN
    res = RechercheService().recherche_collec_cohe_par_id(id)
    # THEN
    assert not res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.trouver_collec_phys_id_user', return_value=collection_p)
def test_recherche_collec_phys_par_id_oui(patch):
    """Test de recherche d'une collection physique par id d'utilisateur"""
    # GIVEN
    id = 1
    # WHEN
    res = RechercheService().recherche_collec_phys_par_id(id)
    # THEN
    assert res


@patch('dao.collection_physique_dao.CollectionPhysiqueDAO.trouver_collec_phys_id_user', return_value=None)
def test_recherche_collec_phys_par_id_non(patch):
    """Test de recherche d'une collection physique par id d'utilisateur"""
    # GIVEN
    id = 1
    # WHEN
    res = RechercheService().recherche_collec_phys_par_id(id)
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
