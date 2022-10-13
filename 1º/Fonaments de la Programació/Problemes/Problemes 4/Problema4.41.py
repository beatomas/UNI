

resultat = True

contra = input("Introdueix una contrasenya: ")
if len(contra) < 8:
    resultat = False
    
    
digits = 0
mayus = 0
minus = 0
simbol = 0
for i in range(len(contra)):
    if(contra[i] in "0123456789"):
        digits +=1
    if(contra[i] in "abcdefghijklmnopqrstuxwyz"):
        minus += 1
    if(contra[i] in "ABCDEFGHIJKLMNOPQRSTUXYWZ"):
        mayus += 1
    if contra[i] in "$&*€_@#":
        simbol += 1
        
if(digits < 2 or mayus < 1 or simbol < 1 or minus < 1): 
    resultat = False
    
if(resultat == True):
    contra1 = input("Introdueix un altre cop la contrasenya: ")
    if(contra1 == contra):
        print("Contrasenya correcta")
    else:
        print("Error: Les dues contrasenyes no són iguals.")
        
else:
    print("Error. Contrasenya no vàlida.")



