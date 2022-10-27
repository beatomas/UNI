def mergeSortArray(v,indexInici,indexFinal):    
    llista_elements=v
    if indexInici>indexFinal or indexInici==indexFinal:
        return llista_elements
    else:
        r=(indexFinal-indexInici)//2+(indexInici+1)
        inici=indexInici
        
        mergeSortArray(llista_elements, indexInici, r-1)
        mergeSortArray(llista_elements,r,indexFinal)
        while(indexFinal>=r and r!= inici):
            if llista_elements[r]<llista_elements[inici]:
                canvi=llista_elements[r]
                llista_elements.pop(r)
                llista_elements.insert(inici,canvi)
                inici=inici+1
                r=r+1
            else:
                inici=inici+1
        return llista_elements