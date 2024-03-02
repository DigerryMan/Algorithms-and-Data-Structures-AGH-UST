def palindrom(string):
    n=len(string)
    F=[[False for _ in range(n)] for _ in range(n)]

    F[0][0]=True    
    for i in range(1,n):
        F[i][i]=True
        if string[i]==string[i-1]:
            F[i-1][i]=True

    max=[0,0]
    maxLen=1

    for dl in range(3,n+1):
        for i in range(n-dl):
            if not F[i][i+dl-1]:
                F[i][i+dl-1] = (string[i]==string[i+dl-1] and F[i+1][i+dl-2])
                if F[i][i+dl-1] and dl-1>maxLen:
                    max=[i,i+dl-1]
                    maxLen=dl-1

    return max  