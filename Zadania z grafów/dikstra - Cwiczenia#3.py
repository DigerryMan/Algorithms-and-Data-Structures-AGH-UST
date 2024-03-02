"""
dikstra/reprezentacja macierzowa
bellman-ford/ rep. listowa

zadanie 1
iloczyn Wag 
mamy s i t
koszt sciezki to jest iloczyn jej wag 
chcemy najtansza trase z s do t

"""
from queue import PriorityQueue
from math import inf

def iloczynWag(G, s, t):
    n=len(G)
    visited=[False]*n
    parent=[None]*n
    d=[inf]*n
    d[s]=1

    def relax(u, v, weight): 
        if d[u]*weight<d[v]:
            d[v]=d[u]*weight
            parent[v]=u

    q_p=PriorityQueue()
    q_p.put((0, s))

    while not visited[t] and not q_p.empty():
        (priority, s)=q_p.get()
        
        if not visited[s]:
            visited[s]=True

            for v in G[s]:
                if not visited[v[0]]:
                    relax(s, v[0], v[1])
                    q_p.put((d[v[0]], v[0]))

    res=[]
    w=t
    while w is not None:
        res.append(w)
        w=parent[w]

    res.reverse()
    return (res, d[t])

G=[[[1,2],[2,2]],
   [[0,2],[3,2],[4,3]],
   [[0,2],[3,2]],
   [[1,2],[2,2],[4,2]],
   [[1,3],[3,2]]]

#print(iloczynWag(G, 0 , 4))

"""
zamieniamy liczby na logarytmy i puszczamy dikstre
zeby nie bylo giga duzej zlozonosci

zadanie 2
algorytm znajdujacy najkrotsza sciezke w DAGU
sortujemy topologicznie i potem trzeba relaxowac sie 
"""

def shortestPathDAG(G):
    n=len(G)
    
    visited=[False]*n
    sortedGraph=[]
    
    def DFS_visit(G, s):
        visited[s]=True
        for v in G[s]:
            if not visited[v[0]]:
                DFS_visit(G, v[0])

        sortedGraph.append(s)        

    
    for v in range(len(G)):
        if not visited[v]:
            DFS_visit(G, v)

    sortedGraph.reverse()
    print(sortedGraph)
    
    parent=[None]*n
    d=[inf]*n
    d[sortedGraph[0]]=0

    def relax(s, v, weight):
        if d[s]+weight<d[v]:
            d[v]=d[s]+weight
            parent[v]=s

    for s in sortedGraph:
        for w in G[s]:
            relax(s, w[0], w[1])



G=[[[1,2]],
   [[3,2],[4,3]],
   [],
   [[2,2],[4,2]],
   [[3,2]]
   ]



"""
zadanie 3
najkrotsza sciezka z s do t ale po kolejne dlugosci musza byc malejace
sortujemy malejaco krawedzie, i potem iteracja belmana forda 


zadanie4 
mamy graf z odleglosciami na wierzcholkach są stacje paliw z danymi cenami za litr
rozmnazanie wierzcholkow kazdy wierzcholek ma liter D:


4 i 5 na rozmnozenie wierzcholkow

zadanie 5
mamy kierowcow A i B, miasto s i t, mape, trasa dowolna, wybiera ktory kierowca zaczynan jechac 
A jest zaliczany, chce przejechac jak najmniej, b moze jechac jak chce

kazdy wirezcholek rozmnazamy na 2, taki jesli wjechal do niego A albo B
i potem nibi dikstra dodac  jeszcze albo odpalic dikstre 2 razy, albo dodac wierzolek skierowany z dwoma 0

zadanie 6
kazdy wierzcholek to jakas waluta
graf pelny

"""