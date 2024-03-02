def plot(T, k):
    n=len(T)

    F= [[0]*n for _ in range(k)] 
    F[0][0]=T[0]

    for i in range(1,n):
        F[0][i]=F[0][i-1]+T[i]

    for kk in range(1, k):
        for i in range(kk, n):
            for j in range(i-1,kk-2,-1):
                curSum=F[0][i]-F[0][j]       
                F[kk][i] = max(F[kk][i], min(curSum, F[kk-1][j])) 

    print(*F, sep='\n')


T = [5,7,2,4,8,1,3]
k = 5
plot(T, k)