paraules = []

def llegir ():
    nameHandle = open("catala.txt","r", encoding = "utf8")
   
    for line in nameHandle:
        paraules.append(line[:-1])
       
    nameHandle.close()
   
def Palindrom (cadena):
   
    diferent = False
    index = 0
    comptador = len(cadena)-1
   
    while (diferent == False and index < len(cadena)):
        if (cadena[index] != cadena[comptador]):
            diferent = True
       
        index = index + 1
        comptador = comptador -1
       
    if (diferent == False):
        return True
   
    else:
        return False
   
def bisect (llista, busc):
   
    sortida=False
    min = 0
    max = len(llista)
   
    while (min < max and sortida != True):

        mig = (min + max) // 2

        if (llista[mig] == busc):
            sortida=True
       
        elif (llista[mig] < busc):
            min = mig + 1
        else:
            max = mig
    return (sortida)
   
#main

llegir()        
palindroms = []
for i in paraules:
    if (bisect(paraules, i[::-1])):
        palindroms.append(i)
print (palindroms)

  
        