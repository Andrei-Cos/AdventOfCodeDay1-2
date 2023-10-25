def Trouver2020(depenses):
    e1 = None  # Initialise les variables e1 et e2 à None
    e2 = None
    for i in range(len(depenses)):
        for j in range(len(depenses)):
            if depenses[i] != depenses[j]:  # Vérifie que les deux dépenses sont différentes
                if depenses[i] + depenses[j] == 2020:  # Vérifie si la somme de deux dépenses est égale à 2020
                    e1 = depenses[i]  # Stocke la première dépense
                    e2 = depenses[j]  # Stocke la deuxième dépense
    return e1 * e2  # Retourne le produit des deux dépenses trouvées

def Trouver2020V2(depenses):
    e1 = None  # Initialise les variables e1, e2 et e3 à None
    e2 = None
    e3 = None
    
    for i in range(len(depenses)):
        for j in range(len(depenses)):
            for t in range(len(depenses)):
                if depenses[i] != depenses[j] and depenses[i] != depenses[t] and depenses[j] != depenses[t]:  # Vérifie que les trois dépenses sont toutes différentes
                    if depenses[i] + depenses[j] + depenses[t] == 2020:  # Vérifie si la somme des trois dépenses est égale à 2020
                        e1 = depenses[i]  # Stocke la première dépense
                        e2 = depenses[j]  # Stocke la deuxième dépense
                        e3 = depenses[t]  # Stocke la troisième dépense
    return e1 * e2 * e3  # Retourne le produit des trois dépenses trouvées

f = open('day_1_input.txt', "r")  # Ouvre le fichier 'day_1_input.txt' en mode lecture
depenses = f.readlines()  # Lit les lignes du fichier et les stocke dans la liste 'depenses'
for i in range(len(depenses)):
    depenses[i] = int(depenses[i].rstrip())  # Convertit les éléments de la liste en entiers

# Appelle la fonction Trouver2020 pour trouver deux dépenses qui totalisent 2020 et affiche le résultat
print(Trouver2020(depenses))

# Appelle la fonction Trouver2020V2 pour trouver trois dépenses qui totalisent 2020 et affiche le résultat
print(Trouver2020V2(depenses))
