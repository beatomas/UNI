
def DivisioEntera(Dividend,divisor):
    quocient = 0
    residu = 0
    if (divisor == 0):
        error = 1
    else:
        error=0
        if((Dividend > 0 and divisor < 0) or (Dividend < 0 and divisor > 0)):
            signe = -1
        else: 
            signe = 1
        DividendAbs = abs(Dividend)
        divisorAbs = abs(divisor)
       
        while (DividendAbs >= divisorAbs):
            DividendAbs = DividendAbs - divisorAbs
            quocient += signe
        if (Dividend > 0):
           residu = DividendAbs
        else:
            residu = -DividendAbs
    return error,quocient,residu


Dividend = int(input("Introdueix el dividend: "))
divisor = int(input("Introdueix el divisor: "))


error,quocient,residu=DivisioEntera(Dividend,divisor)

if (error):
    print("Error: Divisió per zero")
else:
   print("Resultat - Quocient:",quocient,"i Residu:",residu)