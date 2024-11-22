import pytest
from dao.manga_possede_dao import MangaPossedeDao
from business_object.manga_possede import MangaPossede
from business_object.manga import Manga
from unittest.mock import patch, MagicMock
from business_object.collection_phys import Collection_physique
from business_object.utilisateur import Utilisateur
from dao.collection_physique_dao import CollectionPhysiqueDAO
from dao.utilisateur_dao import UtilisateurDao
from dao.manga_dao import MangaDao

utilisateur1 = Utilisateur("Testuser","Barte8755")
UtilisateurDao().creer(utilisateur1)
manga1 = MangaDao().trouver_manga_par_id(1)

mangap = MangaPossede(id_manga_p=1, num_dernier_acquis=10, statut="En cours")

collecphysique = Collection_physique(id_collectionphysique=0, titre_collection="TestCollec", description_collection="Description test")
CollectionPhysiqueDAO().creer_collectionphys(collecphysique,utilisateur1.id)

def test_ajouter_manga_p():
    # GIVEN

    # WHEN

    # THEN


def test_modifier_num_dernier_acquis():
    # GIVEN

    # WHEN

    # THEN


def test_nb_volume_manga():
    # GIVEN

    # WHEN

    # THEN


def test_trouver_manga_possede_collecphys():
    # GIVEN

    # WHEN

    # THEN


def test_ajouter_num_manquant():
    # GIVEN

    # WHEN

    # THEN


def test_ajouter_ass_num_manquant():
    # GIVEN

    # WHEN

    # THEN


def test_trouver_manga_possede_id():
    # GIVEN

    # WHEN

    # THEN