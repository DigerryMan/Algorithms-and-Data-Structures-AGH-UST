from math import inf 
from collections import deque

def DFS(G, s, t, parent):
    n=len(G)
    visited=[False]*n

    def DFS_visit(G, s):
        nonlocal n
        visited[s]=True

        for v in range(n):
            if G[s][v]!=0 and not visited[v]:    
                parent[v]=s
                DFS_visit(G, v)

    DFS_visit(G, s)
    return visited[t]   

def fordFulkersonMATRIX(G, s, t):
    n=len(G)
    parent=[None]*n
    maxFlow=0 

    while DFS(G,s,t,parent):
        currFlow=inf
        
        v=t
        while v!=s:
            currFlow = min(currFlow, G[parent[v]][v])
            v=parent[v]

        maxFlow+=currFlow
        v=t
        while v!=s:
            G[parent[v]][v] -= currFlow
            G[v][parent[v]] += currFlow
            v=parent[v]


    return maxFlow        
    








def BFS(G, s, t, parent):
    n=len(G)
    visited=[False]*n
    visited[s]=True

    q=deque()
    q.append(s)

    while len(q)>0:
        u = q.popleft() 

        for v in range(n):
            if G[u][v]!=0 and not visited[v]:
                visited[v]=True
                parent[v]=u
                q.append(v)

    return visited[t]            


def edmondsKarpMATRIX(G, s, t):
    n=len(G)
    parent=[None]*n
    maxFlow=0 

    while BFS(G, s, t, parent):
        currFlow=inf
        
        v=t
        while v!=s:
            currFlow = min(currFlow, G[parent[v]][v])
            v=parent[v]

        maxFlow+=currFlow
        v=t
        while v!=s:
            G[parent[v]][v] -= currFlow
            G[v][parent[v]] += currFlow
            v=parent[v]


    return maxFlow        

