# -*- coding: utf-8 -*-
"""

"""
x = int(input("Introdueix el valor de x: "))
y = int(input("Introdueix el valor de y: "))
z = int(input("Introdueix el valor de z: "))

a = (x < 7) and ((y > z) or (7 > z))
b = ((x == 99) and (y < -5)) and ((z >= 100) or (z < 6))
c = ((9 >= x) and (13 < y)) or (-36 >= z)

print("Resultat de les expressions:",a,b,c)