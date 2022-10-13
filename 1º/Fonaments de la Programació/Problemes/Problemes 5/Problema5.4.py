
from time import time


def factorial(valor):
    fact = 1
    for n in range(valor,1,-1):
        fact *= n
    return fact

def sumatori(valor):
    sum = 1
    for n in range(valor,1,-1):
        sum += n
    return sum

def Timer(fnc,arg):
    t0 = time()
    fnc(arg)
    t1 = time()
    return t1-t0

print("Temps d'execució", (Timer(factorial,100)))

print("Temps d'execució", (Timer(sumatori,100)))