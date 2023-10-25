# Définition d'une fonction "calib" qui calcule la somme des éléments dans la liste "data".
def calib(data):
    return sum(data)

# Définition d'une fonction "VraiCalib" qui recherche la première fréquence atteinte deux fois.
def VraiCalib(data):
    freq = 0  # Initialise la fréquence à zéro
    check = set()  # Crée un ensemble pour stocker les fréquences déjà vérifiées
    check.add(freq)  # Ajoute la fréquence initiale à l'ensemble
    i = 0  # Initialise un compteur pour parcourir la liste "data"

    while True:
        freq += data[i]  # Ajoute la valeur actuelle de "data" à la fréquence
        if freq in check:
            # Si la fréquence est déjà dans l'ensemble, retourne cette fréquence
            return freq
        check.add(freq)  # Ajoute la nouvelle fréquence à l'ensemble
        i = (i + 1) % len(data)  # Incrémente le compteur avec une boucle circulaire pour parcourir "data" de manière cyclique.

# Ouverture du fichier 'day_1_input.txt' en mode lecture
f = open('day_1_input.txt', "r")
data = f.readlines()  # Lecture de toutes les lignes du fichier dans une liste

# Conversion des éléments de la liste de chaînes de caractères en entiers
for i in range(len(data)):
    data[i] = int(data[i].rstrip())

# Appel de la fonction "calib" pour calculer la somme des valeurs dans "data" et l'afficher
print(calib(data))

# Appel de la fonction "VraiCalib" pour trouver la première fréquence atteinte deux fois et l'afficher
print(VraiCalib(data))
