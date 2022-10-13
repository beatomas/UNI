
from time import sleep

def Alerta(seg):
    missatge = "Alerta: "
    
    if (seg != 0):
        missatge += "Queden "+str(seg) + " segons"
    else:
        missatge += "S'ha acabat el temps"
        
    print(missatge)
    

segons = int(input("Introdueix un temps: "))

for t in range (segons,-1,-1):
    Alerta(t)
    sleep(1)