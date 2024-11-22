import pytest
from unittest.mock import MagicMock
from dao.utilisateur_dao import UtilisateurDao
from dao.collection_coherente_dao import CollectionCoherenteDAO
from service.collection_coherente_service import CollectionCoherenteService
from service.utilisateur_service import UtilisateurService
from service.recherche_service import RechercheService


def test_creer_collection_oui():
    """Test de création d'une collection cohérente"""
    # GIVEN
    titre, description, idu = "pomme", "rouge", 5
    CollectionCoherenteDAO().creer_collection = MagicMock(return_value=True)

    # WHEN
    collection = CollectionCoherenteService().creer_collectioncohe(titre_collection=titre, desc_collection=description, idu=idu)
    # THEN
    assert collection.titre_collection == titre


def test_creer_collection_non():
    """Test de création d'une collection cohérente"""
    # GIVEN
    UtilisateurDao().creer = MagicMock(return_value=True)
    CollectionCoherenteDAO().creer_collection = MagicMock(return_value=False)

    UtilisateurService().creer_compte("manz1", "1234Azer")
    id = UtilisateurDao().recherche_id_par_pseudo("manz1")

    # WHEN
    res = CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", id)
    # THEN
    assert not res


def test_supprimer_collectioncohe_oui():
    """Test de suppression d'une collection physique"""
    # GIVEN
    CollectionCoherenteDAO().supprimer_collection = MagicMock(return_value=True)
    CollectionCoherenteDAO().creer_collection = MagicMock(return_value=True)

    id = UtilisateurDao().recherche_id_par_pseudo("manz1")
    CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", id)
    nom_collection = RechercheService().recherche_collec_cohe_par_id(id)
    collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(nom_collection[0], id)
    # WHEN
    res = CollectionCoherenteService().supprimer_collectioncohe(collection)
    # THEN
    assert res


def test_ajouter_mangaposs_oui():
    """Test d'ajout d'un manga possédé dans une collection cohérente"""
    # GIVEN
    CollectionCoherenteDAO().supprimer_collection = MagicMock(return_value=True)
    CollectionCoherenteDAO().creer_collection = MagicMock(return_value=True)
    CollectionCoherenteDAO().ajouter_manga = MagicMock(return_value=True)
    CollectionCoherenteDAO().supprimer_collection = MagicMock(return_value=True)

    id = UtilisateurDao().recherche_id_par_pseudo("manz1")
    CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", id)
    nom_collection = RechercheService().recherche_collec_cohe_par_id(id)
    collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(nom_collection[0], id)
    id_manga = 1

    # WHEN
    res = CollectionCoherenteService().ajouter_manga(collection.id_collectioncoherente, id_manga)

    # THEN
    assert res, f"nom : {nom_collection[0]}, {collection}"


def test_ajouter_mangaposs_non():
    """Test d'ajout d'un manga possédé dans une collection cohérente"""
    # GIVEN
    CollectionCoherenteDAO().supprimer_collection = MagicMock(return_value=True)
    CollectionCoherenteDAO().creer_collection = MagicMock(return_value=True)
    CollectionCoherenteDAO().ajouter_manga = MagicMock(return_value=True)

    id = UtilisateurDao().recherche_id_par_pseudo("manz1")
    CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", id)
    nom_collection = RechercheService().recherche_collec_cohe_par_id(id)
    collection = CollectionCoherenteDAO().trouver_collec_cohe_nom(nom_collection[0], id)
    id_manga = 9999999999999

    # WHEN
    res = CollectionCoherenteService().ajouter_manga(collection.id_collectioncoherente, id_manga)

    # THEN
    assert not res


def test_creer_collection2_non():
    """Test de création d'une collection cohérente sans création réelle dans la base"""
    # GIVEN
    UtilisateurDao().creer = MagicMock(return_value=True)
    CollectionCoherenteDAO().recherche_id_par_pseudo = MagicMock(return_value=123)
    CollectionCoherenteDAO().creer_collection = MagicMock(return_value=False)

    # Utilisation des services mockés
    UtilisateurService().creer_compte("manz1", "1234Azer")
    id_utilisateur = CollectionCoherenteService().recherche_id_par_pseudo("manz1")

    # WHEN
    res = CollectionCoherenteService().creer_collectioncohe("pomme", "rouge", id_utilisateur)

    # THEN
    assert not res, f"Résultat attendu : False, mais obtenu : {res}"


if __name__ == "__main__":
    pytest.main([__file__])
