from business_object.manga import Manga
from business_object.CollectionCoherente import CollectionCoherente
from dao.collection_coherente_dao import CollectionCoherenteDAO
import logging


class CollectionCoherenteService:
    """
    Classe contenant les méthodes de service de collection physique
    """

    def supprimer_collectioncohe(self, CollectionC):
        """Suppression d'une collection dans la base de données"""
        return CollectionCoherenteDAO().supprimer_collection(CollectionC)

    def creer_collectioncohe(self, titre_collection, desc_collection, idu):
        """ Création d'une collection cohérente """
        nouvelle_collection_cohe = CollectionCoherente(
            id_collectioncoherente=None,
            titre_collection=titre_collection,
            desc_collection=desc_collection,
            Liste_manga=[],
        )
        logging.info(f"nouvelle_collection_cohe : {nouvelle_collection_cohe}")
        return (
            nouvelle_collection_cohe
            if CollectionCoherenteDAO().creer_collection(nouvelle_collection_cohe, idu)
            else None
        )

    def supprimer_mangaposs(self, CollectionC, MangaC: Manga) -> bool:
        """Supression d'un manga de la collection  """
        return CollectionCoherenteDAO().supprimer_manga(CollectionC, MangaC)

    def ajouter_manga(self, idcollec, idmanga) -> bool: #à modif ?
        """ Ajout d'un manga dans la collection  """
        CollectionC = CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga)
        return CollectionC if CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga) else None
