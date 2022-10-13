
def bisect(llista,n):
    trobat = False
    a = 0
    b = len(llista)
    c = int((a+b)/2)
    while trobat == False and a!=b:
        if llista[c]==n:
            trobat = True
        else:
            if llista[c]>n:
                b=c
                c=int((b+a)/2)
            else:
                a=c
                c=int((a+b)/2)
    return trobat