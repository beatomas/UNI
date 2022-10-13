

def generar_llistat_notes(fitxer):
    suma = 0
    est = 0
    mitjana = 0
    nameHandle = open(fitxer,"r")
    for linia in nameHandle:
        nota = linia[len(linia)-6:len(linia)]
        suma = suma + float(nota)
        est += 1
        print(linia[:7],nota)
    mitjana = suma/est
    print("Nota mitjana classe: "+str(mitjana))
    nameHandle.close()

    
    
nom = input("Introdueix el nom del fitxer: ")
generar_llistat_notes(nom)
