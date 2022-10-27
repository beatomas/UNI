#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 16:54:14 2020

@author: beatomas
"""


import networkx as nx
import numpy as np

G = nx.Graph() # crear un grafo


G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_node("5")
G.add_node("6")
G.add_node("7")
G.add_node("8")
G.add_node("9")
G.add_node("10")
G.add_node("11")
G.add_node("12")
G.add_node("13")



G.add_edge("1", "2")
G.add_edge("2", "5")
G.add_edge("3", "5")
G.add_edge("4", "5")
G.add_edge("10", "5")
G.add_edge("11", "5")
G.add_edge("6", "5")
G.add_edge("6", "7")
G.add_edge("6", "8")
G.add_edge("6", "9")
G.add_edge("11", "12")
G.add_edge("12", "13")


nx.set_node_attributes(G, np.array([0., 0., 0., 1.]), 'label')

house = ['1', '5', '6', 'Unknown']

one_hot = np.array([
    [1., 0., 0., 0.],
    [0., 1., 0., 0.],
    [0., 0., 1., 0.],
    [0., 0., 0., 1.]]
)



G.nodes['1']['label'] = one_hot[0]
G.nodes['5']['label'] = one_hot[1]
G.nodes['6']['label'] = one_hot[2]

def funcio (pos, llista):
    for n in llista:
        if (n == '1') or (n == '5') or (n == '6'):
            llista.remove(n)
        else:
            if pos == 0:
                node = G.nodes["1"]['label'][0]
                vei = G.nodes[n]['label'][0]
                G.nodes[n]['label'][0]= node or vei
                
            if pos ==1:
                node = G.nodes["1"]['label'][1]
                vei = G.nodes[n]['label'][1]
                G.nodes[n]['label'][1]= node or vei
            
            if pos ==2:
                node = G.nodes["1"]['label'][2]
                vei = G.nodes[n]['label'][2]
                G.nodes[n]['label'][2]= node or vei
            
            if pos ==3:
                node = G.nodes["1"]['label'][3]
                vei = G.nodes[n]['label'][3]
                G.nodes[n]['label'][3]= node or vei




L1=list(G.neighbors('1'))

funcio(0,L1)

print(G.nodes["2"]['label'])
print(G.nodes["13"]['label'])