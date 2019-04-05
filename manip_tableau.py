"""
@name manip_tableau.py
@author Aélion
@version 1.0.0
    Algorithmique spécifique sur les collections
"""

# Déclaration du tableau de démonstration
monTableau = [15, 3, 25, 12, 7, -15]

#
# Simple poor loop
#
for indice, val in enumerate(monTableau):
    print(monTableau[indice] *2)

# More complex loop with condition
for indice, val in enumerate(monTableau):
    if indice % 2 == 0:
        print(monTableau[indice] *2)

# Autre exemple
indice = 0
for val in monTableau:
    if indice % 2 ==0:
        print(monTableau[indice]*2)
indice = indice +1

monTableau = [15, 3, 25, 12, 7, -15]

# Plus petite valeur du tableau
minDepart = monTableau[0]  #Initialiser une valeur de départ
print("INDICE", indice)
for val in monTableau[1:]: #Boucler à partir du deuxième élément
    if val < minDepart:    #Condition : lequel est le plus petit
        minDepart = val
        print(val)
print("La plus petite valeur est :", minDepart)

monTableau = [15, 3, 25, 12, 7, -15]

# Plus grande valeur du tableau
maxDepart = monTableau[0]  #Initialiser une valeur de départ
for val in monTableau[1:]: #Boucler à partir du deuxième élément
    if val > maxDepart:    #Condition : lequel est le plus grand
        maxDepart = val
        print(val)
        print(indice)
print("La plus grande valeur est :", maxDepart)

"""
getLowerOf
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal

# Plus petite valeur du tableau EXEMPLE AVEC FONCTION
minDepart = monTableau[0]  #Initialiser une valeur de départ
for val in monTableau[1:]: #Boucler à partir du deuxième élément
    minDepart = getLowerOf(minDepart, val)
print("La plus petite valeur est :", minDepart)

"""
getGreaterOf
return the geatest value of two params
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else:
        return secondVal

# Plus grande valeur du tableau
maxDepart = monTableau[0]  #Initialiser une valeur de départ
for val in monTableau[1:]: #Boucler à partir du deuxième élément
        maxDepart = getGreaterOf(maxDepart, val)
print("La plus grande valeur est :", maxDepart)

"""
COMPARE FUNCTION
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of two depends howTo params
"""

def compare1(firstVal, secondVal, howTo):
    if (howTo == "L"):
        return getLowerOf(firstVal, secondVal)
    
    return getGreaterOf(firstVal, secondVal)    

resultatc = compare1(4,9,"L")  
print(resultatc)

def compare2(firstVal, secondVal, desc=True):
    if (desc):
        return getLowerOf(firstVal, secondVal)
    
    return getGreaterOf(firstVal, secondVal)    

resultatp = compare2(4,9,)  
resultatg = compare2(4,9,False)  
print(resultatp)
print(resultatg)


"""
min function
@param anArray The array from which i want to get the min value
@return the min value of anArray
"""

def min(anArray):
    theMin = anArray[0]
    for value in anArray[1:]:
        theMin = compare(theMin, value)

    return theMin

"""
max function
@param anArray The array from which i want to get the max value
@return the max value of anArray
"""

def max(anArray):
    theMax = anArray[0]
    for value in anArray[1:]:
        theMax = compare(theMax, value, False)

    return theMax

print("La plus petite valeur est :", min(monTableau))
print("La plus grande valeur est :", max(monTableau))

"""
average function
@param anArray Array from which I want to get the average
@return the average value of anArray
"""

def average(anArray):
    total = 0
    for indice in range(len(monTableau)):
        total = total + monTableau[indice]
    average = total / len(monTableau)
    return average

print("La moyenne du tableau est :", average(monTableau))

"""
factorielle function
@param anArray Array from which I want to get the factorielle
@return la factorielle value of anArray
"""

def facto(anArray):
    facto = 1
    for indice in range(len(monTableau)):
        facto = facto * monTableau[indice]
    return facto

print("La factorielle du tableau est :", facto(monTableau))