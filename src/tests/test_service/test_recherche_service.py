from unittest.mock import MagicMock
from service.recherche_service import RechercheService
from business_object.manga import Manga
from business_object.utilisateur import Utilisateur
from service.utilisateur_service import UtilisateurService
from dao.utilisateur_dao import UtilisateurDao


liste_mangas = [
    Manga("My Boyfriend Is a Vampire", None, None, None, None),
    Manga("My Boyfriend Is a Dog", None, None, None, None)
]

liste_utilisateurs = [
    Utilisateur(pseudo="huy", mdp="1234Azer"),
    Utilisateur(pseudo="aze", mdp="0000Poiu"),
    Utilisateur(pseudo="vert", mdp="abcd1Ruy"),
]


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
    """Test de recherche d'un manga par titre """
    # GIVEN
    pseudo1 = "manz1"
    mdp1 = "1234Azer"
    pseudo2 = "z1alan"
    mdp2 = "1234Azrt"
    pseudo3 = "piz1ran"
    mdp3 = "1234Azrt"
    UtilisateurDao.creer = MagicMock(return_value=True)
    UtilisateurService().creer_compte(pseudo1, mdp1)
    UtilisateurService().creer_compte(pseudo2, mdp2)
    UtilisateurService().creer_compte(pseudo3, mdp3)
    n, m, a = 0, 8, 0
    pseudo = "z1"
    # WHEN
    longueur, sous_liste, longueur_tot = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert longueur == 3
    assert sous_liste == ["manz1", "z1alan", "piz1ran"]
    assert longueur_tot == 3


def test_recherche_utilisateur_non():
    """Test de recherche d'un manga par titre """
    # GIVEN
    UtilisateurDao.creer = MagicMock(return_value=False)
    UtilisateurService().creer_compte("manz1", "1234Azer")
    UtilisateurService().creer_compte("z1alan", "1234Azrt")
    UtilisateurService().creer_compte("piz1ran", "1234Azrt")
    n, m, a = 0, 8, 0
    pseudo = "zdfdf"
    # WHEN
    res = RechercheService().recherche_utilisateur(pseudo, n, m, a)
    # THEN
    assert not res


def test_recherche_collec_cohe_par_id_oui():
    """Test de recherche d'un manga par titre """
    # GIVEN
    id_c = 2
    # WHEN
    res = RechercheService().recherche_collec_cohe_par_id(id_c)
    # THEN
    assert res == ["matcha"]


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
