#Mateusz Bobula

#Zaczynam z pustym bakiem, tankuje w pierwszej plamie, następnie dla zakresu baku szukam największej plamy ropy do zatankowania - wszystkie mozliwsci do zakresu baku wrzucam
#do kolejki priorytetowej, nastepnie wyciagam najwiekszą, zakres baku się zwiększa sie o te wartosc, mozliwe nowe tankowania ropy wrzucam do kolejki, powtarzam to wszystko do
#momentu aż bede w stanie dojechac do końca.

#Zlozonosc n*m

from zad8testy import runtests
from queue import PriorityQueue


def takeOil(T, col, n, m):  
    sum=0
    def dfs_visit(T, w, k):
        nonlocal sum
        nonlocal n
        nonlocal m
        sum+=T[w][k]
        T[w][k]=0

        if w+1<n and T[w+1][k]:
            dfs_visit(T, w+1, k)

        if w-1>=0 and T[w-1][k]:
            dfs_visit(T, w-1, k)

        if k+1<m and T[w][k+1]:
            dfs_visit(T, w, k+1)

        if k-1>=0 and T[w][k-1]:
            dfs_visit(T, w, k-1)            
    
    dfs_visit(T,0, col)

    return sum


def plan(T):
    n=len(T)
    m=len(T[0])

    bak=takeOil(T,0,n,m)
    queue=PriorityQueue()
    res=1

    for i in range(1, m-1):
        bak-=1

        if T[0][i]:
            queue.put(-1*takeOil(T,i,n,m))

        if bak==0:
            bak=(-1)*queue.get()
            res+=1

    return res        


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

