

cadena1 = input("Introdueix una primera cadena: ")
cadena2 = input("Introdueix una segona cadena: ")


i = 0
diferent = False
while i < len(cadena1):
    if cadena1[i] != cadena2[i]:
        print("El primer caracter diferent es", cadena1[i])
        diferent = True
        break
    else:
        i += 1
        
if (diferent == False):
    print("No hi ha cap caracter diferent")