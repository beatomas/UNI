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
        self._nodes = {}
        self._out = { }
        self._in={} if digraf else self._out
        #nodes={}
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
    
    def getOut(self):
        return self._out
        
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
        
    def grauOut(self, x):
        return len(self._out[x])

    def grauIn(self, x):
        return len(self._in[x])
    
    def vertices(self):
        """Return una iteracio de tots els vertexs del graf."""
        return self._nodes.__iter__( )

    def edges(self,x):
        """Return una iteracio de tots els nodes veins de sortida de x al graf."""
        #return self._out[x].items()
        return iter(self._out[x].__iter__())
    
    def DFS(self, nInicial):
        visitat = {}
        recorregut = []
        if nInicial in self._nodes: 
            visitat[nInicial] = None 
            recorregut.append(nInicial)
            self.DFSRec(nInicial,visitat,recorregut)
        return visitat, recorregut
        
    def DFSRec(self, n1, visitat, recorregut):  
        for nVei in self.edges(n1):
            if nVei not in visitat:
                recorregut.append(nVei)
                visitat[nVei]= n1
                self.DFSRec(nVei, visitat,recorregut)
                
    def donaPath(self,n1, n2, visitat):
        vis, rec = self.DFS(n1)
        
        
        nodeactual = n2
        path =[nodeactual] 
        while nodeactual !=n1:
            for node in vis.keys():
                if node == nodeactual:
                    path.append(vis[node])
                    nodeactual = vis[node]
        
        path.reverse()
        return path
                
    def __str__(self):
        cad="===============GRAF===================\n"
     
        for it in self._out.items():
            cad1="__________________________________________________________________________________\n"
            cad1=cad1+str(it[0])+" : "
            for valor in it[1].items():
                cad1=cad1+str(str(valor[0])+"("+ str(valor[1])+")"+" , " )
                            
            cad = cad + cad1 + "\n"
        
        return cad
    
