# We have a layout of dominoes. We have it as a list of pairs [a, b]. If we knock over block a, block
# b will also fall over. Find the minimum number of blocks that need to be knocked over by hand so that
# all dominoes are downed.
from collections import deque
from math import sqrt
from math import inf
from queue import PriorityQueue 
from queue import Queue

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





#graph = [[0, 1], [1, 2], [2, 3], [3, 1], [3, 5], [4, 2], [5, 6], [6, 7], [7, 8], [8, 9], [9, 6]]
#graph = [[1,2], [2,3], [3,4], [4,1], [4,5], [0,4], [0,5]]


def dfs(G, topol):
    n=len(G)
    visited=[False]*n

    def dfs_visit(G, s):
        visited[s]=True
        for v in G[s]:
            if not visited[v]:
                dfs_visit(G, v)

    cntr=0
    for s in topol:
        if not visited[s]:
            cntr+=1
            dfs_visit(G, s)

    return cntr        

def domino(G):
    newGraph=[[] for _ in range(6)]

    for i in range(len(graph)):
        newGraph[graph[i][0]].append(graph[i][1])

    return dfs(newGraph, topologoicSortDAGU_DFS(newGraph))    


#print(domino(graph))


def bfs(G, s, t):
    q=deque()
    q.append(s) 
    t_cntr=0

    while q:
        u=q.popleft()
        if u==t:
            t_cntr+=1

        else:    
            for v in G[u]:
                q.append(v)

    return t_cntr            


#graph=[[1],[2,3],[3],[4,5],[5],[]]
#print(bfs(graph, 0, 5))



# Henry the sailor lives on island of an archipelago. All islands including archipelago are so small that
# they can be represented as points in R^2 space. The positions of all islands are given as the sequence
# W = ((x1, y1), ..., (xn, yn)). Henry lives on the island (x1, y1), but he wants to move to the island
# (xn, yn). Normally every day he can sail to an island that is at most Z distance (in standard Euclidean
# distance). He can also sail up to 2Z distance, provided that he will rest all the next day. Henry
# always must stay overnight on some island. Find minimum number of days Henry needs to get to his
# target island (or states that it is impossible).

def dijkstraListowy(G, s, t): # E*log(V)
    #jeden do wszystkich
    n=len(G)        
    q_p=PriorityQueue()
    visited=[False]*n
    parent=[None]*n
    d=[inf]*n
    
    d[s]=0
    q_p.put((0, s))

    def relax(s, v, weight): #s-wierzcholek, v=[wierzcholek, koszt]
        if d[s]+weight<d[v]:
            d[v]=d[s]+weight
            parent[v]=s

    
    while not q_p.empty():
        (prioryty, s)=q_p.get()
        if not visited[s]:
            visited[s]=True

            if visited[t]: break #- dla s do t

            for v in G[s]:
                if not visited[v[0]]:
                    relax(s, v[0], v[1])
                    q_p.put((d[v[0]], v[0]))

    return d[t]        


def count_distance(point1, point2):
    x = abs(point1[0] - point2[0])
    y = abs(point1[1] - point2[1])
    return sqrt(x ** 2 + y ** 2)

def the_sailr_Henry(W, Z, t):
    graph = [[] for _ in range(len(W))]

    for i in range(len(W)):
        for j in range(len(W)):
            if i != j:
                distance = count_distance(W[i], W[j])
                if distance <= Z:
                    graph[i].append([j, 1])
                elif distance > Z and distance <= 2 * Z:
                    if j==len(W)-1:
                        graph[i].append([j, 1])
                    else:    
                        graph[i].append([j, 2])



    #print(graph)
    return dijkstraListowy(graph, 0, t)




Z = 1
W = [(0, 0), (0, 1), (2, 1), (1, 3), (2, 5), (3, 2), (5, 2), (4, 4), (3, 4), (4, 1), (2, 4), (5, 5)]
print(the_sailr_Henry(W, Z, 11))




