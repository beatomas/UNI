#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:07:10 2020

@author: 
"""



def juga_penjat(paraulaendevinar,maxerrors):
    valor= False
    llistaParaulaMost = []
    llista = []
    llistarepeticions=[]
    intents=int(maxerrors)
    x=list(paraulaendevinar)
    
    
    for item in x:
        llistaParaulaMost.append("-")
        
    print(llistaParaulaMost)
   
     
    while(intents>0 and valor==False):
        if(llistaParaulaMost==x):
            valor = True
        else:
            lletra=input("Introdueix una lletra:")
            
            
            if (lletra in llistarepeticions):
                llista.append("ERROR")     
                
            elif (lletra in x) and (lletra not in llistarepeticions):
                for key,value in enumerate(x):
                    if value==lletra:
                        llistaParaulaMost[key]=lletra
                
                llistaParaula="".join(llistaParaulaMost)
                llista.append(llistaParaula)
                llistarepeticions.append(lletra)
            
               
               
            elif (lletra not in x):
                intents=intents-1
                llistaParaula="".join(llistaParaulaMost)
                llista.append(llistaParaula)
            
           
   
       
    return valor, llistarepeticions, llista
