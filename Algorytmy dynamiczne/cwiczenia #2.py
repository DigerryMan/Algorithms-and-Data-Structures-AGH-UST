#zad. 1

def wycinka(T, cache, i):
    if i==0:
        return T[0]
    
    if i==1:
        return max(T[0], T[1])
    
    if cache[i] != -1:
        return cache[i]
    
    cache[i] = max(wycinka(T, cache, -1), wycinka(T, cache, i-2) + T[i])


def wycinka2(T):
    n=len(T)
    F=[-1 for _ in range(n)]
    
    F[0]=0
    F[1]=max(T[0], T[1])

    for i in range(2, n):
        F = max(F[i-1], F[i-2] + T[i])

    return F[n-1]    



#zad.2 - spadajace klocki

def klocki(T, cache, top, i):
    if i==0:
        top[0] = T[0]
        return 0
    
    if cache[i] != -1:
        return cache[i]

    cache[i] = min(klocki(T, cache, top, i-1) + 1,
               min([klocki(T, cache, top, j) + (i-j+1) for j in range(i) if upper(T[i], top[j])]),
               i)    
    
    if cache[i] == (klocki(T, cache, top, i-1)+1):
        top[i] = top[i-1]
    
    else:
        top[i] = T[i]

    return cache[i]

def upper(a,b):
    if a[0]<b[0] or a[1]> b[1]:
        return False
    return True

def klocki(T,n):
    cache=[-1]*n
    top=[None]*n
    cache[0]=0
    top[0]=T[0]
    return klocki(T, cache, top, n)