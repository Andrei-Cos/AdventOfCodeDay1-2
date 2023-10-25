# Fonction pour trouver l'emplacement visité deux fois en premier
def find_first_visited_twice_location(parcours):
    x, y = 0, 0  # Initialisation des coordonnées à (0, 0)
    direction = 0  # 0: Nord, 1: Est, 2: Sud, 3: Ouest

    visited = set()  # Crée un ensemble pour stocker les emplacements visités
    for instruction in parcours:
        sense = instruction[1]  # Récupère le sens (R pour droite, L pour gauche)
        long = int(instruction[2:])  # Récupère la longueur de déplacement

        # Met à jour la direction (tourne à droite si sense est "R" et à gauche sinon)
        direction = (direction + 1) % 4 if sense == "R" else (direction - 1) % 4

        # Effectue le déplacement en mettant à jour les coordonnées
        for _ in range(long):
            if direction == 0:  # Nord
                y += 1
            elif direction == 1:  # Est
                x += 1
            elif direction == 2:  # Sud
                y -= 1
            else:  # Ouest
                x -= 1

            # Vérifie si l'emplacement est déjà dans l'ensemble "visited"
            if (x, y) in visited:
                return abs(x) + abs(y)  # Retourne la somme de la distance absolue

            visited.add((x, y))  # Ajoute l'emplacement à l'ensemble "visited"

# Fonction pour calculer la distance totale parcourue
def course(parcours):
    """
    J'ai un peu triché parce le fichier txt puait la merde et qu'on a des espaces apres toutes les ","
    mais on en a pas dans le premier element du coup tout le code est fucked up 
    donc j'ai triché en ajoutant un espace juste devant le premier elem histoire pas devoir tout changer
    """
    x, y = 0, 0  # Initialisation des coordonnées à (0, 0)
    direction = 0  # 0: Nord, 1: Est, 2: Sud, 3: Ouest

    for i in range(len(parcours)):
        sense = parcours[i][1]  # Récupère le sens (R pour droite, L pour gauche)
        long = int(parcours[i][2:])  # Récupère la longueur de déplacement

        # Met à jour la direction (tourne à droite si sense est "R" et à gauche sinon)
        if sense == "R":
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

        # Effectue le déplacement en mettant à jour les coordonnées
        if direction == 0:  # Nord
            y += long
        elif direction == 1:  # Est
            x += long
        elif direction == 2:  # Sud
            y -= long
        else:  # Ouest
            x -= long

    return abs(x) + abs(y)  # Retourne la somme de la distance absolue

f = open('day_1_input.txt', 'r')  # Ouverture du fichier d'entrée en mode lecture
parcours = f.readline()  # Lecture de la première ligne du fichier
parcours = parcours.split(',')  # Division de la ligne en instructions (séparées par une virgule)

# Appel de la fonction "course" pour calculer la distance totale parcourue et affichage du résultat
print(course(parcours))

# Appel de la fonction "find_first_visited_twice_location" pour trouver l'emplacement visité deux fois en premier
# et affichage de la distance à cet emplacement
print(find_first_visited_twice_location(parcours))
