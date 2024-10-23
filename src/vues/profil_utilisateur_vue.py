from InquirerPy import inquirer

from vues.vue_abstraite import VueAbstraite
from vues.session import Session

class ProfilUtilisateurVue(VueAbstraite):
     """Vue de l'écran du profil

    Returns
    ------
    view
        retourne la prochaine vue, celle qui est choisie par l'utilisateur
    """
    
    def choisir_menu(self):
