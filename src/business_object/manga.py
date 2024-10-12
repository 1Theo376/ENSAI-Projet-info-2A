class Manga:
    def __init__(self,
                 id_manga: int,
                 titre: str,
                 synopsis: str,
                 auteurs: str,
                 themes: list[str],
                 genre: str):
        self.id_manga = id_manga
        self.titre = titre
        self.synopsis = synopsis
        self.auteurs = auteurs
        self.themes = themes
        self.genre = genre

    def __str__(self) -> str:
        return f"{self.titre} - Genre: {self.genre}, Auteurs: {self.auteurs}"
