#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:15:15 2020

@author:
"""


def juga_sudoku(nom_fitxer_sudoku):
    
    sudoku=np.loadtxt(nom_fitxer_sudoku,dtype="int")    
    llista=[]
    llistamov = []
    numero=1
    
    while(0 in sudoku) and (numero!=0):
        
        numero=int(input("Introdueix un número del 1 al 9:"))
        fila=int(input("Introdueix la fila on vols introduir el nombre:"))
        columna=int(input("Introdueix la columna on vols introduir el nombre:"))

        try:
            valid=es_valid(sudoku,numero,fila,columna)
            if (valid==True):
                sudoku[fila-1:columna-1]= numero
                
            else:
                ("ERROR: La posició no esta buida, o aquest nombre ja està en aquesta fila,columna o requadre.")
        
            llista.append(numero)
            llista.append(fila)
            llista.append(columna)
            llistamov.append(llista)
            llista= []
            
        except:
                print("ERROR: Número, fila o columna incorrecte")
        
        return sudoku,llistamov
            
            
        
            
        

import numpy as np

def es_valid(array,m,f,c):
    assert f >= 1 and f<= 9
    assert c >= 1 and c<= 9
    assert m >= 1 and m<= 9
    a=int((f-1)/3)*3
    b=int((c-1)/3)*3
    valid=m not in array[f-1,:]
    valid=valid and m not in array[:,c-1]
    valid=valid and m not in array[a:a+3,b:b+3]
    valid=valid and array[f-1,c-1]==0
    return valid

def juga_sudoku(nom_fitxer_sudoku):
    sudoku=np.loadtxt(nom_fitxer_sudoku,dtype='int')
    print(sudoku)
    numero=1
    zeros=0 
    for i in sudoku:
        for x in i:
            if x == 0:
                zeros+=1
    llista_mov=list()
    while zeros!=0 and numero!=0:
        numero=int(input())
        if (numero != 0):
            fila=int(input())
            columna=int(input())
            print(numero,fila,columna)
            valid=es_valid(sudoku,numero,fila,columna)
            print(valid)
            if valid == True:
                sudoku[fila-1,columna-1]=numero
                print(sudoku)
                zeros-=1
            else:
                print("ERROR")
            llista_mov.append((numero,fila,columna,valid))
            print(llista_mov)
    print("Final de la partida")
    return sudoku,llista_mov
