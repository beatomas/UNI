
def bisect(llista,x):
    a = llista[0]
    pos = len(llista)/2
    b = llista[pos]
    while (a != b):
        
        while (x<b and x>a):
            if x == llista[b]:
                return True
            else: 
                b = b/2
        else: 
            a = b
            b = llista[len(llista)]
            while (x<b and x>a):
                if x == llista[b]:
                    return True
                else: 
                    b = b/2
    return False
        
        
        
    
    
    