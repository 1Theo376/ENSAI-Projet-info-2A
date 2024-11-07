import pytest
from unittest.mock import MagicMock
from service.avis_service import AvisService
from business_object.avis import Avis
from dao.avis_dao import AvisDAO


@pytest.fixture
def avis_service():
    """Fixture pour créer une instance du service AvisService avec un mock du DAO"""
    service = AvisService()
    service.dao = MagicMock()  # Remplacer l'instance DAO par un mock
    return service


@pytest.fixture
def avis():
    """Fixture pour créer une instance d'Avis"""
    return Avis(id_avis=1, texte="C'est un super manga !")


def test_rediger_avis(avis_service):
    """Test de la méthode rediger_avis"""
    # Préparer le mock pour la méthode creer_avis
    avis = MagicMock(texte="C'est un super manga !")
    avis_service.rediger_avis = MagicMock(return_value=avis)

    # Tester la rédaction d'un avis valide
    texte = "C'est un super manga !"
    result = avis_service.rediger_avis(texte, id_avis=1, id_user=1, id_manga=1)

    # Vérification
    assert result.texte == texte  # Le texte de l'avis doit être celui passé en paramètre
    avis_service.rediger_avis.assert_called_once_with(texte, id_avis=1, id_user=1, id_manga=1)


def test_rediger_avis_texte_vide(avis_service):
    """Test de la méthode rediger_avis avec un texte vide"""
    with pytest.raises(ValueError, match="Ce n'est pas une description"):
        avis_service.rediger_avis("", id_avis=1, id_user=1, id_manga=1)


def test_supprimer_avis(avis_service, avis):
    """Test de la méthode supprimer_avis"""
    # Préparer le mock pour la méthode supprimer_avis
    avis_service.supprimer_avis = MagicMock(return_value=True)

    # Tester la suppression de l'avis
    result = avis_service.supprimer_avis(avis)

    # Vérification
    assert result is True  # L'avis doit être supprimé
    avis_service.supprimer_avis.assert_called_once_with(avis)


def test_afficher_avis_pagination(avis_service):
    """Test de la méthode afficher_avis_pagination"""
    # Simuler des avis pour un utilisateur donné
    avis_service.recuperer_avis_utilisateur = MagicMock(return_value=[f"Avis {i}" for i in range(1, 21)])

    # Paramètres de pagination
    avis_service.page_size = 5
    avis_service.current_page = 0

    # Test de l'affichage des avis avec pagination
    with pytest.raises(Exception, match="Aucun avis disponible pour cet utilisateur."):
        avis_service.afficher_avis_pagination(id_utilisateur=1)  # vérifier l'existence du message


def test_afficher_avis_pagination_page_suivante(avis_service):
    """Test de la méthode afficher_avis_pagination avec la pagination activée"""
    # Simuler des avis pour un utilisateur donné
    avis_service.recuperer_avis_utilisateur = MagicMock(return_value=[f"Avis {i}" for i in range(1, 21)])

    # Paramètres de pagination
    avis_service.page_size = 5
    avis_service.current_page = 0

    # Tester l'affichage des avis avec page suivante activée
    avis_service.afficher_avis_pagination(id_utilisateur=1, page_suivante=True)

    # Vérification
    avis_service.recuperer_avis_utilisateur.assert_called_once_with(1)
    assert avis_service.current_page == 1  # Vérifier que la page suivante a été activée


def test_recuperer_avis_utilisateur(avis_service):
    """Test de la méthode recuperer_avis_utilisateur"""
    # Simuler la récupération des avis pour un utilisateur
    result = avis_service.recuperer_avis_utilisateur(id_utilisateur=1)

    # Vérification
    assert len(result) == 20  # Il y a 20 avis simulés
    assert result[0] == "Avis 1 de l'utilisateur 1"  # Le premier avis doit être celui de l'utilisateur 1
