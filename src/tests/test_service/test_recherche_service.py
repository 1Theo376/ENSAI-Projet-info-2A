from unittest.mock import MagicMock
from service.recherche_service import RechercheService
# from dao.utilisateur_dao import UtilisateurDao
# from business_object.utilisateur import Utilisateur


class MockUtilisateurDao:
    def rechercher_tous_pseudo(self, pseudo):
        return []

def test_recherche_utilisateur_non():
    """Le pseudo n'est pas utilisé dans liste_utilisateurs"""

    # GIVEN
    pseudo = "mollusque"

    # Instanciation du mock pour UtilisateurDao
    utilisateur_dao_mock = MockUtilisateurDao()

    # Instanciation du service avec le mock
    service = RechercheService()
    service.utilisateur_dao = utilisateur_dao_mock  # Injection manuelle du mock

    # WHEN
    res = service.recherche_utilisateur(pseudo)

    # THEN
    assert res == "Aucun utilisateur trouvé pour le pseudo 'mollusque'."


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])



""" def test_recherche_utilisateur_non():
    Le pseudo n'est pas utilisé dans liste_utilisateurs

    # GIVEN
    pseudo = "mollusque"

    # WHEN
    res = RechercheService().recherche_utilisateur(pseudo)

    # THEN
    assert not res


if __name__ == "__main__":
    import pytest

    pytest.main([__file__]) """
