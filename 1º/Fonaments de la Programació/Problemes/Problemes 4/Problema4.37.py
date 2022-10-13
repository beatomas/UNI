
llista = []
for valor in range (1,11):
    valor = float(input("Introdueix un valor: "))
    llista.append(valor)

suma = 0
i = 0
while i < len(llista):
    suma = suma + llista[i] 
    if suma > 25:
        print("A la posició",i + 1,"la suma acumulada és superior a 25")
        break
    i += 1
    
 
if suma <= 25: 
    print("La suma acumulada de la llista és inferior o igual a 25")

