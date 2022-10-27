import sys

def testBinaryTreeOpsCrea(grade,correcte):
      
    resOrd='Comment :=>> +\nComment :=>>   *\nComment :=>>     +\nComment :=>>       3\nComment :=>>       9\nComment :=>>     /\nComment :=>>       5\nComment :=>>       2\nComment :=>>   7\n'
    tOps=BinaryTree.BinaryTree()
    tOps.read("arbreOps.txt")
    print(tOps)
    cad=str(tOps)
    if (cad==resOrd):
        print("Comment :=>> CORRECTE RESULTAT CREACIO ARBRE")    
        print("Comment :=>> ARBRE OPERACIONS \n", tOps)
        grade+=5
        
    else:
        print("Comment :=>> ERROR RESULTAT CREACIO ARBRE OPERACIONS")    
        print("Comment :=>> RESULTAT DONAT ", cad)
        print("Comment :=>> RESULTAT ESPERAT:", resOrd)
        correcte=False
        
    return tOps, grade, correcte 
    
def testBinaryTreeOrdenatCrea(grade, correcte):
    resOrd='Comment :=>> 35\nComment :=>>   15\nComment :=>>     10\nComment :=>>     25\nComment :=>>   80\nComment :=>>     47\nComment :=>>     92\nComment :=>>       105\n'
    tOrd=BinaryTree.BinaryTree()
    tOrd.read("arbreOrdenat.txt")
    
    print(tOrd)
    cad=str(tOrd)
    if (cad==resOrd):
        print("Comment :=>> CORRECTE RESULTAT CREACIO ARBRE")    
        print("Comment :=>> ARBRE OPERACIONS \n", tOrd)
        grade+=5        
    else:
        print("Comment :=>> ERROR RESULTAT CREACIO ARBRE ORDENAT")    
        print("Comment :=>> RESULTAT DONAT ", cad)
        print("Comment :=>> RESULTAT ESPERAT:", resOrd)
        correcte=False
        
    return tOrd, grade, correcte 

if __name__ == "__main__":

    import BinaryTree
    print("Comment :=>> ============================================")
    print("Comment :=>> INICI DEL TEST CREACIÓ BINARYTREE        ===")
    print("Comment :=>> ============================================")
    grade =0.0
    correcte=True
    
    tOps, grade, correcte = testBinaryTreeOpsCrea(grade,correcte)
    
    tOrd, grade, correcte = testBinaryTreeOrdenatCrea(grade, correcte)
    
    if (grade >= 10):        
        grade=10
    
    if correcte:
        print("Comment :=>> ============================================")
        print("Comment :=>> FINAL DEL TEST SENSE ERRORS              ===")
        print("Comment :=>> ============================================")

    print("Grade :=>> ",grade)
    
