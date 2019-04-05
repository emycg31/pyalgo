"""
@name motdepasse.py
@author Aélion
@version 1.0.0
    Algorithmique de génération aléatoire de mot de passe
@contrainte1 : min 8 caractères, max 12
@contrainte2 : au moins 1 lettre majuscule
@contrainte3 : au moins 1 caractère de ponctuation
@contrainte4 : 1 chiffre

"""

# Tableaux
tabLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
tabPonct = ["*",",",";","/","+","-",")","(","[","]"]
tabNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tabMinletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
tableauPrinc = [tabLetters, tabPonct, tabNumbers, tabMinletters]

import random

# Choix de la longueur du mot de passe
nbCaract = random.randint(8,12)
print("Nombre de caractère :", nbCaract)

letter = str()
ponct = str()
number = str()
passwordtr = str()
passwordint = str()
passwordf = str()

# Déterminer les caractères obligatoires
indiceL = random.randint(0,len(tableauPrinc[0])-1)
indiceP = random.randint(0,len(tableauPrinc[1]))-1
indiceN = random.randint(0,len(tableauPrinc[2])-1)

letter = tableauPrinc[0][indiceL]
ponct = tableauPrinc[1][indiceP]
number = tableauPrinc[2][indiceN]

print("Letter :", letter, "Ponct :", ponct, "Number :", number)

# Déterminer les caractères restants
if len(passwordtr) < nbCaract-3:
    for i in range(nbCaract-3):
        whichType = random.randint(0,3)
        print("Choix du tableau :", whichType)
        #print("Tableau choisi :", tableauPrinc[whichType])
        indice = random.randint(0,len(tableauPrinc[whichType])-1)
        #print("indice :", indice)
        #print(type(i))
        #print("Valeur :", val)
        val = tableauPrinc[whichType][indice]        
        #print("valeur choisie :", tableauPrinc[whichType][indice])
        passwordtr = passwordtr + val
print("Mot de passe tronqué :", passwordtr)

# Concaténation des caractères obligatoires et non obligatoires
passwordint = passwordtr + letter + ponct + number
print("Mot de passe concaténé:", passwordint)

# Mélange de tous les caractères respectant les contraintes
passwordf = "".join(random.sample(passwordint,len(passwordint)))
print("Mot de passe final:", passwordf)