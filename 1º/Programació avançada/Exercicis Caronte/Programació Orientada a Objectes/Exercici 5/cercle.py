#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:28:27 2020

@author:
"""


from punt import Point
from figura import Figura
import numpy as np

class Cercle(Figura):
    def __init__(self):
        self._centre=Point(0,0)
        self._radi=0
    
    
    def llegeix(self):
        self._centre.x=float(input("X: "))
        self._centre.y=float(input("Y: "))
        self._radi=float(input("Radi: "))
        
    def area(self):
        area = ((np.pi)*((self._radi)**2))
        return area
    
    def perimetre(self):
        perimetre = (2*(np.pi)*((self._radi)))
        return perimetre

    def __str__(self):
        centre= str(self._centre)+str(self._radi)
        return centre