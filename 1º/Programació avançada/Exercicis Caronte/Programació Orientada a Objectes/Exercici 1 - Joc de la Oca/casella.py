#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:22:01 2020

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

   def entra_jugador(self, jugador):
       jugador.posicio=self._posicio
       oca=self.es_oca()
       if oca:
           return True
       else:
           if self.tipus==Casella.CASELLA_POU:
               jugador.torns_inactiu=Casella.N_TORNS_POU
           elif self.tipus==Casella.CASELLA_MORT:
               jugador.posicio=Casella.CASELLA_INICIAL
           elif self.tipus==Casella.CASELLA_FINAL:
               jugador.guanya()
           return False

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