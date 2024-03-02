"""
zad. 1 
szachownica dojsc z lewy gorny do prawy dolny
pola maja wagi 

f(i,j) - minimalny koszt dotarcia na pole i,j
f(i,j) - min(f(i,j-1), f(i-1,j)) + K[i][j]
f(0,0)=0

#nie wyjsc poza tablice
"""
from math import inf
import random



def szachownicum(K):
    n=len(K)
    F=[[inf for _ in range(n)] for _ in range(n)]
    F[0][0]=0

    for w in range(1,n):
        F[w][0]= F[w-1][0] + K[w][0]
        F[0][w]= F[0][w-1] + K[0][w]

    for w in range(1,n):
        for k in range(1,n):
            F[w][k] = min(F[w-1][k], F[w][k-1]) + K[w][k]

    return F[n-1][n-1]       

#print(szachownicum(tablica))     






"""
dlugosc najdluzszego wspolnego podciagu (maja miec taka sama kolejnosc bo inaczej nie dziala)
2 tablice A i B

A=[3 5 1 0 2 10]
#=[0 1 2 3 5 10]
B=[7 8 0 2 1 6]

f(i,j) - dlugosc najdluzszego wspolnego podciagu
         dla A[0, ..., i] i B[0, ..., j]

f(i,j) = f(i-1, j-1) + 1, A[i]=B[j]
         max(f(i-1)(j), f(i,j-1)) A[i]!=B[j]

"""

def krejziFunkcja(A,B):
    n=len(A)
    d=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
               if A[i]==B[j]:
                    d[i][j]=d[i-1][j-1] + 1

               else:
                    d[i][j]=max(d[i-1][j], d[i][j-1])       

    return d[n][n]                  
               





"""
znalezc najdluzszy podciag rosnacy wykorzystujac to wyzej                

"""






"""
#dana tablica n liczb naturalnych A podac algos ktory sprawdza czy da sie wybrac podciag liczb z A ktore sumuja sie do zadanej wartosci T
f(i,t)= True gdy do indexu i da sie wybrac podicag o sumie t
        False w.p.p 

f(i,t)= f(i-1,t) or [[ f(i-1, t-A[i]) - gdy t-A[i]>=0  ]]
"""
def wypisztab(tabi, T):
    n=len(tabi)
    for i in range(n):
        for j in range(T+1):
            print(tabi[i][j], end=" ")
        print("")    

def sumowanieDoT(A, T):
    n=len(A)
    F=[[0 for _ in range(T+1)] for _ in range(n+1)]

    for i in range(n+1):
        F[i][0]=1

    for i in range(1,n+1):
        for t in range(1,T+1):
            if F[i-1][t]:
                F[i][t]=F[i-1][t]
            
            elif t-A[i-1]>=0:
                F[i][t]=F[i-1][t-A[i-1]]

    return F           

"""                     
tab=[11,3,2,7,5]
T=10
wypisztab(sumowanieDoT(tab, T), T)
"""







"""
# mamy tablice nominalow oraz dana kwote T. algors ktory oblciza min liczbe monet potrzebna do wydania kwoty t

f(i) - liczba monet potrzebnych do wydania kwoty i+

tablica na MAXKWOTA+1
f(i) = min(f(i-N[j]) + 1)
"""


def nomialy(N, maxKwota):
    F=[inf]*(maxKwota+1)
    F[0]=0

    for i in range(1, maxKwota+1):
        for n in N:
            if i>=n:
                if F[i] > F[i-n] + 1:
                    F[i] = F[i-n] + 1

    return F               

"""
tabson=[1,2,5,10]
maxi=19

print(nomialy(tabson, maxi))
"""







"""
ciag liczb N a0, ..., an-1 liczby - ciag w ktorym niezmieniamy pozycji zostal podzielony na k spojnych podciagow
(a0,..,al1),(al1+1, ...,al2), .... (alk-1, an-1)  przez wartosc itego podciagu rozumiemy sume jego elementow.
Przez najgorszy podciag rozumiemy podciag o najmniejszej wartosci. wartoscia przedzialu jest wartosc jego najgorszego podciagu.
znalezc podzialu o max wartosci.

na ile podzielic jest zadane - k

f(i,t) - maxymalna wartosc podzialu ciagu a1...aj na t czesci

f(i,t)=max(min(f(k-1, t-1), )


"""                    

def plot(T, k):
    n=len(T)

    F= [[0]*n for _ in range(k)] 
    F[0][0]=T[0]

    for i in range(1,n):
        F[0][i]=F[0][i-1]+T[i]

    for kk in range(1, k):
        for i in range(kk, n):
            for j in range(i-1,kk-2,-1):
                curSum=F[0][i]-F[0][j]       
                F[kk][i] = max(F[kk][i], min(curSum, F[kk-1][j])) 

    print(*F, sep='\n')


tab=[2,7,3,4,1,1]
plot(tab, 4)
