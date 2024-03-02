from kol1testy import runtests
#mateusz bobula
#opis: robie pomocnicza tablcie p posortowanych juz elementow, nastepnie wyciagam najstarszy dodanny do niej element,
#a nowy wkladam w odpowiednie miejsce, na k-tym elemencie tej tablicy jest zi wartosc ktora dodaje do sumy



def przesunWDobreMiejsce(tab, index, n):
    if index==0:
        if index+1<n and tab[index][1]<tab[index+1][1]:
            tab[index], tab[index+1] = tab[index+1], tab[index]
            przesunWDobreMiejsce(tab, index+1, n)

    elif index==n-1:
        if index-1>=0 and tab[index][1]>tab[index-1][1]:
            tab[index], tab[index-1] = tab[index-1], tab[index]
            przesunWDobreMiejsce(tab, index-1, n)      
    
    else:
        if tab[index][1]<tab[index+1][1]:
            tab[index], tab[index+1] = tab[index+1], tab[index]
            przesunWDobreMiejsce(tab, index+1, n)     
        
        elif tab[index][1]>tab[index-1][1]:
            tab[index], tab[index-1] = tab[index-1], tab[index]
            przesunWDobreMiejsce(tab, index-1, n)                

            
def ksum(T, k, p):
    #k - ktora najwieksza
    #p - przedzial
    n=len(T)
    tabPom=[[i, T[i]] for i in range(p)] #tablica malejca

    tabPom.sort(key=lambda x:x[1], reverse=True)
    suma=tabPom[k-1][1]

    najstarszy=0
    for i in range(p,n):
        
        #szukanie najstarszego dodanego elementu:
        indexDoSort=0

        for el in range(p):
            if tabPom[el][0]==najstarszy:
                indexDoSort=el
                tabPom[el]=[i, T[i]]
                break

        przesunWDobreMiejsce(tabPom, indexDoSort, p)
        #ewentualnie zamiast przesunWDobreMiejsce - po prostu tabPom.sort(key=lambda x:x[1], reverse=True)
        
        suma+=tabPom[k-1][1]
        najstarszy+=1

    return suma   
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )





####STARY KOD

def countingSort(A, maxi):
    n=len(A)
    B=[0]*(maxi+1)
    C=[0]*n

    for i in range(n):
        B[A[i][0]] +=1

    for i in range(1,maxi+1):
        B[i] += B[i-1] 

    for i in range(n-1,-1,-1):   
        C[B[A[i][0]] - 1]   = A[i]
        B[A[i][0]] -= 1

    for i in range(n):
        A[i]=C[i]

def ksum(T, k, p):
    n=len(T)
    suma=0
    tab2=[[T[i], i] for i in range(n)]
    tabPom=[tab2[i] for i in range(p)]
    maxi=0
    for i in range(p):
        if tabPom[i][0]>maxi:
            maxi=tabPom[i][0]

    countingSort(tabPom, maxi)

    suma+=T[p-k]
    for i in range(1,n-p):  
        
        new_el=T[p+1-i]
        wstawiony=False
        for j in range(p):
            if tabPom[j][1]<1: #ten napewno wywalamy, nowy wstawauny
                wstawiony=True
                tabPom[j]=new_el
                for k in range(j+1,p): #reszte zaimeniamy jak  wieksze
                    if tabPom[k-1]>tabPom[k]:
                        tabPom[k-1], tabPom[k] = tabPom[k], tabPom[k-1]
            
            if new_el[0]<tabPom[j][0]: #TO WSTAWIAMY
                tabPom[j], new_el = new_el, tabPom[j]

        sum+=T[p-k]        


    return sum



"""