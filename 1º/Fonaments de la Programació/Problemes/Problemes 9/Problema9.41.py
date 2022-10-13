
Dict = {}
opcio = 1

while opcio != 6:
    print("1.Afegir client\n2.Eliminar client\n3.Mostra client\n4.Llistar tots els clients\n5.Llistar clients preferents\n6.Acabar")
    opcio = int(input("Escull una opció del menú: ")) 
    if opcio == 1:
        NIF = int(input("Introdueix el NIF: "))
        if NIF in Dict:
            print("Error: Client Existent")
            
        else:
       
            nom = input("Introdueix el teu nom: ")
            adreça = input("Introdueix la teva adreça: ")
            telefon = int(input("Introdueix el teu telèfon: "))
            correu = input("Introdueix el teu correu: ")
            preferent = input("Introdueix si ets preferent o no: ")
            
            pref = False
            if preferent == 's' or preferent == 'S':
                pref = True
          
            Dict[NIF] = {}
            Dict[NIF]['Nom'] = nom
            Dict[NIF]['Adreça'] = adreça
            Dict[NIF]['Telèfon'] = telefon
            Dict[NIF]['Correu'] = correu
            Dict[NIF]['Preferent'] = pref
            
       
    
    elif opcio == 2:
        NIF = int(input("Introdueix el NIF: "))
        if NIF in Dict:
            del(Dict[NIF])
            
        else:
            print("Error: Client inexistent")
       
        
        
    elif opcio == 3:
        NIF = int(input("Introdueix el NIF: "))
        if NIF in Dict:
            print(NIF,Dict[NIF]['Nom'], Dict[NIF]['Adreça'],Dict[NIF]['Telèfon'],Dict[NIF]['Correu'],Dict[NIF]['Preferent'])
        else:
            print("Error: Client inexistent")
    
       
        
    elif opcio == 4:
        for x in Dict:
            print(x,Dict[x]['Nom'])

    elif opcio == 5:
        for x in Dict:
            if Dict[x]['Preferent'] == True:
                print(x,Dict[x]['Nom'])
       
"""               
opcio=0
clients = {}

while (opcio !=6):
   
    print("1.Afegir client")
    print("2.Eliminar client")
    print("3.Mostra client")
    print("4.Llistar tots els clients")
    print("5.Llistar clients preferents")
    print("6.Acabar")
   
    opcio=int(input("Entra l'opció:"))
   
    if (opcio==1):
        nif=str(input("Entra el NIF"))
        if (nif in clients):
            print("Error: Client existent")
        else:
            nom=str(input("Entra el nom"))
            dir=str(input("Entra l'adreça"))
            tel=str(input("Entra el tel"))
            correu=str(input("Entra el correu"))
            pref=str(input("Entra si és preferent"))
            if (pref=="S" or pref=='s'):
                pref=True
            else:
                pref=False
               
            clients[nif]={'nom':nom,'adreça':dir,'telefon':tel,'correu':correu,'preferent':pref}
           
    elif (opcio==2):
        nif=str(input("Entra el NIF"))
        if (nif not in clients):
            print("Error: Client inexistent")    
        else:
            del(clients[nif])
       
    elif (opcio==3):
        nif=str(input("Entra el NIF"))
        if (nif not in clients):
            print("Error: Client inexistent")    
        else:
            print (nif,clients[nif]['nom'],clients[nif]['adreça'],clients[nif]['telefon'],clients[nif]['correu'],clients[nif]['preferent'])  
   
    elif (opcio==4):
        for i in clients:
            print (i,clients[i]['nom'])
           
    elif (opcio==5):
        for i in clients:
            if (clients[i]['preferent']==True):
                print (i,clients[i]['nom'])


             
"""     