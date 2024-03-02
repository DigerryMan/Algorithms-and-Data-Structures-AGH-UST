from zad9testy import runtests
from math import inf

#Mateusz Bobula
#OPIS: tworze krotki z pozycjami i ceną, dodajac krotke(0,0) i (L,0) - sortuje je rosnąco 
#       a nastepnie lecąc po tych krotkach sprawdzam którą stacje można osiągnąc w odl. T - aktualizuje min. cenę w F[0]
#       oraz którą w 2*T - aktualizując min. cene w F[1]. Dodatkowo mogę z F[1][i] osiągnąc odl. T do F[1][j], i<j - 
#       (interpretacja: ciężarówka użyła już przejechania odl. 2*T) więc tam też aktualizuję mozliwe najniższą cene
#       F[0][i] - min cena dotarcia do i-tej stacji bez użycia przejechania 2*T
#       F[1][i] - min cena do i-tej użyciem przejechania 2*T

#zlozonosc n^2

def min_cost( O, C, T, L ):
   
    n=len(O)
    krotki=[[0,0], [L,0]]
    for i in range(n):
        krotki.append([O[i], C[i]])

    krotki.sort(key=lambda x:x[0])
    
    F=[[inf for _ in range(n+2)] for i in range(2)]
    F[0][0]=0
    F[1][0]=0

    
    for i in range(n+1):
        stacja=krotki[i][0]

        for j in range(i+1,n+2):
            if krotki[j][0] <= stacja + T:
                if F[0][i]+krotki[j][1] < F[0][j]:
                    F[0][j]=F[0][i]+krotki[j][1] 

                if F[1][i]+krotki[j][1] < F[1][j]:
                    F[1][j]=F[1][i]+krotki[j][1]   
        

            elif krotki[j][0] <= stacja + 2*T:
                if F[0][i]+krotki[j][1] < F[1][j]:
                    F[1][j]=F[0][i]+krotki[j][1]

            else: break       

    res=F[0][n+1]
    if F[1][n+1]<res:
        res=F[1][n+1]    

    return res
 

runtests( min_cost, all_tests = True )

