#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:11:33 2020

@author: 
"""


import os
import re

def llegir_fitxer(fitxer, directori):
    
    paraules_fitxer=[]
    with open (directori+fitxer, 'r') as arxiu:
        for linia in arxiu:
            paraules = (re.sub("[^a-zA-Z0-9]", " ", linia.lower()).split())
            for i in paraules:
                paraules_fitxer.append(i)
        
            
                
        return paraules_fitxer
        
            
    

def llegir_vocabulari(vocabulari, paraules_fitxer):
    diccionari={}
    for paraula in paraules_fitxer:
        if paraula in vocabulari:
            if paraula in diccionari:
                diccionari[paraula]+=1
            else:
                diccionari[paraula]=1
            
    return diccionari

def cal_distancia(entreno, dic_test):
    cont_num=0
    cont_den=0
    cont_den1=0
    cont_den2=0
    for paraula in dic_test.keys():
        if paraula in entreno.keys():
            cont_num+=min(dic_test[paraula], entreno[paraula])
        cont_den1+=dic_test[paraula]
    for paraula in entreno.keys():
        cont_den2+=entreno[paraula]
    cont_den=min(cont_den1, cont_den2)
    distancia=1-(cont_num/cont_den)
    return distancia
    
        
def deteccio_spam(train, test, fitxer_vocabulari, k):
    llista_train=[]
    
    llista_fitxers_train=os.listdir(train)
    llista_fitxers_test=os.listdir(test)
    paraules_vocabulari=llegir_fitxer(fitxer_vocabulari,"")
    
    
    for fitxer in llista_fitxers_train:
        
        paraules_fitxer=llegir_fitxer(fitxer, train)
        dic_fitxer=llegir_vocabulari(paraules_vocabulari, paraules_fitxer)
        
        spam=False
        if 'spmsg' in fitxer:
            spam=True
        llista_train.append((dic_fitxer, spam))
    resultat=[]
      
    for fitxer in llista_fitxers_test:
        llista_distancia=[]
        paraules_fitxer=llegir_fitxer(fitxer, test)
        dic_fitxer=llegir_vocabulari(paraules_vocabulari, paraules_fitxer)
        
        for i in range(len(llista_fitxers_train)):
            distancia=cal_distancia(llista_train[i][0], dic_fitxer)
            tupla_distancia=(distancia, llista_train[i][1])
            llista_distancia.append(tupla_distancia)
        llista_distancia_ordre=sorted(llista_distancia)
        
        llista_k_bool=[]
        llista_k_distancia=[]
        for i in range(k):
            llista_k_distancia.append(llista_distancia_ordre[i][0])
            llista_k_bool.append( llista_distancia_ordre[i][1])
        cont_F=0
        cont_T=0
        for bol in llista_k_bool:
            if bol:
                cont_T+=1
            else:
                cont_F+=1
        res=False
        if cont_T>cont_F:
            res=True
        resultat.append((fitxer,(res, llista_k_distancia, dic_fitxer)))
    return resultat
