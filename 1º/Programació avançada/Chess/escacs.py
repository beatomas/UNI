#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:42:34 2020

@author:
"""


from partida import Partida
import numpy as np
partida = Partida("","torn_blanques")


with open("input.txt","r") as fitxer:
    
    llista_moviments= []
    llista_files= []
    
    for line in fitxer:
        llista_files.append(line)
        


while len(llista_files) != 0:
        
   x = 0
   pos_inicial = llista_files[x][0]+llista_files[x][1]
   pos_final = llista_files[x][3]+llista_files[x][4]
        
   resultat = partida.realitza_moviment(pos_inicial,pos_final)
    
   a = pos_inicial+"\t"+pos_final
    
   if resultat == True:
       llista_moviments.append(a+"\t"+"VALID"+"\t"+"MATA")
    
   if resultat == None:
        
        llista_moviments.append(a+"\t"+"VALID"+"\t"+"NO_MATA")
        
   if resultat == False:
        
        llista_moviments.append(a+"\t"+"NO_VALID"+"\t"+"NO_MATA")  
            
    #y = partida.final_partida()
   del llista_files[0]


a = partida._llista_blanques
z = partida._llista_negres

#for t in a:
    #print(t._esta_viva, t.get_tipus())
    
#for u in z:
    #print(u._esta_viva, u.get_tipus())


y = partida.final_partida()

if (y == 0):
    llista_moviments.append("BLANQUES")
    
if (y == 1):
    llista_moviments.append("NEGRES")
    
if (y == 2):
    llista_moviments.append("EMPAT")

        
with open("output.txt","w") as arxiu:
    for posicio in llista_moviments:
        arxiu.write(posicio+" \n")
        
estat_partida = partida.array()

np.savetxt("tauler.txt",estat_partida,fmt="%s")

#crear una función partida para devolver array

        
        