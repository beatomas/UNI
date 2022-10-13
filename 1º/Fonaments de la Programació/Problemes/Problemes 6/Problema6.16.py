
def codificar_fitxer(nom,n):
    file = open(nom,"r")
    fole = open(nom[:-4]+"_2.txt","a")
    for line in file:
        for x in range (len(line)):
            fole.write(chr(ord(line[x])+n))
    
    file.close()
    fole.close()

