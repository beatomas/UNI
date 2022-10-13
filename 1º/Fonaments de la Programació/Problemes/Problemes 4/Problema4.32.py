

llista = []
for i in range (0,9):
    valor = int(input("Introdueix un valor: "))
    llista.append(valor)
    
i = 0
senars = True
while i < len(llista):
    if (llista[i]%2 == 0):
        print("NO TOTS SON SENARS")
        senars = False
        break
    else: 
        i += 1

if senars:
    print("TOTS SON SENARS")