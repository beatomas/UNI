# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 18:53:38 2020

@author: andre
"""
import os
import os.path
import copy

class MusicFiles(): 
    def __init__(self):
        self._llista_mp3 = []
        self._llista_mp3_antiga = []
        self._added = []
        self._removed = []

    def reload_fs(self, path):
        contador = 0
        self._llista_mp3 = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                if filename.lower().endswith(tuple(['.mp3'])):
                    file = os.path.join(root, filename)
                    self._llista_mp3.append(file)
        
        if self._llista_mp3_antiga == [] and contador == 0:
            contador = 1
            self._llista_mp3_antiga = copy.copy(self._llista_mp3)
            self._added = copy.copy(self._llista_mp3)
            
        else:
            self._added = []
            for element in self._llista_mp3:
                if element not in self._llista_mp3_antiga:
                    self._added.append(element)
                    self._llista_mp3_antiga.append(element)
                    
            self._removed = []     
            for elemento in self._llista_mp3_antiga:
                if elemento not in self._llista_mp3:
                    self._removed.append(elemento) 
            for el in self._removed:
                self._llista_mp3_antiga.remove(el)

        
    def files_added(self):
        return self._added
        
           
    def files_removed(self):
        return self._removed

