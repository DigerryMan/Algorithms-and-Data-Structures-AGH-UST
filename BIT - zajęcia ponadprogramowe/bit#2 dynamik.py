from math import inf

def opt(T, P):
    k=len(T[0])
    n=len(T)

    suma_prefix=[[T[j][0] for i in range(P)] for j in range(n)]
    for i in range(1,P):
        for j in range(n):
            dodatek=0
            if i<k:
                dodatek=T[j][i]

            suma_prefix[j][i] = suma_prefix[j][i-1] + dodatek

    
    F=[[-inf]*(P+1) for _ in range(n)]

    for i in range(P):   
        F[0][i+1]=suma_prefix[0][i]

    for i in range(n):
        F[i][0]=0    

    for s in range(1, n):
        for p_count in range(1,P+1):
            for ile_biere in range(p_count):     
                F[s][p_count] = max(F[s][p_count], F[s-1][p_count-ile_biere-1] + suma_prefix[s][ile_biere])      


    return F[n-1][P-1]            

"""
Tab=[[1,0,2],
     [2,-1,1],
     [1,0,3]]
    
print(opt(Tab, 4))
"""

dis=False
def zbajdzWynik(tab, w):
    global dis
    if dis: return

    if w<0:
        dis=True
        return
        
    for i in range(w, -1,-1):
        if tab[i][w]:
            zbajdzWynik(tab, i-1, i-1)


"""
slowo=[[0,0,1,0,0],
       [0,0,1,0,1],
       [0,0,0,0,0],
       [0,0,0,0,1],
       [0,0,0,0,0]]


zbajdzWynik(slowo, 4)
print(dis)
"""

def fabric(X, Y, T):
    F = [[0 for _ in range(X + 1)] for _ in range(Y + 1)]

    for x in range(1, X + 1):
        for y in range(1, Y + 1):
            for xi, yi, price in T:
                if xi <= x and yi <= y:
                    F[y][x] = max(F[y][x], 
                                  price + F[y-yi][xi] + F[y-yi][x-xi]
                                  + F[yi][x-xi])

                xi, yi = yi, xi

                if xi <= x and yi <= y:
                    F[y][x] = max(F[y][x], 
                                  price + F[y-yi][xi] + F[y-yi][x-xi]
                                  + F[yi][x-xi])

    return F[Y][X]


T = [(1,2,1),(6,2,4),(5,4,6),(7,3,15)]

print(fabric(7,4,T))