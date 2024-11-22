import pytest
from unittest.mock import patch, MagicMock
from business_object.collection_phys import Collection_physique
from business_object.manga_possede import MangaPossede
from business_object.manga import Manga
from business_object.utilisateur import Utilisateur
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.utilisateur_dao import UtilisateurDao


utilisateur = Utilisateur("huy1", "1234Azer")

liste_collection = [
    Collection_physique("macollec1", "action", []),
    Collection_physique("macollec2", "action", []),
    Collection_physique("macollec3", "action", [])
]

collection = Collection_physique("manouvellecolec", "action", [])


@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"POSTGRES_SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        yield


@pytest.fixture(scope="session", autouse=True)
def utilisateur_test():
    """Crée un utilisateur pour les tests"""
    return UtilisateurDao().creer(utilisateur)


@pytest.fixture(scope="session", autouse=True)
def collection_test():
    """Crée des collections pour les tests"""
    id_utilisateur = 1
    for collec in liste_collection:
        CollectionPhysiqueDAO().creer_collectionphys(collec, id_utilisateur)
    return liste_collection


def test_creer_collectionphys_oui():
    """Création d'une collection physique dans la base de données"""

    # GIVEN
    id_utilisateur = 1
    # WHEN
    res = CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # THEN
    assert res


def test_creer_collectionphys_non():
    """Création d'une collection physique dans la base de données"""

    # GIVEN
    id_utilisateur = 30
    # WHEN
    res = CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # THEN
    assert not res


def test_supprimer_collectionphys_oui():
    """Suppression d'une collection physique dans la base de données"""

    # GIVEN
    collection2 = Collection_physique("manouvellecolec2", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection2, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().supprimer_collectionphys(1)
    # THEN
    assert res


def test_supprimer_collectionphys_non():
    """Suppression d'une collection physique dans la base de données"""

    # GIVEN
    collection3 = Collection_physique("manouvellecolec3", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection3, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().supprimer_collectionphys(9999)
    # THEN
    assert not res


def test_supprimer_mangaposs_oui():
    """Suppression d'un manga possédé dans la base de données"""

    # GIVEN
    collection3 = Collection_physique("manouvellecolec3", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection3, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().supprimer_mangaposs(9999)
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
