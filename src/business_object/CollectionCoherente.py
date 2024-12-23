class CollectionCoherente:
    """
    Classe représentant une collection cohérente de mangas.

    Attributs :
    ----------
    id_collectioncoherente : int
        L'identifiant unique de la collection

    titre_collection : str
        Le titre de la collection

    desc_collection : str
        Une description de la collection

    Liste_manga : list[Manga]
        Une liste contenant les objets Manga qui font partie de
        cette collection

    """

    def __init__(
        self,
        id_collectioncoherente: int,
        titre_collection: str,
        desc_collection: str,
        Liste_manga=[],
    ):
        """Initialise un nouvel objet CollectionCoherente"""

        self.id_collectioncoherente = id_collectioncoherente
        self.titre_collection = titre_collection
        self.desc_collection = desc_collection
        self.Liste_manga = Liste_manga
