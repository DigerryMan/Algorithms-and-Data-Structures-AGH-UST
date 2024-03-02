#1 - graf, Dag  | Nalezy stwierdzic czy G ma sciezke hamiltona
# posortowac topologicznie potem sprawdzac czy miedzy kazda dwojka jest krawedz

graph=[[1,2,3],
       [2,3],
       [],
       [4],
       [2]]

def hamilltonPathDAG(G):
    n=len(G)
    parent=[None]*n
    visited=[False]*n
    topologicList=[]

    def DFS_visit(G, s):
        visited[s]=True

        for v in G[s]:
            if not visited[v]:
                parent[v]=s
                DFS_visit(G, v)

        topologicList.append(s)        

    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)    

    topologicList.reverse()

    def binSearch(G, s, vWeLookFor, start, end):
        while(start<end):
            mid=(start+end)//2
            if G[s][mid]>vWeLookFor:
                end=mid-1

            elif G[s][mid]<vWeLookFor:
                start=mid+1

            return True

        return G[s][start]==vWeLookFor

    for i in range(n-1):
        if not binSearch(G,topologicList[i], topologicList[i+1], 0, len(G[topologicList[i]])-1):            
            return False

    return True    

print(hamilltonPathDAG(graph))


#2 - wierzcholek v w grafie skierowanym jest dolnym poczatkiem jesli z v mozna osiagnac kazdy inny wierzcholek 
# dwa wywolania dfs, od dwolnego wierzcholka, a potem jak nie byl tym to puszczamy od tego ktory mial najwiekszy czas przetworzenia po pierwszym dfs
# 2 opcja ( policzyc ile ich jest) jak juz znajdziemy to szukamy silnych skladowych, ta ktora nie bedzie miec wchodzacych to tam beda dobre poczatki
# 3 wywolania dfs zweryfikowanie 

def dobryPoczatek(G):

    n=len(G)
    visited=[False]*n
    lastV=0

    def DFS_visit(G, s):
        nonlocal lastV
        visited[s]=True

        for v in G[s]:
            if not visited[v]:
                DFS_visit(G, v)

        lastV=s       

    for i in range(n):
        if not visited[i]:
            DFS_visit(G, i)    

    visited=[False]*n
    DFS_visit(G, lastV)

    for i in range(n):
        if not visited[i]:
            return False

    return lastV    


#3 - przejsc z s do t tak by bylo najwieksze waskie gardlo ( krawdzie maja ceny )
# usuwamy sciezki ktora maja najmniejsze koszty i usuwamy je w kolejnosci wyszukiwania binarnego

#4 - implementacja algorytmu dla reprezentacji macierzowej odtwarzania cyklu eulera 
def eulerCycle(G): #macierzowo
    n=len(G)
    #sprawdzanie czy moze byc cykl:
    for w in range(n):
        wCntr=0
        for k in range(n):
            wCntr+=G[w][k]

        if wCntr%2==1 or wCntr==0:
            return False

    cycle=[]
    def DFS_visit(G, s):
        for v in range(len(G[s])):
            if G[s][v]==1:
                G[s][v]=0
                G[v][s]=0
                DFS_visit(G, v)

        cycle.append(s)

    cycle.reverse()
    return cycle            




#5 - "szachuje" - mape gdzie sa miasta i oazy, kazde miasto ma tylko dwie wychodzace drogi, do oaz mozna wjezdzac ile razy sie chce
# trzeba sprawdzic czy istnieje przejazd po wszytskich miastach tak ze przejezdza sie przez kazde miasto tylko raz 
#  traktowac miasta jako krawedzie i wyszukac cykl eulera

#6 - bezpieczny przelot - mamy graf z lotniskiem startowym s i lotniskiem koncowym t, miedzy lotniskami sie lata i sa tam takie punkty gdzi
# sa korytarze powietrzne na danych wysokosciach, wybieram sobie jaka wysokoscia chce leciec i mam zadany blad(roznice miedzy koryatrzem)
# a obrana przez mnie i musze stwierdzic czy da sie przeleciec od s do t dla tego bledu
# rozwazamy okna, od najmijeszej wartosci korytazra i takich w przedzizale od 2t wiekszym, i potem w gore az znajdziemy 
