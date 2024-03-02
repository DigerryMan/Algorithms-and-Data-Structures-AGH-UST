#Mateusz Bobula

'''Algorytm polega na wybieraniu maximum z mozliwych kupek sniegu, dopóki mozliwa ilosc sniegu nie bedzie mniejsza
od efektu topnienia w kolejnych dniach, oraz sumowaniu sniegu uwzględniając topnienie. Gdy owy snieg nie jest 
oplacalny, to zebranie go spowoduje zmniejszenie  maxymalnej mozliwej ilosci sniegu do zebrania. Dzieki dostepowi 
do sniegu z obydwu stron, nie dojdzie do sytuacji, ze zostanie rozjechany oplacalny snieg. '''

from zad2testy import runtests

def left(i):
    return (2*i)+1

def rigth(i):
    return (2*i)+2

def parent(i):
    return (i-1)//2

def heapify(A, i, n):
    l=left(i)
    r=rigth(i)
    maxIndx=i
    
    if l<n and A[maxIndx]<A[l]: maxIndx=l
    if r<n and A[maxIndx]<A[r]: maxIndx=r

    if maxIndx != i:
        A[maxIndx], A[i] = A[i], A[maxIndx]
        heapify(A, maxIndx, n)

def buildHeap(A):
    n=len(A)

    for i in range(parent(n-1), -1, -1):
        heapify(A, i ,n)

def heapSortAndDaysCounter(A):
    n=len(A)
    buildHeap(A)
    dayCntr=0 #ilosc dni w ktorej bierzemy snieg

    for i in range(n-1, 0, -1):
        if(A[0]<=dayCntr): #nieoplaca sie brac sniegu
            break          # wiec nie ma po co dalej sortowac
        
        A[i], A[0] =  A[0], A[i]
        heapify(A, 0, i) 
        dayCntr+=1

    return dayCntr  #zwraca ilosc dni zbierania sniegu, zapisana w ostanich dayCntr indexach tablicy A



def snow( S ):
    n=len(S)
    days=heapSortAndDaysCounter(S)
    # days==0 -> nic sie nie oplaca brac

    res=0
    for i in range(n-days,n):
        res+=(S[i]-days+1)  #days==1 bierzemy 1 snieg (bez utraty od stopnienia)
        days-=1
    
    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )


