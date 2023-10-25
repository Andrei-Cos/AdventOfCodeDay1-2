# Fonction pour calculer la différence entre le maximum et le minimum de chaque ligne de la matrice
def minmax(matrice):
    tot = 0  # Initialise la somme totale à zéro

    # Parcourt chaque ligne de la matrice
    for i in range(len(matrice)):
        maxi = max(matrice[i])  # Trouve la valeur maximale dans la ligne
        mini = min(matrice[i])  # Trouve la valeur minimale dans la ligne
        tot += (maxi - mini)  # Ajoute la différence au total

    return tot  # Renvoie la somme totale des différences

# Fonction pour trouver la division exacte de chaque paire de nombres dans la matrice
def IsDiv(matrice):
    tot = 0  # Initialise la somme totale à zéro

    # Parcourt chaque ligne de la matrice
    for i in range(len(matrice)):#Parcourt les lignes
        for j in range(len(matrice[i])):#Parcourt les colonnes 
            for t in range(len(matrice[i])): #Compare tout les éléments de la meme ligne en eux pour trouver ceux qui sont divisibles entre eux
                nombre1 = matrice[i][j]
                nombre2 = matrice[i][t]
                # Vérifie si le nombre1 est divisible par le nombre2 et qu'ils ne sont pas égaux
                if nombre1 % nombre2 == 0 and nombre1 != nombre2:
                    tot += (nombre1 / nombre2)  # Ajoute le résultat de la division au total

    return tot  # Renvoie la somme totale des divisions exactes

f = open("day_2_input.txt", 'r')  # Ouverture du fichier d'entrée en mode lecture
fichier = f.read()  # Lecture de tout le contenu du fichier
lignes = fichier.split("\n")  # Divise le contenu en lignes en utilisant le saut de ligne comme séparateur

# Crée une matrice en parcourant chaque ligne, en divisant chaque élément et les convertissant en entiers
matrice = [[int(elem) for elem in ligne.split()] for ligne in lignes]
matrice.pop(-1)  # Supprime la dernière ligne vide

# Appel de la fonction minmax avec la matrice et affichage du résultat
print(minmax(matrice))

# Appel de la fonction IsDiv avec la matrice et affichage du résultat
print(IsDiv(matrice))
