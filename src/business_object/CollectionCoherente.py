from Manga import Manga


class CollectionCoherente:
    """
    Représente une collection cohérente de mangas.

    Parameters :
    ----------
    id_collection : int
        L'identifiant unique de la collection

    titre_collection : str
        Le titre de la collection

    desc_collection : str
        Une description de la collection

    Liste_manga : list[Manga]
        Une liste contenant les objets Manga qui font partie de
        cette collection

    Methods :
    --------
    __init__(self,
             id_collection: int,
             titre_collection: str,
             desc_collection: str,
             Liste_manga: list[Manga])
        Initialise un nouvel objet CollectionCoherente avec les
        informations fournies

    ajouter_manga(self, manga: Manga)
        Ajoute un objet Manga à la collection

    supprimer_manga(self, manga: Manga)
        Supprime un objet Manga de la collection s'il existe

    __str__(self) -> str
        Retourne une représentation en chaîne de caractères de la collection,
    en listant les titres des mangas qu'elle contient

    """

    def __init__(self,
                 id_collectioncoherente: int,
                 titre_collection: str,
                 desc_collection: str,
                 Liste_manga: list[Manga]):
        """
        Initialise un nouvel objet CollectionCoherente
        """

        self.id_collectioncoherente = id_collectioncoherente
        self.titre_collection = titre_collection
        self. desc_collection = desc_collection
        self.Liste_manga = Liste_manga
