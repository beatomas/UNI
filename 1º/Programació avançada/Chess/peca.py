#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 22:57:18 2020

@author:
"""


class Peca:
    def __init__(self,posicio,color):
        self._posicio = posicio
        self._color = color
        self._esta_viva = True
        
    def set_posicio(self,posicio):
        if ((posicio[0] >= 'A') and (posicio[0] <= 'H') and (posicio[1] >= '1') and (posicio[1] <= '8')):
            
            self._posicio = posicio
            
        elif((posicio[0] >= '1') and (posicio[0] <= '8') and (posicio[1] >= 'A') and (posicio[1] <= 'H')):
            x = posicio[0]
            y = posicio[1]
            self._posicio = y+x
            
        else:
            raise ValueError('Valor incorrecte posició')
    
    def get_posicio(self):
        return self._posicio
    
    def mata(self):
        self._esta_viva = False
        
    def esta_viva(self):
        return self._esta_viva
        
    
    def get_tipus(self):
        return self._tipus
        
    def moviment_valid(self,pos_final,tauler):
        x = pos_final[0]
        y = pos_final[1]#tauler = Classe Tauler
        if((pos_final[0] >= '1') and (pos_final[0] <= '8') and (pos_final[1] >= 'A') and (pos_final[1] <= 'H')):
            pos_final = y+x
        valid = []
        
        if (tauler.get_posicio(self._posicio) != self._color) or (self._color == 2):
            valid.append(False)
            valid.append(False)
            valid.append(False)
        
        if len(valid) == 0:
            
            if (tauler.get_posicio(pos_final) == "X"):
                valid.append(True)
                
            if (tauler.get_posicio(pos_final) == 2):
                valid.append(False)
                valid.append(False)
                valid.append(False)
            
            if (tauler.get_posicio(pos_final) == self._color):
                valid.append(False)
            
            if (tauler.get_posicio(pos_final) != self._color) and (tauler.get_posicio(pos_final) != "X") and  (tauler.get_posicio(pos_final) != 2): 
                valid.append("Hi ha una peça")
            
        
        return valid


class Alfil(Peca):
    def __init__(self,posicio,color):
        super().__init__(posicio,color)
        self._tipus = "A"
        
        if color == 0:
            
            self._color = 0
        else:
            self._color= 1
            
            
    def moviment_valid(self,pos_final,tauler):
        valid = super().moviment_valid(pos_final,tauler)
        llista_lletres=["A","B","C","D","E","F","G","H"]
        llista_numeros=[1,2,3,4,5,6,7,8]
    
        x = pos_final[0]
        y = pos_final[1]
        if x in llista_lletres:
            pos_final = x+y
        else:
            pos_final = y+x
    
        lletra_inicial= self._posicio[0]
        numero_inicial = int(self._posicio[1])
        lletra_final= pos_final[0]
        numero_final = int(pos_final[1])
        
        llet1 = llista_lletres.index(lletra_inicial)
        num1 = llista_numeros.index(numero_inicial)
        
        llet2 = llista_lletres.index(lletra_final)
        num2 = llista_numeros.index(numero_final)
        contador = 0
    
        if valid ==[True] or valid ==["Hi ha una peça"]:
        
            if (lletra_inicial != lletra_final) and (numero_inicial!=numero_final) and ((llet2-llet1) == (num2-num1)) or ((llet2-llet1) == (num1-num2)):
                
                valid.append(True)
            else:
                valid.append(False)
                valid.append(False)
        
        if (valid==[True,True]) or valid==["Hi ha una peça",True]:
            
            if (llet1 < llet2) and (num1 < num2):
                llista=[]
                llista2=[]
            
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 < inde and llet2 > inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i>numero_inicial and i<numero_final):
                        llista2.append(i)
            
                for r in llista:
                    q = 0
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[q])
                
                    fin = pos1+pos2
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                        
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
                return valid
                
                
            if (llet1 < llet2) and (num1>num2):
                llista=[]
                llista2=[]
                
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 < inde and llet2 > inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i<numero_inicial and i>numero_final):
                        llista2.append(i)
            
                for r in llista:
                    q = 0
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[q])
                
                    fin = pos1+pos2
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                        
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
                return valid
                
            
            if (llet1 > llet2) and (num1<num2):
                llista=[]
                llista2=[]
                
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 > inde and llet2 < inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i>numero_inicial and i<numero_final):
                        llista2.append(i)
            
                for r in llista:
                    q = 0
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[q])
                
                    fin = pos1+pos2
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                        
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
                return valid
            
            
            if (llet1 > llet2) and (num1>num2):
                llista=[]
                llista2=[]
                
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 > inde and llet2 < inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i<numero_inicial and i>numero_final):
                        llista2.append(i)
            
                for r in llista:
                    q = 0
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[q])
                
                    fin = pos1+pos2
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                        
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
        if valid == [False]:
            valid.append(False)
            valid.append(False)
                        
        return valid
    


class Torre(Peca):
    def __init__(self,posicio,color):
        super().__init__(posicio,color)
        
        self._tipus = "T"
        
        if color == 0:
            
            self._color = 0
        else:
            self._color= 1
        
    def moviment_valid(self,pos_final,tauler):
        valid = super().moviment_valid(pos_final,tauler)
        
        llista_lletres=["A","B","C","D","E","F","G","H"]
        llista_numeros=[1,2,3,4,5,6,7,8]
    
        x = pos_final[0]
        y = pos_final[1]
        if x in llista_lletres:
            pos_final = x+y
        else:
            pos_final = y+x
        
        lletra_inicial= self._posicio[0]
        numero_inicial = int(self._posicio[1])
        lletra_final= pos_final[0]
        numero_final = int(pos_final[1])
        
        llet1 = llista_lletres.index(lletra_inicial)
        num1 = llista_numeros.index(numero_inicial)
        llet2 = llista_lletres.index(lletra_final)
        num2 = llista_numeros.index(numero_final)
        llista2=[]
        contador = 0
        
        if valid ==[True] or valid == ["Hi ha una peça"]:
            if ((lletra_inicial == lletra_final) or (numero_inicial == numero_final)):
                valid.append(True)
            else:
                valid.append(False)
                valid.append(False)
                
        
        if (valid==[True,True]) or valid==["Hi ha una peça",True]:
        
            if (lletra_inicial == lletra_final) and (num1<num2):
                
                for i in llista_numeros:
                    if (i>numero_inicial and i<numero_final):
                        llista2.append(i)
                for q in llista2:
            
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
                    
                     
                        
            if (lletra_inicial == lletra_final) and (num1>num2):
        
                for i in llista_numeros:
                    if (i<numero_inicial and i>numero_final):
                        llista2.append(i)
            
                for q in llista2:
                
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
        
    
            if (llet1 < llet2) and (numero_inicial==numero_final):
                
                for x in llista_lletres:
                    indice = llista_lletres.index(x)
                    if (llet1 > indice and llet2 < indice):
                        llista2.append(x)
        
            
                for q in llista2:
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
        
    
            if (llet1 > llet2) and (numero_inicial==numero_final):
        
                for x in llista_lletres:
                    if (llet1 <x and llet2 >x):
                        llista2.append(x)
            
            
                for q in llista2:
                   
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
                      
        if valid == [False]:
            valid.append(False)
            valid.append(False)
            
        return valid
    
 
     
class Rei(Peca):
    def __init__(self,posicio, color):
        super().__init__(posicio,color)
        self._tipus = "R"
        
        if color == 0:
            
            self._color = 0
        else:
            self._color= 1
        
    def moviment_valid(self,pos_final,tauler):
        valid = super().moviment_valid(pos_final,tauler)
                
        lletra_inicial= self._posicio[0]
        numero_inicial = int(self._posicio[1])
        lletra_final= pos_final[0]
        numero_final = int(pos_final[1])
        llista_lletres=["A","B","C","D","E","F","G","H"]
        
        llet1= llista_lletres.index(lletra_inicial)
        llet2= llista_lletres.index(lletra_final)
    
        if valid == [True] or valid ==["Hi ha una peça"]:
            
            if ((numero_inicial==numero_final) or (numero_inicial==numero_final-1) or (numero_inicial==numero_final+1)):
                if (llet1 == llet2-1) or (llet1 == llet2+1) or (llet1 == llet2):
                    valid.append(True)
                    valid.append(True)
                else:
                    valid.append(False)
                    valid.append(False)     
            
        if valid == [False]:
            valid.append(False)
            valid.append(False)
        
        
        return valid


class Reina(Peca):
    def __init__(self,posicio,color):
        super().__init__(posicio,color)
        self._tipus = "N"
        
        if color == 0:
            
            self._color = 0
        else:
            self._color= 1
        
    def moviment_valid(self,pos_final,tauler):
        valid = super().moviment_valid(pos_final,tauler)
        llista_lletres=["A","B","C","D","E","F","G","H"]
        llista_numeros=[1,2,3,4,5,6,7,8]
    
        x = pos_final[0]
        y = pos_final[1]
        if x in llista_lletres:
            pos_final = x+y
        else:
            pos_final = y+x
        
        lletra_inicial= self._posicio[0]
        numero_inicial = int(self._posicio[1])
        lletra_final= pos_final[0]
        numero_final = int(pos_final[1])
        
                
        llet1= llista_lletres.index(lletra_inicial)
        num1= llista_numeros.index(numero_inicial)
                
        llet2= llista_lletres.index(lletra_final)
        num2= llista_numeros.index(numero_final)
        llista=[]
        llista2=[]
        contador = 0
        
        if valid == [True] or valid ==["Hi ha una peça"]:
            llista_random=[]
                    
            if (lletra_inicial != lletra_final) and (numero_inicial!=numero_final) and ((llet2-llet1) == (num2-num1)) or ((llet2-llet1) == (num1-num2)):
                llista_random.append(True)
                
            else:
                llista_random.append(False)
            
            if  (lletra_inicial == lletra_final) or (numero_inicial == numero_final):
                llista_random.append(True)
            else:
                llista_random.append(False)
            
            if True in llista_random:
                valid.append(True)
            else:
                valid.append(False)
                valid.append(False)
                
        if (valid==[True,True]) or valid==["Hi ha una peça",True]:
        
            if (lletra_inicial == lletra_final) and (num1<num2):
                #print("NO ENTRAR")
                for i in llista_numeros:
                    if (i>numero_inicial and i<numero_final):
                        llista2.append(i)
                for q in llista2:
            
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
                    
                     
                        
            if (lletra_inicial == lletra_final) and (num1>num2):
                #print("NO ENTRAR")
                for i in llista_numeros:
                    if (i<numero_inicial and i>numero_final):
                        llista2.append(i)
            
                for q in llista2:
                
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
        
    
            if (llet1 < llet2) and (numero_inicial==numero_final):
                #print("NO ENTRAR")
                for x in llista_lletres:
                    indice = llista_lletres.index(x)
                    if (llet1 > indice and llet2 < indice):
                        llista2.append(x)
        
            
                for q in llista2:
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
        
    
            if (llet1 > llet2) and (numero_inicial==numero_final):
                #print("NO ENTRAR")
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 < inde and llet2 > inde):
                        llista2.append(x)
            
            
                for q in llista2:
                   
                    q = 0
                    pos1 = str(lletra_inicial)
                    pos2 = str(llista2[q])
                    fin = pos1+pos2
                    q += 1
                    
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
            
                if contador == len(llista2):
                    valid.append(True)
                    
                else:
                    valid.append(False)
                            
                
            if (llet1 < llet2) and (num1 < num2):
                llista=[]
                llista2=[]
            
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 < inde and llet2 > inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i>numero_inicial and i<numero_final):
                        llista2.append(i)
                        
                for r in llista:
                    q = 0
                    x = len(llista2)
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[x])
                
                    fin = pos1+pos2
                    x-=1
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
                return valid
                
                
            if (llet1 < llet2) and (num1 > num2):
                llista=[]
                llista2=[]
                #print("DEBERIA ENTRAR")
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 < inde and llet2 > inde):
                        llista.append(x)
                
                for i in llista_numeros:
                    if (i<numero_inicial and i >numero_final):
                        llista2.append(i)
                
            
                q = 0
                x = len(llista2)
                
                for r in llista:                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[x-1])
                
                    fin = pos1+pos2
                   
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                    q+=1
                    x-=1
                    
                
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
                return valid
                
            
            if (llet1 > llet2) and (num1<num2):
                llista=[]
                llista2=[]
                
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 > inde and llet2 < inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i>numero_inicial and i<numero_final):
                        llista2.append(i)
            
                for r in llista:
                    q = 0
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[q])
                
                    fin = pos1+pos2
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                        
                if contador == len(llista):
                    valid.append(True)
                    
                else:
                    valid.append(False)
                        
                return valid
            
            
            if (llet1 > llet2) and (num1>num2):
                llista=[]
                llista2=[]
                
                for x in llista_lletres:
                    inde = llista_lletres.index(x)
                    if (llet1 > inde and llet2 < inde):
                        llista.append(x)
                    
                for i in llista_numeros:
                    if (i<numero_inicial and i>numero_final):
                        llista2.append(i)
            
                for r in llista:
                    q = 0
                
                    pos1 = str(llista[q])
                    pos2 = str(llista2[q])
                
                    fin = pos1+pos2
                    q+=1
                
                    if (tauler.get_posicio(fin) == "X"): 
                        contador += 1
                        
                if contador == len(llista):
                    valid.append(True)
                else:
                    valid.append(False)
                        
                
        if valid == [False]:
            valid.append(False)
            valid.append(False)
                        
        return valid

class Cavall(Peca):
    def __init__(self,posicio,color):
        super().__init__(posicio,color)
        self._tipus = "C"
        
        if color == 0:
            self._color = 0
        else:
            self._color= 1
        
    def moviment_valid(self,pos_final,tauler):
        valid = super().moviment_valid(pos_final,tauler)
        llista_lletres=["A","B","C","D","E","F","G","H"]  
        x = pos_final[0]
        y = pos_final[1]
        if x in llista_lletres:
            pos_final = x+y
        else:
            pos_final = y+x
            
        lletra_inicial= self._posicio[0]
        numero_inicial = int(self._posicio[1])
        lletra_final= pos_final[0]
        numero_final = int(pos_final[1])
    
        pos_in= llista_lletres.index(lletra_inicial)
        pos_fin = llista_lletres.index(lletra_final)
            
        if valid ==[True] or valid ==["Hi ha una peça"]:
            
            if (numero_inicial==numero_final) or (lletra_inicial == lletra_final):
                valid.append(False)
                valid.append(True)
                
            if (pos_in == pos_fin-1) or (pos_in == pos_fin+1): #moviment vertical
                if (numero_inicial == numero_final+2) or (numero_inicial == numero_final-2):
                    valid.append(True)
                    valid.append(True)
                else:
                    valid.append(False)
                    valid.append(True)
           
                    
            if (pos_in == pos_fin-2) or (pos_in == pos_fin+2): #moviment horitzontal
                if (numero_inicial == numero_final+1) or (numero_inicial == numero_final-1):
                    valid.append(True)
                    valid.append(True)
                else:
                    valid.append(False)
                    valid.append(True)        
                    
                    
        else:
            valid.append(False)
            valid.append(False)
       
        return valid


class Peo(Peca):
    def __init__(self,posicio,color):
        super().__init__(posicio,color)
        self._tipus = "P"
        if color == 0:
            self._color = 0
        else:
            self._color= 1
        
    def moviment_valid(self,pos_final,tauler):
        valid = super().moviment_valid(pos_final,tauler)
        llista_lletres=["A","B","C","D","E","F","G","H"]
    
        x = pos_final[0]
        y = pos_final[1]
        if x in llista_lletres:
            pos_final = x+y
        else:
            pos_final = y+x
        
        lletra_inicial= self._posicio[0]
        numero_inicial = int(self._posicio[1])
        lletra_final= pos_final[0]
        numero_final = int(pos_final[1])
            
        llet1 = llista_lletres.index(lletra_inicial)
        llet2 = llista_lletres.index(lletra_final)
        
        if valid == [True] or valid == ["Hi ha una peça"]:
            
            if (lletra_inicial == lletra_final):
                
                if (self._color == 0):
                    if (numero_inicial == numero_final - 1):
                        valid.append(True)
                        valid.append(True)
                    else:
                        valid.append(False)
                        valid.append(False)
                       
                
                
                if (self._color == 1):
                    if (numero_inicial == numero_final + 1):
                        valid.append(True)
                        valid.append(True)
                        
                    else:
                        valid.append(False)
                        valid.append(False)
                        
        
            elif (tauler.get_posicio(pos_final) != self._color) and (tauler.get_posicio(pos_final) != "X"):
    
                if (self._color == 0):
                    if ((llet1 == llet2+1) and (numero_inicial == numero_final+1)) or ((llet1== llet2-1) and (numero_inicial== numero_final-1)):
                        valid.append(True)
                        valid.append(True)
                        
                    else:
                        valid.append(False)
                        valid.append(False)
                                            
                if (self._color == 1):
                    if ((llet1 == llet2+1) and (numero_inicial == numero_final+1)) or ((llet1== llet2-1) and (numero_inicial== numero_final-1)):
                        valid.append(True)
                        valid.append(True)
                        
                    else:
                        valid.append(False)
                        valid.append(False)
                        
            else:
                valid.append(False)
                valid.append(False)
                
        return valid
   
