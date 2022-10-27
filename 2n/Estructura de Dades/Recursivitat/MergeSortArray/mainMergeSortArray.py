import Ex4MergeSortArray


grade = 0

print ("Grade :=>>", grade)
print ("Comment :=>> Iniciant test")
print ("Comment :=>> =============")
print ("Comment :=>>")


lEx=[[3,5,6,2,13,45,78],[],[1,2,3],[1,99,2,89,3,56,8,37],[7,6,5,4,3]]
lOri=[[3,5,6,2,13,45,78],[],[1,2,3],[1,99,2,89,3,56,8,37],[7,6,5,4,3]]
lExRev=[[2, 3, 5, 6, 13, 45, 78],[],[1,2,3],[1, 2, 3, 8, 37, 56, 89, 99],[3,4, 5, 6, 7]]

for i in range(len(lEx)):
    print ("Comment :=>> ========================================")
    print ("Comment :=>> Test ordenaArray",lEx[i])
    Ex4MergeSortArray.mergeSortArray(lEx[i],0,len(lEx[i])-1)
    if lEx[i]==lExRev[i]:
        print ("Comment :=>> OK: mergeSortArray(",lOri[i],",0,",len(lOri[i])-1,")=",lEx[i])
        grade+=2
    else:
        print ("Comment :=>> ERROR: mergeSortArray(",lOri[i],",0,",len(lOri[i])-1,")=",lExRev[i],"Tu has donat:",lEx[i])


if (grade < 0):
    grade = 0
print ("Grade :=>>", grade)


print ("Comment :=>> ------------------------------------------")
if (grade == 10.0):
    print ("Comment :=>> Final del test sense errors")
print ("Grade :=>> ", grade)
