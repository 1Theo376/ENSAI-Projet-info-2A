from business_object.manga import Manga
from business_object.CollectionCoherente import CollectionCoherente
from dao.collection_coherente_dao import CollectionCoherenteDAO


class CollectionCoherenteService:
    """
    Classe contenant les méthodes de service de collection physique
    """

    def supprimer_collectioncohe(self, CollectionC):
        """Suppression d'une collection dans la base de données"""
        return CollectionCoherenteDAO().supprimer_collection(CollectionC)

    def creer_collectioncohe(self, titre_collection, desc_collection):
        """ """
        nouvelle_collection_cohe = CollectionCoherente(
            id_collectioncoherente=None,
            titre_collection=titre_collection,
            desc_collection=desc_collection,
            Liste_manga=[],
        )

        return (
            nouvelle_collection_cohe
            if CollectionCoherenteDAO().creer_collection(nouvelle_collection_cohe)
            else None
        )

    def supprimer_mangaposs(self, CollectionC, MangaC: Manga) -> bool:
        """ """
        return CollectionCoherenteDAO().supprimer_manga(CollectionC, MangaC)

    def ajouter_mangaposs(self, idcollec, idmanga) -> bool:
        """ """
<<<<<<< HEAD
        CollectionC = CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga)
        return CollectionC if CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga) else None
=======
        return True if CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga) else None
>>>>>>> 4ed2054bb2fd2b1e75e9f026b9c75a4fe0396910
