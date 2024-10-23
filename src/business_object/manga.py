class Manga:
    """
    Représente un manga avec ses informations de base
    """

    def __init__(self,
                 id_manga: int,
                 titre: str,
                 synopsis: str,
                 auteur: str,
                 themes: list[str],
                 genre: str):
        """

        Initialise un manga

    Parameters :
    ----------
    id_manga : int
        L'identifiant unique du manga.
    titre : str
        Le titre du manga.
    synopsis : str
        Un résumé ou une description du manga.
    auteurs : str
        Les auteurs du manga.
    themes : list[str]
        Une liste de thèmes associés au manga (par exemple, aventure, drame).
    genre : str
        Le genre principal du manga (par exemple, action, romance).

        """

        self.id_manga = id_manga
        self.titre = titre
        self.synopsis = synopsis
        self.auteur = auteur
        self.themes = themes
        self.genre = genre

    def __str__(self) -> str:
        """
        Retourne une représentation en chaîne de caractères du manga.

        Return : str
        -------
            Une chaîne de caractères formatée contenant le titre, le genre et les auteurs du manga.
        """
        return f"{self.titre} - Genre: {self.genre}, Auteurs: {self.auteur}"
