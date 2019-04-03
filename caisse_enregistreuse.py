"""
@name caisse_enregistreuse.py
@author Aélion
@version 0.0.1
A poor coins counter 2
"""
sommeAttendue = 957
sommePayee = 1000
sommeRendue = sommePayee - sommeAttendue

billet100 = sommeRendue    // 100
reste100  = sommeRendue    %  100
billet50  = reste100 // 50
reste50   = reste100 %  50
billet20  = reste50  // 20
reste20   = reste50  %  20
billet10  = reste20  // 10
reste10   = reste20  %  10
billet5   = reste10  // 5
reste5    = reste10  %  5
piece2    = reste5   // 2
piece1    = reste5   %  2

listeBillet = [billet100, billet50, billet20, billet10, billet5]
listeChaineB = ["","","","",""]
listeMontantB = [100, 50, 20, 10, 5]

for i in range(5):
    if listeBillet[i] == 1:
        listeChaineB[i] = str(listeBillet[i]) + " billet de " + str(listeMontantB[i])
    elif listeBillet[i] == 0:
        listeChaineB[i] = ""
    else:
        listeChaineB[i] = str(listeBillet[i]) + " billets de " + str(listeMontantB[i])


listePiece = [piece2, piece1]
listeChaineP = ["",""]
listeMontantP = [2, 1]

for i in range(2):
    if listePiece[i] == 1:
        listeChaineP[i] = str(listePiece[i]) + " pièce de " + str(listeMontantP[i])
    elif listePiece[i] == 0:
        listeChaineP[i] = ""
    else:
        listeChaineP[i] = str(listePiece[i]) + " pièces de " + str(listeMontantP[i])


print("Nous vous rendons : ")
for i in range(5):
    if listeChaineB[i] != "":
        print(listeChaineB[i])
for i in range(2):
    if listeChaineP[i] != "":
        print(listeChaineP[i])
print("Merci de votre visite")