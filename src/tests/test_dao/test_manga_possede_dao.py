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
from service.collection_physique_service import Collection_physique_service

liste_utilisateurs = [
    Utilisateur(pseudo="huy", mdp="1234Azer"),
    Utilisateur(pseudo="aze", mdp="0000Poiu"),
    Utilisateur(pseudo="vert", mdp="abcd1Ruy"),
]


@pytest.fixture(scope="function", autouse=True)
def setup_test_environment():
    """Initialisation des données de test pour UtilisateurDao"""
    with patch.dict("os.environ", {"POSTGRES_SCHEMA": "projet_test_dao"}):
        from utils.reset_database import ResetDatabase
        ResetDatabase().lancer(test_dao=True)
        MangaDao().inserer_mangas("testmangas.json")
        yield


@pytest.fixture(scope="function", autouse=True)
def utilisateur_test():
    """Crée un joueur pour les tests"""



def test_ajouter_manga_p():
    # GIVEN
    mangap = MangaPossede(
        idmanga=2, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours"
    )
    # WHEN
    res = MangaPossedeDao().ajouter_manga_p(mangap)
    # THEN
    assert res


def test_nb_volume_manga():
    # GIVEN
    nom = "Monster"  # il y a 18 tomes dans ce manga
    # WHEN
    volumes = MangaPossedeDao().nb_volume_manga(nom)
    # THEN
    assert volumes == 18


def test_trouver_manga_possede_collecphys():
    # GIVEN
    utilisateur = Utilisateur(pseudo="hy", mdp="HuYT7894")
    UtilisateurDao().creer(utilisateur)
    manga1 = MangaDao().trouver_manga_par_id(1)
    mangap = MangaPossede(
        idmanga=1, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours"
    )
    MangaPossedeDao().ajouter_manga_p(mangap)
    titre = manga1.titre
    collecphysique = Collection_physique(
            titre_collection="TestCollec",
            description_collection="Description test",
            )
    Collection_physique_service().creer_collectionphys(collecphysique.titre_collection, collecphysique.description_collection, utilisateur.id)
    collection = CollectionPhysiqueDAO().trouver_collec_phys_id_user(utilisateur.id)
    Collection_physique_service().ajouter_mangaposs(
            collection.id_collectionphysique, mangap.id_manga_p
        )
    # WHEN

    mangap2 = MangaPossedeDao().trouver_manga_possede_collecphys(
        titre, collection.id_collectionphysique
    )
    # THEN
    assert mangap.num_dernier_acquis == mangap2.num_dernier_acquis


def test_trouver_id_num_manquant_id():  # difficile
    # GIVEN
    mangap = MangaPossede(
        idmanga=1, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours"
    )
    MangaPossedeDao().ajouter_manga_p(mangap)
    idp = mangap.id_manga_p
    for elt in mangap.num_manquant:
        id_num = MangaPossedeDao().ajouter_num_manquant(elt)
        MangaPossedeDao().ajouter_ass_num_manquant(mangap.id_manga_p, id_num)
    # WHEN
    liste_id_num_manquant = MangaPossedeDao().trouver_id_num_manquant_id(idp)
    # THEN
    assert liste_id_num_manquant == [1,2,3]


def test_ajouter_num_manquant():
    # GIVEN
    num_manquant1 = 5
    # WHEN
    res = MangaPossedeDao().ajouter_num_manquant(num_manquant1)
    # THEN
    assert res == 1


def test_ajouter_ass_num_manquant():  # à revoir
    # GIVEN
    mangap = MangaPossede(
        idmanga=1, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours"
    )
    MangaPossedeDao().ajouter_manga_p(mangap)
    res = []
    for elt in mangap.num_manquant:
        id_num = MangaPossedeDao().ajouter_num_manquant(elt)
        res.append(id_num)
    # WHEN
    resultat = MangaPossedeDao().ajouter_ass_num_manquant(mangap.id_manga_p, res[0])
    # THEN
    assert resultat


def test_trouver_manga_possede_id():
    # GIVEN
    mangap = MangaPossede(
        idmanga=1, num_dernier_acquis=10, num_manquant=[1, 2, 3], statut="En cours"
    )
    MangaPossedeDao().ajouter_manga_p(mangap)
    idp = mangap.id_manga_p
    # WHEN
    mangap3 = MangaPossedeDao().trouver_manga_possede_id(idp)
    # THEN
    assert mangap.num_dernier_acquis == mangap3.num_dernier_acquis


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
