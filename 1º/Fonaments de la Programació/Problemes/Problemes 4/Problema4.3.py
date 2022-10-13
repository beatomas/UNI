
MAX = int(input("Valor màxim: "))
NP = []
P = []

for num in range(2,MAX+1):
    if num not in NP:
        P.append(num)
        i=2
        multiple = num*i
        while (multiple <= MAX):
            NP.append(multiple)
            i+=1
            multiple = num*i
print(P)