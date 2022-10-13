#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 20:24:58 2019

@author: beatomas
"""
import numpy as np
import matplotlib.pyplot as plt

def carregaDades(fnodes,flinks,fllocs):
    try:
        nodes = np.loadtxt(fnodes, dtype=np.int, delimiter='::', skiprows=0)
        links = np.loadtxt(flinks, dtype=np.int, delimiter='::', skiprows = 0)
        llocs = np.loadtxt(fllocs, dtype=np.str, delimiter='::', skiprows = 0)
    
    except IOError:
        raise IOError("No es poden carregar les dades del mapa.")
    else:
        return {
                "nodes": nodes,
                "links": links,
                "llocs": llocs
        }
   
class Mapa():
    
    def __init__(self, dades):
        self.nodes = dades['nodes']
        self.llocs = dades['llocs']
        self.links = dades['links']
        
    def dibuixaMapa(self):
        # Configuració del tamany de la imatge
        initial_fig_size = plt.rcParams["figure.figsize"]
        plt.rcParams["figure.figsize"] = [15, 15]
         # Preparem les dades
        nodes = self.nodes
        nx = nodes[::, 1]
        ny = nodes[::, 2]
        links = self.links
        llocs = self.llocs
         # Afegim links
        for link in links:
            lx=[nx[link[0]], nx[link[1]]];
            ly=[-ny[link[0]], -ny[link[1]]];
            plt.plot(lx, ly, color='y')
             # Afegim llocs
        for lloc in llocs:
            lli = lloc[0]
            lln = int(lloc[1])
            llx = nx[lln]
            lly = ny[lln]
            plt.plot(llx-2, -lly+2, 'ro', markersize=4)
            plt.annotate(lli, xy=(llx, -lly+30), color='r')
         # Mostrem el mapa
        plt.xlim(0, 6000)
        plt.ylim(-6000, 0)
        plt.axis('off')
        plt.show()
         # Restablim el tamany per defecte de les figures
        plt.rcParams["figure.figsize"] = initial_fig_size
        

    def mostraDirectori(self):
        print("Directori: ")
        for x in self.llocs:
            print (str(x[0])+". "+str(x[2]))
                   
    def obtenirLloc(self,nlloc):
            
            for x in self.llocs:
                if str(nlloc) == x[0]:
                    return x
                        

            raise ValueError("No s'ha trobat el lloc.")
           
  
    def obtenirNode(self, nnode):
       
            for x in self.nodes: 
                if nnode == x[0]:
                    return x

            raise ValueError("No s'ha trobat el node.")
           
            
    
    def obtenirVeins(self, node):
        llista = []
        for x in self.links:
            if x[0] == node[0]:
                enllaç = x[1]
                llista.append(Mapa.obtenirNode(self,enllaç))    
            if x[1] == node[0]:
                enllaç = x[0]
                llista.append(Mapa.obtenirNode(self,enllaç))
    
        return llista
        

    def obtenirLink(self, node1, node2):
        llista = []
        for x in self.links:
            if x[0] == node1[0]:
                if x[1] == node2[0]:
                    llista.append(node1[0])
                    llista.append(node2[0])
            if x[1] == node1[0]:
                if x[0] == node2[0]:
                    llista.append(node1[0])
                    llista.append(node2[0])
            

        return llista
        
    def distanciaEntreNodes(self, node1, node2):
        x1 = node1[1]
        y1 = node1[2]
        x2 = node2[1]
        y2 = node2[2]
        
        distancia =(((x2-x1)**2)+(y2-y1)**2)**(1/2)
        return distancia
        
    def rutaEntreNodes(self, node_origen, node_desti):

        llista_distancies = []
        llista_visitats = []
        distancia_maxima = 10000
        llista_nodes = self.nodes.copy()

        for x in llista_nodes:
            llista_distancies.append(distancia_maxima)
            llista_visitats.append([])
           
        llista_distancies[node_origen[0]] = 0 
        
        while len(llista_nodes) != 0: #> 0:
            #llista = novaLlista.sort(key=lambda node: llista_distancies[node[0]])
            llista_nodes = sorted(llista_nodes, key = lambda node: llista_distancies[node[0]])


            node_avaluat = llista_nodes[0]
            llista_nodes = np.delete(llista_nodes,0,0)
        
            #llista_veins = Mapa.obtenirVeins(self,node_avaluat)
            llista_veins = self.obtenirVeins(node_avaluat)
            
            for vei in llista_veins:
                link_len = 0
                link = self.obtenirLink(node_avaluat, vei)
                if len(link) > 0:
                    link_len = self.distanciaEntreNodes(node_avaluat,vei)
                alt = llista_distancies[node_avaluat[0]] + link_len
                if (alt < llista_distancies[vei[0]]):
                    llista_distancies[vei[0]] = alt
                    llista_visitats[vei[0]] = node_avaluat

        ruta = self.reconstruirRuta(llista_visitats, node_desti, node_origen)
        
        return ruta
    
    def reconstruirRuta(self, nodes_previs, node_desti, node_origen):
         path = []
         node_avaluat = node_desti
         path.append(node_desti)
         while len(node_avaluat) > 0 and node_avaluat[0] != node_origen[0]:
            node_avaluat = nodes_previs[node_avaluat[0]]
            if len(node_avaluat) > 0:
                path.append(node_avaluat)
         return path[::-1]
        
    def dibuixaRuta(self, ruta):
         # Configuració del tamany de la imatge
         initial_fig_size = plt.rcParams["figure.figsize"]
         plt.rcParams["figure.figsize"] = [10, 10]
         # Preparem les dades
         nodes = self.nodes
         nx = nodes[::, 1]
         ny = nodes[::, 2]
         links = self.links
         llocs = self.llocs
         # Afegim links
         for link in links:
             lx=[nx[link[0]], nx[link[1]]];
             ly=[-ny[link[0]], -ny[link[1]]];
             plt.plot(lx, ly, color='y')
         # Afegim llocs
         for lloc in llocs:
             lli = lloc[0]
             lln = int(lloc[1])
             llx = nx[lln]
             lly = ny[lln]
             plt.plot(llx-2, -lly+2, 'ro', markersize=4)
             plt.annotate(lli, xy=(llx, -lly+30), color='r')
         # Afegim la ruta
         index = 0
         while index < len(ruta) - 1:
             n1 = ruta[index]
             n2 = ruta[index+1]
             rx = [n1[1], n2[1]]
             ry = [-n1[2], -n2[2]]
             plt.plot(rx, ry, color='b', linewidth=3)
             index += 1
         # Mostrem el mapa
         plt.xlim(0, 6000)
         plt.ylim(-6000, 0)
         plt.axis('off')
         plt.show()
         # Restablim el tamany per defecte de les figures
         plt.rcParams["figure.figsize"] = initial_fig_size
       
def main():
    fnodes = 'nodes.dat'
    flinks = 'links.dat'
    fllocs = 'llocs.dat'
    
    try: 
        dades_mapa = carregaDades(fnodes,flinks,fllocs)
        mapa = Mapa(dades_mapa)
        mapa.dibuixaMapa()
        
        mapa.mostraDirectori()
        
        n_origen = int(input("Tria el lloc d'origen: "))
        lloc_origen = mapa.obtenirLloc(n_origen)
        node_origen = mapa.obtenirNode(int(lloc_origen[1]))
        
        #print(lloc_origen)
        #print(node_origen)
        
        n_desti = int(input("Tria el lloc de destí: "))
        lloc_desti = mapa.obtenirLloc(n_desti)
        node_desti = mapa.obtenirNode(int(lloc_desti[1]))
        
        #print(lloc_desti)
        #print(node_desti)
        
        #veins_origen = mapa.obtenirVeins(node_origen)
        #veins_desti = mapa.obtenirVeins(node_desti)
        
        #print("Veins origen: ",veins_origen)
        #print("Veins destí: ",veins_desti)
        
        ruta = mapa.rutaEntreNodes(node_origen,node_desti)
        mapa.dibuixaRuta(ruta)

        
    except IOError as missatge:
        print("ERROR: ",missatge)
    except ValueError as missatge:
        print("ERROR: ",missatge)

        
    
main()


