"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins counter
"""
somme = 460
billet100 = somme    // 100
reste100  = somme    %  100
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


listeBillet = [billet100, billet50, billet20, billet10, billet5, piece2, piece1]
listeChaine = ["","","","","","",""]
listeMontant = [100, 50, 20, 10, 5, 2, 1]

for i in range(7):
    if listeBillet[i] == 1:
        listeChaine[i] = str(listeBillet[i]) + " billet de " + str(listeMontant[i])
    elif listeBillet[i] == 0:
        listeChaine[i] = ""
    else:
        listeChaine[i] = str(listeBillet[i]) + " billets de " + str(listeMontant[i])

print("Veuillez retirer : ")
for i in range(7):
    if listeChaine[i] != "":
        print(listeChaine[i])


