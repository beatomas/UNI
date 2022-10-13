
llista = []

for i in range (0,10):
    valor = int(input("Introdueix un valor: "))
    llista.append(valor)
    
maxim = max(llista)

i = 0

while i < 10:
    if llista[i] == maxim:
        print("El màxim de la llista és",maxim,"i es troba a l'índex",i)
        break
    else:
        i += 1