from egzP5btesty import runtests 


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

    visited=[0]*n
    res=0
    for i in range(n):
        if d[i]==originalTime[i] and parent[i] is not None:
            if not visited[i]:
                visited[i]=True
                if len(G[i])>1:
                    res+=1

            if not visited[parent[i]]:     
                visited[parent[i]]=True
                if len(G[parent[i]])>1:
                    res+=1

    return res


def compare(a, b):
    return a[0]==b[0] and a[1]==b[1]

def koleje ( B ):
    n=len(B)
    maxVertex=0
    tab=[]
    for i in range(n):
        if B[i][0]>maxVertex:
            maxVertex=B[i][0]

        if B[i][1]>maxVertex:
            maxVertex=B[i][1]    

        if B[i][0]<=B[i][1]:
            tab.append([B[i][0], B[i][1]])
            

        else:
            tab.append([B[i][1], B[i][0]])

    tab.sort(key=lambda x:(x[0], x[1]))

    last=tab[0]
    graph=[[]*(maxVertex+1) for _ in range(maxVertex+1)]
    graph[last[0]].append(last[1])
    graph[last[1]].append(last[0])

    for i in range(1,n):            
        if not compare(last, tab[i]):
            last=tab[i]
            graph[last[0]].append(last[1])
            graph[last[1]].append(last[0])


    return bridgeGraph(graph)




runtests ( koleje, all_tests=True )

"""
B = [
(3, 1), (0, 1), (4, 2),
(1, 2), (0, 1), (2, 4),
(2, 4), (0, 3), (2, 4),
(1, 0), (2, 1)
]

print(koleje(B))
"""