# Fonction pour résoudre le captcha (version 1)
def captchat(data):
    somme = 0  # Initialise la somme à zéro

    # Parcourt la liste de données jusqu'à l'avant-dernier élément
    for i in range(len(data) - 1):
        # Vérifie si l'élément actuel est égal à l'élément suivant
        if data[i] == data[i + 1]:
            somme += data[i]  # Ajoute l'élément actuel à la somme

    # Vérifie si le dernier élément est égal au premier
    if data[-1] == data[0]:
        somme += data[0]  # Ajoute le premier élément à la somme

    return somme  # Renvoie la somme des éléments

# Fonction pour résoudre le captcha (version 2)
def captchatV2(data):
    somme = 0  # Initialise la somme à zéro

    # Vérifie si la longueur de la liste de données est impair
    if len(data) % 2 == 1:
        data.append(0)  # Ajoute un zéro pour rendre la longueur paire

    step = int(len(data) / 2)  # Calcule le pas pour la deuxième partie des données

    # Parcourt la liste de données
    for i in range(len(data) - step):
        # Vérifie si l'élément actuel est égal à l'élément avec un décalage de "step"
        if data[i] == data[i + step]:
            somme += data[i]  # Ajoute l'élément actuel à la somme

    # Parcourt la première moitié des données (décalage de "step" à partir de la fin)
    for j in range(step):
        # Vérifie si l'élément actuel est égal à l'élément correspondant dans la deuxième moitié
        if data[-step + j] == data[j]:
            somme += data[j]  # Ajoute l'élément actuel à la somme

    return somme  # Renvoie la somme des éléments

f = open("day_1_input.txt", "r")  # Ouverture du fichier d'entrée en mode lecture
data = f.readline()  # Lecture de la première ligne du fichier

liste = []

# Parcourt les caractères de la ligne lue et les convertit en entiers, puis les ajoute à la liste "liste"
for i in range(len(data)):
    liste.append(int(data[i]))

# Appel de la fonction captchat avec la liste de données pour la version 1 et affichage du résultat
print(captchat(liste))

# Appel de la fonction captchatV2 avec la liste de données pour la version 2 et affichage du résultat
print(captchatV2(liste))
