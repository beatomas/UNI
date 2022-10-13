
cadena = input("Introdueix una cadena de caràcters: ")

valor1 = int(input("Introdueix un primer valor entre 0 i la longitud de la cadena: "))
valor2 = int(input("Introdueix un segon valor entre 0 i la longitud de la cadena: "))

while (valor1 < 0) or (valor1 >= len(cadena)) or (valor2 < 0) or (valor2 >= len(cadena)):
    print("Error: rang de valors incorrecte")
    valor1 = int(input("Introdueix un primer valor entre 0 i la longitud de la cadena: "))
    valor2 = int(input("Introdueix un segon valor entre 0 i la longitud de la cadena: "))
    
print(cadena[valor1:valor2+1])
    
print(cadena[valor1:valor2+1:2])

print(cadena[:valor1+1])

print(cadena[valor2:])