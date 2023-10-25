# Fonction pour vérifier si un ID de boîte contient exactement n occurrences d'une lettre
def a_exactly_n_lettres(box_id, n):
    # Dictionnaire pour stocker le nombre d'occurrences de chaque lettre
    lettres_compte = {}
    for lettre in box_id:
        # Incrémente le compteur pour chaque lettre dans l'ID de la boîte
        lettres_compte[lettre] = lettres_compte.get(lettre, 0) + 1
    # Vérifie si au moins une lettre a exactement n occurrences
    return any(compte == n for compte in lettres_compte.values())

# Lecture de l'entrée du puzzle depuis un fichier nommé 'input.txt'
with open('day_2_input.txt', 'r') as fichier:
    # Création d'une liste contenant les ID de boîtes en supprimant les espaces en début et en fin de chaque ligne
    boites_ids = [ligne.strip() for ligne in fichier]

# Initialisation des compteurs pour les ID de boîtes avec exactement deux et trois lettres identiques
compte_deux = 0
compte_trois = 0

# Calcul du checksum
for box_id in boites_ids:
    if a_exactly_n_lettres(box_id, 2):
        compte_deux += 1
    if a_exactly_n_lettres(box_id, 3):
        compte_trois += 1

# Calcul du checksum final en multipliant le nombre d'ID de boîtes avec exactement deux et trois lettres identiques
checksum = compte_deux * compte_trois

# Affichage du checksum
print(checksum)
