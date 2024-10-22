from manga_possede import MangaPossede


class Collection_physique:
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
        Une liste contenant les objets Manga qui font partie de cette collection

    """

    def __init__(self,
                 id_collectionphysique: int,
                 titre_collection: str,
                 description_collection: str,
                 Liste_manga=[]):
        """
        Initialise un nouvel objet CollectionCoherente
        """
        self.id_collectionphysique = id_collectionphysique
        self.titre_collection = titre_collection
        self.description_collection = description_collection
        self.Liste_manga = Liste_manga
