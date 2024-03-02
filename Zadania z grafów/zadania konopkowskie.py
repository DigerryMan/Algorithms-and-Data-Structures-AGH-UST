
#JEZIORKA
def lakes(G):
    n=len(G)
    lakesCntr=0
    maxLakeSize=0
    visited=[[False for _ in range(n)] for g in range(n)]

    def DFS(G,w,k):
        counter=0

        def DFS_visit(G, w, k):
            nonlocal counter
            if n>w>=0 and n>k>=0 and not visited[w][k] and G[w][k]=="W":
                visited[w][k]=True
                counter+=1
                DFS_visit(G, w+1, k)
                DFS_visit(G, w-1, k)
                DFS_visit(G, w, k+1)
                DFS_visit(G, w, k-1)

        DFS_visit(G, w, k)
        
        return counter


    for w in range(n):
        for k in range(n):
            if not visited[w][k] and G[w][k]=="W":
                c=DFS(G, w, k)
                lakesCntr+=1

                if c>maxLakeSize:
                    maxLakeSize=c

    return lakesCntr, maxLakeSize


"""
T = [["L", "W", "L", "L", "L", "L", "L", "L"],
     ["L", "W", "L", "W", "W", "L", "L", "L"],
     ["L", "L", "L", "W", "W", "L", "W", "L"],
     ["L", "W", "W", "W", "W", "L", "W", "L"],
     ["L", "L", "W", "W", "L", "L", "L", "L"],
     ["L", "W", "L", "L", "L", "L", "W", "W"],
     ["W", "W", "L", "W", "W", "L", "W", "L"],
     ["L", "L", "L", "W", "L", "L", "L", "L"]]

print(lakes(T))
"""



#jakies drzewa

def subtree_size(edges, root):
    max_vertex = 0
    for i in range(len(edges)):
        max_vertex = max(max_vertex, max(edges[i]))
    G = [[] for _ in range(max_vertex + 1)]
    for i in range(len(edges)):
        G[edges[i][0]].append(edges[i][1])
        G[edges[i][1]].append(edges[i][0])

    n=len(G)
    visited=[False]*n
    subTreesLen=[0]*n

    def DFS_visit(G, s):
        visited[s]=True
        sumTreeLen=1
        for v in G[s]:
            if not visited[v]:
                sumTreeLen+=DFS_visit(G, v)

        subTreesLen[s]=sumTreeLen
        return sumTreeLen        
    
    chuj=DFS_visit(G, root)

    return subTreesLen

"""
edges = [[0, 1], [0, 2], [1, 3], [2, 4], [2, 5], [2, 6], [3, 7], [3, 8], [3, 9], [4, 10], [5, 11], [5, 12], [7, 13],
         [7, 14], [8, 15], [9, 16], [9, 17], [11, 18], [11, 19], [11, 20], [12, 21]]
print(subtree_size(edges, 0))
"""


#sortowanie topologiczne

def topoligicSort(G):
    n=len(G)
    visited=[False]*n
    topologicList=[]

    def DFS_visit(G, s):
        visited[s]=True

        for v in G[s]:
            if not visited[v]:
                DFS_visit(G, v)

        topologicList.append(s)

    
    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)

    topologicList.reverse()
    return topologicList            

"""
graph = [[1, 2], [2, 3], [], [4, 5, 6], [], [], [], [3], [7]]
print(topoligicSort(graph))
"""


def spojneSkladowe(G):
    n=len(G)
    visited=[False]*n
    sequence=[]

    def DFS_visit(G, s, tab:list):
        visited[s]=True
        
        for v in G[s]:
            if not visited[v]:
                DFS_visit(G, v, tab)

        tab.append(s)

    for i in range(len(G)):
        DFS_visit(G, i, sequence)    


    G2=[[] for _ in range(n)]
    for i in range(n):
        for j in range(len(G[i])):
            G2[G[i][j]].append(i)

    visited=[False]*n      
    squad=[]
    for i in range(n-1,-1,-1):
        if not visited[sequence[i]]:
            locSquad=[]
            DFS_visit(G2, sequence[i], locSquad)  
            squad.append(locSquad)

    return squad

"""
graph = [[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]
print(spojneSkladowe(graph)) 
"""