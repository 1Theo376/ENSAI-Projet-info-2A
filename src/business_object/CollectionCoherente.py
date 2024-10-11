from Manga import Manga

class CollectionCoherente:
    def __init__(self, id_collection: int, titre_collection: str, desc_collection: str, Liste_manga: list[Manga]):
        self.id_collection = id_collection
        self.titre_collection = titre_collection
        self. desc_collection = desc_collection
        self.Liste_manga = Liste_manga

    def ajouter_manga(self, manga: Manga):
        self.Liste_manga.append(manga)

    def supprimer_manga(self, manga: Manga):
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
        Texte_Liste_Titre_Manga = ""
        for i in range(0, len(self.Liste_manga)):
            Texte_Liste_Titre_Manga = Texte_Liste_Titre_Manga + self.Liste_manga[i].titre + ","
        return "Voici les mangas présents dans cette collection : " + Texte_Liste_Titre_Manga.strip(', ')