#from egzP8atesty import runtests 

def reklamy ( T, S, o ):
    n=len(T)
    tab=[[T[i][0], T[i][1], S[i]] for i in range(n)]
    
    tab.sort(key=lambda x:(x[0], x[2]))
    
    #szukanie o bo debil daje złe na wejsciu
    for i in range(n):
        if T[i][1]>o:
            o=T[i][1]

    o+=1        

    #koniec szukania o bo debil złe dawał

    M=[0]*(o)
    start=tab[n-1][0]
    M[start]=tab[n-1][2]
    index=n-2

    for i in range(start-1, -1, -1):
        M[i]=M[i+1]
        while(index>=0 and tab[index][0]>=i):
            M[i]=max(M[i], tab[index][2])
            index-=1

    maxi=M[0]
    for p,k,siano in tab:
        if k+1<o and M[k+1]+siano>maxi:
            maxi = M[k+1]+siano   

    return maxi            

#runtests ( reklamy, all_tests=True )


T = [ (0, 3), (4, 5), (1, 4), (6,6)]
S = [ 5000, 3000, 15000, 100000 ]

print(reklamy(T,S, 0))

