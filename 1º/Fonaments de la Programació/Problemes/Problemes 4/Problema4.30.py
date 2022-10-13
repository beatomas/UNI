

cadena = input("Introdueix una cadena: ")


i = 0
espais = False
while i < len(cadena):
    if (cadena[i] == " "):
        print("Hi ha un espai en blanc")
        espais = True
        break
    else:
        i += 1

if (espais == False):
    print("NO hi ha cap espai en blanc")

        