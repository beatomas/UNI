#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""
x = int(input("Introdueix la coordenada x: "))
y = int(input("Introdueix la coordenada y: "))

sol = (x > 0 and y > 0) and (x < 10 and y < 10)
print("El resultat de la comparació és:",sol)