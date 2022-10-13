

cadena = input("Introdueix una cadena de caràcters: ")


i = 0
diferents = False
while (i < (len(cadena)/2)+1):
    if cadena[i] == cadena[len(cadena)-1-i]:
        i += 1
    else:
        diferents = True
        break

if (diferents):
    print("La cadena NO és palíndrom")
else:
    print("La cadena és palíndrom")
    
    
