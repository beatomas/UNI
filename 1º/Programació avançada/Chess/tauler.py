# -*- coding: utf-8 -*-
"""
Created on Sat May 16 12:30:47 2020

@author:
"""
import numpy as np


class Tauler:
    
    def __init__(self,llista_blanques,llista_negres):
        self._estat_partida = np.array ([["T","C","A","N","R","A","C","T"],
                                         ["P","P","P","P","P","P","P","P"],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["P","P","P","P","P","P","P","P"],
                                         ["T","C","A","N","R","A","C","T"],])
    
        self._estat_color = np.array ([[0,0,0,0,0,0,0,0],
                                         [0,0,0,0,0,0,0,0],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["X","X","X","X","X","X","X","X"],
                                         ["X","X","X","X","X","X","X","X"],
                                         [1,1,1,1,1,1,1,1],
                                         [1,1,1,1,1,1,1,1]])
    
        self._llista_blanques= llista_blanques
        self._llista_negres= llista_negres
        
    def busca_posicio(self,posicio):
        posicio = list(posicio)
        
        row = posicio[0]
        column = posicio[1]
        
        llista_lletres=["A","B","C","D","E","F","G","H"]
        
        if row in llista_lletres:
            number_column = int(llista_lletres.index(row))
            column = int(column)
            number_row = int(column - 1)
            
            
        if column in llista_lletres:
            number_column = int(llista_lletres.index(column))
            row = int(row)
            number_row = int(row - 1)
            
        posicio_array = number_row,number_column 
        
        return posicio_array
    
    def get_posicio(self,posicio): #color
        try:
            position = self.busca_posicio(posicio)
            self._color = self._estat_color[position]
            if self._color != "X":
                self._color = int(self._color)
            
        except IndexError:
            self._color = 2
                
        return self._color

    def set_posicio(self,pos_inicial,pos_final,color): #modificar estat de la partida
        
        if color ==1:
            
            for peca_negra in self._llista_negres:
                if peca_negra.get_posicio() == pos_inicial:
                    peca_negra.set_posicio(pos_final)
    
        if color ==0:
            
            for peca_blanca in self._llista_blanques:
                if peca_blanca.get_posicio() == pos_inicial:
                    peca_blanca.set_posicio(pos_final)
                

    def mostra(self):
        return self._estat_partida #print
    
