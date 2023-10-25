def verif(mdps):
    isvalid = 0  # Cette variable comptera le nombre de mots de passe valides.
    
    for i in range(len(mdps)):
        elem = mdps[i]  # Prend un élément de la liste 'mdps' (un mot de passe).
        partie = elem.split()  # Divise l'élément en trois parties (nombres, lettre, texte).
        nombres = partie[0]  # La première partie contient les nombres.
        lettre = partie[1][0]  # La deuxième partie contient la lettre (premier caractère).
        text = partie[2]  # La troisième partie contient le texte du mot de passe.
        
        bornes = nombres.split('-')  # Divise la chaîne des nombres en bornes minimale et maximale.
        borneMin = int(bornes[0])  # Convertit la borne minimale en entier.
        borneMax = int(bornes[1])  # Convertit la borne maximale en entier.
        
        # Vérifie si le nombre d'occurrences de 'lettre' dans 'text' est compris entre borneMin et borneMax.
        if text.count(lettre) >= borneMin and text.count(lettre) <= borneMax:
            isvalid += 1  # Incrémente le compteur si le mot de passe est valide.
    
    return isvalid  # Renvoie le nombre total de mots de passe valides.
def NewVerif(mdps):
    isvalid = 0  # Cette variable comptera le nombre de mots de passe valides.

    for i in range(len(mdps)):
        elem = mdps[i]  # Prend un élément de la liste 'mdps' (un mot de passe avec sa politique).
        partie = elem.split()  # Divise l'élément en trois parties (positions, lettre, et texte).
        positions = partie[0]  # La première partie contient les positions.
        lettre = partie[1][0]  # La deuxième partie contient la lettre (premier caractère).
        text = partie[2]  # La troisième partie contient le texte du mot de passe.

        positions = positions.split('-')  # Divise les positions en deux positions.
        pos1 = int(positions[0])  # Convertit la première position en entier.
        pos2 = int(positions[1])  # Convertit la deuxième position en entier.

        # Vérifie si exactement l'une des positions spécifiées contient la lettre donnée.
        if (text[pos1 - 1] == lettre) ^ (text[pos2 - 1] == lettre):
            isvalid += 1  # Incrémente le compteur si le mot de passe est valide.

    return isvalid  # Renvoie le nombre total de mots de passe valides.


# Ouvre le fichier 'day_2_input.txt' en mode lecture
f = open('day_2_input.txt', "r")

# Lit les lignes du fichier et les stocke dans la liste 'mdps'
mdps = f.readlines()

# Supprime les caractères de nouvelle ligne ("\n") de chaque élément de la liste 'mdps'
for i in range(len(mdps)):
    mdps[i] = mdps[i].rstrip()

# Appelle la fonction 'verif' pour vérifier les mots de passe et stocke le résultat dans 'isvalid'
isvalid1 = verif(mdps)
isvalid2=NewVerif(mdps)

# Affiche le nombre total de mots de passe valides
print(isvalid1)
print(isvalid2)