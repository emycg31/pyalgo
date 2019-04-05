"""
@name motdepasse.py
@author Aélion
@version 1.0.0
    Algorithmique de génération aléatoire de mot de passe
"""

# Tableaux
tabLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
tabPonct = ["*",",",";","/","+","-",")","(","[","]"]
tabNumbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
tabMinletters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
tableauPrinc = [tabLetters, tabPonct, tabNumbers, tabMinletters]

from random import *
nbCaract = int(uniform(8,12))
print("Nombre de caractère :", nbCaract)

letter = str()
ponct = str()
number = str()
passwordtr = str()
passwordint = str()
passwordf = str()

# Déterminer les caractères obligatoires
indiceL = int(uniform(0,len(tableauPrinc[0])))
indiceP = int(uniform(0,len(tableauPrinc[1])))
indiceN = int(uniform(0,len(tableauPrinc[2])))

letter = tableauPrinc[0][indiceL]
ponct = tableauPrinc[1][indiceP]
number = tableauPrinc[2][indiceN]

print("Letter :", letter, "Ponct :", ponct, "Number :", number)

# Déterminer les caractères restants
if len(passwordtr) < nbCaract-3:
    for i in range(nbCaract-3):
        whichType = int(uniform(0,3))
        print("Choix du tableau :", whichType)
        #print("Tableau choisi :", tableauPrinc[whichType])
        indice = int(uniform(0,len(tableauPrinc[whichType])))
        #print("indice :", indice)
        #print(type(i))
        #print("Valeur :", val)
        val = tableauPrinc[whichType][indice]        
        #print("valeur choisie :", tableauPrinc[whichType][indice])
        passwordtr = passwordtr + val
print("Mot de passe tronqué :", passwordtr)

passwordint = passwordtr + letter + ponct + number
print("Mot de passe concaténé:", passwordint)

import random
passwordf = "".join(random.sample(passwordint,len(passwordint)))
print("Mot de passe final:", passwordf)