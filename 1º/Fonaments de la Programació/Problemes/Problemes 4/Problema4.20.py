

llista = []

x = 1

while x <= 12:
    numero = int(input("Introdueix un valor: "))
    llista.append(numero)
    x += 1

print("Entrada:",llista)


i = 0
while i < 12:
    if llista[i] > 0:
        i +=1
    else:
        llista[i]=0
        i += 1
       
    
print("Sortida:",llista)

