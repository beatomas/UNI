# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:48:28 2020

@author: andre
"""
import eyed3
import sys
import numpy
import cfg
import os

class MusicData():
    #add_song solo entra la canción y el método load_metadata carga 
    def __init__(self):
        self._metadates = dict()
    
    def __len__(self):
        return len(self._metadates)
        
        
    def add_song(self, uuid, file):
        #
        if uuid and file:  
            self._metadates[uuid] = [None,None,None,None,None,file]
        
            
    def remove_song(self, uuid):
        if uuid in self._metadates:
            del self._metadates[uuid]
        
    def load_metadata(self, uuid):
        
        if uuid in self._metadates.keys():
            
            path = os.path.join(cfg.get_root(),self._metadates[uuid][5])
            os.path.exists(path)
            
            metadata = eyed3.load(path)
            if metadata is None:
                print("ERROR: Arxiu MP3 erroni!")
                sys.exit(1)
            
            duration  = int(numpy.ceil(metadata.info.time_secs))
            title     = metadata.tag.title
            artist    = metadata.tag.artist
            album     = metadata.tag.album
            
            try:
                genre = metadata.tag.genre.name
            except:
                genre = None
            
            file = self._metadates[uuid][5]
            self._metadates[uuid]=[duration,title,artist,album,genre,file]
                    
                    
    def get_title(self,uuid):
        try:
            return self._metadates[uuid][1]
        except KeyError:
            return None
    
    def get_artist(self,uuid):
        try:
            return self._metadates[uuid][2]
        except KeyError:
            return None
    
    
    def get_album(self,uuid):
        try:
            return self._metadates[uuid][3]
        except KeyError:
            return None
    
    def get_genre(self,uuid):
        try:
            return self._metadates[uuid][4]
        except KeyError:
            return None
        
    def get_filename(self,uuid):
        try:
            return self._metadates[uuid][5]
        except KeyError:
            return None
    
    

        
