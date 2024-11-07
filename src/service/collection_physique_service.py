from business_object.manga_possede import MangaPossede
from business_object.collection_phys import Collection_physique
from dao.collection_physique_dao import CollectionPhysiqueDAO


class Collection_physique_service:
    """
    Classe contenant les méthodes de service de collection physique
    """

    def supprimer_collectionphys(self, collectionphys):
        """Suppression d'une collection dans la base de données"""
        return CollectionPhysiqueDAO().supprimer_collectionphys(collectionphys)

    def creer_collectionphys(self, titre_collection, desc_collection):
        """ """
        nouvelle_collection_phys = Collection_physique(
            id_collectionphysique=None,
            titre_collection=titre_collection,
            description_collection=desc_collection,
            Liste_manga=[],
        )

        return (
            nouvelle_collection_phys
            if CollectionPhysiqueDAO().creer_collectionphys(nouvelle_collection_phys)
            else None
        )

    def supprimer_mangaposs(self, CollectionP, MangaPoss: MangaPossede) -> bool:
        """ """
        return CollectionPhysiqueDAO().supprimer_mangaposs(CollectionP, MangaPoss)

    def ajouter_mangaposs(self, CollectionP, MangaPoss) -> bool:
        """ """
        CollectionP.Liste_manga.append(MangaPoss)
        return (
            MangaPoss if CollectionPhysiqueDAO().ajouter_mangaposs(CollectionP, MangaPoss) else None
        )

    def __str__(self, CollectionP):
        """Affiche tous les titres des mangas présents dans la collection."""
        if len(CollectionP.Liste_manga) == 0:
            return "La collection ne contient aucun manga."

        Texte_Liste_Titre_Manga = ", ".join(manga.titre for manga in CollectionP.Liste_manga)

        return f"Voici les mangas présents dans cette collection : {Texte_Liste_Titre_Manga}"
