import BinaryTree

print("Comment :=>> ============================================")
print("Comment :=>> INICI DEL TEST AVALUA EX2 AVALUABLES     ===")
print("Comment :=>> ============================================")
grade =0.0
correcte=True


fitxers=["arbreOps0.txt","arbreOps1.txt","arbreOps2.txt","arbreOps3.txt"]
solucions=["Comment :=>>\n3 9 + 5 2 / * 7 + ","Comment :=>>\n5 ","Comment :=>>\n5 4 * 5 2 - + "]
punts=[3,1,3,3]
resValor=[37,5,23,33]

for i,f in enumerate(fitxers):
     print("Comment :=>> =====================")
     print("Comment :=>> CREANT ARBRE ", fitxers[i]," ===")
     print("Comment :=>> =====================")
    
     t=BinaryTree.BinaryTree()
     t.read(f)
     print("Comment :=>> ARBRE AVALUAT:")
     print(t)
     valor=t.avalua()
     if (valor==resValor[i]):
        print("Comment :=>> RESULTAT OK", valor)
        grade+=punts[i]
     else:
        print("Comment :=>> ERROR RESULTAT. Hauria de ser:",resValor[i],"i has donat:",valor)
        correcte = False


if correcte:
    print("Comment :=>> ============================================")
    print("Comment :=>> FINAL DEL TEST SENSE ERRORS              ===")
    print("Comment :=>> ============================================")

print("Grade :=>> ",grade)
