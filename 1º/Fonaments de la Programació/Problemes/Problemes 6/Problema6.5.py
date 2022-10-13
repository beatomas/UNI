
nom = input("Introdueix el nom del fitxer: ")

fitxer = open(nom,"r")

for linia in fitxer:
    cont = 0
    print(linia)
    for i in linia:
        if i==" " or i=="\n":
            cont += 1
    print(cont)
    cont = 0            
            
            
    