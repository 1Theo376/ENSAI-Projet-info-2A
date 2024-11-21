import pytest
from unittest.mock import MagicMock
from service.manga_possede_service import MangaPossedeService
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao
from unittest.mock import MagicMock


mangap = MangaPossedeService().creer_manga_possede(1, 8, [5, 7], "En cours")


def test_creer_manga_possede_ok():
    # GIVEN
    MangaPossedeDao().creer_manga_possede = MagicMock(return_value=True)
    # WHEN
    mangap = MangaPossedeService().creer_manga_possede(1, 8, [5, 7], "En cours")
    # THEN
    assert mangap.id_manga == 1


def test_creer_manga_possede_ko():
    # GIVEN
    MangaPossedeDao().creer_manga_possede = MagicMock(return_value=False)
    # WHEN
    mangap = MangaPossedeService().creer_manga_possede(-1, 8, [5, 7], "En cours")
    # THEN
    assert mangap is None


def test_modifier_num_dernier_acquis_ok():
    # GIVEN
    MangaPossedeDao().modifier_num_dernier_acquis = MagicMock(return_value=True)
    # WHEN
    numacqmang = MangaPossedeService().modifier_num_dernier_acquis(mangap, 6)
    # THEN
    assert numacqmang == 6


def test_modifier_num_dernier_acquis_ko():
    # GIVEN
    MangaPossedeDao().modifier_num_dernier_acquis = MagicMock(return_value=False)
    # WHEN
    numacqmang = MangaPossedeService().modifier_num_dernier_acquis(mangap, 6)
    # THEN
    assert numacqmang == 6


def test_modifier_num_manquant_ok():
    # GIVEN
    MangaPossedeDao().modifier_num_dernier_acquis = MagicMock(return_value=False)
    # WHEN
    numacqmang = MangaPossedeService().modifier_num_dernier_acquis(mangap, 6)
    # THEN
    assert numacqmang == 6


def test_modifier_num_manquant_ko():
    # GIVEN
    MangaPossedeDao().modifier_num_dernier_acquis = MagicMock(return_value=False)
    # WHEN
    numacqmang = MangaPossedeService().modifier_num_dernier_acquis(mangap, 6)
    # THEN
    assert numacqmang == 6


def test_modifier_statut_ok():
    # GIVEN
    MangaPossedeDao().modifier_num_dernier_acquis = MagicMock(return_value=False)
    # WHEN
    numacqmang = MangaPossedeService().modifier_num_dernier_acquis(mangap, 6)
    # THEN
    assert numacqmang == 6


def test_modifier_statut_ko():
    # GIVEN
    MangaPossedeDao().modifier_num_dernier_acquis = MagicMock(return_value=False)
    # WHEN
    numacqmang = MangaPossedeService().modifier_num_dernier_acquis(mangap, 6)
    # THEN
    assert numacqmang == 6