
#counting sort
def countingSort(A):
    n=len(A)
    B = [0]*10
    C = [0]*n

    for i in range(n):
        B[A[i]] += 1

    for i in range(1,n):
        B[i]+=B[i-1]

    #gdy malejąco (0, n)
    for i in range(n-1,-1,-1):
        C[B[A[i]] - 1] = A[i]
        B[A[i]] -= 1         

    #gdy malejaco A[i] = C[n-1-i]
    for i in range(n):
        A[i] = C[i]    

#merge sort
def merge(T, p, q, r):
    L=T[p:q+1]
    R=T[q+1:r+1]
    LLen=len(L)
    RLen=len(R)
    i=j=0
    k=p

    while(i<LLen and j<RLen):
        if L[i] <= R[j]:
            T[k]=L[i]
            i+=1
        
        else:
            T[k]=R[j]
            j+=1

        k+=1    

    while(i<LLen):
        T[k]=L[i]
        i+=1
        k+=1

    while(j<RLen):
        T[k]=R[j]
        j+=1
        k+=1    



def mergeSort(T, p, r):
    if p<r:
        q=(p+r)//2
        mergeSort(T, p, q)
        mergeSort(T, q+1, r)
        merge(T, p, q, r)





####  QUICK SORT

def partition(A, p, r):
    pivot=A[r]
    i=p-1
    for j in range(p,r):
        if(A[j]<=pivot):
            i+=1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[r] = A[r], A[i+1] 
    return i+1       

def quickSort(A, p, r):
    if p<r:
        q=partition(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)


#tab=[2,3,12,4,21,5,12,2]
#quickSort(tab, 0, len(tab)-1)
#print(tab)       

#QUICK SELECT

def quickSelect(A, p, r, k):
    q=partition(A, p, r)
    if q == k-1:
        return A[q]
    
    elif q < k-1:
        return quickSelect(A, q+1, r, k)
    
    return quickSelect(A, p, q-1, k)

def quickSelectBezRekurencji(A, p, r, k):
    q=partition(A,p,r)
    while(q!=k):
        if(q<k):
            q=partition(A,q+1,r)
        else:
            q=partition(A,p,q-1)    
            

arr = [ 10, 4, 5, 8, 6, 11, 26 ]

print(quickSelect(arr, 0, len(arr)-1, 5))


#heap sort
def left(i):
    return i*2+1

def right(i):
    return i*2+2

def parent(i):
    return (i-1)//2

def heapify(T,i,n):
    l=left(i)
    r=right(i)
    max_index=i
    if l<n and T[l]>T[max_index]:
        max_index=l

    if r<n and T[r]>T[max_index]:
        max_index=r

    if max_index!=i:
        T[max_index], T[i] = T[i], T[max_index]        
        heapify(T,max_index,n)

def buildHeap(T):
    n=len(T)
    for i in range(parent(n-1), -1, -1 ):
        heapify(T, i, n)

def heapSort(T):
    n=len(T)
    buildHeap(T)

    for i in range(n-1, 0, -1):
        T[0], T[i], = T[i], T[0]
        heapify(T, 0, i)


#bucket sort
def bucketSort(T):
    n=len(T)
    buckets=[[] for _ in range(n)]

    for i in range(n):
        index_b = int(n*T[i])
        buckets[index_b].append(T[i])

    for i in range(n):
        mergeSort(buckets[i], 0, len(buckets[i])-1)

    k=0
    for i in range(n):      
        for j in range(len(buckets[i])):
            T[k]=buckets[i][j]
            k+=1


def binarySearch(T,p,r, el):
    if p>r:
        return False

    q=(p+r)//2
    if el<T[q]:
        return binarySearch(T,p,q-1,el)
    elif el==T[q]:
        return True
    
    return(binarySearch(T,q+1,r,el))
    

