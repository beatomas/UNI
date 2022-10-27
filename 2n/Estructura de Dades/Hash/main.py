import Hash

    
grade=0
print("Comment :=>>=====CREEM DICCIONARI=====\n") 
th=Hash.Hash()
grade+=0.5
   
print("Comment :=>>=====MOSTRA DICCIONARI BUIT=====")
print(th)
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
           th[e[0]]=e[1]
           print("Comment :=>> AFEGIM : ",e[0])
           acceptat.append(True)
       except KeyError: # otherwise:
           print("Comment :=>> COLLISIO " , e[0])
           acceptat.append(False)
grade+=1
   
print("Comment :=>>=====MOSTRA DICCIONARI AMB ITEMS=====")
print(th)
print("\n")
grade+=0.5
   
   
print("Comment :=>>=====CONSULTA DICCIONARI ITEMS EXISTENTS=====")
for i in range(len(l)):       
       if acceptat[i] and l[i][0] in th:
           grade+=0.5
           print("Comment :=>>CORRECTE ", l[i][0], " EXISTEIX A LA TAULA HASH")
           
           print("Comment :=>>Definicio de ", l[i][0], " es: ", th[l[i][0]])
           if (th[l[i][0]]==l[i][1]):
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
if "ornitorrinco" in th:
       print("Comment :=>>ERROR ornitorrinco NO EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Definicio d'ornitorrinco es: ", th["ornitorrinco"])
else:
       print("Comment :=>>OK ornitorrinco NO EXISTEIX A LA TAULA HASH")
       grade+=0.5
print("\n")
   
if "caleidoscopi" in th:
       print("Comment :=>>ERROR caleidoscopi NO EXISTEIX A LA TAULA HASH")
       print("Comment :=>>Definicio de caleidoscopi es: ", th["caleidoscopi"])
else:
       print("Comment :=>>OK caleidoscopi NO EXISTEIX A LA TAULA HASH")
       grade+=0.5
print("\n")
       
if "eina" in th:
   print("Comment :=>>ERROR eina NO EXISTEIX A LA TAULA HASH")
   print("Comment :=>>Definicio d'eina es: ", th["eina"])
else:
   print("Comment :=>>OK eina NO EXISTEIX A LA TAULA HASH")
   grade+=0.5
print("\n")
   
print("Comment :=>>=====FENT RESIZE OBLIGATORI=====")   
th._resize(len(th._table)*2-1)
grade+=0.5
   
print("Comment :=>>=====MOSTRA DICCIONARI DESPRES DE REHASH OBLIGATORI=====")
print(th)
print("\n")
grade+=0.5
   
if (grade < 0):
   grade = 0.0
   print("Comment :=>> ------------------------------------------" )
if (grade == 10.0):
   print("Comment :=>> Final del test sense errors" )

print("Grade :=>> " , grade )
