# Fonction pour trouver les lettres communes entre deux ID de boîtes correctes
def trouver_lettres_communes(boites_ids):
    for i in range(len(boites_ids)):
        for j in range(i + 1, len(boites_ids)):
            # Initialise le compteur de caractères différents et la liste des lettres communes
            caracteres_differents = 0
            lettres_communes = []
            for k in range(len(boites_ids[i])):
                if boites_ids[i][k] != boites_ids[j][k]:
                    caracteres_differents += 1
                else:
                    lettres_communes.append(boites_ids[i][k])
            # Si une seule lettre est différente, renvoie les lettres communes sous forme de chaîne
            if caracteres_differents == 1:
                return ''.join(lettres_communes)
    return None

# Lecture de la liste des ID de boîtes depuis le fichier d'entrée
with open('day_2_input.txt', 'r') as fichier:
    boites_ids = [ligne.strip() for ligne in fichier]

# Recherche des lettres communes entre les deux ID de boîtes correctes
lettres_communes = trouver_lettres_communes(boites_ids)

# Affichage des lettres communes
print("Lettres communes dans les ID de boîtes correctes:", lettres_communes)
