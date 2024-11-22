import logging
from InquirerPy import inquirer
from InquirerPy.validator import PasswordValidator
from vues.vue_abstraite import VueAbstraite
from service.utilisateur_service import UtilisateurService


class InscriptionVue(VueAbstraite):
    def choisir_menu(self):
        # Demande à l'utilisateur de saisir pseudo, mot de passe...
        pseudo = inquirer.text(message="Entrez votre pseudo : ").execute()
        logging.info(f"Pseudo : {pseudo} (length: {len(pseudo)})")

        if UtilisateurService().pseudo_deja_utilise(pseudo):
            from vues.accueil.accueil_vue import AccueilVue

            return AccueilVue(f"Le pseudo {pseudo} est déjà utilisé.")

        mdp = inquirer.secret(
            message="Entrez votre mot de passe : ",
            validate=PasswordValidator(
                length=8,
                cap=True,
                number=True,
                message="Au moins 8 caractères, incluant une majuscule et un chiffre",
            ),
        ).execute()

        # Appel du service pour creer le utilisateur
        utilisateur = UtilisateurService().creer_compte(pseudo, mdp)

        # Si l'utilisateur a été créé
        if utilisateur:
            message = (
                f"Votre compte {utilisateur.pseudo} a été créé. "
                "Vous pouvez maintenant vous connecter."
            )

        else:
            message = "Erreur de connexion (pseudo ou mot de passe invalide)"

        from vues.accueil.accueil_vue import AccueilVue

        return AccueilVue(message)
