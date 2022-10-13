
llista = []


i = 0
while i < 12:
    valor = int(input("Introdueix la temperatura mitjana: "))
    llista.append(valor)
    i += 1

maxim = max(llista)
minim = min(llista)
m = 0

while (m < 12):
    if llista[m] == minim:
        print ("Mes amb temperatura mínima:",m+1)
        m = 13
    else: 
        m += 1

n = 0
while (n < 12):
    if llista[n] == maxim:
        print ("Mes amb temperatura màxima:",n+1)
        n = 13
    else: 
        n += 1
        

suma = 0
for i in llista:
    suma += i
    
mitjana = suma/12
print("Temperatura mitjana:",mitjana)


i = 0
while i < 12:
    if llista[i] == mitjana:
        print("El mes",i+1,"ha tingut temperatura igual a la mitjana anual.")
        i += 1
    if llista[i] < mitjana:
        print("El mes",i+1,"ha tingut temperatura inferior a la mitjana anual.")
        i += 1
    else:
        print("El mes",i+1,"ha tingut temperatura superior a la mitjana anual.")
        i += 1
