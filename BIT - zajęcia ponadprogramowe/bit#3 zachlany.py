from queue import PriorityQueue
from math import inf

def peronczici(T, m):
    PQ=PriorityQueue()
    n=len(T)
    for i in range(n):
        PQ.put((T[i][0], 1))
        PQ.put((T[i][1], -1))

    cntr=0
    while not PQ.empty():
        priority, arrival = PQ.get()
        cntr+=arrival
        if cntr>m:
            return False

    return True



"""
T = [[0,1],[1,3],[2,3],[2,4],[3,4],[4,5],[4,5]]
m=3

print(peronczici(T,m))
"""

def ochronaKoronawirusa(T, k):
    n=len(T)
    
    res=0
    lastCity=-1

    for i in range(k-1,-1,-1):
        if T[i]:
            lastCity=i
            res+=1
            break
    
    if lastCity == -1:
        return False
       

    cityToProtect = i+k 
    cityToPlace = lastCity  

    for i in range(lastCity+1, n):
        if cityToProtect+k-1 < i:
            if lastCity == cityToPlace:
                return False
            
            res+=1
            cityToProtect = cityToPlace+k
            lastCity = cityToPlace

        elif T[i]:
            cityToPlace = i    

    
    if cityToProtect < n:
        if cityToPlace != lastCity:
            return res+1
        else: return False
    
    return res        

"""
T=[0,1,1,0,1,0,0,0,1,1,0,0,1,1,0,0,0,1,1,0,0,0,1]
k=3
print(ochronaKoronawirusa(T,k))
"""


def przedzialyOtwarte(T, k):
    T.sort(key=lambda x:x[1])

    RES=[]
    lastDl=inf

    for j in range(0, len(T)):
        curr=T[j]
        cntr=1
        res=[T[j]]

        for i in range(j+1,len(T)):
            if T[i][0]>=curr[1]:
                cntr+=1
                res.append(T[i])
                curr=T[i]
                
                if cntr==k and res[len(res)-1][1] - res[0][0]< lastDl:
                    RES=res.copy()
                    lastDl = res[len(res)-1][1] - res[0][0]
                    break

    if RES==None:
        return False
    return RES    


"""
T = [[6,10],[1,2],[2,4],[3,4],[4,5],[4,5],[3,6],[6,7],[7,8]]
k = 4

print(przedzialyOtwarte(T,k))
"""

def smallest_word(s):
    n = len(s)
    cnt = [0] * 26
    v = [False] * 26
    q = deque()

    for c in s:
        cnt[ord(c) - 97] += 1

    q.append(s[0])
    cnt[ord(s[0]) - 97] -= 1
    v[ord(s[0]) - 97] = True

    for i in range(1, n):
        c = s[i]
        
        if v[ord(c) - 97]:
            cnt[ord(c) - 97] -= 1
            continue

        while q:
            stack_c = q.pop()
            if c < stack_c and cnt[ord(stack_c) - 97] > 0:
                v[ord(stack_c) - 97] = False
                q.append(c)
                v[ord(c) - 97] = True
                cnt[ord(c) - 97] -= 1
                break

            else:
                q.append(stack_c)
                q.append(c)
                v[ord(c) - 97] = True
                cnt[ord(c) - 97] -= 1
                break

    res = ""

    while q:
        c = q.popleft()
        res += c

    return res

"""
s = "cbdaccbc"

print(smallest_word(s))
"""