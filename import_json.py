import requests
import json
import time


def get_mangas():
    """
    Ajoute tous les mangas avec les informations voulues dans un fichier json
    """
    limit = 20
    page = 1
    mangas = []
    has_next_page = True
    while has_next_page:
        try:
            req = requests.get(f"https://api.jikan.moe/v4/manga?limit={limit}&page={page}")
        except requests.exceptions.RequestException as e:
            raise Exception(f"Request error: {e}")

        # Si la réponse est 429 (rate limiting), attendre quelques secondes
        if req.status_code == 429:
            print("Rate limit reached. Waiting for 10 seconds before retrying...")
            time.sleep(1)
            continue  # Refaire la requête après l'attente
        if req.status_code != 200:
            raise Exception(f"Cannot reach (HTTP {req.status_code}): {req.text}")
        data = req.json()
        raw_manga = data["data"]
        for t in raw_manga:
            liste = []
            liste.append(t.get("title_english", "N/A"))
            liste.append(t.get("volumes", "N/A"))
            liste.append(t.get("status", "N/A"))
            liste.append(t.get("published", {}))
            liste.append(t.get("synopsis", "N/A"))
            liste.append([manga["name"] for manga in t.get("authors", [])])
            liste.append([manga["name"] for manga in t.get("genres", [])])
            liste.append([manga["name"] for manga in t.get("demographics", [])])
            mangas.append(liste)
        has_next_page = data["pagination"]["has_next_page"]
        page += 1
        time.sleep(1)

    # Sauvegarder les résultats dans un fichier JSON
    with open("mangas.json", "w") as fichier:
        json.dump(mangas, fichier, indent=4)


get_mangas()
