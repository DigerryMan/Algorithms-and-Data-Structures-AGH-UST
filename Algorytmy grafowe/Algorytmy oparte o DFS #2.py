def topologoicSortDAGU_DFS(G): #O(V+E)
    n=len(G)
    visited=[False]*n
    topologicSorted=[]

    def DFS_visit(G, s):
        visited[s]=True

        for v in G[s]:
            if not visited[v]:
                DFS_visit(G, v)
        
        topologicSorted.append(s)

              
    for v in range(n):
        if not visited[v]:
            DFS_visit(G, v)

    topologicSorted.reverse()
    return topologicSorted


def eulerCycleMatrix(G): #O(V^2)
    cycle=[]
    n=len(G)

    def DFS(G, v):
        nonlocal cycle
        for i in range(len(G)):
            if G[v][i]==1:
                G[v][i]=0
                G[i][v]=0
                DFS(G, i)

        cycle.append(v)

    DFS(G, 0)
    cycle.reverse()
    return cycle


def silnieSpojneSkladoweGrafSkierowany(G):  #O(V+E)
    n=len(G)
    visited=[False]*n
    lastOutTime=[]

    def DFS_visit(G, s, tab:list):
        visited[s]=True

        for v in G[s]:
            if not visited[v]:
                DFS_visit(G, v, tab)

        tab.append(s)

    def DFS1(G):   #wyznaczenie kolejnosci wzgl. czasu przetworzenia
        for v in range(len(G)):
            if not visited[v]:
                DFS_visit(G, v, lastOutTime)

    DFS1(G) 

    #odwracanie krawedzi
    G2= [[] for _ in range(n)]
    for w in range(n):
        for v in G[w]:
            G2[v].append(w)   



    visited=[False]*n       #znajdywanie silnie spojych skladowych
    components=[]
    def componentsSearch(G2):
        for i in range(n-1,-1,-1):
            if not visited[lastOutTime[i]]: #silnie wspolna skladowa
                squad=[]
                DFS_visit(G2, lastOutTime[i], squad)
                components.append(squad)  

    componentsSearch(G2)

    return components

print(silnieSpojneSkladoweGrafSkierowany([[1], [2], [0, 3, 8], [4, 6], [5], [3], [5], [8], [9], [5, 10], [3, 7]]))



def bridgeGraph(G): #graf nieskierowany O(V+E)
    n=len(G)
    visited=[False]*n
    parent=[None]*n
    d=[float('inf')]*n
    time=0
    originalTime=[0]*n

    def DFS_visit(G, s):
        nonlocal time
        visited[s]=True
        originalTime[s]=time
        d[s]=time
        time+=1
        
        for v in G[s]:
            if not visited[v]:
                parent[v]=s
                DFS_visit(G, v)
                d[s]=min(d[s], d[v]) #low z dziecka 

            elif parent[s]!=v:  #gdy jest visited i nie parent
                d[s]=min(d[s], originalTime[v])
                 

    for v in range(len(G)):
        if not visited[v]:
            DFS_visit(G, v)

    for i in range(n):
        if d[i]==originalTime[i] and parent[i] is not None:
            print((parent[i], i), "\n")


