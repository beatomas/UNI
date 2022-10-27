# -*- coding: utf-8 -*-
"""
main_local.py : Script Test Part I per executar en **LOCAL**
"""

import cfg
from MusicFiles     import MusicFiles
from MusicID        import MusicID
from MusicData      import MusicData
from MusicPlayer    import MusicPlayer
from PlayList       import PlayList
from SearchMetadata import SearchMetadata
import os
import shutil

# RESUM DE LES FUNCIONALITATS:
    # Func1: /* llistat d’arxius mp3 */
    # Func2: /* generar ID de cançons */
    # Func3: /* consultar metadades cançons */
    # Func4: /* reproduir cançó amb metadades */
    # Func5: /* reproduir llistes de reproducció m3u */
    # Func6: /* cercar cançons segons certs criteris */
    # Func7: /* generar llista basada en una cerca */


# Comentaris per a executar el Test en LOCAL
print ("Comment :=>> Test en LOCAL per la part I del projecte      ")
print ("Comment :=>> ============================================  ")
print ("Comment :=>> ")                                            
print ("Comment :=>> NOTA IMPORTANT: ")                            
print ("Comment :=>>    Aquest test és una versió per a executar   ")
print ("Comment :=>>    exclusivament en el vostre PC. No és la    ")
print ("Comment :=>>    versió publicada al Caronte degut a que    ")
print ("Comment :=>>    la versió del server utilitza un Corpus    ")
print ("Comment :=>>    de cançons MP3 diferent.                   ")
print ("Comment :=>> ")                                            
print ("Comment :=>> ")                                            
print ("Comment :=>> Llista de comprovacions inicials (MANUAL!):   ")
print ("Comment :=>>  - Tots els arxius *.py inclouen import cfg   ")
print ("Comment :=>>  - L'arxiu cfg.py te configurat el ROOT_DIR   ")
print ("Comment :=>>  - Tots els MP3 del Corpus estan a ROOT_DIR   ")
print ("Comment :=>>  - El PLAY_MODE es 0 al cfg.py                ")
print ("Comment :=>>  - Dins el ROOT_DIR hi han dos arxius M3U:    ")
print ("Comment :=>>       `Blues.m3u`  i  `pop.m3u`               ")
print ("Comment :=>>  - MusicPlayer: constructor rep un objecte    ")
print ("Comment :=>>     MusicData --> MusicPlayer(music_data)     ")
print ("Comment :=>>  - SearchMetadata: constructor rep un objecte ")
print ("Comment :=>>     MusicData --> SearchMetadata(music_data)  ")
print ("Comment :=>>  - MusicData: afegir get_filename(uuid) que   ")
print ("Comment :=>>     retorna el string del filename guardat    ")
print ("Comment :=>>  - MusicData: cal implementer el mètode       ")
print ("Comment :=>>     per a obtenir la longitut: __len()__      ")
print ("Comment :=>>  - PlayList: cal implementer el mètode        ")
print ("Comment :=>>     per a obtenir la longitut: __len()__      ")
print ("Comment :=>>  - Totes les classes de les que es farà test  ")
print ("Comment :=>>     han d'implementar el mètode __str__()     ")
print ("Comment :=>> ")                                            
print ("Comment :=>> Llista d'arxius a fer-lis els tests:          ")
print ("Comment :=>>    * MusicFiles.py                            ")
print ("Comment :=>>    * MusicID.py                               ")
print ("Comment :=>>    * MusicData.py                             ")
print ("Comment :=>>    * MusicPlayer.py                           ")
print ("Comment :=>>    * PlayList.py                              ")
print ("Comment :=>>    * SearchMetadata.py                        ")
print ("Comment :=>> ")


# Inicialització del test
grade = 0

print ("Grade :=>>", grade)
print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")


# Instanciació dels objectes
ROOT = cfg.get_root()
music_collection = MusicFiles()
files_uuids      = MusicID()
music_data       = MusicData()
audio_player     = MusicPlayer(music_data)
list_playlist    = []
searcher_worker  = SearchMetadata(music_data)

if (grade < 0):
    grade = 0
grade += 1


