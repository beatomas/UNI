import sys

class BinaryTree:
    __slots__= '_valor','_pare','_left','_right'
    
    def __init__(self,valor=None,pare=None,FE=None,FD=None):
            self._valor=valor
            self._pare = pare
            self._left = FE
            self._right = FD
        
    
    def read(self,nomF):
        with open(nomF,"rt") as file:
            line = file.readline()
            if line: 
                h=int(line)
                line = file.readline()
                if line: 
                    v = line.split()
                    if len(v)>1:
                        self._addArrel(h,int(v[1]) if v[1].isdigit() else v[1])
                        self.llegirTreeRec(h,file,"ESQ")                                            
                        self.llegirTreeRec(h,file,"DRET")                                            
                            
    def llegirTreeRec(self,h,file,tipFillED):
        if (h > 0):
            line = file.readline()
            if line: 
                val = line.split()
                if len(val)>1:
                    nodPareAct=None
                    #Creem arrel del subarbre actual                   
                    if (tipFillED=="ESQ"):
                        #subarbre actual sera fill esquerre del seu pare
                        nodPareAct=self._addLeft( int(val[1]) if val[1].isdigit() else val[1])                        
                    else:
                        #subarbre actual sera fill dret del seu pare                        
                        nodPareAct=self._addRight( int(val[1]) if val[1].isdigit() else val[1])                        
                    #Creem fill esquerre
                    h-=1                   
                    nodPareAct.llegirTreeRec(h,file,"ESQ")
                    #Creem fill dret
                    nodPareAct.llegirTreeRec(h,file,"DRET")

    def _addArrel(self, h,v):
        """Posa v com a valor de l'arrel a un BinaryTree buit. Raise error si Tree no esta buit"""
        if self._valor is not None: raise sys.ValueError( "Arrel ja existeix")
        self._valor= v
        

    def _addLeft(self, v):
        """Crea fill left i posa _valor v
        retorna node creat que es un binaryTree
        """                        
        if self._valor is not None:
            self._left = BinaryTree(v,self)
        return self._left

    def _addRight(self, v):
        """Crea fill right i posa _valor v
        retorna node creat que es un binaryTree
        """                
        if self._valor is not None:
            self._right = BinaryTree(v,self)
        return self._right
     
    #==================================S19
       
    def esBuit(self):
        return self._valor==None
        
    def fills(self): #Genera iteració dels nodes fills
        if self._left is not None: 
            yield self._left
        if self._right is not None: 
            yield self._right
            
            
    def germa(self):
        if self._pare is None: 
            return None
        if self == self._pare._left: 
            return self._pare._right 
        return self._pare._left

    def esFulla(self): 
        return self._left == self._right == None
  
    def avaluaRec(self,fill):
        if fill.esFulla():
            germa= fill.germa()
            if germa.esFulla():
                
                pare = fill._pare
                op = eval(str(pare._left._valor)+fill._pare._valor+str(pare._right._valor))
                fill._pare._valor = op
                fill._pare._left = None
                fill._pare._right = None
                
                return op
        
        else:
            for fill in fill.fills():
                self.avaluaRec(fill)
        
    def avalua(self):
        if self._left == None and self._right == None:
            return self._valor
        if not self.esBuit():
            while self._left != None and self._right !=None:
               for fill in self.fills():
                   op = self.avaluaRec(fill)
        return op
        
    def __str__(self):
        if self._valor is not None:
            return self.escriuIdent(0)
        else:
            return ""
            
  
    def escriuIdent(self, depth):        
        cadRes = "Comment :=>> " + 2 * depth * " " + str(self._valor)+"\n"
        if self._left is not None:
            cadRes += self._left.escriuIdent(depth+1)
        if self._right is not None:
            cadRes += self._right.escriuIdent(depth+1)        
        return cadRes    
        


