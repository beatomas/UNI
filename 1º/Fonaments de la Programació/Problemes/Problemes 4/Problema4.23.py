
llista = []
nens = 0
suma = 0
while nens < 15:
    mes = int(input("Introdueix un mes: "))
    while (mes < 9 or mes > 18):
        print("Error: Valor no valid")
        mes = int(input("Introdueix un mes: "))
    else: 
        llista.append(mes)
        suma = suma + mes
        nens += 1
        
mitjana = suma/15
print("Mitjana d'edat en caminar:",mitjana,"mesos")     
    