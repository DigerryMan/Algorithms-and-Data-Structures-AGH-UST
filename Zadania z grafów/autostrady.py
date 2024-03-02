from queue import PriorityQueue
from math import ceil


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
    rootX=findSet(x)
    
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


def autostrady(E):
    n = len(E)
    inf = float("inf")
    G = []
    for i in range(n):
        for j in range(n):
            if i != j:
                xi,yi = E[i]
                xj,yj = E[j]
                G.append([i,j,((xi-xj)**2 + (yi-yj)**2)**(1/2)])
     
    def kruskal(edges):


        maxEdge=-1
        miniEdge=inf
        MST=[]
        for i in range(n):
            if parent[i] != None:
                MST.append([parent[i],i,wagi[i]])
                if maxEdge<wagi[i]:
                    maxEdge=wagi[i]

                if miniEdge>wagi[i]:
                    miniEdge=wagi[i]

        if len(MST) < n - 1:
            return -1
        
        return ceil(maxEdge) - ceil(miniEdge)
    
   
    G.sort(key=lambda x: x[2])
    
    res=condition=primPrzerobionym(G)
    while condition>=0:
        G.remove(G[0])
        condition=primPrzerobionym(G)
        if condition<res:
            res=condition
  
    return res



E=[(10,10), (15,25), (20,20), (30,40)]
print(autostrady(E))