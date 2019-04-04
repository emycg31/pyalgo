"""
    Algorithm #0.01
    Declare var
    Store some arithmetics into the var
    Display result
    Operands and Operators, functions

    @version 0.0.2
    Add two operands and replace compute method
"""
resultat = 0 # Définition de la variable
operande1 = -3
operande2 = 3
resultat = operande1 + operande2
print(resultat)

if resultat > 0: 
    print("Le résultat est positif")
elif resultat < 0: 
    print("Le résultat est négatif")
else:
    print("Le résultat est nul")
#print(resultat)

"""
Fin de l'algorithme
"""

"""
FUNCTION SETTING
"""
def addition(operande1, operande2):
    return operande1 + operande2

resultat = 0 # Définition de la variable
operande1 = -3
operande2 = 2
resultat = addition(5,3) #call function with two parameters
print(resultat)

"""
getLowerOf
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
    if firstVal < secondVal:
        return firstVal
    else:
        return secondVal

"""
getGreaterOf
return the geatest value of two params
"""
def getGreaterOf(firstVal, secondVal):
    if firstVal > secondVal:
        return firstVal
    else:
        return secondVal