# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 19:38:00 2020

@author: andre
"""

from MusicID import MusicID
import vlc  
import time
import cfg
import os

class MusicPlayer:
    def __init__(self,music_data):
        self._musicdata = music_data
        self._musicid = MusicID()
            
    def print_song(self,uuid):
        try:
            uri_song = str(self._musicid._ids[uuid][5])
        except KeyError:
            return None
        
        print("Reproduïnt [{}]".format(uri_song))
        print(" Duració:  {} segons".format(self._musicdata._metadates[uuid][0]))
        print(" Títol:    {}".format(self._musicdata._metadates[uuid][1]))
        print(" Artista:  {}".format(self._musicdata._metadates[uuid][2]))
        print(" Àlbum:    {}".format(self._musicdata._metadates[uuid][3]))
        print(" Gènere:   {}".format(self._musicdata._metadates[uuid][4]))
        print(" UUID:     {}".format(uuid)) 
        print(" Arxiu:    {}".format(self._musicid._ids[uuid][1]))
    
    def play_file(self,file):
        try:
            uuid = self._musicid.get_uuid(file)
            path = os.path.join(cfg.get_root(),self._musicdata._metadates[uuid][5])
                                
            player = vlc.MediaPlayer(path)
    
            player.play()
            
            timeout = time.time() + self._musicdata._metadates[uuid][0] #suma el duration
            while True:
                if time.time() < timeout:
                    try:
                        time.sleep(1)
                    except KeyboardInterrupt:  
                        break
                else:
                    break
                
            player.stop()
            
        except KeyError:
            return None
    
    def play_song(self,uuid,mode):
        try:
            path = str(self._musicdata._metadates[uuid][5])
            file = os.path.basename(path)
            if mode == 0:
                self.print_song(uuid)

            if mode == 1:
                self.play_file(file)
                self.print_song(uuid)
            
            if mode ==2:
                self.play_file(file)

        except KeyError:
            return None