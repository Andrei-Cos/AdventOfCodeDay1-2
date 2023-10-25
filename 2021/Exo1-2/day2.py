# Définition de la fonction 'trajet' pour calculer la position finale après un trajet.
def trajet(course):
    hor = 0  # Initialise la variable pour la position horizontale à 0.
    vert = 0  # Initialise la variable pour la position verticale à 0.

    # Parcourt la liste 'course'.
    for i in range(len(course)):
        if "forward" in course[i]:  # Si l'élément de la liste contient "forward".
            hor += int(course[i][-1])  # Ajoute à la variable horizontale le dernier caractère de l'élément (le chiffre).
        if "up" in course[i]:  # Si l'élément de la liste contient "up".
            vert -= int(course[i][-1])  # Soustrait de la variable verticale le dernier caractère de l'élément (le chiffre).
        if "down" in course[i]:  # Si l'élément de la liste contient "down".
            vert += int(course[i][-1])  # Ajoute à la variable verticale le dernier caractère de l'élément (le chiffre).

    return hor * vert  # Renvoie le produit de la position horizontale et verticale, comme demandé.

# Définition de la fonction 'trajetV2' pour calculer la position finale après un trajet avec une orientation variable.
def trajetV2(course):
    hor = 0  # Initialise la variable pour la position horizontale à 0.
    vert = 0  # Initialise la variable pour la position verticale à 0.
    aim = 0  # Initialise la variable pour l'orientation à 0.

    # Parcourt la liste 'course'.
    for i in range(len(course)):
        if "forward" in course[i]:  # Si l'élément de la liste contient "forward".
            hor += int(course[i][-1])  # Ajoute à la variable horizontale le dernier caractère de l'élément (le chiffre).
            vert += aim * int(course[i][-1])  # Modifie la variable verticale en fonction de l'orientation (aim) et de la distance parcourue.
        if "up" in course[i]:  # Si l'élément de la liste contient "up".
            aim -= int(course[i][-1])  # Diminue la valeur de l'orientation.
        if "down" in course[i]:  # Si l'élément de la liste contient "down".
            aim += int(course[i][-1])  # Augmente la valeur de l'orientation.

    return hor * vert  # Renvoie le produit de la position horizontale et verticale, comme demandé.

# Ouverture du fichier 'day_2_input.txt' en mode lecture.
f = open('day_2_input.txt', "r")
course = f.readlines()  # Lit les lignes du fichier et les stocke dans la liste 'course'.

# Parcourt la liste 'course' pour enlever les caractères de nouvelle ligne ("\n").
for i in range(len(course)):
    course[i] = course[i].rstrip()

# Appelle la fonction 'trajet' pour calculer la position finale avec le trajet standard et l'affiche.
print(trajet(course))

# Appelle la fonction 'trajetV2' pour calculer la position finale avec une orientation variable et l'affiche.
print(trajetV2(course))
