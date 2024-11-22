import pytest
from unittest.mock import patch, MagicMock
from business_object.CollectionCoherente import CollectionCoherente
from business_object.manga import Manga
from business_object.utilisateur import Utilisateur
from dao.collection_coherente_dao import CollectionCoherenteDAO
from dao.utilisateur_dao import UtilisateurDao
from dao.manga_dao import MangaDao


utilisateur = Utilisateur("huy1", "1234Azer")

liste_collection = [
    CollectionCoherente("macollec1", "action", []),
    CollectionCoherente("macollec2", "action", []),
    CollectionCoherente("macollec3", "action", [])
]

collection = CollectionCoherente("manouvellecolec", "action", [])


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


@pytest.fixture(scope="function", autouse=True)
def collection_test():
    """Crée des collections pour les tests"""
    id_utilisateur = 1
    for collec in liste_collection:
        CollectionCoherenteDAO().creer_collection(collec, id_utilisateur)
    return liste_collection


def test_creer_collectionphys_oui():
    """Création d'une collection physique dans la base de données"""

    # GIVEN
    id_utilisateur = 1
    # WHEN
    res = CollectionCoherenteDAO().creer_collection(collection, id_utilisateur)
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
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().supprimer_collectionphys(1)
    # THEN
    assert res


def test_supprimer_collectionphys_non():
    """Suppression d'une collection physique dans la base de données"""

    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().supprimer_collectionphys(9999)
    # THEN
    assert not res


def test_trouver_collec_phys_id_user_oui():
    """Trouve une collection physique dans la base de données
       selon l'identifiant de l'utilisateur"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().trouver_collec_phys_id_user(id_utilisateur)
    # THEN
    assert res


def test_trouver_collec_phys_id_user_non():
    """Trouve une collection physique dans la base de données
       selon l'identifiant de l'utilisateur"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 3
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().trouver_collec_phys_id_user(id_utilisateur)
    # THEN
    assert not res


def test_trouver_collec_phys_nom_oui():
    """Trouve une collection physique dans la base de données
       selon son titre"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().trouver_collec_phys_nom("manouvellecolec")
    # THEN
    assert res


def test_trouver_collec_phys_nom_non():
    """Trouve une collection physique dans la base de données
       selon son titre"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().trouver_collec_phys_nom("manouvelle")
    # THEN
    assert not res


def test_modifier_titre_oui():
    """Modifie le titre d'une collection physique la base de données"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().modifier_titre(1, "nouveautitre")
    # THEN
    assert res


def test_modifier_titre_non():
    """Modifie le titre d'une collection physique la base de données"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().modifier_titre(34, "nouveautitre")
    # THEN
    assert not res


def test_modifier_desc_oui():
    """Modifie la description d'une collection physique la base de données"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().modifier_desc(1, "nouvelle_desc")
    # THEN
    assert res


def test_modifier_desc_non():
    """Modifie la description d'une collection physique la base de données"""
    # GIVEN
    collection = Collection_physique("manouvellecolec", "action", [])
    id_utilisateur = 1
    CollectionPhysiqueDAO().creer_collectionphys(collection, id_utilisateur)
    # WHEN
    res = CollectionPhysiqueDAO().modifier_desc(34, "nouvelle_desc")
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
