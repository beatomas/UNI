

def taula_multiplicar(N):
    nom = "Taula_del_"+str(N)+".txt"
    file = open(nom,"a")
    for x in range(11):
        mul = N * x
        res = str(N)+" x "+str(x)+" = "+str(mul)
        file.write(res+'\n')
        
    return file
