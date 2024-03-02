from queue import PriorityQueue

"""
class Node:
    def __init__(self, value):
        self.value = value
        self.parent = self

def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent

def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.value < y.value:
        y.parent = x
    else:
        x.parent = y


def equivalentLetters(A, B, C):
    letters=[Node(i) for i in range(26)]
    n=len(A)
    for i in range(n):
        first=ord(A[i])-ord('a')
        second=ord(B[i])-ord('a')

        union(letters[first], letters[second])

        
    newString=""
    for i in range(len(C)):
        idx=ord(C[i])-ord('a')
        x=find(letters[idx])

        char= chr(x.value + ord('a'))   
        newString+=char

    return newString     

A = "caef"
B = "fbga"
C = "abdfe"

A = "oauhihunosjrnhijsr"
B = "hozonbibieguiyuigb"
C = "abdfeiohiub"

print(equivalentLetters(A,B,C))
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.rank = 0
        self.parent = self


def find(x):
    if x != x.parent:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1

    return True        


def make_set(val):
    return Node(val)


def airports(graph, K):
    graph.sort(key=lambda x: x[2])
    n=len(graph)

    
    max_V=0
    for i in range(n):
        max_V=max(max_V, graph[i][0], graph[i][1])

    cities=[Node(i) for i in range(max_V+1)]


    cost=0
    for i in range(n):
        if graph[i][2]>=K:
            break

        elif union(cities[graph[i][0]], cities[graph[i][1]]):
            cost+=graph[i][2]

    airports=0
    for i in range(1, max_V+1):
        if cities[i].parent==cities[i]:
            airports+=1

    cost+=airports*K        

    return cost, airports        



graph = [(0, 1, 2), (0, 2, 3), (0, 6, 4), (0, 7, 7), (2, 3, 1), (2, 5, 5), (3, 4, 3),
         (6, 7, 4), (6, 8, 6), (7, 8, 2)]
K = 4
print(airports(graph, K))



def super_cool_paths(G, s):
    n=len(G)        
    q_p=PriorityQueue()
    parent=[None]*n
    d=[float('inf')]*n
    vertices=[float('inf')]*n

    d[s]=0
    vertices[s]=0

    
    def relax(s, v, weight):
        if d[s]+weight<d[v]:
            d[v]=d[s]+weight
            vertices[v]=vertices[s]+1
            parent[v]=s
            return True

        elif d[s]+weight==d[v] and vertices[s]+1<vertices[v]: 
            vertices[v]=vertices[s]+1
            parent[v]=s
            return True

        return False   

    
    q_p.put((0, s))  
    while not q_p.empty():
        dist, w = q_p.get()
        
        for v, waga in G[w]:
            if relax(w, v, waga):
                q_p.put((d[v], v))

    return d, parent, vertices   


graph = [[(1, 1), (5, 1), (7, 2)],
         [(0, 1), (2, 1)],
         [(1, 1), (3, 1)],
         [(2, 1), (4, 1)],
         [(3, 1), (6, 1), (7, 2)],
         [(0, 1), (6, 2)],
         [(5, 2), (4, 1)],
         [(0, 2), (4, 2)]]

distance, parent, vertices_length = super_cool_paths(graph, 0)
i = len(parent) - 1
while parent[i] is not None:
    print(i, distance[i], vertices_length[i])
    i -= 1
