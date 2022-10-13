# -*- coding: utf-8 -*-
"""

"""

x = int(input("Introdueix un nombre enter: "))
y = int(input("Introdueix un nombre enter: "))
z = int(input("Introdueix un nombre enter: "))

A = (x < 7) and ((y > z) or (7 > z))
B = ((x == 99) and (y < -5)) and ((z >= 100) or (z < 6))
C =  ((9 >= x) and (13 < y)) or (-36 >= z)

print("Resultat de les expressions:",A,B,C,)