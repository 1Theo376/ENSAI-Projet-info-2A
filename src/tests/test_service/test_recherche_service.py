from unittest.mock import MagicMock
from service.recherche_service import RechercheService
from business_object.manga import Manga
from business_object.utilisateur import Utilisateur
from service.utilisateur_service import UtilisateurService
from dao.utilisateur_dao import UtilisateurDao
from service.collection_coherente_service import CollectionCoherenteService


#UtilisateurService().creer_compte("manz1", "1234Azer")
#UtilisateurService().creer_compte("z1alan", "1234Azrt")
#UtilisateurService().creer_compte("piz1ran", "1234Azrt")

id_1 = UtilisateurDao().recherche_id_par_pseudo("manz1")
CollectionCoherenteService().creer_collectioncohe("matcha", "vert", id_1)


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
    pseudo = "zdfdf"
    # WHEN
    res = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert not res


def test_recherche_collec_cohe_par_id_oui():
    """Test de recherche d'une collection cohérente par id d'utilisateur"""
    # GIVEN
    id = id_1
    # WHEN
    res = RechercheService().recherche_collec_cohe_par_id(id)
    # THEN
    assert res == ["matcha"]


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
