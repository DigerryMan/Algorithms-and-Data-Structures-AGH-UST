from queue import PriorityQueue
from math import inf

def dijkstraListowy(G, parent, s=0): # E*log(V)
    #jeden do wszystkich
    n=len(G)        
    q_p=PriorityQueue()
    visited=[False]*n
    d=[inf]*n
    
    d[s]=0
    q_p.put((0, s))

    def relax(s, v, weight): #s-wierzcholek, v=[wierzcholek, kosztt
        if d[s]+weight < d[v]:
            d[v] = d[s]+weight
            parent[v].append(s)
            return True
        
        if d[s]+weight == d[v]:
            parent[v].append(s)

        return False    


    
    while not q_p.empty():
        (prioryty, s)=q_p.get()
        
        if not visited[s]:
            visited[s]=True
            #if visited[t]: break - dla s do t
            for v, weight in G[s]:
                if relax(s, v, weight):
                    q_p.put((d[v], v))

def DFS(G, y):
    cntr=0

    return cntr

def edgesInGraphMinPath(G, s, t):
    n=len(G)
    parent=[[]*n for _ in range(n)]
    dijkstraListowy(G, parent, s)
    cntr=0
    for i in range(n):
        cntr+=len(parent[i])

    return DFS(parent, t)



G=[[(1,1), (6,1)],
   [(0,1), (2,1)],
   [(1,1), (3,1), (4,1)],
   [(2,1), (5,1)],
   [(2,1), (5,1), (7,1)],
   [(3,1), (3,1)],
   [(0,1), (7,1)],
   [(6,1), (4,1)]]

print(edgesInGraphMinPath(G,0,5))
