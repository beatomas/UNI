#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:32:00 2020

@author:
"""



class Venda:
    def __init__(self, codi, unitats, data):
        self.codi=codi
        self.unitats=unitats
        self.data=data
        
    @property
    def codi(self):
        return self._codi
    @codi.setter
    def codi(self, codi):
        self._codi = codi

    @property
    def unitats(self):
        return self._unitats
    @unitats.setter
    def unitats(self, unitats):
        self._unitats = unitats

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, valor):
        self._data = valor
        
class VendaOnline(Venda):
    def __init__(self, codi, unitats, data, adreca):
        x=super()
        x.__init__(codi, unitats, data)
        self.adreca=adreca
        
    def preu(self, producte):
        des=producte.descompte(self.unitats)
        self.enviament=producte.despesesEnviament()
        preu=producte._preu*self.unitats+self.enviament
        preu=preu*(1-des/100)
        preu=round(preu, 2)
        self.importe=preu
        return preu
        
    @property
    def adreca(self):
        return self._adreca
    @adreca.setter
    def adreca(self, adreca):
        self._adreca= adreca
        
class VendaPresencial(Venda):
    def __init__(self, codi, unitats, data, identificador):
        x= super()
        x.__init__(codi, unitats, data)
        self.identificador=identificador
        
    def preu(self, producte):
        uni = self.unitats
        desco =producte.descompte
        des=desco(uni)
        preu=producte._preu*uni
        preu=preu*(1-des/100)
        self.importe=int(preu)
        return preu
         