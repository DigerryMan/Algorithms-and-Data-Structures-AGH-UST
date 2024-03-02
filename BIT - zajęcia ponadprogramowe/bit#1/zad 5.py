def countingSort(A, k):
    n=len(A)
    C=[0 for _ in range(k+1)]
    B=[0 for _ in range(n)]
    for i in range(n):
        C[A[i]]+=1

    for i in range(1, k+1):
        C[i] = C[i] + C[i-1]

    for i in range(n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1

    for i in range(n):
        A[i]=B[i] 


def zadanie(A, k):
    B=[0 for _ in range(10)]
    cntrB=0
    cntrC=0
    n=len(A)
    C=[0 for _ in range(n-10)]
    
    #rozdzial dobrych od zlych wartosci, gdzie zle w B, dobre w C
    for i in range(n):
        if (A[i]<0 or A[i]>k):
            B[cntrB]=A[i]
            cntrB+=1
        else:
            C[cntrC]=A[i]
            cntrC+=1

    #0->n-10 z przediali [0,k]         n-9 -> n [<0 lub >k]
    
    countingSort(C, k)
    B.sort()
    print(B)
    print(C)
    iter=0
    start=0
    while(B[iter]<0):
        A[iter]=B[iter]
        iter+=1
        start=iter

    for i in range(n-10):
        A[iter]=C[i] 
        iter+=1

    while start<10:
        A[iter]=B[start]
        start+=1
        iter+=1


A=[19,-3,2,3,9,4,2,4,6,73,-3,-3,-4,54,464,44,4,1,0,3,2,58]
k=9
zadanie(A,k)
print(A)






