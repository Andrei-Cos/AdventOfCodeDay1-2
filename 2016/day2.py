# Fonction pour obtenir le code de toilettes en utilisant un clavier avec des caractères alphanumériques (version 2)
def ToilletHackV2(data):
    # Définition du clavier avec des caractères alphanumériques
    keypad = [
        ['0', '0', '1', '0', '0'],
        ['0', '2', '3', '4', '0'],
        ['5', '6', '7', '8', '9'],
        ['0', 'A', 'B', 'C', '0'],
        ['0', '0', 'D', '0', '0']
    ]

    position = (2, 0)  # Position de départ à '5'
    code = []  # Liste pour stocker le code

    for instruction in data:
        for move in instruction:
            if move == 'U' and position[0] > 0 and keypad[position[0] - 1][position[1]] != '0':
                position = (position[0] - 1, position[1])
            elif move == 'D' and position[0] < 4 and keypad[position[0] + 1][position[1]] != '0':
                position = (position[0] + 1, position[1])
            elif move == 'L' and position[1] > 0 and keypad[position[0]][position[1] - 1] != '0':
                position = (position[0], position[1] - 1)
            elif move == 'R' and position[1] < 4 and keypad[position[0]][position[1] + 1] != '0':
                position = (position[0], position[1] + 1)

        code.append(keypad[position[0]][position[1]])

    return ''.join(code)  # Renvoie le code sous forme de chaîne

# Fonction pour obtenir le code de toilettes en utilisant un clavier numérique standard (version 1)
def ToilletHack(data):
    # Définition du clavier numérique standard
    keypad = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]
    
    position = (1, 1)  # Position de départ à '5'
    code = []  # Liste pour stocker le code

    for instruction in data:
        for move in instruction:
            if move == 'U' and position[0] > 0:
                position = (position[0] - 1, position[1])
            elif move == 'D' and position[0] < 2:
                position = (position[0] + 1, position[1])
            elif move == 'L' and position[1] > 0:
                position = (position[0], position[1] - 1)
            elif move == 'R' and position[1] < 2:
                position = (position[0], position[1] + 1)

        code.append(keypad[position[0]][position[1]])

    return ''.join(code)  # Renvoie le code sous forme de chaîne

f = open("day_2_input.txt", "r")  # Ouverture du fichier d'entrée en mode lecture
data = f.readlines()  # Lecture de toutes les lignes du fichier dans une liste
for i in range(len(data)):
    data[i] = data[i].rstrip()  # Suppression des caractères de saut de ligne en fin de chaque ligne

# Appel de la fonction "ToilletHack" avec les données et affichage du résultat
print(ToilletHack(data))

# Appel de la fonction "ToilletHackV2" avec les données et affichage du résultat
print(ToilletHackV2(data))
