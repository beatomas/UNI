# -*- coding: utf-8 -*-
"""
test-mp3.py : Script de proves per reproduïr MP3
"""

import cfg      # Necessari per a la pràctica !!
                # Mireu el contingut de l'arxiu

import os.path
import sys
import numpy    #  installed in anaconda by default
import uuid
import eyed3    #  $ pip install eyed3
import vlc      #  $ pip install python-vlc
import time


# STEP 1: Cerca dels arxius al filesystem
print("Cercant arxius dins [" + cfg.get_root() + "]\n")
uri_file = cfg.get_one_file(0)  # Aquesta funció és només de proves!
if not os.path.isfile(uri_file):
    print("ERROR: Arxiu MP3 inexistent!")
    sys.exit(1)


# STEP 2: Obtenció de les metadades
metadata = eyed3.load(uri_file)
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
    genre = "None"


# STEP 3: Generació del identificador únic
name_file = cfg.get_canonical_pathfile(uri_file)
mp3_uuid  = uuid.uuid5(uuid.NAMESPACE_URL, name_file)


# STEP 4: Reproducció
print("Reproduïnt [{}]".format(uri_file))
print(" Duració:  {} segons".format(duration))
print(" Títol:    {}".format(title))
print(" Artista:  {}".format(artist))
print(" Àlbum:    {}".format(album))
print(" Gènere:   {}".format(genre))
print(" UUID:     {}".format(mp3_uuid))
print(" Arxiu:    {}".format(name_file))
      
player = vlc.MediaPlayer(uri_file)

player.play()     # Nota: Crida ASYNC !!

# Poolling loop pel control de la reproducció
timeout = time.time() + duration
while True:
    if time.time() < timeout:
        try:
            time.sleep(1)
        except KeyboardInterrupt:  # STOP amb <CTRL>+<C> a la consola
            break
    else:
        break
    
player.stop()


# END
print("\nFinal!")
