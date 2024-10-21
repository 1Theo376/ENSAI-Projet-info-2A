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

    Methods :
    --------
    __init__(self,
            id_collection: int,
            titre_collection: str,
            desc_collection: str,
            Liste_manga: list[Manga])
        Initialise un nouvel objet CollectionCoherente avec les informations fournies

    ajouter_manga(self, manga: Manga)
        Ajoute un objet Manga à la collection

    supprimer_manga(self, manga: Manga)
        Supprime un objet Manga de la collection s'il existe

    __str__(self) -> str
        Retourne une représentation en chaîne de caractères de la collection,
         en listant les titres des mangas qu'elle contient

    """

    def __init__(self,
                 id_collection: int,
                 Liste_manga: list[Serie_Manga],
                 num_dernier_acquis: int,
                 num_manquant: int,
                 status: str):
        """
        Initialise un nouvel objet CollectionCoherente
        """
        self.id_collection = id_collection
        self.Liste_manga = Liste_manga
        self.num_dernier_acquis = num_dernier_acquis
        self.num_manquant = num_manquant
        self.status = status

    def ajouter_manga(self, manga: Serie_Manga):
        """
        Ajoute un objet Manga à la collection
        """

        self.Liste_manga.append(manga)

    def supprimer_manga(self, manga: Serie_Manga):
        """
        Supprime un objet Manga de la collection s'il existe
        """

        i = 0
        Trouver = False
        while not Trouver and i < len(self.Liste_manga):
            if manga.id_manga == self.Liste_manga[i].id_manga:
                Trouver = True
            else:
                i = i + 1
        if Trouver:
            del self.Liste_manga[i]
        else:
            print("Manga non présent dans la collection ")

    def __str__(self):
        """
        Retourne une représentation en chaîne de caractères de la collection
        """

        Texte_Liste_Titre_Manga = ""
        for i in range(0, len(self.Liste_manga)):
            Texte_Liste_Titre_Manga = Texte_Liste_Titre_Manga + self.Liste_manga[i].titre + ","
        return "Voici les mangas présents dans cette collection : "
        + Texte_Liste_Titre_Manga.strip(', ')