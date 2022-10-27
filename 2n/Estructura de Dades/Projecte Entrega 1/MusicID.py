# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:16:58 2020

@author: andre
"""
import uuid
import cfg

class MusicID():
    def __init__(self):
        self._ids = dict()
    
    def __len__(self):
      return len(self._ids)

    
    def generate_uuid(self, file):
        
        path_file = cfg.get_canonical_pathfile(file)
        mp3_uuid  = str(uuid.uuid5(uuid.NAMESPACE_URL, path_file))
        
        if mp3_uuid not in self._ids.keys():
            self._ids[mp3_uuid] = file
            return mp3_uuid
        else:
            return None
    
    def get_uuid(self, file):
                            
        for key, value in self._ids.items(): 
            if file == value: 
                return key 
            

    def remove_uuid(self, uuid):
        if uuid in self._ids:
            del self._ids[uuid]
        
  
            
            
            
        
        
    
            
            
            
            
        
        