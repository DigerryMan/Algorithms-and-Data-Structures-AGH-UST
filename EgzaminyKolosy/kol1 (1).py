from kol1testy import runtests
#mateusz bobula
#opis: robie pomocnicza tablcie p posortowanych juz elementow, nastepnie wyciagam najstarszy dodanny do niej element,
#a nowy wkladam w odpowiednie miejsce, na k-tym elemencie tej tablicy jest zi wartosc ktora dodaje do sumy


"""
def ksum(T, k, p):
    #k - ktora najwieksza
    #p - przedzial
    n=len(T)
    suma=0

    tabPom=[[i, T[i]] for i in range(p)]

    tabPom.sort(key=lambda x:x[1], reverse=True)
    suma+=tabPom[k-1][1]

    najstarszy=0
    for i in range(p,n):
        
        #szukanie najstarszego dodanego elementu:
        for el in range(p):
            if tabPom[el][0]==najstarszy:
                tabPom[el]=[i, T[i]]
                break

        tabPom.sort(key=lambda x:x[1], reverse=True)    
        suma+=tabPom[k-1][1]
        najstarszy+=1

    return suma   
"""


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
    suma=0

    tabPom=[[i, T[i]] for i in range(p)] #tablica malejca


    tabPom.sort(key=lambda x:x[1], reverse=True)
    suma+=tabPom[k-1][1]

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

        suma+=tabPom[k-1][1]
        najstarszy+=1

    return suma   






T = [7,9,1,5,8,6,2,12]
k = 4
p = 5


print(ksum(T,k,p))


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )


