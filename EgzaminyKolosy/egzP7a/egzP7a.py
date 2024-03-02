from egzP7atesty import runtests 
from math import inf

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



def akademik( T ):
    n=len(T)

    ileNone=0
    for i in range(n):
        if T[i][0] is None:
            ileNone+=1

    matrix=[[0]*(2*n+2) for _ in range(2*n+2)]
    for i in range(n):
        for j in range(3):
            if T[i][j] is not None:
                matrix[i][n+T[i][j]]=1
    

    for i in range(n):
        matrix[2*n][i]=1

        matrix[n+i][2*n+1]=1

    resCntr=fordFulkersonMATRIX(matrix, 2*n, 2*n+1)           

    
    return n-resCntr-ileNone        



runtests ( akademik )