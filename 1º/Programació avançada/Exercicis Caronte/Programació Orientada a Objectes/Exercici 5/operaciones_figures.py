#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:28:51 2020

@author:
"""


import cercle
import triangle
import rectangle

def crea_figura(tipus):
    if tipus == "C":
        a= cercle.Cercle()
    elif tipus == "R":
        a= rectangle.Rectangle()
    elif tipus =="T":
        a=triangle.Triangle()
    a.llegeix()
    return a

def suma_area(figures):
    suma=0
    for element in figures:
        suma += element.area()
        
    return suma
    

def max_perimetre(figures):
    maxim=0
    pos=0
    for i in range(len(figures)):
        if maxim < figures[i].perimetre():
            maxim=figures[i].perimetre()
            pos=i
    
    return figures[pos]
    
