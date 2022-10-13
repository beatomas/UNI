#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:23:33 2020

@author:
"""


from abc import ABC, abstractmethod

class Figura(ABC):
    @abstractmethod
    def area (self):
        raise NotImplementedError()
        
        
    @abstractmethod  
    def perimetre(self):
        raise NotImplementedError()
        
        
    @abstractmethod   
    def llegeix(self):
        raise NotImplementedError()
        
    
    @abstractmethod
    def __str__(self):
        raise NotImplementedError()