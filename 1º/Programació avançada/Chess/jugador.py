# -*- coding: utf-8 -*-
"""
Created on Thu May 14 19:07:36 2020

@author:
"""

class Jugador:
   
    def __init__(self,peces,color):
        self._peces = peces
        self._color = color
        
   
    def mou_peca(self,pos_inicial,pos_final,tauler):
        
        #print(pos_inicial)
        posicio_array = tauler.busca_posicio(pos_inicial)
        #print(posicio_array)
        
        x = tauler._estat_partida[posicio_array]
                
        for p in self._peces:
            pos_inicial_tmb = pos_inicial[1]+pos_inicial[0]
            
            if (p.get_tipus() == x) and (p.get_posicio() == pos_inicial) or (p.get_posicio() == pos_inicial_tmb):
                
                valido = p.moviment_valid(pos_final,tauler)
    
                return valido
                    
           
    def mata_peca(self,posicio,tauler):
        
        for y in self._peces:
            if y.get_posicio() == posicio:
                y.mata()
                
    
    def perd(self):
        rei_mort = False
        for p in self._peces:
            if p.get_tipus() == "R":
                if p.esta_viva() == False:
                    rei_mort = True
        return rei_mort