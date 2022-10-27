

def sumaXifres(n):
    if n<0:
        n=n*(-1)
    if n==0:
        return 0
    return ((n%10)+ sumaXifres(n//10))
   
   