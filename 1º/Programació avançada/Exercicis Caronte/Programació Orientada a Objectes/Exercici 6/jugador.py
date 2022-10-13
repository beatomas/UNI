#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:31:11 2020

@author:
"""


class Jugador:

   def __init__(self, casella = 1, n_torns_inactiu = 0, guanyador = False):
       self.casella=casella
       self.n_torns_inactiu=n_torns_inactiu
       self.guanyador=guanyador

   @property
   def posicio(self):
       return self.casella

   @posicio.setter
   def posicio(self, casella):
       self.casella=casella

   @property
   def torns_inactiu(self):
      return self.n_torns_inactiu

   @torns_inactiu.setter
   def torns_inactiu(self, n_torns):
       self.n_torns_inactiu=n_torns

   def pot_tirar(self):
       if self.n_torns_inactiu==0:
           return True
       else:
           return False

   def guanya(self):
       self.guanyador=True

   def es_guanyador(self):
       if self.guanyador:
           return True
       else:
           return False