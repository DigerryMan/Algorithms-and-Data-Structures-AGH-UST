from collections import deque

def DFS(G):
    n=len(G)
    visited=[False]*n
    parent=[None]*n
    time=0

    def DFS_visit(G, v):
        nonlocal time
        nonlocal visited
        nonlocal parent

        time+=1
        visited[v]=True

        for neigh in G[v]:
            if not visited[neigh]:
                parent[neigh]=v
                DFS_visit(G,neigh)

        time+=1        

    

    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

    return time




#print(DFS(graf))






def BFS(G, s):
    n=len(G)
    visited = [False]*n
    parent = [None]*n
    d = [-1]*n
    Q=deque()
    Q.append(s)
    
    
    d[s]=0
    visited[s]=True

    while len(Q)>0:
        s=Q.popleft()
        for N in G[s]:
            if not visited[N]:
                visited[N]=True
                d[N]=d[s]+1
                parent[N]=s
                Q.append(N)

    return max(d)

def isSpojny(G,s):

    n=len(G)
    visited = [False]*n
    Q=deque()
    Q.append(s)
    
    visited[s]=True

    while len(Q)>0:
        s=Q.popleft()
        for N in G[s]:
            if not visited[N]:
                visited[N]=True
                Q.append(N)

    for i in range(n):
        if not visited[i]:
            return False
    return True    




#print(BFS(graf, 0))



"""

#ZADANIE 1
#DETEKCJA CYKLU w grafie nieskierowanym


#DFS sobie leci i jak na stosie beda 2 te same wartosci to znaczy ze mamy cykla

#BFS lecimy dopisujac do kolejki normalnie, i zmieniajac visited, gdy w kolejce bedzie jakis visited ktory byl to zwracamy true i koniec

"""
def cycleDetection_DFS(G):
    n=len(G)
    visited=[False]*n
    parent=[None]*n
    result=False

    def DFS_visit(G, v):
        visited[v]=True

        for neigh in G[v]:
            if visited[neigh] and neigh!=parent[v]:
                result=True
    
            elif not visited[neigh]:
                parent[neigh]=v
                DFS_visit(G,neigh)

    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

    return result

def cycleDetection_BFS(G,s=0):
    n=len(G)
    visited = [False]*n
    parent=[None]*n
    Q=deque()
    Q.append(s)
    
    
    visited[s]=True

    while len(Q)>0:
        s=Q.popleft()
        for N in G[s]:
            if visited[N] and parent[s]!=N:
                return True
            elif not visited[N]:
                visited[N]=True
                parent[N]=s
                Q.append(N)

    return False



def cycleDetectionBFS(G,s): 
    n=len(G)    
    visited=[False]*n
    parent=[-1]*n

    Q=deque()
    visited[s]=True
    
    Q.append(s)
    
    while len(Q)>0:
        s=Q.popleft()
        for neigh in G[s]:
            if neigh != parent[s]: #źle
                if visited[neigh]:
                    return True
                else:
                    visited[neigh]=True
                    parent[neigh]=s
                    Q.append(neigh)

    return False

#print(cycleDetectionBFS(graf, 0))






def czyDwudzielny_BFS(G, s=0): #dzielimy wierzcholki jak drzewo, na dla wierzcholka o kolorze 1, 
    n=len(G)                       #sasaiedzi musza miec 0 i na odwrot jezeli 0=0 lub 1=1 graf nie jest dwudzielny
    colors=[-1]*n
    Q=deque()     
    Q.append(s)
    colors[s]=1

    while len(Q)>0:
        v=Q.popleft()
        for neigh in G[v]:
            if colors[neigh]==-1:
                colors[neigh] = (colors[v]+1)%2
                Q.append(neigh)
            elif colors[neigh]== colors[v]: 
                return False

    return True            

#print(czyDwudzielny_BFS(graf))





#liczba spoinych skladowych w grafie

def ileSpojnychSkladowychNIESKIEROWANY(G): #liczymy ile razy nam sie wywola DFS, (ilosc takich stadek )
    VIS=[0]*len(G)
    def DFS(G, s):
        nonlocal VIS
        VIS[s]=1

        for neigh in G[s]:
            if not VIS[neigh]:
                DFS(G, neigh)

        return 0

    counter=0
    for i in range(len(G)):
        if not VIS[i]:
            counter+=1
            DFS(G, i)
            

    return counter


# jakies odlaczanie wierzcholkow ponoc
#DFS odcinamy te ktore juz nie maja dalej gdzie isc

