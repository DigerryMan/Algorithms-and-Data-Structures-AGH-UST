from egzP4atesty import runtests 

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


def LIN_nlogn_wiekszeRowne(tab): 
    tab2=[tab[i][1] for i in range(len(tab))]
    res=[tab2[0]]
    n=len(tab2)
    for i in range(1,n):
        l=len(res)
        if res[l-1]<=tab2[i]:
            res.append(tab2[i])

        else:
            s=binSearch(res,0,l-1,tab2[i])
            res[s]=tab[i][1]

    return len(res)            
        


def mosty ( T ):
    T.sort(key=lambda x:(x[0], x[1]))


    return LIN_nlogn_wiekszeRowne(T)

runtests ( mosty, all_tests=True )
