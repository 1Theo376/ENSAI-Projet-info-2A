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
        """Création d'une collection cohérente"""
        nouvelle_collection_cohe = CollectionCoherente(
            id_collectioncoherente=None,
            titre_collection=titre_collection,
            desc_collection=desc_collection,
            Liste_manga=[],
        )
        logging.info(f"nouvelle_collection_cohe : {nouvelle_collection_cohe}")
        if CollectionCoherenteDAO().creer_collection(nouvelle_collection_cohe, idu):
            return nouvelle_collection_cohe
        else:
            return None

    def supprimer_mangaposs(self, CollectionC, MangaC: Manga) -> bool:
        """Supression d'un manga de la collection"""
        return CollectionCoherenteDAO().supprimer_manga(CollectionC, MangaC)

    def ajouter_manga(self, idcollec, idmanga) -> bool:
        """Ajout d'un manga dans la collection"""
        CollectionC = CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga)
        return CollectionC if CollectionCoherenteDAO().ajouter_manga(idcollec, idmanga) else None

    def trouver_collec_cohe_id_user(self, id_utilisateur) -> CollectionCoherente:
        return CollectionCoherenteDAO().trouver_collec_cohe_id_user(id_utilisateur)

    def trouver_collec_cohe_nom(self, nom, idu) -> CollectionCoherente:
        return CollectionCoherenteDAO().trouver_collec_cohe_nom(nom, idu)

    def modifier_titre(self, id_collection: int, nouveau_titre: str) -> bool:
        return CollectionCoherenteDAO().modifier_titre(id_collection, nouveau_titre)

    def modifier_desc(self, id_collection: int, nouvelle_desc: str) -> bool:
        return modifier_desc(id_collection, nouvelle_desc)
