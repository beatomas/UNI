

def estadistics_fitxer(nom_fitxer):
    fileHandle=open(nom_fitxer, "r")
    text=fileHandle.read()
    longitud=len(text)
    i=0
    suma=0
    comptador=0
    while i<longitud:
        num=""
        while i<longitud and text[i]>='0' and text[i]<='9':
            num+=text[i]
            i+=1
        valor=int(num)
        suma+=valor
        comptador+=1
        
        while i<longitud and (text[i]<'0' or text[i]>'9'):
            i+=1
    mitjana=suma/comptador
    return mitjana

try:
    nom_fitxer=input("Introdueix el nom del fitxer: ")
    mitjana=estadistics_fitxer(nom_fitxer)
except IOError:
    print("ERROR: Fitxer inexistent")
except ZeroDivisionError:
    print("ERROR: El fitxer no conté valors enters")
except ValueError:
    print("ERROR: Format de fitxer incorrecte")
except:
    print("ERROR: Error indeterminat")
else:
    print("Mitjana: "+str(mitjana))