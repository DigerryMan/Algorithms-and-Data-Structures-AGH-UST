#Mateusz Bobula
"""Odwracam kazde ze slow w tablicy array tylko gdy jego rewers jest alfabetycznie mniejszy, tak by nastepnie po posortowaniu calej tablicy, te same slowa 
(z ktorych jeden moze byc oryginalnie rewersem) byly zawsze kolo siebie dzięki czemu pozniej moge je latwo zliczyc idąc liniowo po tablicy i zliczając najdluzsza serie par tych samych slow.
"""
#Zlozonosc: (2N+nlogn) => O(N+nlogn)


from zad3testy import runtests
   

def reverseString(tab, i):
    str_pom=tab[i][::-1]
    tab[i]=str_pom
        

def reverseStringsIfNeeded(A, n):
    for i in range(n):
        le=len(A[i])

        for j in range(le//2):
            k=le-1-j
            if A[i][j]<A[i][k]:
                break

            if A[i][j]>A[i][k]:
                reverseString(A, i)
                break  

def merge(A, p, q, r):
    
    B=A[p:q+1:]
    C=A[q+1:r+1:]
    bLen=len(B)
    cLen=len(C)
    
    i=j=0
    t=p

    while i<bLen and j<cLen:
            if B[i]<C[j]:
                A[t]=B[i]
                i+=1
            
            else:
                A[t]=C[j]
                j+=1
           
            t+=1

    while i<bLen:
            A[t]=B[i]
            i+=1
            t+=1

    while j<cLen:
            A[t]=C[j]
            j+=1
            t+=1

def mergeSort(A, p, r):
    if p<r:
        q = (p+r)//2
        mergeSort(A, p, q)
        mergeSort(A, q+1, r)

        merge(A, p, q, r)

def findStrongestString(T, n):
    maxi=1
    lok=1
    for i in range(1,n):
        if T[i-1]==T[i]:
            lok+=1
            if(lok>maxi):
                maxi=lok
        
        else:
            lok=1

    return maxi        

def strong_string(T):
    n=len(T)
    reverseStringsIfNeeded(T, n)
    mergeSort(T, 0, n-1)

    return findStrongestString(T, n)




# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True )


