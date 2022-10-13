

def funcio(fitxer):
    file = open(fitxer,"r")
    llista = []
    maxim = 0
    minim = 0
    suma = 0
    nom = 0
    for linia in file:
        i = 0
        for x in range(len(linia)):
            if linia[x] == " ":
                num = linia[i:x]
                nom += 1
                llista.append(num)
                i = x +1
                suma = suma + float(num) 
            elif x == (len(linia)-1):
                num = linia[i:]
                nom += 1
                llista.append(num)     
                suma = suma + float(num)
    maxim = max(llista)
    minim = min(llista)
    mitjana = suma/nom
    
    return minim,maxim,mitjana           

fitxer = input("Introdueix el nom del fitxer: ")
minim,maxim,mitjana = funcio(fitxer)
print("Mínim: "+str(minim)+", Màxim: "+str(maxim)+", Mitjana: "+str(mitjana))