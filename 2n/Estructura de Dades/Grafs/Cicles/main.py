import GrafHash

grade = 0
print ("Comment :=>> =================================")
print ("Comment :=>> Iniciant TEST CICLES")
print ("Comment :=>> =================================")
print ("Comment :=>>")



nodes=[["T1","T2","T3","T4","T5","T6","T7","T8","T9","T10","T11"],
       ["Pl. Sants","Hostafr.","Esp.","Roc.","Urgell","Univ.","Cat.","Urq.","Triomf","Marina","Glòries","Clot","Navas","Sagrera",
				 "Paral·lel","St. Ant.","Pg. Gràcia","Tetuan","Monumental","S. Família","Encants","Bac Roda","Sant Martí","La Pau",
		         "Sants Est.","Tarragona","Poble Sec","Drassanes","Liceu","Diagonal",
				  "Besòs","Besòs Mar","El Maresme","Selva Mar","Poblenou","Llacuna","Bogatell","Ciutadella","Barcelone.","Jaume I","Girona","Verdaguer","Joanic","Alfons X",
		          "Guinardó","Maragall","Llucmajor","Via Júlia",
		          "Entença","H. Clínic","Sant Pau","Camp Arpa","Congrés"],
        ["Tu","Marta","Maria","Jordi","Berta","Aritz","Nikita",
                     "Joshua","Marc","Mar","Umair","Neus","LA persona"]]         
relacions=[[["T1","T2"],["T1","T3"],["T1","T4"],["T2","T5"],["T2","T6"],
                      ["T3","T2"],["T3","T4"],["T4","T6"],
                      ["T5","T8"],["T5","T9"],["T6","T5"],["T6","T7"],
                      ["T7","T4"],["T7","T9"],["T7","T10"],
                      ["T8","T9"],["T8","T11"],["T9","T10"],["T9","T11"],
                      ["T10","T11"]],
            [['Pl. Sants', 'Hostafr.'],['Hostafr.', 'Esp.'],['Esp.', 'Roc.'],['Roc.', 'Urgell'],['Urgell', 'Univ.'],['Univ.', 'Cat.'],['Cat.', 'Urq.'],['Urq.', 'Triomf'],
                       ['Triomf', 'Marina'],['Marina', 'Glòries'],['Glòries', 'Clot'],['Clot', 'Navas'],['Navas', 'Sagrera'],['Paral·lel', 'St. Ant.'],['St. Ant.', 'Univ.'],
                       ['Univ.', 'Pg. Gràcia'],['Pg. Gràcia', 'Tetuan'],['Tetuan', 'Monumental'],['Monumental', 'S. Família'],['S. Família', 'Encants'],['Encants', 'Clot'],
                       ['Clot', 'Bac Roda'],['Bac Roda', 'Sant Martí'],['Sant Martí', 'La Pau'],['Sants Est.', 'Tarragona'],['Tarragona', 'Esp.'],['Esp.', 'Poble Sec'],
                       ['Poble Sec', 'Paral·lel'],['Paral·lel', 'Drassanes'],['Drassanes', 'Liceu'],['Liceu', 'Cat.'],['Cat.', 'Pg. Gràcia'],['Pg. Gràcia', 'Diagonal'],
                       ['La Pau', 'Besòs'],['Besòs', 'Besòs Mar'],['Besòs Mar', 'El Maresme'],['El Maresme', 'Selva Mar'],['Selva Mar', 'Poblenou'],['Poblenou', 'Llacuna'],
                       ['Llacuna', 'Bogatell'],['Bogatell', 'Ciutadella'],['Ciutadella', 'Barcelone.'],['Barcelone.', 'Jaume I'],['Jaume I', 'Urq.'],['Urq.', 'Pg. Gràcia'],
                       ['Pg. Gràcia', 'Girona'],['Girona', 'Verdaguer'],['Verdaguer', 'Joanic'],['Joanic', 'Alfons X'],['Alfons X', 'Guinardó'],['Guinardó', 'Maragall'],
                       ['Maragall', 'Llucmajor'],['Llucmajor', 'Via Júlia'],['Pl. Sants', 'Sants Est.'],['Sants Est.', 'Entença'],['Entença', 'H. Clínic'],['H. Clínic', 'Diagonal'],
                       ['Diagonal', 'Verdaguer'],['Verdaguer', 'S. Família'],['S. Família', 'Sant Pau'],['Sant Pau', 'Camp Arpa'],['Camp Arpa', 'Sagrera'],['Sagrera', 'Congrés'],
                       ['Congrés', 'Maragall']
            ],
            [["Tu","Maria"],["Tu","Jordi"],["Tu","Marc"],
                     ["Maria","Marta"],["Maria","Jordi"],["Maria","Aritz"],
                     ["Jordi","Berta"],
                     ["Berta","Nikita"],["Berta","Joshua"],
                     ["Aritz","Nikita"],
                     ["Joshua","LA persona"],
                     ["Marc","Mar"],["Marc","Umair"],
                     ["Umair","Neus"],["Umair","LA persona"],
                     ["LA persona","Neus"]]
            ]
