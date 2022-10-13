
cops = 0
suma = 0

num = int(input("Introdueix un nombre: "))
cops = cops + 1
suma = num + suma

if (num == 0):
    print ("Error: La seqüència és buida. No es pot calcular la mitjana")

while (num != 0):
    num = int(input("Introdueix un nombre: "))
    if (num != 0):
        cops = cops + 1
        suma = num + suma
    else:
        mitjana = suma/cops
        print("Mitjana dels nombres de la seqüència:",mitjana)
    
    
    
