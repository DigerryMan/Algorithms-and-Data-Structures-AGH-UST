def krejziFunkcja(A,B):
    n=len(A)
    d=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1,n+1):
               if A[i]==B[j]:
                    d[i][j]=d[i-1][j-1] + 1

               else:
                    d[i][j]=max(d[i-1][j], d[i][j-1])       

    return d[n][n]        