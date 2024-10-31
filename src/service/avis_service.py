from business_object.avis import Avis
from dao.avis_dao import AvisDAO


class AvisService:
    """Classe contenant les méthodes de service des avis"""

    def rediger_avis(self, texte, id_avis):
        """Rédaction d'un avis
        Parameters
        ----------
        texte : str

        Returns
        --------
        Avis rédigé
        """

        if not texte or len(texte.strip()) == 0:
            raise ValueError("Ce n'est pas une description")

        nouvel_avis = Avis(id_avis=id_avis, texte=texte)

        return nouvel_avis if AvisDAO().creer_avis(nouvel_avis) else None

    def supprimer_avis(self, avis):
        """Suppression d'un avis"""
        return self.dao.avis_dao.supprimer_avis(avis)

    def afficher_avis_pagination(self, id_utilisateur, page_suivante=False):
        """Affiche les avis d'un utilisateur avec pagination"""
        if page_suivante:
            self.current_page += 1
        avis_utilisateur = self.recuperer_avis_utilisateur(id_utilisateur)
        total_avis = len(avis_utilisateur)
        if total_avis == 0:
            print("Aucun avis disponible pour cet utilisateur.")
            return
        start_index = self.current_page * self.page_size
        end_index = min(start_index + self.page_size, total_avis)
        # Affichage des avis pour la page courante
        for i in range(start_index, end_index):
            print(f"{i + 1}. {avis_utilisateur[i]}")
        print(f"\nAffichage des avis {start_index + 1} à {end_index} sur {total_avis}.\n")

    def recuperer_avis_utilisateur(self, id_utilisateur):
        """Simule la récupération des avis d'un utilisateur"""
        # Simuler une liste d'avis pour l'exemple
        return [f"Avis {i} de l'utilisateur {id_utilisateur}" for i in range(1, 21)]
