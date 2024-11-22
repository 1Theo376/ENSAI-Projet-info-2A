class Collection_physique:
    """
    Classe représentant une collection physique de mangas, c'est-à-dire les mangas
    possédés en vrai, par tome.

    Attributs:
    ----------
    id_collectionphysique : int
        L'identifiant unique de la collection.

    titre_collection : str
        Le titre de la collection.

    description_collection : str
        Une description de la collection.

    Liste_manga : list[Manga]
        Une liste contenant les objets Manga qui font partie de cette collection.

    """

    def __init__(
        self,
        titre_collection: str,
        description_collection: str,
        Liste_manga=[],
        id_collectionphysique=None
    ):
        """ Initialise un nouvel objet Collection_physique"""
        self.id_collectionphysique = id_collectionphysique
        self.titre_collection = titre_collection
        self.description_collection = description_collection
        self.Liste_manga = Liste_manga
