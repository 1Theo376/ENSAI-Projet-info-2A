import pytest
from avis import Avis
from avisdao import AvisDAO

from utils.reset_database import ResetDatabase

@pytest.fixture(autouse=True)
def reset_db():
    ResetDatabase.reset()

@pytest.fixture
def avis_dao():
    return AvisDAO()


@pytest.fixture
def avis1():
    return Avis(id_avis=1, texte="Avis 1")


@pytest.fixture
def avis2():
    return Avis(id_avis=2, texte="Avis2")


def test_creer_avis(avis_dao, avis1):
    result = avis_dao.creer_avis(avis1)
    assert result == True
    result = avis_dao.creer_avis(avis1)
    assert result == False


def test_trouver_avis_par_id(avis_dao, avis1):
    avis_dao.creer_avis(avis1)
    found_avis = avis_dao.trouver_avis_par_id(avis1.id_avis)
    assert found_avis == avis1
    assert avis_dao.trouver_avis_par_id(999) is None


def test_supprimer_avis(avis_dao, avis1):
    avis_dao.creer_avis(avis1)
    result = avis_dao.supprimer_avis(avis1)
    assert result == True
    result = avis_dao.supprimer_avis(avis1)
    assert result == False


def test_modifier_avis(avis_dao, avis1, avis2):
    avis_dao.creer_avis(avis1)
    avis1_modifie = Avis(id_avis=1, texte="Avis modifié")
    result = avis_dao.modifier_avis(avis1_modifie)
    assert result == True
    assert avis_dao.trouver_avis_par_id(avis1.id_avis).texte == "Avis modifié"
    result = avis_dao.modifier_avis(avis2)
    assert result == False


def test_consulter_avis(avis_dao, avis1):
    avis_dao.creer_avis(avis1)
    found_avis = avis_dao.consulter_avis(avis1.id_avis)
    assert found_avis == avis1
    assert avis_dao.consulter_avis(999) is None


def test_recuperer_avis_utilisateur(avis_dao, avis1, avis2):
    avis_dao.creer_avis(avis1)
    avis_dao.creer_avis(avis2)
    avis_utilisateur = avis_dao.recuperer_avis_utilisateur(1)
    assert len(avis_utilisateur) == 1
    assert avis_utilisateur[0].id_avis == avis1.id_avis
