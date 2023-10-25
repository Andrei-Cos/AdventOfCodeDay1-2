# Définition de la fonction 'Depth' pour calculer le nombre d'augmentations successives dans une liste 'radar'.
def Depth(radar):
    increase = 0  # Initialise un compteur d'augmentations à zéro.

    # Parcourt la liste 'radar' à partir du deuxième élément (le premier n'ayant pas de précédent).
    for i in range(1, len(radar)):
        # Si la valeur actuelle est plus grande que la valeur précédente, cela signifie qu'il y a une augmentation.
        if radar[i] > radar[i - 1]:
            increase += 1  # Incrémente le compteur d'augmentations.

    return increase  # Renvoie le nombre total d'augmentations.

# Définition de la fonction 'RefineRadar' pour affiner une liste 'radar' en ajoutant la somme de chaque élément et des deux éléments suivants.
def RefineRadar(radar):
    newRadar = []  # Initialise une nouvelle liste qui prendra les nouvelles valeurs.

    # Parcourt la liste 'radar'.
    for i in range(len(radar)):
        # Ajoute à la nouvelle liste la somme de la position actuelle jusqu'au troisième élément qui suit.
        newRadar.append(sum(radar[i:i + 3]))

    return newRadar  # Renvoie la liste 'radar' raffinée.

if __name__ == "__main__":
    f = open('day_1_input.txt', "r")  # Ouvre le fichier 'day_1_input.txt' en mode lecture.
    radar = f.readlines()  # Lit les lignes du fichier et les stocke dans la liste 'radar'.

    # Parcourt la liste 'radar' pour enlever les caractères de nouvelle ligne ("\n") et convertir les éléments en entiers.
    for i in range(len(radar)):
        radar[i] = int(radar[i].rstrip())

    # Appelle la fonction 'Depth' pour calculer le nombre d'augmentations dans la liste 'radar' et l'affiche.
    print(Depth(radar))

    # Rafine la liste 'radar' en appelant la fonction 'RefineRadar'.
    betterradar = RefineRadar(radar)

    # Réutilise la fonction 'Depth' pour calculer le nombre d'augmentations dans la liste raffinée et l'affiche.
    print(Depth(betterradar))
