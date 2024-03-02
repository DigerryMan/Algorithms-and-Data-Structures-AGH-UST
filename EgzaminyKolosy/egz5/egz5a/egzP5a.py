from egzP5atesty import runtests 

def inwestor ( T ):
    n=len(T)
    mini=[[float('inf')]*n for _ in range(n)]
    for i in range(n):
        mini[i][i]=T[i]

    for i in range(n):
        for j in range(i+1,n):
            mini[i][j]=min(mini[i][j-1], T[j])

    F=[[0]*n for _ in range(n)]
    maxi=0

    for i in range(n):
        for j in range(i, n):
            F[i][j]= (j-i+1)*mini[i][j]
            if F[i][j]>maxi:
                maxi=F[i][j]

    return maxi            

        




runtests ( inwestor, all_tests=True )