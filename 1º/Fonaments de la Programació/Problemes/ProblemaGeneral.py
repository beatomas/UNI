#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 12:38:40 2019

@author: beatomas
"""
def LlegirNombre (minim,maxim):
    valor = int(input("Entra un valor entre " +str(minim)+ " i " +str(maxim)+ ": "))
    while ((valor < minim) or (valor > maxim)):
        print("Error: valor incorrecte")
        valor = int(input("Entra un valor entre " +str(minim)+ " i " +str(maxim)+ ": "))   
    return valor
    
def Votar(llista1,llista2):
    i = 0
    while i != 80:
        NIU = int(input("Introdueix el teu NIU: "))
        if NIU in llista1:
            print("Error: Ja has votat")  
        else:
           vot = LlegirNombre(1,4)
           llista2.append(vot)
           llista1.append(NIU)
           i += 1
        

llista1 = []
llista2 = []
llista3 = []

def Escrutini(llista2):
    londres = 0
    paris = 0
    roma = 0
    eivissa = 0
    
    for i in range (0,len(llista2)):
        if llista2[i] == 1:
            londres += 1 
        if llista2[i] == 2:
            paris +=  1
        if llista2[i] == 3:
            roma +=  1
        if llista2[i] == 4:
            eivissa +=  1
    llista3.append(londres)
    llista3.append(paris)
    llista3.append(roma)
    llista3.append(eivissa)
            
    return llista3

def MaximIndex(llista3):
    resultat = max(llista3)
    if resultat == llista3[0]:
        final = "Londres"
    if resultat == llista3[1]:
        final = "París"
    if resultat == llista3[2]:
        final = "Roma"
    if resultat == llista3[3]: 
        final = "Eivissa"
    
    return final


vots = Votar(llista1,llista2)
escrutinis = Escrutini(llista2)
opcio = MaximIndex(llista3)


print("La destinació escollida és",opcio,"amb",max(llista3),"vots")



