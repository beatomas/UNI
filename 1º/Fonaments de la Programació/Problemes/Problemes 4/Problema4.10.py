
cadena = input("Introdueix una cadena de caràcters: ")

pos = int(input("Introdueix una posició a modificar: "))

while ((pos >= 0) and (pos < len(cadena))):
    valor = input("Introdueix un valor a assignar a la posició: ")
    cadena = cadena[0:pos]+valor+cadena[pos+1:]
    pos = int(input("Introdueix una posició a modificar: "))

print(cadena)