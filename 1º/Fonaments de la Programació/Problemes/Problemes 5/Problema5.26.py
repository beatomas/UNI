

from math import sqrt
    
def equacio(a,b,c):
    arrel = ((b**2)-(4*a*c))
    if arrel >= 0:
        if arrel == 0:
            res = 1
            x1 = (-b/(2*a))
            return res,x1,None
        else:
            res = 2
            x1 = (-b+sqrt(arrel))/(2*a)
            x2 = ((-b)-sqrt(arrel))/(2*a)
            return res,x1,x2
    else:
        res = 0
        return res,None,None
    
a = int(input("Intorudueix un valor a: "))
b = int(input("Intorudueix un valor b: "))
c = int(input("Intorudueix un valor c: "))

nombre,resultat1,resultat2 = equacio(a,b,c)

print("El nombre d'arrels és",nombre,"i el reusltat és",resultat1,resultat2)