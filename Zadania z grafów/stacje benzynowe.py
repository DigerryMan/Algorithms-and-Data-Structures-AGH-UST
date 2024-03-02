# A certain land consists of islands between which there are air, ferry and bridge connections.
# There is at most one type of connection between two islands. The cost of the overflight from
# island to island costs 8B, ferry crossing costs 5B and for bridge crossing you have to pay 1B.
# Find route from island A to island B which on each subsequent island changes the transport
# to a different one and minimizes the cost of the trip. We are given an array G that specifies
# the cost of connections between the islands. Value 0 means that there is no direct connection.
# Implement islands(G, A, B) function that returns the minimum travels cost from island A
# to island B. If such a route doesn't exist, the function should return None.
from math import inf
from queue import PriorityQueue

def zadymka(G, A, B):
    n=len(G)
    q=PriorityQueue()

    d=[[inf]*3 for _ in range(n)]
    d[A][0]=d[A][1]=d[A][2]=0

    #1 - most #5 lodka 8# lot
    def relax(u, v, cost, queue):
        if cost == 1: #aktualnie chcemy mostem            
            bylo=False
            if d[u][1] + cost < d[v][0]:  #wczesniej lodz
                d[v][0] = d[u][1] + cost
                bylo=True
                
            if d[u][2] + cost < d[v][0]:  #wczesniej lot
                d[v][0] = d[u][2] + cost
                bylo=True

            if bylo: queue.put((d[v][0], v, 1))


        elif cost == 5: #aktualnie chcemy lodz
            bylo=False
            if d[u][0] + cost < d[v][1]: #wczesniej most
                d[v][1] = d[u][0] + cost
                bylo=True
                
            if d[u][2] + cost < d[v][1]: #wczesniej lot
                d[v][1] = d[u][2] + cost
                bylo=True
            
            if bylo: queue.put((d[v][1], v, 5))
       
       
        else: #aktualnie chcemy lot
            bylo=False
            if d[u][0] + cost < d[v][2]: #wczesniej most
                d[v][2] = d[u][0] + cost
                bylo=True
                
            if d[u][1] + cost < d[v][2]:  #wczesniej lodz
                d[v][2] = d[u][1] + cost
                bylo=True
            
            if bylo: queue.put((d[v][2], v, 8))


    q.put((0, A, 0))
    #1, 5, 8  
    while not q.empty():
        prority, s, lastVisit = q.get()

        for v in range(n):
            if G[s][v]!=0 and G[s][v]!=lastVisit:
                relax(s, v, G[s][v], q)

    return d            






G = [[0, 5, 1, 8, 0, 0, 0],
     [5, 0, 0, 1, 0, 8, 0],
     [1, 0, 0, 8, 0, 0, 8],
     [8, 1, 8, 0, 5, 0, 1],
     [0, 0, 0, 5, 0, 1, 0],
     [0, 8, 0, 0, 1, 0, 5],
     [0, 0, 8, 1, 0, 5, 0]]
print(zadymka(G, 5, 2))