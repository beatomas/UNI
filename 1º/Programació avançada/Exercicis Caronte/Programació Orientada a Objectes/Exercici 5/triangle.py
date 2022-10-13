#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:27:47 2020

@author:
"""


from punt import Point
from figura import Figura

class Triangle(Figura):
    def __init__(self):
        self._llistavertexs=[Point(0,0),Point(0,0),Point(0,0) ]
            
    
    def llegeix(self):
        
        x=float(input("X: "))
        y=float(input("Y: "))
        self._llistavertexs[0]=Point(x,y)
        
        x=float(input("X: "))
        y=float(input("Y: "))
        self._llistavertexs[1]=Point(x,y)
        
        x=float(input("X: "))
        y=float(input("Y: "))
        self._llistavertexs[2]=Point(x,y)
        
    
    def perimetre(self):
        self.punt_a=self._llistavertexs[0] 
        self.punt_b=self._llistavertexs[1] 
        self.punt_c=self._llistavertexs[2] 
        
        self._a=float(self.punt_a.__sub__(self.punt_b))
        self._b=float(self.punt_a.__sub__(self.punt_c))
        self._c=float(self.punt_b.__sub__(self.punt_c))
        self._perimetre=self._a+self._b+self._c
    
        return self._perimetre
    
    
    def area(self):
        area =  self._perimetre/2
        return (area*(area-self._a)*(area-self._b)*(area-self._c))**(1/2)
    
    
    def __str__(self):
        centre= str(self.punt_a)+str(self.punt_b)+str(self.punt_c)
        return centre