

def factorial(num):
    fact = 1
    for n in range (1,num+1):
        fact *= n
      
    
    return fact

n = int(input("Intrdueix el nombre de jugadors: "))
r = int(input("Intrdueix el nombre de jugadors per partit: "))
k = n - r

n_fact = factorial(n)
r_fact = factorial(r)
k_fact = factorial(k)

resultat = n_fact/(r_fact*k_fact)

print("El nombre d'equips que es poden formar és",resultat)


    