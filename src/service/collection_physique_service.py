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
            Liste_manga=[],

        )

        return nouvelle_collection_phys if self.dao.CollectionPhysiqueDAO.supprimer(nouvelle_collection_phys) else None

    def supprimer_mangaposs(self, CollectionP, MangaPoss: MangaPossede) -> bool:
        """
        """
        return self.dao.CollectionPhysiqueDAO.supprimer_mangaposs(CollectionP, MangaPoss)

    def ajouter_mangaposs(self, CollectionP, MangaPoss) -> bool:
        """
        """
        self.CollectionP.Liste_manga.append(MangaPoss)
        return MangaPoss if self.dao.CollectionPhysiqueDAOajouter_mangaposs(CollectionP, MangaPoss) else None

    def __str__(self, CollectionP):
        """Affiche tous les titres des mangas présents dans la collection."""
        if len(self.CollectionP.Liste_manga) == 0:
            return "La collection ne contient aucun manga."

        Texte_Liste_Titre_Manga = ", ".join(manga.titre for manga in self.Liste_manga)

        return f"Voici les mangas présents dans cette collection : {Texte_Liste_Titre_Manga}"
