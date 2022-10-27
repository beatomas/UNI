import BinaryTree

print("Comment :=>> ============================================")
print("Comment :=>> INICI DEL TEST POSTORDRE EX1 AVALUABLES  ===")
print("Comment :=>> ============================================")
grade =0.0
correcte=True


fitxers=["arbreOps0.txt","arbreOps1.txt","arbreOps2.txt","arbreOps3.txt"]
solucions=['Comment :=>> 3 9 + 5 2 / * 7 +','Comment :=>> 5','Comment :=>> 5 4 * 5 2 - +','Comment :=>> 10 25 * 8 10 * + 10 /']
punts=[3,1,3,3]

for i,f in enumerate(fitxers):
    print("Comment :=>> =====================")
    print("Comment :=>> CREANT ARBRE ", fitxers[i]," ===")
    print("Comment :=>> =====================")
    t=BinaryTree.BinaryTree()
    t.read(f)
    print("Comment :=>> ARBRE AVALUAT:")
    print(t)
    cad="Comment :=>>"
    for n in t.postordre():
        cad=cad+" "+str(n._valor)
    if (cad==solucions[i]):
        print("Comment :=>> RESULTAT OK", cad)
        grade+=punts[i]
    else:
        print("Comment :=>> ERROR RESULTAT. Hauria de ser:",solucions[i],"i has donat:",cad)
        correcte=False
    


if correcte:
    print("Comment :=>> ============================================")
    print("Comment :=>> FINAL DEL TEST SENSE ERRORS              ===")
    print("Comment :=>> ============================================")

print("Grade :=>> ",grade)
