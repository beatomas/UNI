

def funcio(radi):
    assert (radi >= 0), "El radi no pot ser negatiu"
    assert (radi != 0), "El radi no pot ser zero"
    pi = 3.141592
    area = pi*radi**2
    perimetre = 2*pi*radi
    
    return area,perimetre
    

try: 
    radi = float(input("Introdueix el radi: "))
    
    area,perimetre = funcio(radi)
    
except ValueError: 
    print("ERROR: El radi ha de ser un valor numèric")
except AssertionError as missatge:
    print("ERROR:",missatge)
else:
    print("Àrea:",area,"- Perímetre:",perimetre)
    
