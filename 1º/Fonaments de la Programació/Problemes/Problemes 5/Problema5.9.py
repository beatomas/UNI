
def operacio(nombre,exponent):
    final = (nombre**exponent)
    return final

        
x = int(input("Introdueix un nombre: "))
n = int(input("Introdueix l'exponent: "))

resultat = operacio(x,n)
print("El resultat d'elevar",x,"a la potència",n,"és",resultat)


