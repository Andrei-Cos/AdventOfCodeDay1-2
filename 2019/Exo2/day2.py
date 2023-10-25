def gravite(data, Part1):
    # Copie les données pour éviter de modifier les données d'origine
    data = data[:]

    if Part1:
        # Si c'est la première partie, initialise les valeurs de data[1] et data[2]
        data[1] = 12
        data[2] = 2

    for i in range(0, len(data), 4):
        opp = data[i]
        loc1 = data[i + 1]
        loc2 = data[i + 2]
        locF = data[i + 3]

        if opp == 99:
            # Si l'opcode est 99, retourne la valeur à l'indice 0
            return data[0]

        if opp == 1:
            # Si l'opcode est 1, additionne les valeurs à loc1 et loc2, puis stocke le résultat à locF
            data[locF] = data[loc1] + data[loc2]

        if opp == 2:
            # Si l'opcode est 2, multiplie les valeurs à loc1 et loc2, puis stocke le résultat à locF
            data[locF] = data[loc1] * data[loc2]

    return data[0]

if __name__ == "__main__":
    # Lecture des données depuis un fichier
    f = open('input_day_2.txt', 'r')
    fichier = f.readline()
    data = fichier.split(',')
    data[-1] = int(data[-1].rstrip())

    # Conversion des chaînes de caractères en entiers
    for i in range(len(data) - 1):
        data[i] = int(data[i])

    # Appel de la fonction gravite avec Part1=True
    print(gravite(data, True))

    # Partie 2
    for noun in range(100):
        for verb in range(100):
            # Réinitialisation des valeurs de data[1] et data[2] pour chaque combinaison de noun et verb
            data[1] = noun
            data[2] = verb

            # Appel de la fonction gravite avec Part1=False
            output = gravite(data, False)

            if output == 19690720:
                # Si la sortie correspond à la valeur recherchée, affiche le résultat
                print(100 * noun + verb)
                break
