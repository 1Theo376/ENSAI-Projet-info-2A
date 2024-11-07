import pytest
from unittest.mock import MagicMock
from service.manga_possede_service import MangaPossedeService
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao


@pytest.fixture
def manga_possede_service():
    """Fixture pour creer une instance de MangaPossedeService avec un mock du DAO"""
    service = MangaPossedeService()
    service.dao = MagicMock()  # Remplace l'instance DAO par un mock
    return service


@pytest.fixture
def manga_possede():
    """Fixture pour creer une instance de MangaPossede"""
    return MangaPossede(
        id_manga_p=1,
        manga="Titre Manga",
        num_dernier_acquis=5,
        num_manquant=[1, 3],
        statut="en cours",
    )


def test_creer_manga_possede(manga_possede_service, manga_possede):
    """Test de la méthode creer_manga_possede"""
    # Préparation du mock pour la méthode ajouter_manga_p
    manga_possede_service.dao.MangaPossedeDAO.ajouter_manga_p.return_value = True

    # Test de création d'un manga possédé
    result = manga_possede_service.creer_manga_possede(
        id_manga_p=1,
        manga=manga_possede.manga,
        num_dernier_acquis=5,
        num_manquant=[1, 3],
        statut="en cours",
    )

    # Vérifications
    assert result is not None  # Un nouvel objet doit être retourné
    assert result.id_manga_p == 1
    assert result.num_dernier_acquis == 5
    assert result.num_manquant == [1, 3]
    assert result.statut == "en cours"


def test_modifier_num_dernier_acquis(manga_possede_service, manga_possede):
    """Test de la méthode modifier_num_dernier_acquis"""
    # Préparation du mock pour la méthode modifier_num_dernier_acquis
    manga_possede_service.dao.MangaPossedeDAO.modifier_num_dernier_acquis.return_value = True

    # Test de modification du dernier numéro acquis
    nouveau_num = 6
    result = manga_possede_service.modifier_num_dernier_acquis(manga_possede, nouveau_num)

    # Vérifications
    assert result == nouveau_num  # Le numéro doit être mis à jour
    assert manga_possede.num_dernier_acquis == 6  # L'objet MangaPossede doit être mis à jour


def test_modifier_num_manquant(manga_possede_service, manga_possede):
    """Test de la méthode modifier_num_manquant"""
    # Préparation du mock pour la méthode ajouter_num_manquant
    manga_possede_service.dao.MangaPossedeDAO.ajouter_num_manquant.return_value = True

    # Test de suppression d'un numéro manquant après acquisition
    num_acquis = 1
    result = manga_possede_service.modifier_num_manquant(
        manga_possede, manga_possede.num_manquant, num_acquis
    )

    # Vérifications
    assert result == [3]  # Le numéro manquant doit être supprimé de la liste
    assert manga_possede.num_manquant == [3]


def test_modifier_statut(manga_possede_service, manga_possede):
    """Test de la méthode modifier_statut"""
    # Préparation du mock pour la méthode modifier_statut
    manga_possede_service.dao.MangaPossedeDAO.modifier_statut.return_value = True

    # Test de modification du statut
    nouveau_statut = "completé"
    result = manga_possede_service.modifier_statut(manga_possede, nouveau_statut)

    # Vérifications
    assert result == nouveau_statut  # Le statut doit être mis à jour
    assert manga_possede.statut == "completé"
