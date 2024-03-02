from math import inf

def roznicaZerIJedynek(S):
    n=len(S)
    F=[[-inf]*n for _ in range(n)]
    

    maxi=0
    for i in range(n):
        if S[i]=='0':
            F[i][i]=1
            maxi=1

        else:
            F[i][i]=-1


    
    for i in range(n):
        for j in range(i+1, n):
            if S[j]=='0':
                F[i][j]=F[i][j-1]+1
            else:
                F[i][j]=F[i][j-1]-1    

            if F[i][j]>maxi:
                maxi=F[i][j]

    if not maxi:
        return -1
    return maxi                

"""
stringos="111111111"
print(roznicaZerIJedynek(stringos))
"""

def kLadnaSuma(tab, k):
    n=len(tab)
    F=[inf]*n

    for i in range(k):
        F[i]=tab[i]


    for i in range(k, n):
        for tyl in range(i-k, i):
            F[i] = min(F[i], F[tyl] + tab[i])


    res=inf
    for i in range(n-k, n):
        res=min(res, F[i])

    return res


k=4
tab=[1,2,3,4,6,15,8,7]
print(kLadnaSuma(tab,k))




def ograjGarka(T):
    n=len(T)
    F=[[0 for _ in range(n)] for _ in range(n)]

    F[0][0]=T[0]
    for i in range(1,n):
        F[i][i]=T[i]
        F[i-1][i]=max(T[i-1], T[i])

    for dl in range(3,n+1):
        for i in range(n-dl+1):
            
            j=i+dl-1
            F[i][j] = max(T[i] + min(F[i+2][j], F[i+1][j-1]), T[j] + min(F[i][j-2], F[i+1][j-1]))




    return F[0][n-1]


"""
tab=[8,15,3,7]
print(ograjGarka(tab))
"""


def prom(T, L):
    n=len(T)
    F=[[-1 for _ in range(L+1)] for _ in range(n)]

    F[0][0]=T[0]
    F[0][T[0]]=0

    for i in range(1,n):  
        ENDING=1

        for j in range(L+1):
            if F[i-1][j]!=-1:
                L1=j 
                L2=F[i-1][j]

                if L1+T[i]<=L:
                    ENDING=0
                    F[i][L1+T[i]]=L2

                if L2+T[i]<=L:
                    F[i][L1]=L2+T[i]  
                    ENDING=0

        if ENDING: return i  

    return n 



"""
t = [2,1,4,2,3]
l = 6
print(prom(t,l))
"""

def swap_string(kawiory, s):
    F = [[inf for _ in range(len(s))] for _ in range(len(kawiory))]
    if s[0] == kawiory[0]:
        F[0][0] = 0

    else:
        F[0][0] = 1

    for i in range(1, len(s)):
        if s[i] == kawiory[0]:
            F[0][i] = i

        else:
            F[0][i] = F[0][i - 1] + 1

    for i in range(1, len(kawiory)):
        if s[0] == kawiory[i]:
            F[i][0] = i

        else:
            F[i][0] = F[i - 1][0] + 1

    
    for j in range(1, len(s)):
        for i in range(1, len(kawiory)):
            if s[j] == kawiory[i]:
                F[i][j] = F[i - 1][j - 1]

            else:
                F[i][j] = min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1]) + 1

    print(*F, sep='\n')
    return F[len(kawiory) - 1][len(s) - 1]

"""
print(swap_string("pomidor", "pomidor"))
"""



def konterenowiec(T):
    n=len(T)
    L=sum(T)
    F=[[-1 for _ in range(L+1)] for _ in range(n)]
    F[0][0]=T[0]
    F[0][T[0]]=0

    for i in range(1,n):  

        for j in range(L+1):
            if F[i-1][j]!=-1:
                L1=j 
                L2=F[i-1][j]

                if L1+T[i]<=L:
                    F[i][L1+T[i]]=L2

                if L2+T[i]<=L:
                    F[i][L1]=L2+T[i]  

    mini=inf
    for i in range(0, L+1):
        roz=abs(i-F[n-1][i])
        if roz<mini:
            mini=roz

    return mini 


"""
tab=[1,6,5,11]
print(konterenowiec(tab))
"""


def pseudoPlot(T,k):
    n=len(T)

    F=[[inf for _ in range(n)] for _ in range(k)]

    F[0][0]=T[0]
    for i in range(1,n):
        F[0][i]=F[0][i-1]+T[i]


    for i in range(1,k):
        for j in range(i,n):
            for m in range(i-1, j):
                F[i][j] = min(F[i][j], max(F[i-1][m], sum[j] - sum[m]))

                

