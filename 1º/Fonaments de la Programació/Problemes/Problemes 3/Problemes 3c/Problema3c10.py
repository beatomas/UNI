
parell = False

num = int (input ("Introdueix un numero: "))

if (num == 0):
    print ("No hi ha cap nombre parell en la seqüència")
   
while (num != 0):
   
    if (num%2 == 0):
        parell = True
       
    num = int (input ("Introdueix un numero: "))

if (parell):
    print ("Algun nombre de la seqüència és parell")  
 
else:
    print ("No hi ha cap nombre parell en la seqüència")


   