# ###########################################################################
# Func1: /* llistat d’arxius mp3 */
def func1(debug: int = 0):
    global grade
    global music_collection
    print ("Comment :=>> Test: Func1 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Comprovar que les llistes son buïdes
    # Step 2: Llegir les cançons des de zero
    # Step 3: Tornar a llegir les cançons sense canvis
    # Step 4a: Fem una còpia de dues cançons a un directory temporal
    # Step 4b: Tornem a llegir, ara amb les dues cançons "noves"
    # Step 4c: I tornem a llegir, per a comprovar que les dues "noves" ja hi són
    # Step 5a: Esborrem el directory temporal, eliminant les dues cançons "noves"
    # Step 5b: Tornem a llegir, pero ara faltaran dues cançons eliminades
    # Step 6: Esborrem tot i tornem a llegir les cançons des de zero
    #         perquè poguem consultar amb files_added() tota la col·lecció
    #########################################################################

    if (music_collection is not None) and (isinstance(music_collection,MusicFiles)):
        print("Comment :=>> OK: initializing MusicFiles")
        grade += 1
    else:
        print("Comment :=>> ERROR: initializing MusicFiles")

    print(" ", music_collection)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Comprovar que les llistes son buïdes
    if len(music_collection.files_added()) == 0:
        print("Comment :=>> OK: empty files_added")
        grade += 1
    else:
        print("Comment :=>> ERROR: not empty files_added")

    if len(music_collection.files_removed()) == 0:
        print("Comment :=>> OK: empty files_removed")
        grade += 1
    else:
        print("Comment :=>> ERROR: not empty files_removed")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Llegir les cançons des de zero
    music_collection.reload_fs(ROOT)
    print(" ", music_collection)
    add = music_collection.files_added()
    rem = music_collection.files_removed()
    sa  = len(add)
    sr  = len(rem)
    sc  = 0  # Inicialment no hi ha cap cançó!
    grade += 1

    # Adicionalment guardem el path de dos arxius MP3 per a un STEP futur
    if sa < 2:
        raise NotImplementedError("ERROR: Cal tenir-ne com a mínim 2 arxius MP3 al ROOT_DIR!")
    f1 = add[0]
    f2 = add[1]

    if debug :
        print(" new files: " + str(sa) + " and removed: " + str(sr))

    sc = sc + sa - sr
    if (sa == 414) and (sr == 0) and (sc == 414):
        print("Comment :=>> OK: loading collection from disk")
        grade += 1
    else:
        print("Comment :=>> ERROR: loading collection from disk")

    print(" Total in collection: " + str(sc))
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Tornar a llegir les cançons sense canvis
    music_collection.reload_fs(ROOT)
    print(" ", music_collection)
    add = music_collection.files_added()
    rem = music_collection.files_removed()
    sa  = len(add)
    sr  = len(rem)
    grade += 1

    if debug :
        print("\n ADDED: ")
        print("  ", *add, sep = "\n  ")
        print("\n REMOVED: ")
        print("  ", *rem, sep = "\n  ")
        print("\n new files: " + str(sa) + " and removed: " + str(sr))

    sc = sc + sa - sr
    if (sa == 0) and (sr == 0) and (sc == 414):
        print("Comment :=>> OK: reloading collection from disk")
        grade += 1
    else:
        print("Comment :=>> ERROR: reloading collection from disk")

    print(" Total in collection: " + str(sc))
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4a: Fem una còpia de dues cançons a un directory temporal
    temp_dir = os.path.join(ROOT , "__TEMP__-__TEMP__")
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)
    shutil.copy(f1, temp_dir)
    shutil.copy(f2, temp_dir)

    #########################################################################
    # Step 4b: Tornem a llegir, ara amb les dues cançons "noves"
    music_collection.reload_fs(ROOT)
    print(" ", music_collection)
    add = music_collection.files_added()
    rem = music_collection.files_removed()
    sa  = len(add)
    sr  = len(rem)
    grade += 1

    if debug :
        print("\n ADDED: ")
        print("  ", *add, sep = "\n  ")
        print("\n REMOVED: ")
        print("  ", *rem, sep = "\n  ")
        print("\n new files: " + str(sa) + " and removed: " + str(sr))

    sc = sc + sa - sr
    if (sa == 2) and (sr == 0) and (sc == 416):
        print("Comment :=>> OK: reloading with new files from disk")
        grade += 1
    else:
        print("Comment :=>> ERROR: reloading with new files from disk")
    print(" Total in collection: " + str(sc))

    #########################################################################
    # Step 4c: I tornem a llegir, per a comprovar que les dues "noves" ja hi són
    music_collection.reload_fs(ROOT)
    print(" ", music_collection)
    add = music_collection.files_added()
    rem = music_collection.files_removed()
    sa  = len(add)
    sr  = len(rem)
    grade += 1

    if debug :
        print("\n ADDED: ")
        print("  ", *add, sep = "\n  ")
        print("\n REMOVED: ")
        print("  ", *rem, sep = "\n  ")
        print("\n new files: " + str(sa) + " and removed: " + str(sr))

    sc = sc + sa - sr
    if (sa == 0) and (sr == 0) and (sc == 416):
        print("Comment :=>> OK: reloading second time with new files from disk")
        grade += 1
    else:
        print("Comment :=>> ERROR: reloading second time with new files from disk")
    print(" Total in collection: " + str(sc))

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 5a: Esborrem el directory temporal, eliminant les dues cançons "noves"
    shutil.rmtree(temp_dir)

    #########################################################################
    # Step 5b: Tornem a llegir, pero ara faltaran dues cançons eliminades
    music_collection.reload_fs(ROOT)
    print(" ", music_collection)
    add = music_collection.files_added()
    rem = music_collection.files_removed()
    sa  = len(add)
    sr  = len(rem)
    grade += 1

    if debug :
        print("\n ADDED: ")
        print("  ", *add, sep = "\n  ")
        print("\n REMOVED: ")
        print("  ", *rem, sep = "\n  ")
        print("\n new files: " + str(sa) + " and removed: " + str(sr))

    sc = sc + sa - sr
    if (sa == 0) and (sr == 2) and (sc == 414):
        print("Comment :=>> OK: reloading third time with deleted files from disk")
        grade += 1
    else:
        print("Comment :=>> ERROR: reloading third time with deleted files from disk")
    print(" Total in collection: " + str(sc))

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 6: Esborrem tot i tornem a llegir les cançons des de zero
    #         perquè poguem consultar amb files_added() tota la col·lecció
    music_collection = None          # Equivalent a el·liminar la col·lecció
    music_collection = MusicFiles()  # Començem des de zero
    sc  = 0

    music_collection.reload_fs(ROOT)
    print(" ", music_collection)
    add = music_collection.files_added()
    rem = music_collection.files_removed()
    sa  = len(add)
    sr  = len(rem)
    grade += 1

    if debug:
        print(" new files: " + str(sa) + " and removed: " + str(sr))

    sc = sc + sa - sr
    if (sa == 414) and (sr == 0) and (sc == 414):
        print("Comment :=>> OK: restarting reloading last time")
        grade += 1
    else:
        print("Comment :=>> ERROR: restarting reloading last time")
    print(" Total in collection: " + str(sc))

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # End actions
    print(" ", music_collection)
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [16]  --------------------")
    return


