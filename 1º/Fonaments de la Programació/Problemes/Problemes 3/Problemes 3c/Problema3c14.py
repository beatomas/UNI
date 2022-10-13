
from time import sleep

temps = input("Introdueix una hora en format hh:mm:ss: ")

hh = int(temps[0:2])
mm = int(temps[3:5])
ss = int(temps[6:8])

comp = 0

while (ss >= 0 and comp < 5):
    ss = ss + 1
    comp = comp + 1
    sleep(1)
    
    if (ss == 60):
        ss = 0
        mm = mm + 1
           
    if (mm == 60):
        ss = 0
        mm = 0
        hh = hh + 1
    
    if (hh == 24):
        hh=0
        
    if (hh < 10):
        sortida1 = "0" + str(hh) + ":"
    if (hh > 10):
        sortida1 = str(hh) + ":"
    
    
    if (mm < 10):
        sortida2 = "0" + str(mm) + ":"
    if (mm > 10):
        sortida2 = str(mm) + ":"
        
    
    if (ss < 10):
        sortida3 = "0" + str(ss)
    if (ss >= 10):
        sortida3 = str(ss) 
    
    print(sortida1 + sortida2 + sortida3)
