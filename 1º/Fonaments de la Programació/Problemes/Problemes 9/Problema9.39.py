
Dict = {}
nom = 2
llista = []
s = 0
while nom != str(-1):
    nom = input("Introdueix el nom: ")
    if nom == str(-1):
        break
    if nom in Dict:
        Dict[nom] += 1
       
    else:
        Dict[nom] = 1
        llista.append(nom)
     
    
print("ESCRUTINI")
for x in Dict:
    print(x,Dict[x])
    
notes = Dict.values()

maxim = max(notes)



res = 0
a = 0
for i in Dict:
    if maxim == Dict[i]:
        res = a
        break
    a += 1


claus = Dict.keys()
llista2 = []
for x in claus:
    llista2.append(x) 

print("Els CANDIDATS més votats amb",maxim,"han estat:",llista2[a])