import pytest
from unittest.mock import MagicMock, patch
from service.manga_possede_service import MangaPossedeService
from business_object.manga_possede import MangaPossede
from dao.manga_possede_dao import MangaPossedeDao

@patch('dao.manga_possede_dao.MangaPossedeDao.ajouter_manga_p', return_value=True)
def test_creer_manga_possede_ok(patch):
    # GIVEN
    MangaPossedeDao().ajouter_manga_p = MagicMock(return_value=True)
    # WHEN
    mangap = MangaPossedeService().creer_manga_possede(1, 8, [5, 7], "En cours")
    # THEN
    assert mangap.idmanga == 1


def test_creer_manga_possede_ko():
    # GIVEN
    MangaPossedeDao().creer_manga_possede = MagicMock(return_value=False)
    # WHEN
    mangap = MangaPossedeService().creer_manga_possede(-1, 8, [5, 7], "En cours")
    # THEN
    assert mangap is None


def test_modifier_num_manquant_ok():  
    # GIVEN
    MangaPossedeDao().trouver_id_num_manquant_id = MagicMock(return_value=[])
    MangaPossedeDao().supprimer_num_manquant = MagicMock(return_value=True)
    MangaPossedeDao().ajouter_num_manquant = MagicMock(return_value=True)
    mangap = MangaPossede(idmanga=1, num_dernier_acquis=8, num_manquant=[5, 7], statut="En cours")
    # WHEN
    mangap.num_manquant = MangaPossedeService().modifier_num_manquant(mangap, [6])
    # THEN
    assert mangap.num_manquant == [6]

@patch('dao.manga_possede_dao.MangaPossedeDao.ajouter_num_manquant', return_value=False)
def test_modifier_num_manquant_ko(patch):
    # GIVEN
    MangaPossedeDao().trouver_id_num_manquant_id = MagicMock(return_value=[5, 7])
    MangaPossedeDao().supprimer_num_manquant = MagicMock(return_value=True)
    mangap = MangaPossede(1, 8, [5, 7], "En cours")
    # WHEN
    mangap.num_manquant = MangaPossedeService().modifier_num_manquant(mangap, [6])
    # THEN
    assert mangap.num_manquant == []


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
