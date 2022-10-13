

def LlegirLlista(num):
    llista = []
    for n in range(num):
        valor = int(input("Introdueix un valor: ")) 
        llista.append(valor)
    return llista
    
def InicialitzarLlista(nombre,valor):
    llista = []
    for i in range(nombre):
        llista.append(valor)
    return llista
    
    
def MitjanaLlista(llista):
    suma = 0
    for element in llista:
        suma += element
    mitjana = suma/len(llista)
    return mitjana


def MaximLlista(llista):
    maxim = llista[0]
    posicio = 0
    for i in range(1,len(llista)):
        element = llista[i]
        if element>maxim:
            maxim = element
            posicio = i
    return posicio

def MinimLlista(llista):
    minim = min(llista)
    i = 0
    while minim != llista[i]:
        i += 1
    return i


def MinimLlistaNoZero(llista):
    minim = llista[MaximLlista(llista)]
    index = 0
    for i in range(len(llista)):
        if llista[i] <= minim and llista[i] != 0:
            minim = llista[i]
            index = i
    return index
    


minim = MinimLlista(LlegirLlista(8))
print(minim)
    
