import pytest
from unittest.mock import MagicMock
from service.collection_physique_service import Collection_physique_service
from business_object.collection_phys import Collection_physique
from business_object.manga_possede import MangaPossede


def test_creer_collectionphys():
    # Configuration du service avec un DAO simulé
    service = Collection_physique_service()
    service.dao = MagicMock()
    service.dao.CollectionPhysiqueDAO = MagicMock()

    # Configuration du mock pour le DAO
    service.dao.CollectionPhysiqueDAO.supprimer.return_value = True

    # Données de test
    id_collectionphysique = 1
    titre_collection = "Collection Shonen"
    description_collection = "Description de la collection Shonen"

    # Exécution de la fonction
<<<<<<< HEAD
    nouvelle_collection = service.creer_collectionphys(
        id_collectionphysique, titre_collection, desc_collection
    )
=======
    nouvelle_collection = service.créer_collectionphys(id_collectionphysique, titre_collection, description_collection)
>>>>>>> 55fc9a369faaeee2d2989d9b26321c7f4aa82dff

    # Vérifications
    assert nouvelle_collection is not None, "La collection physique n'a pas été créée correctement."
    assert nouvelle_collection.id_collectionphysique == id_collectionphysique
    assert nouvelle_collection.titre_collection == titre_collection
    assert nouvelle_collection.description_collection == description_collection
    assert nouvelle_collection.Liste_manga == []

    # Vérifie que le DAO a bien été appelé
    service.dao.CollectionPhysiqueDAO.supprimer.assert_called_once_with(nouvelle_collection)


def test_supprimer_collectionphys():
    service = Collection_physique_service()
    service.dao = MagicMock()
    service.dao.CollectionPhysiqueDAO = MagicMock()

    # Mock pour la suppression
    collection = Collection_physique(
        id_collectionphysique=1,
        titre_collection="Collection Test",
        description_collection="Test",
        Liste_manga=[],
    )
    service.dao.CollectionPhysiqueDAO.supprimer_collectionphys.return_value = True

    result = service.supprimer_collectionphys(collection)

    assert result is True
    service.dao.CollectionPhysiqueDAO.supprimer_collectionphys.assert_called_once_with(collection)


def test_ajouter_mangaposs():
    service = Collection_physique_service()
    service.dao = MagicMock()
    service.dao.CollectionPhysiqueDAO = MagicMock()

    # Données de test
    collection = Collection_physique(
        id_collectionphysique=1,
        titre_collection="Collection Test",
        description_collection="Test",
        Liste_manga=[],
    )
    manga = MangaPossede(
        id_manga_p=101, manga="Manga Test", num_dernier_acquis=10, num_manquant=[], statut="A lire"
    )

    # Configuration du mock
    service.dao.CollectionPhysiqueDAO.ajouter_mangaposs.return_value = True

    # Appel de la méthode
    result = service.ajouter_mangaposs(collection, manga)

    # Vérifications
    assert result == manga
    assert manga in collection.Liste_manga
    service.dao.CollectionPhysiqueDAO.ajouter_mangaposs.assert_called_once_with(collection, manga)


def test_supprimer_mangaposs():
    service = Collection_physique_service()
    service.dao = MagicMock()
    service.dao.CollectionPhysiqueDAO = MagicMock()

    # Données de test
    collection = Collection_physique(
        id_collectionphysique=1,
        titre_collection="Collection Test",
        description_collection="Test",
        Liste_manga=[],
    )
    manga = MangaPossede(
        id_manga_p=101, manga="Manga Test", num_dernier_acquis=10, num_manquant=[], statut="A lire"
    )
    collection.Liste_manga.append(manga)

    # Configuration du mock
    service.dao.CollectionPhysiqueDAO.supprimer_mangaposs.return_value = True

    # Appel de la méthode
    result = service.supprimer_mangaposs(collection, manga)

    # Vérifications
    assert result is True
    assert manga not in collection.Liste_manga
    service.dao.CollectionPhysiqueDAO.supprimer_mangaposs.assert_called_once_with(collection, manga)


def test_str():
    service = Collection_physique_service()
    collection = Collection_physique(
        id_collectionphysique=1,
        titre_collection="Collection Test",
        description_collection="Test",
        Liste_manga=[],
    )
    manga1 = MangaPossede(
        id_manga_p=101, manga="Manga1", num_dernier_acquis=10, num_manquant=[], statut="A lire"
    )
    manga2 = MangaPossede(
        id_manga_p=102, manga="Manga2", num_dernier_acquis=5, num_manquant=[], statut="En cours"
    )

    collection.Liste_manga.extend([manga1, manga2])
    service.CollectionP = collection

    result = service.__str__(collection)

    assert result == "Voici les mangas présents dans cette collection : Manga1, Manga2"
