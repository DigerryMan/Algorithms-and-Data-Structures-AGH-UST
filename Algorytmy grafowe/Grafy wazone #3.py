from collections import deque
from queue import PriorityQueue
from math import inf


def bfs_wazony(G, s):
    n=len(G)
    visited=[False]*n
    Q=deque()
    Q.append(0,0)
    visited[0]=True

    while(len(Q)>0):
        s, weight = Q.popleft()   
        if weight==0:
            for v, weight_v in G[s[0]]:
                if not visited[v]:   
                    visited[v]=True
                    Q.append((v, weight_v))
                    

        else:
            Q.append((s[0], s[1]-1))    





def dijkstraListowy(G, s=0): # E*log(V)
    #jeden do wszystkich
    n=len(G)        
    q_p=PriorityQueue()
    visited=[False]*n
    parent=[None]*n
    d=[inf]*n
    
    d[s]=0
    q_p.put((0, s))

    def relax(s, v, weight): #s-wierzcholek, v=[wierzcholek, kosztt
        if d[s]+weight<d[v]:
            d[v]=d[s]+weight
            parent[v]=s

    
    while not q_p.empty():
        (prioryty, s)=q_p.get()
        
        if not visited[s]:
            visited[s]=True
            #if visited[t]: break - dla s do t
            for v, weight in G[s]:
                if not visited[v]:
                    relax(s, v, weight)
                    q_p.put((d[v], v))

    return d               




G=[[[1,1], [4,2]],
   [[0,1], [2,3]],
   [[1,3], [3,3], [4,1]],
   [[2,3], [4,7]],
   [[0,2], [2,1], [3,7]]]

print(dijkstraListowy(G))


def dijkstra_Matrix(G, s=0): #O(V^2)
    n=len(G)
    visited=[False]*n
    parent=[None]*n
    d=[inf]*n
    d[s]=0
    

    def relax(s,v, weight): 
        if d[s]+weight<d[v]:
            d[v]=d[s]+weight
            parent[v]=s

    while True:
        mini=inf
        v=-1
        for i in range(n):    #szukanie minimalnego priorytetu wierzcholka
            if not visited[i] and d[i]<mini:
                mini=d[i]
                v=i

        if v==-1:
            break

        visited[v]=True
        for k in range(n):
            if G[v][k]!=inf and not visited[k]:
                relax(v, k, G[v][k])
                    

G=[[inf,1,inf,inf,2],
   [1,inf,3,inf,inf],
   [inf,3,inf,3,1],
   [inf,inf,3,inf,7],
   [2,inf,1,7,inf]]




def bellmanFordList(G, sV): #dla ujemnych wag tez
    n=len(G)            #GRAF SKIEROWANY
    parent=[None]*n     #wykrywanie cyklu ujemnego
    d=[inf]*n
    d[sV]=0

    def relax(s,v, weigth):
        if d[s]+weigth<d[v]:
            d[v]=d[s]+weigth
            parent[v]=s

    for _ in range(n-1):
        for s in range(n):
            for v, weight in G[s]:
                relax(s, v, weight)            

    #weryfikacja
    for s in range(n):
        for v, weight in G[s]:
            if d[v]>d[s]+weight:
                return False #gdzies jest cykl o ujemnej wartosci

    return d              



def bellmanFordMatrix(G, s=0): #-inf - brak krawedzi
    #ZAŁOZENIE: nie ma cyklu
    n=len(G)
    d=[inf]*n
    parent=[None]*n

    d[s]=0
    for _ in range(n-1):
        anyChanges=False

        for u in range(n):
            for v in range(n):
                if G[u][v]!= -inf:
                    if d[v]> d[u] + G[u][v]:
                        d[v] = d[u] + G[u][v]
                        parent[v] = u
                        anyChanges=True

        if not anyChanges:
            break                

    return d        

"""
graph=[[-inf,3,-inf, 3, 2],
       [-inf,-inf,-7, -inf, -inf],
       [-inf,-inf,-inf, 8, -inf],
       [-inf,-1,-inf, -inf, -2],
       [-inf,-inf,-inf, -inf, -inf]]

       
graph=[ [(1,3),(3,3),(4,2)],
        [(2,-7)],
        [(3,8)],
        [(1,-1),(4,-2)],
        []
]      


print(bellmanFordMatrix(graph))
"""

def bellmanFordListowePodejscie(G, s=0): # SUS
    n=len(G)
    d=[inf]*n
    parent=[None]*n
    d[s]=0

    for i in range(n-1):
        anyChanges=False

        for u in range(n):
            for v, weight in G[u]:
                if d[v] > d[u] + weight:
                    d[v] = d[u] + weight
                    parent[v]=u
                    anyChanges=True

        if not anyChanges:
            break            

    return d    





