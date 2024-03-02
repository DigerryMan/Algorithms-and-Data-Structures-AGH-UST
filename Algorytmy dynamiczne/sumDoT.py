def sumowanieDoT(A, T):
    n=len(A)
    F=[[0 for _ in range(T+1)] for _ in range(n+1)]

    for i in range(n+1):
        F[i][0]=1

    for i in range(1,n+1):
        for t in range(1,T+1):
            if F[i-1][t]:
                F[i][t]=F[i-1][t]
            
            elif t-A[i-1]>=0:
                F[i][t]=F[i-1][t-A[i-1]]

    return F  