# ###########################################################################
# Func2: /* generar ID de cançons */
def func2(debug: int = 0):
    global grade
    global music_collection
    global files_uuids
    print ("Comment :=>> Test: Func2 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Intenta retornar un UUID d'una col·lecció buida
    # Step 2: Intenta esborrar un UUID d'una col·lecció buida
    # Step 3: Genera els UUIDs de tots els MP3 de la col·lecció
    # Step 4: Intenta generar un UUID repetit
    # Step 5: Insereix i esborra multiples vegades
    # Step 6: Check d'un filename ja inserit que ha de retornar el UUID vàlid
    #########################################################################

    if (files_uuids is not None) and (isinstance(files_uuids,MusicID)):
        print("Comment :=>> OK: initializing MusicID")
        grade += 1
    else:
        print("Comment :=>> ERROR: initializing MusicID")

    uu_fake  = "00000000-1111-2222-3333-444444444444"
    ff_fake  = ROOT + os.sep + "nofile.mp3"

    print(" ", files_uuids)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Intenta retornar un UUID d'una col·lecció buida
    uuid = files_uuids.get_uuid(ff_fake)
    if uuid is None:
        print("Comment :=>> OK: not returning UUID from empty collection")
        grade += 1
    else:
        print("Comment :=>> ERROR: returning UUID from empty collection")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Intenta esborrar un UUID d'una col·lecció buida
    files_uuids.remove_uuid(uu_fake)
    if len(files_uuids) == 0:
        print("Comment :=>> OK: not deleting UUID from empty collection")
        grade += 1
    else:
        print("Comment :=>> ERROR: deleting UUID from empty collection")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Genera els UUIDs de tots els MP3 de la col·lecció
    total = 0
    elems = len(music_collection.files_added())
    for file in music_collection.files_added():
        file = cfg.get_canonical_pathfile(file)
        uu = files_uuids.generate_uuid(file)
        if not uu is None:
            total += 1

    if (total == elems) and (total > 0) and (len(files_uuids) == 414):
        print("Comment :=>> OK: Generated UUIDs: " + str(total) + " from files: " + str(elems))
        grade += 1
    else:
        print("Comment :=>> ERROR: Generated UUIDs: " + str(total) + " from files: " + str(elems))

    print(" ", files_uuids)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4: Intenta generar un UUID repetit
    file = music_collection.files_added()[0]
    file = cfg.get_canonical_pathfile(file)
    uu = files_uuids.generate_uuid(file)

    if uu is None:
        print("Comment :=>> OK: UUID repeated")
        grade += 1
    else:
        print("Comment :=>> ERROR: new UUID created: " + str(uu))

    print(" ", files_uuids)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 5: Insereix i esborra multiples vegades
    if debug:
        print(" generating UUID for: " + ff_fake)
    un = files_uuids.generate_uuid(ff_fake)
    print(" ", files_uuids)

    if debug:
        print(" deleting for: " + ff_fake)
    files_uuids.remove_uuid(un)
    print(" ", files_uuids)

    if debug:
        print(" regenerating for: " + ff_fake)
    un = files_uuids.generate_uuid(ff_fake)
    print(" ", files_uuids)

    if debug:
        print(" redeleting for: " + ff_fake)
    files_uuids.remove_uuid(un)
    print(" ", files_uuids)

    if debug:
        print(" redeleting second time for: " + ff_fake)
    files_uuids.remove_uuid(un)
    print(" ", files_uuids)

    if (un is not None) and (len(files_uuids) == 414):
        print("Comment :=>> OK: UUIDs can be deleted")
        grade += 1
    else:
        print("Comment :=>> ERROR: new UUID can't be created after delete it: " + str(uu))

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 6: Check d'un filename ja inserit que ha de retornar el UUID vàlid
    file = music_collection.files_added()[0]
    if debug:
        print(" Check UUID of file: " + file)
    file = cfg.get_canonical_pathfile(file)
    if debug:
        print("   filepath: " + file)
    uu = files_uuids.get_uuid(file)
    if debug:
        print("   uuid: " + uu)

    if not uu is None:
        print("Comment :=>> OK: UUID returned")
        grade += 1
    else:
        print("Comment :=>> ERROR: can't recuperate UUID of: " + file)

    #########################################################################
    # End actions
    print(" ", files_uuids)
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [23]  --------------------")
    return


# ###########################################################################
# Func3: /* consultar metadades cançons */
def func3(debug: int = 0):
    global grade
    global music_collection
    global files_uuids
    global music_data
    print ("Comment :=>> Test: Func3 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Intenta recuperar dades abans de ficar cap element
    # Step 2: Insereix una cancó ficticia i intenta llegir les serves metadades
    # Step 3: Intenta re-insertar la cancó anterior i inserir sense sentit
    # Step 4: Esborra (dos vegades) la cancó existent anterior
    # Step 5: Afegeix totes les cançons de la col·lecció
    # Step 6: Intenta retornar metadades abans de llegir-les
    # Step 7: Llegeix les metadades de totes les cançons i recupera després els valors
    #########################################################################

    if (music_data is not None) and (isinstance(music_data,MusicData) and (len(music_data) == 0)):
        print("Comment :=>> OK: initializing MusicData (0 elements)")
        grade += 1
    else:
        print("Comment :=>> ERROR: initializing MusicData")

    ff_fake  = ROOT + os.sep + "nofile.mp3"
    uu_fake  = "00000000-1111-2222-3333-444444444444"

    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Intenta recuperar dades abans de ficar cap element
    uu       = files_uuids.generate_uuid(ff_fake)
    title    = music_data.get_title(   uu)
    artist   = music_data.get_artist(  uu)
    album    = music_data.get_album(   uu)
    genre    = music_data.get_genre(   uu)
    filename = music_data.get_filename(uu)  # not in public interface

    if  (title    is not None) and \
        (artist   is not None) and \
        (album    is not None) and \
        (genre    is not None) and \
        (filename is not None) :
            print("Comment :=>> ERROR: with empty MusicData class")
    else:
            print("Comment :=>> OK: with empty MusicData class")
            grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Insereix una cancó ficticia i intenta llegir les serves metadades
    music_data.add_song(uu_fake, ff_fake)
    try:
        music_data.load_metadata(uu_fake)
    except OSError:
        print("Comment :=>> OK: not loading fake files")
        grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Intenta re-insertar la cancó anterior i inserir sense sentit
    music_data.add_song(uu_fake, ff_fake)  # Reinsereix per substitució
    music_data.add_song(  ""   , ff_fake)  # No insereix res
    music_data.add_song(uu_fake,   ""   )  # No es pot inserrir
    #  Cap de les anteriors crides genera un error directe
    if len(music_data) == 1:
        print("Comment :=>> OK: adding fake songs (1 element)")
        grade += 1
    else:
        print("Comment :=>> ERROR: adding fake songs")

    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4: Esborra (dos vegades) la cancó existent anterior
    music_data.remove_song(uu_fake)  # Esborra una primera vegada
    music_data.remove_song(uu_fake)  # Aquesta segona no pot tornar a esborrar
    #  Cap de les anteriors crides genera un error directe
    if len(music_data) == 0:
        print("Comment :=>> OK: testing remove songs (0 elements)")
        grade += 1
    else:
        print("Comment :=>> ERROR: testing remove songs")

    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 5: Afegeix totes les cançons de la col·lecció
    for file in music_collection.files_added():
        file = cfg.get_canonical_pathfile(file)
        uuid = files_uuids.get_uuid(file)
        music_data.add_song(uuid, file)
    if len(music_data) == 414:
        print("Comment :=>> OK: testing adding all songs (414 elements)")
        grade += 1
    else:
        print("Comment :=>> ERROR: testing adding all songs")

    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 6: Intenta retornar metadades abans de llegir-les
    errors = 0
    for file in music_collection.files_added():
        file = cfg.get_canonical_pathfile(file)
        uuid = files_uuids.get_uuid(file)
        title    = music_data.get_title(   uuid)
        artist   = music_data.get_artist(  uuid)
        album    = music_data.get_album(   uuid)
        genre    = music_data.get_genre(   uuid)
        filename = music_data.get_filename(uuid)  # not in public interface
        if  (title    is not None) and \
            (artist   is not None) and \
            (album    is not None) and \
            (genre    is not None) and \
            (filename is not None) :
                print("Comment :=>> error with empty metadata elements")
                errors += 1
        else:
            pass

    if errors == 0 :
        print("Comment :=>> OK: with empty metadata elements")
        grade += 1
    else:
        print("Comment :=>> ERROR: with empty metadata elements")

    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 7: Llegeix les metadades de totes les cançons i recupera després els valors
    for file in music_collection.files_added():
        file = cfg.get_canonical_pathfile(file)
        uuid = files_uuids.get_uuid(file)
        music_data.load_metadata(uuid)
    for file in music_collection.files_added():
        file = cfg.get_canonical_pathfile(file)
        uuid = files_uuids.get_uuid(file)
        title    = music_data.get_title(   uuid)
        artist   = music_data.get_artist(  uuid)
        album    = music_data.get_album(   uuid)
        genre    = music_data.get_genre(   uuid)
        filename = music_data.get_filename(uuid)  # not in public interface


    grade += 1
    print("Comment :=>> OK: (expected) when loading metadata elements")

    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # End actions
    files_uuids.remove_uuid(uu)
    print(" ", files_uuids)
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [31]  --------------------")
    return


# ###########################################################################
# Func4: /* reproduir cançó amb metadades */
def func4(debug: int = 0):
    global grade
    global music_collection
    global files_uuids
    global music_data
    global audio_player
    print ("Comment :=>> Test: Func4 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Intenta reproduir una cançó inexistent
    # Step 2: Intenta cridar a print_song() amb un UUID inexistent
    # Step 3: Intenta cridar a play_file() amb un filepath inexistent
    # Step 4: Reprodueix totes les cancons existents dins la col·lecció
    #########################################################################

    if (audio_player is not None) and (isinstance(audio_player,MusicPlayer)):
        print("Comment :=>> OK: initializing MusicPlayer")
        grade += 1
    else:
        print("Comment :=>> ERROR: initializing MusicPlayer")

    cmode    = cfg.PLAY_MODE
    uu_fake  = "00000000-1111-2222-3333-444444444444"
    ff_fake  = ROOT + os.sep + "nofile.m3u"

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Intenta reproduir una cançó inexistent
    audio_player.play_song(uu_fake, cmode)
    print("Comment :=>> OK: (expected) when playing non existent song")
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Intenta cridar a print_song() amb un UUID inexistent
    audio_player.print_song(uu_fake)
    print("Comment :=>> OK: (expected) when print_song() with fake UUID")
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Intenta cridar a play_file() amb un filepath inexistent
    audio_player.play_file(ff_fake)
    print("Comment :=>> OK: (expected) when play_file() with fake filepath")
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4: Reprodueix totes les cancons existents dins la col·lecció
    for idx,file in enumerate(music_collection.files_added()):
        file = cfg.get_canonical_pathfile(file)
        uuid = files_uuids.get_uuid(file)
        audio_player.play_song(uuid, cmode)
    if idx+1 == 414:
        print("Comment :=>> OK: playing all songs (414 elements)")
        grade += 1
    else:
        print("Comment :=>> ERROR: playing all songs")

    print("  MusicPlayer(\'Total played songs: " + str(idx+1) + "\')")

    #########################################################################
    # End actions
    print(" ", files_uuids)
    print(" ", music_data)
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [36]  --------------------")
    return


# ###########################################################################
# Func5: /* reproduir llistes de reproducció m3u */
def func5(debug: int = 0):
    global grade
    global music_collection
    global files_uuids
    global music_data
    global audio_player
    global list_playlist
    print ("Comment :=>> Test: Func5 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Intenta reproduir una PlayList sense cançons
    # Step 2: Intenta llegir un arxiu M3U que no existeix
    # Step 3: Llegeix un arxiu M3U
    # Step 4: Intenta tornar a llegit l'arxiu M3U amb cançons a la PlayList
    # Step 5: Reprodueix la PlayList anterior
    #########################################################################

    if len(list_playlist) == 0:
        print("Comment :=>> OK: initializing PlayList list")
        grade += 1
    else:
        print("Comment :=>> ERROR: initializing PlayList list")

    cmode    = cfg.PLAY_MODE
    ff_fake  = ROOT + os.sep + "nofile.m3u"
    ff_m3u   = ROOT + os.sep + "Blues.m3u"
    pl       = PlayList(files_uuids, audio_player)

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Intenta reproduir una PlayList sense cançons
    if len(pl) == 0:
        print("Comment :=>> OK: empty Playlist")
        grade += 1
    else:
        print("Comment :=>> ERROR: non empty Playlist")
    pl.play(cmode)
    print("Comment :=>> OK: (expected) when playing an empty PlayList")
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Intenta llegir un arxiu M3U que no existeix
    try:
        pl.load_file(ff_fake)
        print("Comment :=>> ERROR: when loading fake M3U files")
    except FileNotFoundError:
        print("Comment :=>> OK: not loading fake M3U files")
        grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Llegeix un arxiu M3U
    try:
        pl.load_file(ff_m3u)
        grade += 1
    except FileNotFoundError:
        print("Comment :=>> ERROR: loading from M3U file: " + ff_m3u)
    if len(pl) == 20:
        print("Comment :=>> OK: loading (20 elements) from M3U file: " + ff_m3u)
        grade += 1
    else:
        print("Comment :=>> ERROR: loading (from M3U file: " + ff_m3u)

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4: Intenta tornar a llegit l'arxiu M3U amb cançons a la PlayList
    try:
        pl.load_file(ff_m3u)
        grade += 1
    except FileNotFoundError:
        print("Comment :=>> ERROR: reloading from M3U file: " + ff_m3u)
    if len(pl) == 20:
        print("Comment :=>> OK: reloading (20 elements) from M3U file: " + ff_m3u)
        grade += 1
    else:
        print("Comment :=>> ERROR: reloading (from M3U file: " + ff_m3u)

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 5: Reprodueix la PlayList anterior
    pl.play(cmode)
    grade += 1
    print("Comment :=>> OK: (expected) when playing the PlayList")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # End actions
    print(" ", pl)
    list_playlist.append(pl)
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [45]  --------------------")
    return


# ###########################################################################
# Func6: /* cercar cançons segons certs criteris */
def func6(debug: int = 0):
    global grade
    global music_collection
    global files_uuids
    global music_data
    global audio_player
    global list_playlist
    global searcher_worker
    print ("Comment :=>> Test: Func6 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Intenta fer cerques amb valors extrems
    # Step 2: Realitza cerques completes
    # Step 3: Realitza cerca NONE
    # Step 4: Opera les cerques anteriors NONE
    # Step 5: Realitza una cerca complexa
    #########################################################################

    if (searcher_worker is not None) and (isinstance(searcher_worker,SearchMetadata)):
        print("Comment :=>> OK: initializing SearchMetadata")
        grade += 1
    else:
        print("Comment :=>> ERROR: initializing SearchMetadata")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Intenta fer cerques amb valors extrems
    search1 = searcher_worker.title(  1234567890 )
    search2 = searcher_worker.title(  str('\0')  )
    search3 = searcher_worker.artist( 1234567890 )
    search4 = searcher_worker.artist( str('\0')  )
    search5 = searcher_worker.album(  1234567890 )
    search6 = searcher_worker.album(  str('\0')  )
    search7 = searcher_worker.genre(  1234567890 )
    search8 = searcher_worker.genre(  str('\0')  )

    if ((len(search1) == 0) and \
        (len(search2) == 0) and \
        (len(search3) == 0) and \
        (len(search4) == 0) and \
        (len(search5) == 0) and \
        (len(search6) == 0) and \
        (len(search7) == 0) and \
        (len(search8) == 0)) :
            print("Comment :=>> OK: search A returns 0 elements")
            grade += 1
    else:
            print("Comment :=>> ERROR: search A returns N elements")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Realitza cerques completes
    search1 = searcher_worker.title(  "" )
    search2 = searcher_worker.artist( "" )
    search3 = searcher_worker.album(  "" )
    search4 = searcher_worker.genre(  "" )

    if ((len(search1) == 414) and \
        (len(search2) == 414) and \
        (len(search3) == 414) and \
        (len(search4) == 414)) :
            print("Comment :=>> OK: search B returns 414 elements")
            grade += 1
    else:
            print("Comment :=>> ERROR: search B returns ? elements")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Realitza cerca NONE
    search1 = searcher_worker.title(  "None" )
    search2 = searcher_worker.artist( "NONE" )
    search3 = searcher_worker.album(  "none" )
    search4 = searcher_worker.genre(  "NOne" )

    if ((len(search1) == 10) and \
        (len(search2) == 25) and \
        (len(search3) == 28) and \
        (len(search4) == 85)) :
            print("Comment :=>> OK: search C returns (10,25,28,85) elements")
            grade += 1
    else:
            print("Comment :=>> ERROR: search C returns ? elements")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4: Opera les cerques anteriors NONE
    search5 = searcher_worker.or_operator(  search1 , search2)
    search6 = searcher_worker.or_operator(  search3 , search4)
    search7 = searcher_worker.and_operator( search5 , search6)
    
    if ((len(search5) ==  25) and \
        (len(search6) == 101) and \
        (len(search7) ==  13)) :
            print("Comment :=>> OK: operations OR:25 OR:101 AND:13 elements")
            grade += 1
    else:
            print("Comment :=>> ERROR: operations OR/AND")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 5: Realitza una cerca complexa
    search1 = searcher_worker.title(  "love"  )
    search2 = searcher_worker.title(  "vie"   )
    search3 = searcher_worker.artist( "derek" )

    result1 = searcher_worker.or_operator(  search1 , search2)
    result2 = searcher_worker.and_operator( result1 , search3)

    if ((len(search1) == 3) and \
        (len(search2) == 1) and \
        (len(search3) == 3) and \
        (len(result1) == 4) and \
        (len(result2) == 1)) :
            print("Comment :=>> OK: complex search 1 element")
            audio_player.print_song(result2[0])
            grade += 1
    else:
            print("Comment :=>> ERROR: in complex search")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [51]  --------------------")
    return


# ###########################################################################
# Func7: /* generar llista basada en una cerca */
def func7(debug: int = 0):
    global grade
    global music_collection
    global files_uuids
    global music_data
    global audio_player
    global list_playlist
    global searcher_worker
    print ("Comment :=>> Test: Func7 (debug=" + str(debug) + ")")
    #########################################################################
    # TESTS:
    # Step 1: Intenta esborrar cançons en una PlayList sense cançons
    # Step 2: Afegeix multiples vegades el mateix UUID (que és vàlid!)
    # Step 3: Esborra la cançó anterior les N vegades inserida
    # Step 4: Torna a intentar esborrar la cançó anterior dues vegades més
    # Step 5: Fer una cerca complexa i generar una PlayList amb el resultat
    # Step 6: Reprodueix la PlayList anterior
    #########################################################################

    cmode    = cfg.PLAY_MODE
    ff_fake  = ROOT + os.sep + "nofile.m3u"
    uu_fake  = "00000000-1111-2222-3333-444444444444"
    pl       = PlayList(files_uuids, audio_player)
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 1: Intenta esborrar cançons en una PlayList sense cançons
    try:
        pl.load_file(ff_fake)
    except OSError:
        print("Comment :=>> OK not loading fake M3U files")
        grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 2: Afegeix multiples vegades el mateix UUID (que és vàlid!)
    pl.add_song_at_end(uu_fake)
    pl.add_song_at_end(uu_fake)
    pl.add_song_at_end(uu_fake)
    pl.add_song_at_end(uu_fake)
    if len(pl) == 4:
        print("Comment :=>> OK: adding repeated songs in a PlayList")
        grade += 1
    else:
        print("Comment :=>> ERROR: adding repeated songs in a PlayList")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 3: Esborra la cançó anterior les N vegades inserida
    pl.remove_first_song()
    pl.remove_last_song()
    pl.remove_first_song()
    pl.remove_last_song()
    if len(pl) == 0:
        print("Comment :=>> OK: deleting/consuming songs from a PlayList")
        grade += 1
    else:
        print("Comment :=>> ERROR: deleting/consuming songs from a PlayList")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 4: Torna a intentar esborrar la cançó anterior dues vegades més
    pl.remove_last_song()
    pl.remove_first_song()
    if len(pl) == 0:
        print("Comment :=>> OK: deleting/consuming songs from an empty PlayList")
        grade += 1
    else:
        print("Comment :=>> ERROR: deleting/consuming songs from an empty PlayList")

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 5: Fer una cerca complexa i generar una PlayList amb el resultat
    search1 = searcher_worker.album( "live"  )
    search2 = searcher_worker.genre( "BLUES" )
    search3 = searcher_worker.genre( "FOLK"  )
    search4 = searcher_worker.genre( "JAZZ"  )

    result1 = searcher_worker.or_operator(  search2 , search3)
    result2 = searcher_worker.or_operator(  result1 , search4)
    result3 = searcher_worker.and_operator( result2 , search1)

    if ((len(search1) == 42) and \
        (len(search2) == 24) and \
        (len(search3) == 14) and \
        (len(search4) == 46) and \
        (len(result1) == 38) and \
        (len(result2) == 84) and \
        (len(result3) == 13)) :
            print("Comment :=>> OK: last complex search 13 element")
            grade += 1
    else:
            print("Comment :=>> ERROR: in last complex search")

    for uuid in result3:
        pl.add_song_at_end(uuid)
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # Step 6: Reprodueix la PlayList anterior
    pl.play(cmode)
    print("Comment :=>> OK (expected) when playing the PlayList of the Search")
    grade += 1

    print ("Grade :=>>", grade)
    print ("Comment :=>> --------------------------------------------")

    #########################################################################
    # End actions
    print(" ", pl)
    list_playlist.append(pl)
    print ("Grade :=>>", grade)
    print ("Comment :=>> Expected Grade is [59]  --------------------")
    return


# ###########################################################################
def main():
# START

    # Func1 --> class MusicFiles.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: MusicFiles (Func1)                    ")
    print ("Comment :=>> --------------------------------------------")
    func1(0)

    # Func2 --> class MusicID.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: MusicID (Func2)                       ")
    print ("Comment :=>> --------------------------------------------")
    func2(0)

    # Func3 --> class MusicData.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: MusicData (Func3)                     ")
    print ("Comment :=>> --------------------------------------------")
    func3(0)

    # Func4 --> class MusicPlayer.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: MusicPlayer (Func4)                   ")
    print ("Comment :=>> --------------------------------------------")
    func4(0)

    # Func5 --> class PlayList.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: PlayList (Func5)                      ")
    print ("Comment :=>> --------------------------------------------")
    func5(0)

    # Func6 --> class SearchMetadata.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: SearchMetadata (Func6)                ")
    print ("Comment :=>> --------------------------------------------")
    func6(0)

    # Func7 --> class PlayList.py
    print ("Comment :=>> --------------------------------------------")
    print ("Comment :=>> Test: PlayList (Func7)                      ")
    print ("Comment :=>> --------------------------------------------")
    func7(0)

    print ("Comment :=>> --------------------------------------------")
    if (grade == 59.0):
        print ("Comment :=>> Final del Test sense errors !!")
    print ("Grade :=>> ", grade)
# END

if __name__ == "__main__":
    main()
    