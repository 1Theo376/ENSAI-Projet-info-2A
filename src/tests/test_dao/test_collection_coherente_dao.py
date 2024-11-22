import pytest
from unittest.mock import patch
from business_object.CollectionCoherente import CollectionCoherente
from business_object.utilisateur import Utilisateur
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.utilisateur_dao import UtilisateurDao
from dao.manga_dao import MangaDao


utilisateur = Utilisateur("huy1", "1234Azer")

collection = CollectionCoherente(1, "manouvellecolec", "action", [])


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


def test_creer_collection_oui():
    """Création d'une collection cohérente dans la base de données"""
    # GIVEN
    id_utilisateur = 1
    # WHEN
    res = CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # THEN
    assert res


def test_creer_collection_non():
    """Création d'une collection cohérente dans la base de données"""
    # GIVEN
    id_utilisateur = 999
    # WHEN
    res = CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # THEN
    assert not res


def test_supprimer_collection_oui():
    """Suppression d'une collection cohérente dans la base de données"""

    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().supprimer_collection(collection)
    # THEN
    assert res


def test_trouver_collec_cohe_id_user_oui():
    """Trouve une collection cohérente dans la base de données
       selon l'identifiant de l'utilisateur"""
    # GIVEN

    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().trouver_collec_cohe_id_user(id_utilisateur)
    # THEN
    assert res


def test_trouver_collec_cohe_id_user_non():
    """Trouve une collection cohérente dans la base de données
       selon l'identifiant de l'utilisateur"""
    # GIVEN
    id_utilisateur = 1
    # WHEN
    res = CollectionCoherenteDAO().trouver_collec_cohe_id_user(id_utilisateur)
    # THEN
    assert not res


def test_trouver_collec_cohe_nom_oui():
    """Trouve une collection cohérente dans la base de données
       selon l'identifiant de l'utilisateur et le titre de la collection"""
    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().trouver_collec_cohe_nom("manouvellecolec",
                                                           id_utilisateur)
    # THEN
    assert res


def test_trouver_collec_cohe_nom_non():
    """Trouve une collection cohérente dans la base de données
       selon l'identifiant de l'utilisateur et le titre de la collection"""
    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().trouver_collec_cohe_nom("manouvelle",
                                                           id_utilisateur)
    # THEN
    assert not res


def test_modifier_titre_oui():
    """Modifie le titre d'une collection cohérente la base de données"""
    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().modifier_titre(1, "nouveautitre")
    # THEN
    assert res


def test_modifier_titre_non():
    """Modifie le titre d'une collection cohérente la base de données"""
    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().modifier_titre(34, "nouveautitre")
    # THEN
    assert not res


def test_modifier_desc_oui():
    """Modifie la description d'une collection cohérente la base de données"""
    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().modifier_desc(1, "nouvelle_desc")
    # THEN
    assert res


def test_modifier_desc_non():
    """Modifie la description d'une collection cohérente la base de données"""
    # GIVEN
    id_utilisateur = 1
    CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
    # WHEN
    res = CollectionCoherenteDAO().modifier_desc(34, "nouvelle_desc")
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
