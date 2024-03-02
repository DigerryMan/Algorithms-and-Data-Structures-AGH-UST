def prety(T, x):
    T.sort()
    F=[0]*(x+1)

    for i in range(1,x+1):
        for dl, k in T:
            if dl<=i:
                F[i] = max(F[i], k+F[i-dl])

            else: break        

    return F[x]

"""
T=[(3,3),(1,1),(5,8),(7,12)]
x=18

print(prety(T,x))
"""

def binarnyciong(n):

    F=[0]*n+1
    F[1]=2
    F[2]=3

    for i in range(3,n):
        F[i]=F[i-2]+F[i-1]





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
            F[i][i+dl-1] = (string[i]==string[i+dl-1] and F[i+1][i+dl-2])
                
            if F[i][i+dl-1] and dl-1>maxLen:
                max=[i,i+dl-1]
                maxLen=dl-1

    return max                    


#jf="okokon"
#print(palindrom(jf))


def skokiAmazona(T):
    n=len(T)
    F=[0]*n
    F[0]=1

    for i in range(n):
        for j in range(1,T[i]+1):
            F[i+j]+=F[i]

    return F       


tab=[2,3,2,1,0]
print(skokiAmazona(tab))