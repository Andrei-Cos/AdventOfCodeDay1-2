# Fonction pour calculer la quantité de ruban nécessaire (version "Ribbon")
def Ribbon(data):
    tot = 0  # Initialise le total à 0

    for i in range(len(data)):
        qte = data[i].split("x")  # Divise la chaîne en trois dimensions (longueur, largeur, hauteur)
        l = int(qte[0])  # Convertit la longueur en entier
        w = int(qte[1])  # Convertit la largeur en entier
        h = int(qte[2])  # Convertit la hauteur en entier

        # Calcule le périmètre du plus petit rectangle qui entoure le cadeau
        peri = 2 * (l + w + h - max(l, w, h))

        # Calcule la quantité de ruban nécessaire
        rubban = l * w * h

        tot += peri + rubban  # Ajoute le périmètre et la quantité de ruban au total

    return tot  # Renvoie le total

# Fonction pour calculer la quantité de papier nécessaire (version "Papier")
def Papier(data):
    tot = 0  # Initialise le total à 0

    for i in range(len(data)):
        qte = data[i].split("x")  # Divise la chaîne en trois dimensions (longueur, largeur, hauteur)
        l = int(qte[0])  # Convertit la longueur en entier
        w = int(qte[1])  # Convertit la largeur en entier
        h = int(qte[2])  # Convertit la hauteur en entier

        # Calcule les aires de chaque face du cadeau
        commande = [l * w, w * h, h * l]

        # Trouve la plus petite de ces aires (nécessaire pour calculer la quantité de papier)
        small = min(commande)

        # Calcule la quantité de papier nécessaire (surface des faces + la plus petite aire)
        tot += (2 * commande[0] + 2 * commande[1] + 2 * commande[2]) + small

    return tot  # Renvoie le total

f = open('day_2_input.txt', 'r')  # Ouverture du fichier d'entrée en mode lecture
data = f.readlines()  # Lecture de toutes les lignes du fichier dans une liste

for i in range(len(data)):
    data[i] = data[i].rstrip()  # Suppression des caractères de saut de ligne en fin de chaque ligne

# Appel de la fonction "Papier" avec les données et affichage du résultat
print(Papier(data))

# Appel de la fonction "Ribbon" avec les données et affichage du résultat
print(Ribbon(data))
