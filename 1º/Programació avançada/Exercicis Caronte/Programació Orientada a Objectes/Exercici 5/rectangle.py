#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:27:13 2020

@author:
"""



from punt import Point
from figura import Figura

class Rectangle(Figura):
    def __init__(self):
        self._alçada = 0
        self._base = 0
        self._vertexse = Point(0,0) 
       
    def llegeix(self):
        self._vertexse.x=float(input("X: "))
        self._vertexse.y=float(input("Y: "))
        self._alçada=float(input("Alçada: "))
        self._base=float(input("Base: "))
        
    def area(self):
        area = (self._base*self._alçada)
        return area
    
    def perimetre(self):
        perimetre = (2*(self._base))+(2*(self._alçada))
        return perimetre


    def __str__(self):
        
        centre=  (str(self._alçada))+str(self._base)+str(self._vertexse)
        
        return centre    
