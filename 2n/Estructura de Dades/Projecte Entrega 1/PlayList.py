# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 20:29:01 2020

@author: andre
"""

class PlayList:
    def __init__(self, music_ids, music_player):
        self._playlist = []
        self._musicid = music_ids
        self._musicplayer = music_player
        
    def __len__(self):
        return len(self._playlist)
    
    def load_file(self,file):
        self._playlist = []
        
        with open(file, "rb") as arxiu:
            for line in arxiu:
                if line[0]!='#' and line[-5:-1] =='.mp3':
                    key = self._musicid.get_uuid(line[:-1])
                    if key is not None:
                        self._playlist.append(key)
                                                
        
    def play(self, mode):
        for uuid in self._playlist:
            self._musicplayer.play_song(uuid, mode)
            
    def add_song_at_end(self,uuid):
        self._playlist.append(uuid)
    
    def remove_first_song(self):
        if self._playlist ==[]:
            pass
        else:
            self._playlist.pop(0)
    
    def remove_last_song(self):
        if self._playlist == []:
            pass
        else:
            self._playlist.pop(-1)
        
            
            
        