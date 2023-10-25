def fuelcacl(fuel):
    return (fuel//3)-2


def conmpteurEssence(conso):
    for i in range(len(conso)):
        conso[i]=fuelcacl(conso[i])
    return sum(conso)
        







f = open('day_1_input.txt', "r")  # Ouvre le fichier 'day_1_input.txt' en mode lecture
conso = f.readlines()  # Lit les lignes du fichier et les stocke dans la liste 'conso'

for i in range(len(conso)):
    conso[i] = int(conso[i].rstrip())  # Convertit les éléments de la liste en entiers


#print(conso)
print(conmpteurEssence(conso))


