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
