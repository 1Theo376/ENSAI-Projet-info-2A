from collection_physique import Collection_physique
from collec import Collection
import csv


class Utilisateur:
    """
    Définition de la classe Utilisateur.

    Attributs
    ----------
    id: str
        identifiant rentré par l'utilisateur

    mdp: str
        mot de passe rentré par l'utilisateur

    collec_phys: Collection_physique
        La collection physique de l'utilisateur
    """
    def __init__(self, id: str, mdp: str, collec_phys: Collection_physique,
                 collections: list[Collection]):
        """
        Initialise une instance de Utilisateur
        """
        self.id = id
        self.mdp = mdp
        self.collec_phys = collec_phys
        self.collections = collections

    @staticmethod
    def creer_profil():
        """
        Demande à l'utilisateur d'entrer ses informations pour
        créer son compte

        Returns
        ----------
        Utilisateur
            une instance de Utilisateur avec les informations reçues
        """
        print("Entrez un nom d'utilisateur :")
        id = input()
        print("Entrez un mot de passe :")
        mdp = input()
        return Utilisateur(id, mdp, None, None)

    @staticmethod
    def identification(nom_fichier):
        """
        Demande à l'utilisateur son nom d'utilisateur et son mot de passe
        pour qu'il puisse se connecter et récupérer ses données.

        Parameters
        ----------
        nom_fichier : str
            le nom du fichier de sauvegarde

        Returns
        ----------
        Utilisateur
            une instance de Utilisateur avec les informations du fichier
            de sauvegarde
        """
        print("Quel est votre nom d'utilisateur ?")
        nom_utilisateur = input()
        try:
            with open('content/' + nom_fichier + '.csv', 'r',
                      newline='') as sauvegarde:
                reader = csv.reader(sauvegarde)
                for colonne in reader:
                    if colonne[0] == nom_utilisateur and colonne[1] == mdp:
                        print("Vous vous êtes bien identifié.")
                        return Utilisateur(colonne[0], colonne[1], colonne[2], colonne[3])
                print("Vous n'êtes pas incrit.")
                return -1

        except IOError:
            print("Une erreur s'est produite lors de l'identification")

    def enregistrer_profil(self, nom_fichier):
        """
        Enregistre l'utilisateur dans le fichier de sauvegarde lors de la
        création de son compte.

        Parameters
        ----------
        nom_fichier : str
            le nom du fichier de sauvegarde
        """
        try:
            with open('content/' + nom_fichier + '.csv', 'a',
                    newline='') as sauvegarde:
                writer = csv.writer(sauvegarde)
                writer.writerow([self.id, self.mdp, self.collec_phys, self.collections])
            print("Enregistrement terminée avec succès !")
        except IOError:
            print("Une erreur s'est produite lors de votre enregistrement")

        def sauvegarde_profil(self, nom_fichier):
            """
            Met a jour le fichier de sauvegarde en modifiant 
            les données de l'utilisateur

            Parameters
            ----------
            nom_fichier : str
                le nom du fichier de sauvegarde
            """
            try:
                with open('content/' + nom_fichier + '.csv', 'r',
                        newline='', encoding="latin-1") as sauvegarde:
                    lignes = []
                    reader = csv.reader(sauvegarde)
                    for ligne in reader:
                        if ligne[0] == self.nom_utilisateur and ligne[1] == self.mdp:
                            lignes.append([self.nom_utilisateur, self.nom,
                                           self.collec_phys, self.collections])
                        else:
                            lignes.append(ligne)
                with open('content/' + nom_fichier + '.csv', 'w',
                        newline='', encoding="latin-1") as sauvegarde:
                    writer = csv.writer(sauvegarde)
                    writer.writerows(lignes)
                print("Sauvegarde terminée avec succès !")
            except IOError:
                print("Une erreur s'est produite lors de la mise à jour")







    def creer_fichier_save():
        """
        Créé un fichier sauvegarde si il n'existe pas et spécifie les en-têtes
        """
        try:
            with open('content/sauvegarde.csv', 'a',
                    newline='') as sauvegarde:
                writer = csv.writer(sauvegarde)
                writer.writerow(["nom_utilisateur", "mdp", "collection_physique",
                                 "collections"])
            print("fichier et en-tete créé avec succes")
        except IOError:
            print("Une erreur s'est produite lors de la creation du fichier")

    def supprimer_contenu_save():
        """
        Supprime tout le contenu du fichier save (il devient un fichier vide)
        """
        try:
            with open('content/sauvegarde.csv', 'w') as sauvegarde:
                sauvegarde.write('')
            print("fichier supprimé")
        except IOError:
            print("Une erreur s'est produite lors de la suppresion du contenu")