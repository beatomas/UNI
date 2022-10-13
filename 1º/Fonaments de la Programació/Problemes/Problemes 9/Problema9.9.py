
def circular(x,y):
    i = 0
    res = True
    while (i<len(x) and res == True):  
        if y[i] in x:
            res = True
            i += 1
        else:
            res = False
            break
    i = 0    
    while (i<len(y) and res == True):  
        if x[i] in y:
            res = True
            i += 1
        else:
            res = False
    return res        
        
x = [1,2,3,4,5,6]
y = [2,3,4,5,4,1]

final = circular(x,y)

print(final)