from math import inf

def blackForest(c):
    n=len(c)
    F=[0]*n
    F[0]=c[0]
    F[1]=max(c[0], c[1])
    takenList=[[] for _ in range(n)]
    takenList[0].append(0)
    if F[1]==F[0]:
        takenList[1].append(0)
    else:
        takenList[1].append(1)    

    for i in range(2,n):
        F[i]=F[i-1] #nie bierzemy

        if F[i] < F[i-2]+c[i]:
            kopia=takenList[i-2].copy()
            kopia.append(i)
            takenList[i]=kopia.copy()
            F[i] =  F[i-2]+c[i]    

        else:
            takenList[i]=takenList[i-1].copy()   

    return F[n-1], takenList


#c = [1,5,1,0,1,3,9,1]
#print(blackForest(c))


def possibleToPlace(k1, k2):
    return k2[0]<=k1[0] and k1[1]<=k2[1]

def fallingKloces(L):
    n=len(L)
    high=[1 for _ in range(n)]

    for i in range(1,n):
        for j in range(i):
            if possibleToPlace(L[i], L[j]):
                if high[i] < high[j] + 1:
                    high[i] = high[j] + 1

    #szukanie najlepszego kloca
    index=0
    maxi=0
    for i in range(n):
        if high[i]>maxi:
            maxi=high[i]
            index=i

    return n-maxi        



#Bricks = [[0,3],[1,7],[3,7],[0,3],[1,3],[1,2],[4,7],[5,6]]
#print(fallingKloces(Bricks))

def zabson(T):
    n=len(T)
    snack_amount=0

    for i in range(n):
        snack_amount+=T[i]


    F=[[inf]*n for _ in range(snack_amount+1)]
    F[T[0]][0]=0

    for i in range(n):
        for p in range(snack_amount+1):
            if F[p][i] != inf:  # w p jest stan aktualnej energii
                for j in range(i+1,n):
                    odl=(j-i)**2
                    snack=T[j]
                    if p>=odl:
                        miejsce=p-odl+snack
                        if F[p][i]+1 < F[miejsce][j]:
                            F[miejsce][j] = F[p][i]+1
 
                    else: break        

    mini=inf
    for p in range(snack_amount+1):
        if F[p][n-1]<mini:
            mini=F[p][n-1]

    return F


T = [3,0,0,3,2,1,0,0,5,0,1,7,7,1,1,2,0]

def print_tab(T):
    w=len(T)
    k=len(T[0])
    for i in range(w):
        print(T[i])
 

Tab=zabson(T)
print_tab(Tab)

