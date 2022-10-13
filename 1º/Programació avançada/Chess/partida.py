#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 20:43:25 2020

@author:
"""


from tauler import Tauler
from peca import Rei, Reina, Alfil, Cavall, Torre, Peo
from jugador import Jugador

class Partida():
    
    def __init__(self,tauler="",jugador_actual = "torn_blanques"):
        
        self._tauler = tauler
        self._jugador_actual = "torn_blanques"
        

        t = Torre("A1",0)
        c = Cavall("B1",0)
        a = Alfil("C1",0)
        n = Rei("E1",0)
        r = Reina("D1",0)
        a1 = Alfil("F1",0)
        c1 = Cavall("G1",0)
        t1 = Torre("H1",0)
        p = Peo("A2",0)
        p1 = Peo("B2",0)
        p2 = Peo("C2",0)
        p3 = Peo("D2",0)
        p4 = Peo("E2",0)
        p5 = Peo("F2",0)
        p6 = Peo("G2",0)
        p7 = Peo("H2",0)
        
        self._llista_blanques = [t,c,a,n,r,a1,c1,t1,p,p1,p2,p3,p4,p5,p6,p7]
        
        to = Torre("A8",1)
        co = Cavall("B8",1)
        ao = Alfil("C8",1)
        no = Rei("E8",1)
        ro = Reina("D8",1)
        a1o = Alfil("F8",1)
        c1o = Cavall("G8",1)
        t1o = Torre("H8",1)
        po = Peo("A7",1)
        p1o = Peo("B7",1)
        p2o = Peo("C7",1)
        p3o = Peo("D7",1)
        p4o = Peo("E7",1)
        p5o = Peo("F7",1)
        p6o = Peo("G7",1)
        p7o = Peo("H7",1)
        
        self._llista_negres= [to,co,ao,no,ro,a1o,c1o,t1o,po,p1o,p2o,p3o,p4o,p5o,p6o,p7o]
        
        self._tauler = Tauler(self._llista_blanques,self._llista_negres)
        
        self._jugador_blanques = Jugador(self._llista_blanques,0)
        self._jugador_negres = Jugador(self._llista_negres,1)
        
        
    def realitza_moviment(self,pos_inicial,pos_final):
        
        #print(self._tauler.get_posicio(pos_inicial))
        #print(self._tauler.get_posicio(pos_final))
        
        posicio_array_inicial = self._tauler.busca_posicio(pos_inicial)
        posicio_array_final = self._tauler.busca_posicio(pos_final)
        
        
        if self._jugador_actual == "torn_blanques":
            
            valid = self._jugador_blanques.mou_peca(pos_inicial,pos_final,self._tauler)
            if valid == None:
                valid == [False,False,False]
            
            #print("BLANC")
            if valid == [True, True, True]:
                
                self._jugador_actual = "torn_negres"
                
                self._tauler._estat_partida[posicio_array_final] = self._tauler._estat_partida[posicio_array_inicial] 
                self._tauler._estat_partida[posicio_array_inicial] = "X"
                                
                self._tauler._estat_color[posicio_array_final] = self._tauler._estat_color[posicio_array_inicial] 
                self._tauler._estat_color[posicio_array_inicial] = "X"
                
                self._tauler.set_posicio(pos_inicial,pos_final,0)
                
                return None
                
            
            elif (valid == ["Hi ha una peça", True, True]):
                
                self._jugador_actual = "torn_negres"
                
                self._jugador_negres.mata_peca(pos_final,self._tauler)
                self._tauler._estat_partida[posicio_array_final] = self._tauler._estat_partida[posicio_array_inicial] 
                self._tauler._estat_partida[posicio_array_inicial] = "X"
                
                
                self._tauler._estat_color[posicio_array_final] = self._tauler._estat_color[posicio_array_inicial] 
                self._tauler._estat_color[posicio_array_inicial] = "X"
                
                self._tauler.set_posicio(pos_inicial,pos_final,0)
                
                return True
            
            else:
                return False  
                    
            
        if self._jugador_actual == "torn_negres":
            
            valid = self._jugador_negres.mou_peca(pos_inicial,pos_final,self._tauler)
          
            #print("NEGRE")
            if valid == [True, True, True]:
                self._jugador_actual = "torn_blanques"
                
                self._tauler._estat_partida[posicio_array_final] = self._tauler._estat_partida[posicio_array_inicial] 
                self._tauler._estat_partida[posicio_array_inicial] = "X"
                
                self._tauler._estat_color[posicio_array_final] = self._tauler._estat_color[posicio_array_inicial] 
                self._tauler._estat_color[posicio_array_inicial] = "X"
                
                self._tauler.set_posicio(pos_inicial, pos_final,1)
                
                
                return None
                
            
            elif (valid == ["Hi ha una peça", True, True]):
                
                self._jugador_actual = "torn_blanques"
                
                self._jugador_blanques.mata_peca(pos_final,self._tauler)
                
                self._tauler._estat_partida[posicio_array_final] = self._tauler._estat_partida[posicio_array_inicial] 
                self._tauler._estat_partida[posicio_array_inicial] = "X"
                
                self._tauler._estat_color[posicio_array_final] = self._tauler._estat_color[posicio_array_inicial] 
                self._tauler._estat_color[posicio_array_inicial] = "X"
                
                self._tauler.set_posicio(pos_inicial, pos_final,1)
            
                return True
            
            else:
                return False    
               
    def final_partida(self):
        
        contador_Reiblanques=0
        contador_Reinegres=0
        cantador_pecesblanques=0
        cantador_pecesnegres=0
        
        if self._jugador_blanques.perd() == True:
    
            return 1
            
        if self._jugador_negres.perd() == True:
            
            return 0
        
        for peca in self._llista_blanques:
            if (peca.esta_viva()== True) and peca.get_tipus()=="R":
                contador_Reiblanques = 1
                
            if (peca.esta_viva()== False) and peca.get_tipus()!="R":
                cantador_pecesblanques+=1
        
        for pecan in self._llista_negres:
            if (pecan.esta_viva()== True) and pecan.get_tipus()=="R":
                contador_Reinegres = 1
                
            if (pecan.esta_viva()== False) and pecan.get_tipus()!="R":
                cantador_pecesnegres+=1 
            
        if (contador_Reiblanques==1) and(contador_Reinegres ==1) and (cantador_pecesblanques==15) and (cantador_pecesnegres==15):
            return 2
        
            
                
    def array(self):
        matriu = self._tauler.mostra()
        ult8 = matriu[0]
        ult7 = matriu[1]
        ult6 = matriu[2]
        ult5 = matriu[3]
        ult4 = matriu[4]
        ult3 = matriu[5]
        ult2 = matriu[6]
        ult1 = matriu[7]
        
        self._nova = [ult1,ult2,ult3,ult4,ult5,ult6,ult7,ult8]
        
        return self._nova