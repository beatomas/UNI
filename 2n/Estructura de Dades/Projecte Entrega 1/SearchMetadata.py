# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 19:06:50 2020

@author: andre
"""

class SearchMetadata:
    def __init__(self, music_data):
        self._musicdata = music_data
    
    def title(self,sub):
        
        title = []
                   
        for key, value in self._musicdata._metadates.items():
            if value[1] == None:
                x = 'none'  
            else:
                x = (str(value[1])).lower()             
                
            if x.find((str(sub)).lower()) != -1:
                title.append(key) 
                
        return title
    
    def artist(self,sub):
        
        artist = []
                   
        for key, value in self._musicdata._metadates.items():
            if value[2] == None:
                x = 'none'
            else:
                x = (str(value[2])).lower()             
                
            if x.find((str(sub)).lower()) != -1:
                artist.append(key) 
                
        return artist
        
    def album(self,sub):
        
        album = []
                   
        for key, value in self._musicdata._metadates.items():
            if value[3] == None:
                x = 'none'
            else:
                x = (str(value[3])).lower()             
                
            if x.find((str(sub)).lower()) != -1:
                album.append(key) 
                
        return album
     
    
    def genre(self,sub):
        
        genre = []
                   
        for key, value in self._musicdata._metadates.items():
            if value[4] == None:
                x = 'none'
            else:
                x = (str(value[4])).lower()             
                
            if x.find((str(sub)).lower()) != -1:
                genre.append(key) 
                
        return genre
           
    
    def and_operator(self,llista1,llista2): 
        llista3 = []
        for x in llista2:
            if x in llista1: 
                llista3.append(x)
        
        return llista3
                

    def or_operator(self,llista1,llista2):
        llista3 = llista1.copy()
        for value in llista2:
            if value not in llista3:
                llista3.append(value)
                
        return llista3
    
    
