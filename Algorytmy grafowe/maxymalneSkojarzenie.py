def skojarzenie(T):
    n=len(T)
    preferences=[-1]*n    
    vertex=[False]*n
    resCntr=0

    for s in range(n): #poczatkowe rozdysponowanie preferencji
        for w in T[s]:
            if preferences[w] == -1:
                preferences[w]=s
                vertex[s]=True
                resCntr+=1
                break
    
    def dfs(s):
        for v in T[s]:
            if not visited[v]:
                visited[v]=1

                if preferences[v] == -1 or dfs(preferences[v]):
                    preferences[v]=s
                    return 1

        return 0        

    for w in range(n):
        if not vertex[w]:
            visited=[False]*n
            resCntr+=dfs(w)        

    return resCntr    