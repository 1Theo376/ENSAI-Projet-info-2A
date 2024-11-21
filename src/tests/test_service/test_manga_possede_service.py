import pytest
from unittest.mock import MagicMock
from service.manga_possede_service import MangaPossedeService
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao
from unittest.mock import MagicMock


def test_creer_manga_possede_ok():
    # GIVEN
    MangaPossedeDao().creer_manga_possede = MagicMock(return_value=True)
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo


def test_creer_manga_possede_ko():
    # GIVEN
    MangaPossedeDao().creer_manga_possede = MagicMock(return_value=True)
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo


def test_recherche_pseudo_par_id(utilisateur_test):
    # GIVEN
    id_utilisateur = liste_utilisateurs[0].id
    pseudo_utilisateur = liste_utilisateurs[0].pseudo
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo


def test_recherche_pseudo_par_id(utilisateur_test):
    # GIVEN
    id_utilisateur = liste_utilisateurs[0].id
    pseudo_utilisateur = liste_utilisateurs[0].pseudo
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo


def test_recherche_pseudo_par_id(utilisateur_test):
    # GIVEN
    id_utilisateur = liste_utilisateurs[0].id
    pseudo_utilisateur = liste_utilisateurs[0].pseudo
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo


def test_recherche_pseudo_par_id(utilisateur_test):
    # GIVEN
    id_utilisateur = liste_utilisateurs[0].id
    pseudo_utilisateur = liste_utilisateurs[0].pseudo
    # WHEN
    pseudo = UtilisateurDao().recherche_pseudo_par_id(id_utilisateur)
    # THEN
    assert pseudo_utilisateur == pseudo