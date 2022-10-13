

def funcio(fitxer,NIU):
    file = open(fitxer,"r")
    apuntador = 0
    trobat = 1
    num = 0
    cops = 0
    file.seek(apuntador)
    for linia in file:
        num += 1 
    while (cops < num and trobat == 1):
        cops += 1
        file.seek(apuntador)
        if int(file.read(7)) != NIU:
            apuntador += 53
        else:
            trobat = 2
    if trobat == 1:
        return None
    else:
        file.seek(apuntador)
        return file.read(53)
    
fitxer = input("Introdueix el nom del fitxer: ")
niu = int(input("Introdueix el NIU: "))

resultat = funcio(fitxer,niu)

if resultat == None:
    print("La informació de l'estudiant demanat no es troba al fitxer")
    
else:
    print(resultat)
        
    
        