from manga_possede import MangaPossede
from collection_phys import Collection_physique

class Collection_physique_service:
    """
Classe contenant les méthodes de service de collection physique
    """
    def supprimer_collectionphys(self, collectionphys):
        """Suppression d'une collection dans la base de données


        """
        return self.dao.CollectionPhysiqueDAO.supprimer_collectionphys(collectionphys)


    def créer_collectionphys(self, id_collectionphysique, titre_collection, desc_collection) :
        """
        """
        nouvelle_collection_phys = Collection_physique(
            id_collectionphysique=id_collectionphysique,
            titre_collection=titre_collection,
            desc_collection=desc_collection,
        )

        return nouvelle_collection_phys if self.dao.CollectionPhysiqueDAO.supprimer(nouvelle_collection_phys) else None

    def supprimer_mangaposs(self, CollectionPhysique, MangaPoss) -> bool:
        """
        """

    def ajouter_mangaposs(self, CollectionPhysique, MangaPoss) -> bool:
        """
        """
