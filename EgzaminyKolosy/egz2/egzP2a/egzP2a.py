#from egzP2atesty import runtests 

def partition(A, p, r):
    nr, pivot=A[r]
    i=p-1
    for j in range(p,r):
        if(A[j][1]<=pivot):
            i+=1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1] 
    return i+1  

def quickSelectBezRekurencji(A, p, r, k):
    q=partition(A,p,r)
    while(q!=k):
        if(q<k):
            q=partition(A,q+1,r)
        else:
            q=partition(A,p,q-1)   


def zdjecie(T, m, k):
    n=len(T)
    start=0
    end=[0]*m
    end[0]=m-1
    cntr=0
    for _ in range


    return None


m = 2 #Ilość rzędów
k = 2
T = [ (1001, 154),(1002, 176),(1003, 189),(1004, 165),(1005, 162) ]

zdjecie(T,m,k)
print(T)
#runtests ( zdjecie, all_tests=True )