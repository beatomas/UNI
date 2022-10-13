
def LlegirLlista(num_elements):
    llista=[]
    for i in range (num_elements):
        valor=int(input("Introdueix valor de l'índex "+str(i)+": "))
        llista.append(valor)
    return llista
    
def SumarLlistes(llista1,llista2):
    res = []
    for i in range (len(llista1)):
        res.append(llista1[i]+llista2[i])
    return res
    
dimensio = int(input("Quina mida vols per les llistes? "))

llista1 = LlegirLlista(dimensio)
llista2 = LlegirLlista(dimensio)

resultat = SumarLlistes(llista1,llista2)

print(resultat)

