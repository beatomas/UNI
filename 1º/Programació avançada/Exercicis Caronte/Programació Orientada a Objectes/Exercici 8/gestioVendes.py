#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:32:50 2020

@author:
"""




from producte import Llibre, Electrodomestic
from venda import VendaPresencial, VendaOnline

class GestioVendes:
    def __init__(self):
        self.llista_productes=[]
        self.llista_vendes=[]
        
    def  llegeixProductes(self, nomFitxer):
        n=0
        fitxer= open(nomFitxer, 'r')
        llista=[]
        for linia in fitxer:
            llista.append(linia.split())
        while n<len(llista):
            if llista[n][0]=="0":
                producte=Llibre(llista[n+1][0], int(llista[n+2][0]), llista[n+3][0], llista[n+4][0], int(llista[n+5][0]))
                self.llista_productes.append(producte)
                n+=6
            else:
                producte=Electrodomestic(llista[n+1][0], int(llista[n+2][0]), llista[n+3][0], llista[n+4][0], int(llista[n+5][0]))
                self.llista_productes.append(producte)
                n+=6
                
                
    def afegeixVendaPresencial(self, codi, unitats, data, identificador):
        res= False
        for y in self.llista_productes:
            if y._codi == codi:
                vp=VendaPresencial(codi, unitats, data, identificador)
                self.llista_vendes.append(vp)
                res = True
                return vp.preu(y)
        if res == False:
            x= -1
        return x
        
    def afegeixVendaOnline(self, codi, unitats, data, adreca):
        res= False
        for y in self.llista_productes:
            if y._codi == codi:
                vo=VendaOnline(codi, unitats, data, adreca)
                preu=vo.preu(y)
                self.llista_vendes.append(vo)
                res= True
                return preu
        if res == False:
            x=-1
            return x
        
       
    def escriuVendes(self, nomFitxer):
        y="\n"
        fitxer= open(nomFitxer, 'w')
        for element in self.llista_vendes:
            fitxer.write(str(element.codi))
            fitxer.write(y)
            fitxer.write(str(element.unitats))
            fitxer.write(y)
            fitxer.write(str(element.data))
            fitxer.write(y)
            if int(element.importe)==float(element.importe):
                fitxer.write(str(int(element.importe)))
                fitxer.write(y)
            else:
                b=str(element.importe)
                fitxer.write(b)
                fitxer.write(y)
            try:
                s=str(int(element.enviament))
                t =str(element.adreca)
                fitxer.write(s)
                fitxer.write(y)
                fitxer.write(t)
                fitxer.write(y)
            except:
                x = str(element.identificador)
                fitxer.write(x)
                fitxer.write(y)