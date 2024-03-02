from egzP8btesty import runtests


def floydWarshallListowa( G ):  #najkrotsze sciezki miedzy kazda para wierzcholkow
    n=len(G)
    D=[[float('inf') for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        D[i][i]=0

    for s in range(n):
        for v in G[s]: #(wierzcholek, waga)
            D[s][v[0]]=v[1]


    for t in range(n):
        for x in range(n):
            for y in range(n):
                D[x][y] = min(D[x][y], D[x][t]+ D[t][y])
                
                
    return D



def robot( G, P ):
    
    G2 = floydWarshallListowa(G)
    cost = 0
    for i in range(1, len(P)):
        cost += G2[P[i - 1]][P[i]]


    return cost
    
runtests(robot, all_tests = True)
