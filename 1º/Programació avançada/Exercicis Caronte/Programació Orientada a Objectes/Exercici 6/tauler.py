#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:30:19 2020

@author:
"""


import casella as c
import jugador as j

class Tauler():
   def __init__(self):
       self._caselles=[]
       self._jugadors=[]
       self._jugador_actual=0
   def inicialitza(self, fitxer_caselles, n_jugadors):
       with open(fitxer_caselles, 'r') as fitxer:
           for linia in fitxer:
               valors=linia.split()
               if valors[1]=="N":
                   nova_casella = c.Normal(int(valors[0]))
               elif valors[1]=="O":
                   nova_casella = c.Oca(int(valors[0]))
               if valors[1]=="P":
                   nova_casella = c.Pou(int(valors[0]))
               if valors[1]=="M":
                   nova_casella = c.Mort(int(valors[0]))
               if valors[1]=="F":
                   nova_casella = c.Final(int(valors[0]))
               self._caselles.append(nova_casella)
       
       for i in range(n_jugadors):
           self._jugadors.append(j.Jugador())
       self._jugador_actual=0


   def torn_joc(self, valor_dau):
       jugador_torn = self._jugadors[self._jugador_actual]
       repeteix_torn = False
       if jugador_torn.pot_tirar():
           nova_posicio = jugador_torn.posicio + valor_dau
           if nova_posicio <= len(self._caselles):
               es_oca = self._caselles[nova_posicio-1].entra_jugador(jugador_torn)

               if es_oca:
                   try:
                       posicio_oca = [c.tipus for c in self._caselles[nova_posicio:]].index(c.Casella.CASELLA_OCA)
                       jugador_torn.posicio = self._caselles[posicio_oca + nova_posicio].posicio
                       repeteix_torn = True
                   except:
                       pass
           else:
               nova_posicio = -1
       else:
           jugador_torn.torns_inactiu -= 1

       jugador_actual = self._jugador_actual
       posicio_actual = jugador_torn.posicio
       pot_tirar = jugador_torn.pot_tirar()
       n_torns_inactiu = jugador_torn.torns_inactiu
       guanyador = jugador_torn.es_guanyador()
       if not repeteix_torn:                
           self._jugador_actual = (self._jugador_actual + 1) % len(self._jugadors)
       return (jugador_actual + 1, posicio_actual, pot_tirar, n_torns_inactiu, guanyador) #(ultim=guanyador )


   def tipus_casella(self, n_casella):
       return self._caselles[n_casella-1].tipus