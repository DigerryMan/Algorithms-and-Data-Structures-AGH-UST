#Mateusz Bobula

#Tworze tablice F którą uzupełniam kolejnymi kolumnami, gdzie dla kazdego pola jest wartość maksymalna dla drogi osiągniętej z lewej, góry i dołu.

#rekurencyjnie:       F[w][k]=max(F[w][k-1], F[w+1][k], F[w-1][k])
#wartosci poczatkowe: F[w][0]=w dopóki nie uderzymy w '#', po uderzeniu w '#' mamy wszedzie -inf.

#Złożoność n^2


from zad7testy import runtests
from math import inf


def maze( L ): 
    n=len(L)
    F=[[-inf for _ in range(n)] for _ in range(n)]

    for w in range(n):     #poczatkowe zalozenie
        if L[w][0]=='#':
            break
        F[w][0]=w


    for k in range(1,n):
        tabPom=[-inf]*n      #tabPom - kolumna do dziedziczenia z lewej i z dołu
        for w in range(n):
            if L[w][k]=='.':
                F[w][k]=F[w][k-1]+1     #dziedziczenie z lewej dla 'góry'
                tabPom[w]=F[w][k-1]+1   #dziedziczenie z lewej dla 'dołu'

                if w-1>=0 and F[w-1][k]+1>F[w][k]:   #dziedziczenie z gory
                    F[w][k]=F[w-1][k]+1             

        
        for w in range(n-2,-1,-1):
            if L[w][k]=='.':
                if tabPom[w+1]+1>tabPom[w]:  #dziedzieczenei z dołu
                    tabPom[w]=tabPom[w+1]+1

                    if tabPom[w]>F[w][k]:    #jezeli odziedziczonyDol > Gora
                       F[w][k]=tabPom[w] 

    
    if F[n-1][n-1]==-inf:
        return -1
    
    return F[n-1][n-1] 


runtests( maze, all_tests = True )



