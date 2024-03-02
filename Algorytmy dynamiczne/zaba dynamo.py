def zabson(T):
    n=len(T)
    snack_amount=0
    inf=float('inf')

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