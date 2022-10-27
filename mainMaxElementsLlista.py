import LlistaN

grade = 0

print ("Grade :=>>", grade)
print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")


lEx=[[3,5,6,2,13,45,78],[],[1,2,3],[1,99,2,89,3,56,8,37],[7,6,5,4,3]]
lExMax=[78,None,3,99,7]

for i in range(len(lEx)):
    print ("Comment :=>> ========================================")
    print ("Comment :=>> Test maxElementsLlista",lEx[i])
    l=LlistaN.LlistaN(lEx[i])
    r=l.MaxElementsLlista()
    if r==lExMax[i]:
        print ("Comment :=>> OK: MaxElements()=",r)
        grade+=2
    else:
        print ("Comment :=>> ERROR:  MaxElements(",lEx[i],",...)=",lExMax[i],"Tu has donat:",r)


if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)


print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
