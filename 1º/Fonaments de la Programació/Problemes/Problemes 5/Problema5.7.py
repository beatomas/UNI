

resultat = 0
def main(num):
    resultat = (num/100)%10
    
    return resultat


n = int(input("Introdueix un nombre: "))

centenes = main(n)
    
print("Les centenes del nombre",n,"són",int(centenes))
    
    