import Ex1SumaXifres


grade = 0

print ("Grade :=>>", grade)
print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")


lEx=[2345,-2345,1,0,7655]
lExRev=[14,14,1,0,23]

for i in range(len(lEx)):
    print ("Comment :=>> ========================================")
    print ("Comment :=>> Test sumaXifres",lEx[i])
    r=Ex1SumaXifres.sumaXifres(lEx[i])
    if r==lExRev[i]:
        print ("Comment :=>> OK: sumaXifres(",lEx[i],")=",r)
        grade+=2
    else:
        print ("Comment :=>> ERROR: sumaXifres(",lEx[i],")=",lExRev[i],"Tu has donat:",r)


if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)


print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
