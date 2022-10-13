

def Fibonacci(n):
    if (n <= 2):
        if n == 0:
            a_n=0
        else:
            a_n=1
    else:
        a_n_2=1
        a_n_1=1
        terme=3
        while (terme <= n):
            a_n = a_n_1 + a_n_2
            a_n_2 = a_n_1
            a_n_1 = a_n
            terme += 1
        
    return a_n
    
n = int(input("Introdueix un nombre n: "))

while(n<0):
    print("Error: El nombre no pot ser negatiu")
    n = int(input("Introdueix un nombre n: "))
    
resultat = Fibonacci(n)
 
print("El terme",n,"de la sèrie de Fibonacci és",resultat) 


