

llista = []

def funcio(llista):
    if llista[0] == 0:
        resultat = 1
    else: 
        resultat = 0
    return resultat


i = 1
num = 1
while num != 0 and i != 10:
    num = int(input("Introdueix un número: "))
    llista.append(num)
    i += 1

final= funcio(llista)

minim = min(llista)
maxim = max(llista)

llista1 = []
if final == 0:
    if minim == 0:
        llista1 = llista
        i = 0
        while llista1[i] != 0:
            i += 1
        llista1.pop(i)
        minim = min(llista1)
    print("El mínim de la seqüència és",minim,"i el màxim és",maxim)
else:
    print("Error: seqüència buida")