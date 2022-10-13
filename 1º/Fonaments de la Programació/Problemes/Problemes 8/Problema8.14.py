
import random

class Carta():
    def __init__(self,rang,pal):
        self.rangs = rang
        self.pals = pal
      
        if self.pals == 0:
            self.pal = "Copes"
        if self.pals == 1:
            self.pal = "Espases"
        if self.pals == 2:
            self.pal = "Bastos"
        if self.pals == 3:
            self.pal = "Oros"
    
        if self.rangs == 0:
            self.rang = "As"
        if self.rangs == 11:
            self.rang = "Cavall"
        if self.rangs == 10:
            self.rang = "Sota"
        if self.rangs == 12:
            self.rang = "Rei"
            
        if self.rangs == 1:
            self.rang = self.rangs
        if self.rangs == 2:
            self.rang = self.rangs
        if self.rangs == 3:
            self.rang = self.rangs
        if self.rangs == 4:
            self.rang = self.rangs
        if self.rangs == 5:
            self.rang = self.rangs
        if self.rangs == 6:
            self.rang = self.rangs
        if self.rangs == 7:
            self.rang = self.rangs
        if self.rangs == 8:
            self.rang = self.rangs
        if self.rangs == 9:
            self.rang = self.rangs
    
    def __str__(self):
        return str(self.rang)+" de "+str(self.pal)

class Baralla():
    def __init__(self):
        self.Munt = []
        for p in range(4):
            for r in range(12):
                c = Carta(r,p)
                self.Munt.append(c)
                
    def __str__(self):
        out = ""
        for c in self.Munt:
            out = out + str(c)+ "\n"
        return(out)
    
    def pop_carta(self):
        return(self.Munt.pop())
    
    def add_carta(self,carta):
        self.Munt.append(carta)
    
    def barrejar(self):
        random.shuffle(self.Munt)
        
class Ma(Baralla):
    def __init__(self):
        self.Munt = []
        

#CARONTE

import random

class Carta():
    def __init__(self,rang,pal):
        self.rangs = rang
        self.pals = pal
      
        if self.pals == 0:
            self.pal = "Copes"
        if self.pals == 1:
            self.pal = "Espases"
        if self.pals == 2:
            self.pal = "Bastos"
        if self.pals == 3:
            self.pal = "Oros"
    
        if self.rangs == 0:
            self.rang = "As"
        if self.rangs == 10:
            self.rang = "Cavall"
        if self.rangs == 9:
            self.rang = "Sota"
        if self.rangs == 11:
            self.rang = "Rei"
            
        if self.rangs == 1:
            self.rang = self.rangs
        if self.rangs == 2:
            self.rang = self.rangs
        if self.rangs == 3:
            self.rang = self.rangs
        if self.rangs == 4:
            self.rang = self.rangs
        if self.rangs == 5:
            self.rang = self.rangs
        if self.rangs == 6:
            self.rang = self.rangs
        if self.rangs == 7:
            self.rang = self.rangs
        if self.rangs == 8:
            self.rang = self.rangs
      
    
    def __str__(self):
        return str(self.rang)+" de "+str(self.pal)

class Baralla():
    def __init__(self):
        self.Munt = []
        for p in range(4):
            for r in range(12):
                c = Carta(r,p)
                self.Munt.append(c)
                
    def __str__(self):
        out = ""
        for c in self.Munt:
            out = out + str(c)+ "\n"
        return(out)
    
    def pop_carta(self):
        return(self.Munt.pop())
    
    def add_carta(self,carta):
        self.Munt.append(carta)
    
    def barrejar(self):
        random.shuffle(self.Munt)
        
class Ma(Baralla):
    def __init__(self):
        self.Munt = []
        
