import random
class MapBase:
    class _Item:
        """Parella de clau,valor que es element de la taula hash o diccionari."""
        __slots__ = "_key" , "_value"
        
        def __init__ (self, k, v):
            self._key = k
            self._value = v

        def __eq__ (self, other):
            return self._key == other._key # compara items segons clay

        def __ne__ (self, other):
            return not (self == other) # oposat de eq

        def __lt__ (self, other):
            return self._key < other._key # compara items
        def __str__(self):
            return "(" + str(self._key)+":"+str(self._value) + ")"
        def __repr__(self):
            return "(" + str(self._key)+":"+str(self._value) + ")"    

class MapUnsorted(MapBase): 
    #Definicio class HAsh Simple sense funcio hash nomes accedeix per klau
    def __init__ (self):
        """Crea una taula hash buida."""
        self._table = []
        
        
    def __getitem__ (self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError(' Key Error: '+ repr(k))

    def __setitem__ (self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        for item in self._table:
            if k == item._key:
                item._value=v
                return
        self._table.append(self._Item(k,v))    

    def __delitem__ (self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        for j in range(len(self._table)):
            if k == self._table[j]._key: # Found a match:
                self._table.pop(j) # remove item
                return # and quit
        raise KeyError(' Key Error: '+ repr(k))

    def __len__ (self):
        """Return number of items in the map."""
        return len(self._table)

    def __iter__ (self):
        """Generate iteration of the map s keys."""
        for item in self._table:
            yield item
            
    def __str__(self):
        return str(self._table)
    
    def __repr__(self):
        return str(self._table)
       
class Hash(MapBase):
   
    def __init__ (self,cap=11, p=109345121):
        """Crea una taula hash buida."""
        self._table = [None]*cap
        self._n = 0
        self._prime = p
        self._scale = 1 + random.randrange(p-1)
        self._shift = random.randrange(p)
        
    def _hash_function(self, k):
        return (hash(k)* self._scale + self._shift) % self._prime % len(self._table)
    
        
    def __iter__ (self):
        for el in self._table:
            if el is not None:
                yield el
        
    def __contains__ (self, k): ###if k in dict.. // if k in table_hash
        try:
            self[k] #crida get item
            return True 
        except KeyError:
            return False
        
        
    #def setdefault(self, k, d):
        #pass
        
    def __getitem__ (self, k):
        """Return value associated with key k (raise KeyError if not found)."""
        j = self._hash_function(k)
        if self._table[j] is None:
            raise KeyError('Key Error:'+repr(k))
        if (self._table[j]._key == k):
            return self._table[j]._value
        else:
            raise KeyError('Key Error:COLLISIO'+repr(k)+'COLLISIO AMB'+repr(self._table[j]._key))
            
            
    def __setitem__ (self, k, v):
        """Assign value v to key k, overwriting existing value if present."""
        j = self._hash_function(k)
        if self._table[j] is None:
            self._table[j] = self._Item(k,v)
            self._n += 1
        elif (self._table[j].key == k): 
            self._table[j]._value = v
        else:
            raise KeyError('Key Error:COLLISIO'+repr(k)+'COLLISIO AMB'+repr(self._table[j]._key))
        if self._n > len(self._table) // 2:
            self._resize(2*len(self._table)-1)
            
    def __delitem__ (self, k):
        """Remove item associated with key k (raise KeyError if not found)."""
        j = self._hash_function(k)
        if (self._table[j] is None):
            raise KeyError('Key Error:NO EXISTEIX'+repr(k))
            
        if not (self._table[j]._key == k):
            raise KeyError('Key Error:COLLISIO'+repr(k)+'COLLISIO AMB'+repr(self._table[j]._key))
        del self._table[j]
        self._n -=1
            
    def __len__ (self):
        """Return number of items in the map."""
        return self._n
           
    def __str__(self):
        return str(self._table)
    
    def __repr__(self):
        return str(self._table)
    
    def _resize(self,c):
        old = [i for i in self]
        self._table = c*[None]
        self._n = 0
        for item in old:
            try: 
                self[item._key]=item._value
            except KeyError:
                print("Comment:=>>COLLISIO",item._key)
        
if __name__ == "__main__":
   grade=0
   print("Comment :=>>=====CREEM DICCIONARI=====\n") 
   h=Hash()
   grade+=0.5
   
   print("Comment :=>>=====MOSTRA DICCIONARI BUIT=====")
   print(h)
   print("\n")
   grade+=0.5
   
   l= [("Hola", "Es una salutacio."),
       ("Adeu","Es un comiat."),
       ("Dia", "Es un periode de 24 hores."),
       ("Mes ", "Es un periode de entre 28 i 31 dies."),
       ("Any", "Es un periode de 12 mesos.")
      ]
   
   print("Comment :=>>=====INICIALITZEM DICCIONARI=====") 
   acceptat=[]
   for e in l:
       try:
           h[e[0]]=e[1]
           acceptat.append(True)
       except KeyError: # otherwise:
           print("Comment :=>> COLLISIO")
           acceptat.append(False)
   grade+=1
   
   print("Comment :=>>=====MOSTRA DICCIONARI AMB ITEMS=====")
   print(h)
   print("\n")
   grade+=0.5
   
   
   print("Comment :=>>=====CONSULTA DICCIONARI ITEMS EXISTENTS=====")
   for i in range(len(l)):       
       if acceptat[i] and l[i][0] in h:
           grade+=0.5
           print("Comment :=>>CORRECTE ", l[i][0], " EXISTEIX A LA TAULA HASH")
           
           print("Comment :=>>Definicio de ", l[i][0], " es: ", h[l[i][0]])
           if (h[l[i][0]]==l[i][1]):
               print("Comment :=>>Definicio CORRECTA \n")
               grade+=0.5
           else:
               print("Comment :=>>Definicio ERRONIA. LA DEFINICIO CORRECTA ES:",l[i][1], "\n")
       elif not(acceptat[i]) :
           print("Comment :=>>CORRECTE ", l[i][0], " HAURIA D'EXISTIR A LA TAULA HASH PERO VA PRODUIR UNA COLLISIO I NO EXISTEIX")
           grade+=1
       else:
           print("Comment :=>>ERROR ", l[i][0], " EXISTEIX A LA TAULA HASH. PERO HAS DIT QUE NO")
           
   print("\n")    
   
   print("Comment :=>>=====CONSULTA DICCIONARI ITEMS NO EXISTENTS ALGUNS PODEN TENIR COLLISIO DEPENENT DE NOMBRES ALEATORIS=====")
   if "ornitorrinco" in h:
       print("Comment :=>>ERROR ornitorrinco NO EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Definicio d'ornitorrinco es: ", h["ornitorrinco"])
   else:
       print("Comment :=>>OK ornitorrinco NO EXISTEIX A LA TAULA HASH")
       grade+=0.5
   print("\n")
   
   if "caleidoscopi" in h:
       print("Comment :=>>ERROR caleidoscopi NO EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Definicio de caleidoscopi es: ", h["caleidoscopi"])
   else:
       print("Comment :=>>OK caleidoscopi NO EXISTEIX A LA TAULA HASH")
       grade+=0.5
   print("\n")
       
   if "caleidoscopi" in h:
       print("Comment :=>>ERROR eina NO EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Definicio d'eina es: ", h["eina"])
   else:
       print("Comment :=>>OK eina NO EXISTEIX A LA TAULA HASH")
       grade+=0.5
   print("\n")
   
   print("Comment :=>>=====MOSTRA DICCIONARI DESPRES DE LES CONSULTES NO EXISTENTS=====")
   print(h)
   print("\n")
   grade+=1
   
   if (grade < 0):
       grade = 0.0
       print("Comment :=>> ------------------------------------------" )
   if (grade == 10.0):
       print("Comment :=>> Final del test sense errors" )
   print("Grade :=>> " , grade )