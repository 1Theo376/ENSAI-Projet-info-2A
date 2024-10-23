from avis import Avis
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
