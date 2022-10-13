
llista = []
for i in range(12):
    temp = int(input("Introdueix la temperatura: "))
    llista.append(temp)

suma = sum(llista)
mitjana = suma/12

    
for i,j in enumerate(llista):
    if j == mitjana:
        print("El mes",i+1,"ha tingut temperatura igual a la mitjana anual")
    if j < mitjana:
        print("El mes",i+1,"ha tingut temperatura inferior a la mitjana anual")
    if j > mitjana:
        print("El mes",i+1,"ha tingut temperatura superior a la mitjana anual")
        
