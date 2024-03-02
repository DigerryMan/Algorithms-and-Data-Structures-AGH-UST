

def longestSubstring(A):
    n=len(A)
    F=[1]*n
    P=[None]*n
    for i in range(1,n):
        for j in range(i):
            if A[j]<A[i] and F[j]+1>F[i]:
                P[i]=j
                F[i]=F[j]+1

    return max(F), P            



def binSearch(tab,l,r, el):

    while(l!=r):
        s=(l+r)//2
        if tab[s]==el:
            return s
        
        if tab[s]<el:
            l=s+1

        else:
            r=s   
     
    return l


def LIN_nlogn(tab): 
    res=[tab[0]]
    n=len(tab)
    for i in range(1,n):
        l=len(res)
        if res[l-1]<tab[i]:
            res.append(tab[i])

        else:
            s=binSearch(res,0,l-1,tab[i])
            res[s]=tab[i]

    return res

T = [2,3,1,2,5,3,7]
print(LIN_nlogn(T))


def LIN_nlogn_wiekszeRowne(tab): 
    res=[tab[0]]
    n=len(tab)
    for i in range(1,n):
        l=len(res)
        if res[l-1]<=tab[i]:
            res.append(tab[i])

        else:
            s=binSearch(res,0,l-1,tab[i])
            res[s]=tab[i]

    return len(res)