pesos=[[5,5,5,10,10,7,7,4,4,3,3,6,6,9,9,1,2,8,8,4],
       [511,995,425,2271,1782,787,375,1603,493,960,1212,499,1181,647,494,124,1794,1607,536,1781,311,708,186,882,1796,1132,1090,1145,2393,1730,620,442,1654,706,292,305,1204,
             617,20,1242,184,655,2034,1170,281,979,1569,990,461,1702,1024,986,647,113,1585,520,962,1339,662,851,1695,1337,622,1290 ],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
      ]
dirigit=[True,False,False]
nodeInicial=["T1","Sants Est.","Tu"]    
nodeFinal=["T11","Besòs Mar","LA persona"]
solucions=[[set(['T4', 'T6', 'T7'])],
           [set(['Cat.', 'Pg. Gràcia', 'Univ.']),set( ['Cat.', 'Pg. Gràcia', 'Urq.'])],
           [set(['Jordi', 'Maria', 'Tu']),set( ['LA persona', 'Neus', 'Umair'])]]
punts=[3,4,3]
i=0

for n,r,p in zip(nodes,relacions,pesos):
    print ("Comment :=>> ========================================")
    print ("Comment :=>> Test CICLES graf:",i)
    print ("Comment :=>> ========================================")
    g=GrafHash.GrafHash(n,r,p,dirigit[i])
    
    print ("Comment :=>> Calculant CICLES graf:",i)
    cicles=g.cicles()
    
    correcteCicles=True
    if (len(cicles)==len(solucions[i])):
        for posCicle in range(len(cicles)):
            if not cicles[posCicle] in cicles:
                print ("Comment :=>> ERROR HAS DONAT EL CICLE: ", cicles[posCicle], "Cicle inexistent")
                correcte = False
                break            
    else:
        print ("Comment :=>> ERROR AL NOMBRE DE CICLES DONAT")
        correcteCicles = False
        correcte = False
        
    if correcteCicles:                
        print ("Comment :=>> -----------------------------------------------")
        print("Comment :=>> FINAL TEST CICLES GRAF ", i, "RESULTAT OK")
        print("Comment :=>> ", cicles)
        print ("Comment :=>> -----------------------------------------------")
        grade+=punts[i]
    else:
        print ("Comment :=>> -----------------------------------------------")
        print ("Comment :=>> FINAL TEST CICLES GRAF ", i, "RESULTAT NO OK.")
        print ("Comment :=>> Hauria de ser:",solucions[i])
        print ("Comment :=>> i has donat:",cicles)  
        print ("Comment :=>> -----------------------------------------------")
        correcte = False
    i+=1

if (grade < 0):
    grade = 0

print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
