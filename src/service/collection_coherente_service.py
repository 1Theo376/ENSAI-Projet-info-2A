from business_object.manga import Manga
from business_object.CollectionCoherente import CollectionCoherente
from dao.collection_coherente_dao import CollectionCoherenteDAO


class CollectionCoherenteService:
    """
    Classe contenant les méthodes de service de collection physique
    """

    def supprimer_collectioncohe(self, CollectionC):
        """Suppression d'une collection dans la base de données"""
        return self.dao.CollectionCoherenteDAO.supprimer_collection(CollectionC)

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
            if self.dao.CollectionCoherenteDAO.créer_collection(nouvelle_collection_cohe)
            else None
        )

    def supprimer_mangaposs(self, CollectionC, MangaC: Manga) -> bool:
        """ """
        return self.CollectionCoherenteDAO().supprimer_manga(CollectionC, MangaC)

    def ajouter_mangaposs(self, CollectionC, MangaC: Manga) -> bool:
        """ """
        self.CollectionC.Liste_manga.append(MangaC)
        return (
            CollectionC
            if self.dao.CollectionCoherenteDAO.ajouter_manga(CollectionC, MangaC)
            else None
        )

    def __str__(self, CollectionC):
        """Affiche tous les titres des mangas présents dans la collection."""
        if len(self.CollectionC.Liste_manga) == 0:
            return "La collection ne contient aucun manga."

        Texte_Liste_Titre_Manga = ", ".join(manga.titre for manga in self.Liste_manga)

        return f"Voici les mangas présents dans cette collection : {Texte_Liste_Titre_Manga}"
