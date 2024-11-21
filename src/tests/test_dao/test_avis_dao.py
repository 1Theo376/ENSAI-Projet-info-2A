import pytest
import os
from src.business_object.avis import Avis
from dao.avis_dao import AvisDAO
from unittest.mock import patch

@pytest.fixture
def avis_dao():
    return AvisDAO()


@pytest.fixture
def avis1():
    return Avis(id_avis=1, texte="Avis 1")


@pytest.fixture
def avis2():
    return Avis(id_avis=2, texte="Avis 2")


def test_creer_avis(avis_dao, avis1):
    result = avis_dao.creer_avis(avis1, id_user=1, id_manga=1)
    assert result == True  # Vérifie que l'avis a bien été créé
    result = avis_dao.creer_avis(avis1)
    assert result == False  # Vérifie qu'un avis ne peut pas être créé deux fois


def test_trouver_avis_par_id(avis_dao, avis1):
    avis_dao.creer_avis(avis1, id_user=1, id_manga=1)
    found_avis = avis_dao.trouver_avis_par_id(avis1.id_avis)
    assert found_avis == avis1  # Vérifie que l'avis est trouvé correctement
    assert avis_dao.trouver_avis_par_id(999) is None  # Vérifie qu'un avis inexistant retourne None


def test_supprimer_avis(avis_dao, avis1):
    avis_dao.creer_avis(avis1, id_user=1, id_manga=1)
    result = avis_dao.supprimer_avis(avis1)
    assert result == True  # Vérifie que l'avis a bien été supprimé
    result = avis_dao.supprimer_avis(avis1)
    assert result == False  # Vérifie qu'un avis déjà supprimé ne peut pas être supprimé à nouveau


def test_modifier_avis(avis_dao, avis1, avis2):
    avis_dao.creer_avis(avis1, id_user=1, id_manga=1)
    avis1_modifie = Avis(id_avis=1, texte="Avis modifié")
    result = avis_dao.modifier_avis(avis1_modifie)
    assert result == True  # Vérifie que l'avis a bien été modifié
    assert avis_dao.trouver_avis_par_id(avis1.id_avis).texte == "Avis modifié"  # Vérifie que le texte de l'avis a bien été modifié
    result = avis_dao.modifier_avis(avis2)
    assert result == False  # Vérifie qu'un avis inexistant ne peut pas être modifié


def test_consulter_avis(avis_dao, avis1):
    avis_dao.creer_avis(avis1, id_user=1, id_manga=1)
    found_avis = avis_dao.consulter_avis(avis1.id_avis)
    assert found_avis == avis1  # Vérifie que l'avis est bien consulté
    assert avis_dao.consulter_avis(999) is None  # Vérifie qu'un avis inexistant retourne None


def test_recuperer_avis_utilisateur(avis_dao, avis1, avis2):
    avis_dao.creer_avis(avis1, id_user=1, id_manga=1)
    avis_dao.creer_avis(avis2, id_user=1, id_manga=1)
    avis_utilisateur = avis_dao.recuperer_avis_utilisateur(1)
    assert len(avis_utilisateur) == 1  # Vérifie qu'un seul avis de l'utilisateur est retourné
    assert avis_utilisateur[0].id_avis == avis1.id_avis  # Vérifie que l'avis retourné correspond bien à l'utilisateur
