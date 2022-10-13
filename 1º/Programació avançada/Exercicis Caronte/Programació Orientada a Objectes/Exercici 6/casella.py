#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:30:35 2020

@author:
"""


class Casella:
   CASELLA_NORMAL='N'
   CASELLA_OCA='O'
   CASELLA_POU='P'
   CASELLA_MORT='M'
   CASELLA_FINAL='F'
   CASELLA_INICIAL=1
   N_TORNS_POU=2
   
   def __init__(self, posicio = 0, tipus = 'N'):
       self._posicio=posicio
       self._tipus=tipus

   @property
   def posicio(self):
       return self._posicio

   @posicio.setter
   def posicio(self, posicio):
       self._posicio=posicio

   @property
   def tipus(self):
       return self._tipus

   @tipus.setter
   def tipus(self, tipus):
       self._tipus=tipus

   def es_oca(self):
       if self._tipus==Casella.CASELLA_OCA:
           return True
       else:
           return False
       
        
        

class Normal(Casella):
    def __init__(self, posicio = 0, tipus = 'N'):
       self._posicio=posicio
       self._tipus='N'
    
    def entra_jugador(self, jugador):
       jugador.posicio=self._posicio
       return False
       
        
class Oca(Casella):
    def __init__(self, posicio = 0, tipus = 'O'):
       self._posicio=posicio
       self._tipus='O'
    
    def entra_jugador(self, jugador):
       jugador.posicio=self._posicio
       return True
       
       
class Pou(Casella):
    def __init__(self, posicio = 0, tipus = 'P'):
       self._posicio=posicio
       self._tipus='P'
    
    def entra_jugador(self, jugador):
       jugador.posicio=self._posicio
       jugador.torns_inactiu=Casella.N_TORNS_POU
       return False
       
class Mort(Casella):
    def __init__(self, posicio = 0, tipus = 'M'):
       self._posicio=posicio
       self._tipus='M'
    def entra_jugador(self, jugador):
       jugador.posicio=Casella.CASELLA_INICIAL
       return False
       
class Final(Casella):
    def __init__(self, posicio = 0, tipus = 'F'):
       self._posicio=posicio
       self._tipus='F'
       
    def entra_jugador(self, jugador):
       jugador.posicio=self._posicio
       jugador.guanya()
       return False