#w BFS rozlewa sie falami, leci od konca usuwajac te najdalsze (TRZEBA MIEC LISTE FAL)


#zadanie 3:
#dany jest graf G jako macierz sąsiedztwa
#czy istnieje cykl o dlugosci 4
# a) O(n^4) sprawdzamy wszystkie 4ki mozliwe n-liczba wierzcholkow
#b) O(n^3)  
# rozwazamt wszystkie pary wierzcholkow x,y (n^2) i potem liniowo idac po tablicy szukamy 
# przynajmniej 2 ktore maja krawedz z tymi dwoma wierzcholkami

def zadanie3(G): #macierz
    n=len(G)

    for i in range(n-1):
        for j in range(i+1,n):
            cntr=0
            for k in range(n):
                if G[i][k] and G[j][k]:
                    cntr+=1

            if cntr>=2:
                return True        

    return False

#zadanie 4  GRAF SKIEROWANY - macierz sąsiedztwa
#chcemy znalec uniwersalne wejscie t
#a) dla kazdego wierzcholka v istnieje krawedz z v do t
#b) t nie posiada krawedzi wychodzacych
# n^2 szukamy kolumny z n-1 jedynkami i potem wiersz jako ta kolumna czy ma same 0
#jakos lecimy wierszem gdy jedynka lecimy w dol i starczy przejsc do konca tablicy

krawedzie=[[0,1,1,0,1],
           [0,0,1,0,0],
           [0,0,0,0,0],
           [0,0,1,0,1],
           [0,0,1,0,0]]

def zadanie4DFSsasiedztwo(G):
    n=len(G)
    visited=[0]*n
    result=False

    def checkAllConnected(G, w):
        cntr=0
        n=len(G)
        for i in range(n):
            cntr+=G[i][w]

        return cntr==n-1

    def DFS_visit(G,w,n):
        nonlocal visited
        nonlocal result
        cntr=0
        visited[w]=True
        for k in range(n):
            if G[w][k]!=0:
                cntr+=1
                if not visited[k]:
                    DFS_visit(G, k, n)

        if cntr==0:
            if checkAllConnected(G, w):
                result=w

    for w in range(n):
        if not visited[w]:
            DFS_visit(G, w, len(G))

    return result      

#print(zadanie4DFSsasiedztwo(krawedzie))


#zadanie 5
#sciezka 
def zadanie5(G,s,t):
    VIS=[0]*len(G)
    PARENT=[-1]*len(G)



#zadanie 6
#dana szachownica n*n
#kazde pole ma koszt {1,2,3,4,5}
#minimalny koszt przejscia znalezc
# skonwertowanie tego do listy sasiedztwa i DFS z modyfikacją
#chodzimy prawo, dol i po skosie
#w BFS-sie wrzucac krotki z iloscią wystapien jeszcze

tab=[[0,2,4],
     [2,5,1],
     [2,2,0]]

def szachownica(tab):
    n=len(tab)
    q=deque()
    q.append((0,0,0))

    visited=[[False for _ in range(n)] for _ in range(n)]
    parent=[[None for _ in range(n)] for _ in range(n)]

    while len(q)>0 and parent[n-1][n-1] is None:
        (w,k,cost)=q.popleft()

        if cost<=1:
            visited[w][k]=True
            if w<n and k+1<n and parent[w][k+1] is None:
                parent[w][k+1]=(w,k)
                q.append((w,k+1,tab[w][k+1]))

            if w+1<n and k<n and parent[w+1][k] is None:
                parent[w+1][k]=(w,k)
                q.append((w+1,k,tab[w+1][k]))

            if w+1<n and k+1<n and parent[w+1][k+1] is None:
                parent[w+1][k+1]=(w,k)
                q.append((w+1,k+1,tab[w+1][k+1]))        

        elif not visited[w][k]:
            q.append((w,k,cost-1))        

    resCost=0
    x,y=n-1,n-1
    while parent[x][y] is not None:
        resCost+=tab[x][y]
        x,y=parent[x][y]

    return resCost    

print(szachownica(tab))
#zadanie 7
#Malejące krawędzie
#G=(v,e) nieskierowany
#kazda krawedz ma inny koszt
#mamy dojsc z s->t
#DFS - nie sprawdzamy czy juz bylim, pamietamy koszt poprzednika,
#  i wchodzimy dalej tylko gdy koszt wejscia mniejszy niz pamietany
