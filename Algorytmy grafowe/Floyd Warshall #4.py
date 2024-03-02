from queue import PriorityQueue
from math import inf

def floydWarshallListowa( G ):  #najkrotsze sciezki miedzy kazda para wierzcholkow
    n=len(G)
    D=[[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        D[i][i]=0

    for s in range(n):
        for v in G[s]: #(wierzcholek, waga)
            D[s][v[0]]=v[1]


    for t in range(n):
        for x in range(n):
            for y in range(n):
                D[x][y] = min(D[x][y], D[x][t]+ D[t][y])

    
    for t in range(n): #detekcja ujemnego cyklu
        for x in range(n):
            for y in range(n):
                if D[x][y] > D[x][t]+ D[t][y]:
                    return None
                
                
    return D

"""
graph=[ [(1,3),(3,3),(4,2)],
        [(2,-7)],
        [(3,8)],
        [(1,-1),(4,-2)],
        []
]    

print(floydWarshallListowa(graph))
"""






def floydWarshallMatrix( G ):  #najkrotsze sciezki miedzy kazda para wierzcholkow
    n=len(G)                    #n^3
    D=[[float('inf') for _ in range(n)] for _ in range(n)]
    
    for w in range(n):
        for k in range(n): #(wierzcholek, waga)
            if w==k:
                D[w][k]=0
            elif G[w][k]!=0:
                D[w][k]=G[w][k]           
     
    for t in range(n):
        for x in range(n):
            for y in range(n):
                D[x][y] = min(D[x][y], D[x][t]+ D[t][y])

    
    for t in range(n): #detekcja ujemnego cyklu
        for x in range(n):
            for y in range(n):
                if D[x][y] > D[x][t]+ D[t][y]:
                    return None
                    
    return D           






"""
graph=[[inf,3,inf, 3, 2],
       [inf,inf,-7, inf, inf],
       [inf,inf,inf, 7, inf],
       [inf,-1,inf, inf, -2],
       [inf,inf,inf, inf, inf]]

print(floydWarshallMatrix(graph))
"""


class Node:
    def __init__(self, value):
        self.parent=self
        self.rank=0
        self.value=value

def findSet(x:Node):
    if x.parent != x:
        x.parent=findSet(x.parent)

    return x.parent    

def union(x:Node,y:Node):
    rootX=findSet(x) #chyba z przepinaniem
    
    while x.parent!=x:
        x, x.parent = x.parent, rootX
    
    rootY=findSet(y)

    while y.parent!=y:
        y, y.parent = y.parent, rootY

    if rootX.rank > rootY.rank:
        rootY.parent=rootX

    else:
        rootX.parent=rootY
        if rootX.rank==rootY.rank:
            rootY.rank+=1



def MST_KruskalLIST(G):
    n=len(G)
    edges=[]
    for i in range(n): #zamiana na krawedzie
        for v in G[i]: #(wierzcholek, waga)
            if (v[1], v[0], i) not in edges:
                edges.append((v[1], i, v[0])) #(waga, u, v)

    edges.sort(key=lambda x: x[2])
 
    v_spojneSquadowe=[] #zamiana na nołdy
    for i in range(n):
        v_spojneSquadowe.append(Node(i))

    MST_result=[]
    for i in range(len(edges)):
        u, v = edges[i][1], edges[i][2]
        if findSet(v_spojneSquadowe[u]) != findSet(v_spojneSquadowe[v]): #nie są w spojnej to:
            MST_result.append((edges[i][1], edges[i][2], edges[i][0]))
            union(v_spojneSquadowe[u], v_spojneSquadowe[v])

    return MST_result # (u, v, waga)



def prim_List(G, w=0): #dijkstra z odczytywaniem sciezki
    n=len(G)            #Elogv
    p_q=PriorityQueue()
    d=[float('inf')]*n
    visited=[False]*n
    parent=[None]*n

    p_q.put((0, w))
    d[w]=0


    while not p_q.empty():
        (prioryty, s)=p_q.get()
        visited[s]=True
        for v, weight in G[s]:
            if weight<d[v] and not visited[v]:
                d[v]=weight
                parent[v]=s
                p_q.put((d[v], v))

    path=[]
    for i in range(n):
        if parent[i] is not None:
            path.append((i, parent[i], d[i]))       

    return parent


graph = [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]
print(MST_KruskalLIST(graph), "\n\n")
print(prim_List(graph))