try:
    # Tente d'ouvrir le fichier 'day_1_input.txt'
    with open('day_1_input.txt') as file:
        result = 1  # Initialise le résultat
        tot = 0  # Initialise le total
        liste = []  # Initialise une liste pour stocker les totaux

        # Parcourt chaque ligne du fichier
        for line in file:
            line.rstrip()  # Supprime les espaces en fin de ligne (cette ligne n'affecte pas le résultat)
            result = int(line)  # Convertit la ligne en un entier et le stocke dans "result"

            # Calcule la masse requise en carburant
            while (result // 3) - 2 > 0:
                result = (int(result) // 3) - 2  # Calcule la masse du carburant nécessaire
                tot += result  # Ajoute la masse du carburant au total

            liste.append(tot)  # Ajoute le total à la liste
            tot = 0  # Réinitialise le total pour la prochaine itération

        print(sum(liste))  # Affiche la somme de tous les totaux

except FileNotFoundError:
    # Gère l'exception si le fichier n'a pas été trouvé
    print('Fichier non trouvé')
except IOError:
    # Gère l'exception en cas d'erreur d'ouverture du fichier
    print("Erreur d'ouverture de fichier")
