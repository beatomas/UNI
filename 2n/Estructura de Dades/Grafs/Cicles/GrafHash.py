# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 15:39:10 2019

@author: gemma
"""
import copy

class GrafHash:
    """Graf amb Adjacency Map structure"""

    class Vertex:
        __slots__ = '_valor'

        def __init__(self, x):
            self._valor=x
                  
        def __str__(self):
            return str(self._valor)
    
################################Definicio Class _Vertex       
    
    def __init__(self, ln=[],lv=[],lp=[],digraf=False):
        """Crea graf (no dirigit per defecte, digraf si dirigit es True.
        """
        self._nodes = { }
        self._out = { }
        self._in = { } if digraf else self._out
              
        for n in ln:
            v=self.insert_vertex(n)
            #nodes[n]=v
        if lp==[]:
            for v in lv:
                self.insert_edge(v[0],v[1])
        else:
            for vA,pA in zip(lv,lp):
                self.insert_edge(vA[0],vA[1],pA)
    
    def es_digraf(self):
        return self._out!=self._in
            
    def insert_vertex(self, x):
        v= self.Vertex(x)
        self._nodes[x] = v
        self._out[x] = { }
        if self.es_digraf():
            self._in[x] = {}
        return v

    def insert_edge(self, n1, n2, p1=1):        
        self._out[n1][n2] = p1
        self._in[n2][n1] = p1
        
    def vertices(self):
        """Return una iteracio de tots els vertexs del graf."""
        return self._nodes.__iter__( )

    def edges(self,x):
        """Return una iteracio de tots els edges de x al graf."""
        return self._out[x].__iter__()
    
    def cicles(self):
        cic=[]
        revisat=[]
        for v1 in self._nodes:
            for v2 in self._out[v1]:
                if v2 not in revisat: 
                    for v3 in self._out[v2]:
                        if self.es_digraf():
                            if v3 in self._in[v1]:
                                if {v1,v2,v3} not in cic:
                                    cic.append({v1,v2,v3})
                        else:
                            if v3 in self._out[v1]:
                                if {v1,v2,v3} not in cic:
                                    cic.append({v1,v2,v3})
                    revisat.append(v2)
                                
        return cic
            
    
    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self._out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+")"+" , " )
                            
            cad = cad + cad1 + "\n"
        
        return cad
        
        
"""
if  self.es_digraf():
            cic=[]
            revisat=[]
            for v1 in self._nodes:
                for v2 in self._out[v1]:
                    if v2 not in revisat: 
                        for v3 in self._out[v2]:
                            if v3 in self._in[v1]:
                                if {v1,v2,v3} not in cic:
                                    cic.append({v1,v2,v3})
                        revisat.append(v2)
                        

        else:
            cic=[]
            revisat=[]
            for v1 in self._nodes:
                for v2 in self._out[v1]:
                    if v2 not in revisat: 
                        for v3 in self._out[v2]:
                            if v3 in self._out[v1]:
                                if {v1,v2,v3} not in cic:
                                    cic.append({v1,v2,v3})
                        revisat.append(v2)
                                
        return cic
"""
    
