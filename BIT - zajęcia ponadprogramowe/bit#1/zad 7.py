def countingSortdoRadixa(A, place):
    #1 nowa tablica [0,...,9]
    n=len(A)
    C=[0 for _ in range(10)]
    B=[0 for _ in range(len(A))]
    
    #2 zliczamy ile w A
    
    for i in range(n):
        index=(A[i]//place)%10
        C[index]+=1

    #3 suma kumulacyjna
    for i in range(1,10):
        C[i]= C[i] + C[i-1]
    #4 wstawianie elementow z tab A do B poprzez C[A[i]]
    for i in range(len(A)-1,-1,-1):
        index=(A[i]//place)%10
        B[C[index] - 1]=A[i]
        C[index]-=1

    for i in range(len(A)):
        A[i]=B[i] 

def radixSort(A, n):
    countingSortdoRadixa(A,n)
    countingSortdoRadixa(A,n*n)


A=[15,0,3,6]
radixSort(A,len(A))
print(A)




    