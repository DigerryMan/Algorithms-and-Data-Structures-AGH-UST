import time
import random

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None


def insertionSort(T):
    n=len(T)
    for i in range(1,n):
        tmp=T[i]
        j=i-1
        while(j>=0 and tmp<T[j]):
            T[j+1]=T[j]
            j-=1
        
        T[j+1]=tmp   

    return T

#insertionSort([7,4,5,2])            


def findTheMinimumSort(T):
    n=len(T)
    for i in range(n-1):
        min_indx=i
        for j in range(i+1,n):
            if T[j]<T[min_indx]:
                min_indx=j
        T[min_indx], T[i] = T[i], T[min_indx]        
        print(T)
    return T    

#findTheMinimumSort([7,6,5,2]) 

def insertNode(L:Node, p:Node):
    while(L.next is not None and L.next.val<p.val):
        L=L.next

    p.next=L.next
    L.next=p    

def sort_node(L:Node):
    head = L
    while L.next:
        tmp = L.next
        L.next = L.next.next
        tmp.next = None
        insertNode(L, tmp)

def min_max(T):
    n=len(T)
    m, M = T[0], T[0]

    for i in range(1,n,2):
        if(T[i]<T[i+1]):
            
            if(T[i]<m):
                m=T[i]
            if(T[i+1]>M):
                m=T[i+1]    
        
        else:    
            if(T[i+1]<m):
                m=T[i]
            if(T[i]>M):
                m=T[i+1]  
    
    if(n%2==1):
        if(T[n-1]<m):
            m=T[n-1]
        
        if(T[n-1]>M):
            m=T[n-1]

    return m,M        

def tabGenerator(n):
    tab=[random.randint(0,1000000) for _ in range(n)]
    return tab

def partition(array, low, high):
 
    # choose the rightmost element as pivot
    pivot = array[high]
 
    # pointer for greater element
    i = low - 1
 
    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
 
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
 
 
def quickSort(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSort(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSort(array, pi + 1, high)

#step=50  
#for i in range(step,10000+1,step): 

    #tab=tabGenerator(1000000)
    #print("jazda")
    #start_time = time.time() 
    #quickSort(tab,0, len(tab)-1)
    #print("--- %s seconds ---" % (time.time() - start_time))


def find_x(t, x):
    n = len(t)
    i = 0
    j = 1
    while True:
        if t[j] - t[i] == x:
            return i,j
        
        if t[j] - t[i] < x:
            j += 1

        else:
            i += 1

        if j == n:
            return -1   
        

#Mamy posortowana tablice liczb. Elementy sa rozne. N < m. Podaj algorytm 
# ktory znajduje najmniejsza liczbe calkowita ktorej nie ma w ciagu.

def binarySearch(T, x):
    l=0
    p=len(T)-1

    while(l<p):
        s=(l+p)//2

        if T[s]==x:
            return True
        
        if T[s]<x:
            l=s+1

        else:
            p=s-1

    return T[l]==x

def findMin(t, ciag):
    dl=len(t)

    mini=100000000000
    for i in range(dl):
        if not binarySearch(ciag, t[i]):
            mini=min(mini, ciag[i])
    
    return mini

            


print(findMin([2,5,7,8], [1,]))


