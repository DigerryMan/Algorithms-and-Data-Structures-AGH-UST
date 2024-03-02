#pretty sort

from math import log
import random
"""
robimy tablice tupli 3 elementowych
sortujemy countsortem po lasciku i po srodkowym
(liczba, jednokrotne, wielokrotne)
(wynik ,  malejace, rosnace)

"""

def countingSort2ndPositionDescending(A, n):
    B=[0]*10
    C=[0]*n

    for i in range(n):
        B[A[i][1]]+=1

    for i in range(1,10):
        B[i] += B[i-1]

    for i in range(n):
        C[B[A[i][1]] - 1] = A[i]
        B[A[i][1]] -= 1 

    for i in range(n):
        A[i] = C[n-1-i][0]    

def countingSort3rdPositionAscendingReturningResult(A, n):
    B=[0]*10
    C=[0]*n

    for i in range(n):
        B[A[i][2]]+=1

    for i in range(1,10):
        B[i] += B[i-1]

    for i in range(n-1, -1, -1):
        C[B[A[i][2]] - 1] = A[i]
        B[A[i][2]] -= 1 

    for i in range(n):
        A[i] = C[i]         



def translateOn3elArrays(T, x):
    digits=[0]*10
    a=T[x]
    solo=duoAndMore=0

    while a>0:
        digits[a%10]+=1
        a//=10

    for i in range(10):
        if(digits[i]>1): 
            duoAndMore+=1
        elif(digits[i]==1):
            solo+=1

    T[x]=[T[x], solo, duoAndMore]        
           



def pretty_sort(T):
    n=len(T)
    for i in range(n):
        translateOn3elArrays(T, i)
    print(T, "\n")


    countingSort3rdPositionAscendingReturningResult(T, n)  #rosnąco w wielokrotnych
    print(T, "\n")
    countingSort2ndPositionDescending(T, n) #malejąco w jednokrotnych
    print(T, "\n")


T=[[123,4], [123, 4], [123,1], [28,0], [22,8], [4456,5]]   
#pretty_sort(T)     



#chaos index
"""
zamienic na tuple z indexem, sortujemy normalnie po liczbach
posortowac stabilnie i potem znalezc maxymalna
roznice miedzy posortowanym a oryginalnym indexem
"""

def merge(T, p, q, r):
    L=T[p:q+1]
    R=T[q+1:r+1]
    LLen=len(L)
    RLen=len(R)
    i=j=0
    k=p

    while(i<LLen and j<RLen):
        if L[i][0] <= R[j][0]:
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


def translateArray(T, n):
    for i in range(n):
        T[i] = (T[i], i)

def chaos_index(T):
    n=len(T)
    translateArray(T,n)
    mergeSort(T, 0, n-1)
    
    maxi=0
    for i in range(n):
        x=abs(T[i][1] - i)
        if(x>maxi):
            maxi=x

    return maxi

#T=[0,2,1,2]
#print(chaos_index(T))




#zadanie z zolnierzami
"""
quickselect wzgledem p i potem wzgledem q w przedziale [p, n-1]

"""

def partition(arr, l, r):  
    x = arr[r]
    i = l
    for j in range(l, r):
          
        if arr[j] >= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
              
    arr[i], arr[r] = arr[r], arr[i]
    return i


def quickSelect(A, p, r, k):
    if p==r:
        return A[p]
    
    q=partition(A, p, r)
    if q == k-1:
        return A[q]
    
    elif q < k-1:
        return quickSelect(A, q+1, r, k)
    
    return quickSelect(A, p, q-1, k)


def section(T, p, q):
    quickSelect(T, 0, len(T)-1, p)
    quickSelect(T, p, len(T)-1, q-p+1)
    return T[p:q+1]


#p=2; q=6 # => [100, 110,    (130, 130, 150, 170, 180, )    190] 
#tab=[110,130,100,190,180,170,150,130]
#print(section(tab, 2, 6))


def bucketSorcik(tab, a, n):
    buckets=[[] for _ in range(n)]
    
    for i in range(n):
        indexB=int(log(tab[i], a)*n)
        buckets[indexB].append(tab[i])

    for i in range(n):
        buckets[i].sort()

    
    k=0
    for i in range(n):
        for j in range(len(buckets[i])):
            tab[k]=buckets[i][j]
            k+=1





#zadanie z eksperymentem fizycznym
def fast_sort(tab, a):
    n=len(tab)
    bucketSorcik(tab, a, n)



#n = 7
#t = [0]*n
#a = 5

#or i in range(n):
   # power = random.random()
   # t[i] = a ** power

#print(t)
#fast_sort(t,a)
#print(t)


""""
log_a(z liczby) to wykladnik
tupla z oryginalem i wykladnikiem
i potem bucket sorcik

"""

#k chaotyczna lista odsylaczowa

def left(i):
    return i*2+1

def right(i):
    return i*2+2

def parent(i):
    return (i-1)//2

def heapify(T, i, n):
    l=left(i)
    r=right(i)
    max_index=i

    if(l<n and T[l].val<T[max_index].val):
        max_index=l

    if(r<n and T[r].val<T[max_index].val):
        max_index=r

    if(max_index!=i):
        T[i], T[max_index] = T[max_index], T[i]
        heapify(T, max_index, n)    

def buildHeap(T):
    n=len(T)
    for i in range(parent(n-1),-1,-1):
        heapify(T, i, n)

def heapSort(T):
    n=len(T)
    buildHeap(T)
    for i in range(n-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T, 0, i)

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None


def sortH(p:Node,k):
    k+=1
    tree=[0 for _ in range(k)]
    srt=Node(None)
    res=srt
    for i in range(k):
        tree[i]=p
        p=p.next
    
    buildHeap(tree)    

    while(p!=None):
        srt.next=tree[0]
        
        srt=srt.next
        tree[0]=p
        p=p.next

        heapify(tree, 0, k)

    while(tree[0].val!=float('inf')):    
        srt.next=tree[0]
        srt=srt.next

        tree[0]=Node(float('inf'))
        heapify(tree, 0, k)

    return res.next    


a = Node(3)
b = Node(2)
c = Node(5)
d = Node(7)
e = Node(6)

a.next = b
b.next = c
c.next = d
d.next = e
w = a
for i in range(5):
    print(w.val)
    w = w.next

print("-----")

w = sortH(a, 1)
for i in range(5):
    print(w.val)
    w = w.next



"""
budujemy kopiec wrzucamy pierwsze k elementow
wyciagamy minimum, on tworzy juz posortowana liste
dopisujemy kolejna(znowu mamy k elementow) heapify zeby naprawic, itd
gdy juz koniec listy to wkladamy infinity"""


#sortTab 
def SortTab(T, P):
    T.sort()
