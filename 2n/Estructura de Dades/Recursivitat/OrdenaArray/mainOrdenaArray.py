import Ex2OrdenaArray


grade = 0

print ("Grade :=>>", grade)
print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")


lEx=[[3,5,6,2,13,45,78],[],[1,2,3],[1,99,2,89,3,56,8,37],[7,6,5,4,3]]
lExRev=[[2, 3, 5, 6, 13, 45, 78],[],[1,2,3],[1, 2, 3, 8, 37, 56, 89, 99],[3,4, 5, 6, 7]]

for i in range(len(lEx)):
    print ("Comment :=>> ========================================")
    print ("Comment :=>> Test ordenaArray",lEx[i])
    r=Ex2OrdenaArray.ordenaArray(lEx[i],0,len(lEx[i])-1)
    if r==lExRev[i]:
        print ("Comment :=>> OK: ordenaArray(",lEx[i],",0,",len(lEx[i])-1,")=",r)
        grade+=2
    else:
        print ("Comment :=>> ERROR: ordenaArray(",lEx[i],",0,",len(lEx[i])-1,")=",lExRev[i],"Tu has donat:",r)


if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)


print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
