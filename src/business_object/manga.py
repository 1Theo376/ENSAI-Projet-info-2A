class Manga:
    """
    Classe représentant un manga

    Attributs :
    ----------
    id_manga : int
        L'identifiant unique du manga.
    titre : str
        Le titre du manga.
    synopsis : str
        Un résumé ou une description du manga.
    auteurs : list[str]
        Les auteurs du manga.
    themes : list[str]
        Une liste de thèmes associés au manga (par exemple, aventure, drame).
    genre : list[str]
        Le genre principal du manga (par exemple, action, romance).
    """

    def __init__(
        self, titre: str, synopsis: str, auteur: str, themes: list[str], genre: str, id_manga=None
    ):
        """Initialise un objet Manga"""

        self.id_manga = id_manga
        self.titre = titre
        self.synopsis = synopsis
        self.auteur = auteur
        self.themes = themes
        self.genre = genre

    def __str__(self) -> str:
        """Affiche des informations du manga."""
        return (
            f"{self.titre} - Genre: {self.genre}, "
            f"Auteurs: {self.auteur}, "
            f"Theme : {self.themes}, "
            f"Synopsis : {self.synopsis}"
        )
