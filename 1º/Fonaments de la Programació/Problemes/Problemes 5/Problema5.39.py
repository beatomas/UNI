

def LlistaInversa(llista1,llista2):
    for i in range(len(llista1)):
        if llista1[i] != llista2[len(llista1)-i-1]:
            return 0
    return 1
    
llista1 = ['1','2','2']
llista2 = ['3','2','1']
valor = LlistaInversa(llista1,llista2)
print(valor)