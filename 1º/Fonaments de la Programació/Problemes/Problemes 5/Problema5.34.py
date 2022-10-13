
def LlegirLlista (elements):
    Llista1 = []
    for i in range (elements):
        posicio = int (input("Introdueix una posició: "))
        num = int (input("Introdueix un numero: "))
   
        Llista1.insert(posicio, num)
   
    return Llista1

def InicialitzarLlista (elements,valor):
    Llista2 = []
    for i in range (elements):
        Llista2.append(valor)
   
    return Llista2

def MitjanaLlista (Llista):
    suma = 0
    comptador = 0
    for i in range (len(Llista)):    
        suma = suma + Llista[i]
        comptador = comptador + 1
       
        mitjana = suma/comptador
   
    return mitjana
   
def MaximLlista (Llista):
    maxim = Llista[0]
    index = 0
    for i in range (len(Llista)):
        if (Llista[i] > maxim):
            maxim = Llista[i]
            index = i
           
    return index

def MinimLlista (Llista):
    minim = Llista[0]
    index = 0
    for i in range (len(Llista)):
        if (Llista[i] < minim):
            minim = Llista[i]
            index = i

    return index

def MinimLlistaNoZero (Llista):
    minim = Llista[MaximLlista(Llista)]
    index = 0
    for i in range (len(Llista)-1,0,-1):
        if (Llista[i] <= minim and Llista[i] != 0):
            minim = Llista[i]
            index = i
   
    return index


from llistes import MinimLlistaNoZero, MaximLlista

llista = []

for i in range (14):
    temp = int(input("Introdueix la temperatura: "))
    llista.append (temp)
   
solucio = []
for i in range (60):
    solucio.append(0)

for i in range(14):
    #+10 ja que llista solucio comença amb -10
    #afegim a la llissta solucio el que ja hi havia en el paràmetre +1
   
    solucio[llista[i]+10] = solucio[llista[i]+10] +1    
print("Temperatura més repetida: ", MaximLlista(solucio)-10)
print("Temperatura menys repetida: ", MinimLlistaNoZero(solucio)-10)