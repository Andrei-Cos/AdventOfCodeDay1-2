# Définition de la fonction 'cleanlist' pour nettoyer une liste de valeurs.
def cleanlist(OldList):
    newlist = []  # Initialise une nouvelle liste pour stocker les valeurs nettoyées.
    cpt = 0  # Initialise un compteur à zéro pour calculer les valeurs actuelles.

    # Boucle 'for' parcourant la liste 'OldList'.
    for i in range(len(OldList)):
        if OldList[i] != "\n":  # Si l'élément n'est pas une ligne vide.
            cpt += int(OldList[i].rstrip())  # Ajoute la valeur à 'cpt' après avoir supprimé le caractère de nouvelle ligne ('\n').
        else:
            """
            Si on trouve une ligne vide, cela signifie qu'il faut calculer un nouvel ensemble.
            On ajoute la valeur actuelle dans 'newlist' et réinitialise 'cpt' à zéro pour calculer le prochain ensemble.
            """
            newlist.append(cpt)
            cpt = 0

    return newlist  # Renvoie la liste nettoyée.

# Définition de la fonction 'Top3' pour trouver la somme des trois plus grandes valeurs dans une liste.
def Top3(Nouvelle_liste):
    Liste_triée = Nouvelle_liste.sort()  # Trie la liste pour avoir les éléments les plus grands à la fin.
    return sum(Nouvelle_liste[-3:])  # Calcule la somme des trois derniers éléments, qui sont les plus grands.

f = open('day_1_input.txt', "r")  # Ouvre le fichier 'day_1_input.txt' en mode lecture.
Vielle_liste = f.readlines()  # Lit les lignes du fichier et les stocke dans la liste 'Vielle_liste'.

Nouvelle_liste = cleanlist(Vielle_liste)  # Appelle la fonction 'cleanlist' pour nettoyer la liste de valeurs.

def ElfList(Nouvelle_liste):
    """
    Renvoie une liste avec tout ce que chaque elfe.
    De type : L'efle 1 a fait un repas de 123 calories.
    """
    ElfList = []
    for i in range(len(Nouvelle_liste)):
        ElfList.append("L'elfe " + str(i+1) + " a fait un repas de " + str(Nouvelle_liste[i]) + " calories.")
    return ElfList


print(Nouvelle_liste)
#Affiche la valeur du repas le plus calorique en utilisant la fonction 'max'.
print("L'elf qui a fait le repas le plus calorique a fait un repas de", max(Nouvelle_liste), "calories !")

# Affiche la somme des trois plus gros repas en utilisant la fonction 'Top3'.
print("Le total des trois plus gros repas est de", Top3(Nouvelle_liste), "calories")

#Affiche la liste des repas de chaque elfe.
for i in range(len(ElfList(Nouvelle_liste))):
    print(ElfList(Nouvelle_liste)[i])