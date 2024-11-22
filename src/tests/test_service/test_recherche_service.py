import pytest
from unittest.mock import MagicMock
from business_object.utilisateur import Utilisateur
from business_object.CollectionCoherente import CollectionCoherente
from dao.utilisateur_dao import UtilisateurDao
from service.recherche_service import RechercheService
from service.utilisateur_service import UtilisateurService
from service.collection_coherente_service import CollectionCoherenteService
from service.collection_physique_service import Collection_physique_service
from dao.collection_coherente_dao import CollectionCoherenteDAO
import logging


liste_utilisateurs = [
    Utilisateur(pseudo="manz1", mdp="1234Azer"),
    Utilisateur(pseudo="z1alan", mdp="1234Azrt"),
    Utilisateur(pseudo="piz1ran", mdp="1234Azrt"),
]

collection_coherente = CollectionCoherente(1, "matcha", "bleu", None)


def test_recherche_manga_par_t_oui():
    """Test de recherche d'un manga par titre """
    # GIVEN
    titre = "my boyfriend is"
    n, m, a = 0, 8, 0
    # WHEN
    longueur, sous_liste, longueur_tot = RechercheService().recherche_manga_par_t(titre, n, m, a)
    # THEN
    assert longueur == 2
    assert sous_liste == ["My Boyfriend Is a Vampire", "My Boyfriend Is a Dog"]
    assert longueur_tot == 2


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
    UtilisateurDao().creer = MagicMock(return_value=True)
    UtilisateurDao().rechercher_tous_pseudo = MagicMock(return_value=liste_utilisateurs)

    UtilisateurService().creer_compte("manz1", "1234Azer")
    UtilisateurService().creer_compte("z1alan", "1234Azrt")
    UtilisateurService().creer_compte("piz1ran", "1234Azrt")

    # WHEN
    longueur, sous_liste, longueur_tot = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert longueur == 3
    assert sous_liste == ["manz1", "z1alan", "piz1ran"]
    assert longueur_tot == 3


def test_recherche_utilisateur_non():
    """Test de recherche d'un utilisateur"""
    # GIVEN
    n, m, a = 0, 8, 0
    pseudo = "z1"
    UtilisateurDao().creer = MagicMock(return_value=False)
    UtilisateurDao().rechercher_tous_pseudo = MagicMock(return_value=liste_utilisateurs)

    UtilisateurService().creer_compte("manz1", "1234Azer")
    UtilisateurService().creer_compte("z1alan", "1234Azrt")
    UtilisateurService().creer_compte("piz1ran", "1234Azrt")

    # WHEN
    longueur, sous_liste, longueur_tot = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert longueur == 3
    assert sous_liste == ["manz1", "z1alan", "piz1ran"]
    assert longueur_tot == 3


def test_recherche_collec_cohe_par_id_oui():
    """Test de recherche d'une collection cohérente par id d'utilisateur"""
    # GIVEN
    UtilisateurDao().recherche_id_par_pseudo = MagicMock(return_value=1)
    CollectionCoherenteDAO().trouver_collec_cohe_id_user = MagicMock(return_value=[collection_coherente])

    id = UtilisateurDao().recherche_id_par_pseudo("manz1")

    # WHEN
    res = RechercheService().recherche_collec_cohe_par_id(id)
    # THEN
    assert res


def test_recherche_collec_cohe_par_id_non():
    """Test de recherche d'une collection cohérente par id d'utilisateur"""
    # GIVEN
    id_1 = 760
    # WHEN
    res = RechercheService().recherche_collec_cohe_par_id(id_1)
    # THEN
    assert not res


def test_recherche_collec_phys_par_id_oui():
    """Test de recherche d'une collection physique par id d'utilisateur"""
    # GIVEN
    id_1 = UtilisateurDao().recherche_id_par_pseudo("manz1")
    Collection_physique_service().creer_collectionphys = MagicMock(return_value=True)
    Collection_physique_service().creer_collectionphys("thé", "vert", id_1)
    # WHEN
    res = RechercheService().recherche_collec_phys_par_id(id_1)
    # THEN
    assert res


def test_recherche_collec_phys_par_id_non():
    """Test de recherche d'une collection physique par id d'utilisateur"""
    # GIVEN
    id_1 = 119
    # WHEN
    res = RechercheService().recherche_collec_phys_par_id(id_1)
    # THEN
    assert not res


if __name__ == "__main__":
    pytest.main([__file__])
