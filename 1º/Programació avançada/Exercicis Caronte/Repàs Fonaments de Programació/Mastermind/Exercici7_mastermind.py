#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:10:15 2020

@author: 
"""


import random

def genera_combinacio(n_valors,colors_disponibles):
    llista=[]
    claus=list(colors_disponibles.keys())
    for i in range(n_valors):
        n=random.randrange(len(claus))
        llista.append(claus[n])
    return llista

def llegeix_combinacio(n_valors,colors_disponibles):
    combinacio=input("Introdueix la combinació de colors: ")
    res= list(combinacio)
    claus= list(colors_disponibles.keys())
     
    assert len(res) == n_valors,res
    for e in res:
        assert e in claus, res
    return res


def comprova_combinacio(combinacio, codi_secret):
    colors=[]
    for i,j in zip(combinacio,codi_secret):
        if (i==j):
            colors.append(1)
        else:
            colors.append(0)
    return colors
        


def mastermind(n_valors, max_intents, codi_secret, colors_disponibles):
    intents=0
    res=False
    llista_combinacions=[]
    llista_comparacions=[]
    while(intents<=max_intents-1 and res==False):
        try:
            combinacio=llegeix_combinacio(n_valors,colors_disponibles)
            llista_combinacions.append(combinacio)
            comprovacio=comprova_combinacio(combinacio, codi_secret)
            
            if 0 not in comprovacio:
                res=True
            else:
                intents+=1
        except AssertionError:
            llista_comparacions.append("ERROR")
    
    return res,llista_combinacions,llista_comparacions
