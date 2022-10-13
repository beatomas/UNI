
variable = "python"

print("La paraula té",len(variable),"lletres:")
print("-"*len(variable))

lletres = []
simbol = "-"
i = 0
while i < 10:
    lletra = input("Introdueix una lletra: ")
    lletres.append(lletra)
    resposta = ""
    for j in range(len(variable)):
        if(variable[j] in lletres):
            resposta += variable[j]
        else: 
            resposta += simbol


    i += 1
    print(resposta,"Et queden",10-i,"intents")
    if(resposta == variable): 
        print("Enhorabona, l'has encertat!!!")
        break
        
        
if(resposta != variable): 
    print("Ho sento, has perdut, la paraula era:",variable)

