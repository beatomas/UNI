
suma = 0
numero = 1

N = int(input("Introdueix un nombre: "))

while (N <= 0):
    print("Error: el valor ha de ser més gran que zero")
    N = int(input("Introdueix un nombre: "))

while (numero <= N):
    suma = suma + numero
    numero += 1
    
print("El sumatori de",N,"és:",suma)