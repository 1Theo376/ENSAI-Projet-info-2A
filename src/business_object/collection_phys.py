from serie_manga import Serie_Manga

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
                 Liste_manga: list[Serie_Manga],
                 num_dernier_acquis: int,
                 num_manquant: int,
                 status: str):
        """
        Initialise un nouvel objet CollectionCoherente
        """
        self.id_collectionphysique = id_collectionphysique
        self.Liste_manga = Liste_manga
        self.num_dernier_acquis = num_dernier_acquis
        self.num_manquant = num_manquant
        self.status = status
