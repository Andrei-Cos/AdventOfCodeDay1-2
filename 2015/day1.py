# Fonction pour résoudre le problème de l'équilibre des parenthèses (version 2)
def NQLV2(data):
    tot = 0  # Initialise la variable "tot" à 0

    for i in range(len(data)):
        if data[i] == ")":
            tot -= 1  # Si une parenthèse fermante est trouvée, décrémente "tot"
        else:
            tot += 1  # Sinon, incrémente "tot"

        if tot < 0:
            return i + 1  # Si "tot" devient négatif, renvoie la position actuelle + 1

# Fonction pour résoudre le problème de l'équilibre des parenthèses (version 1)
def NQL(data):
    tot = 0  # Initialise la variable "tot" à 0

    for i in range(len(data)):
        if data[i] == ")":
            tot -= 1  # Si une parenthèse fermante est trouvée, décrémente "tot"
        else:
            tot += 1  # Sinon, incrémente "tot"

    return tot  # Renvoie la valeur finale de "tot"

f = open("day_1_input.txt", "r")  # Ouverture du fichier d'entrée en mode lecture
data = f.readline()  # Lecture de la première ligne du fichier

# Appel de la fonction "NQL" avec les données et affichage du résultat
print(NQL(data))

# Appel de la fonction "NQLV2" avec les données et affichage du résultat
print(NQLV2(data))
