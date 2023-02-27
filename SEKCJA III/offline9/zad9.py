#Kacper Słoniec

#Opis algorytmu:
#Alogrytm wykorzystuje metodę Forda-Fulkersona.
#Szukamy maksymalnego przepływu dla każdej pary dwóch miast niebędących miastem początkowym.

from zad9testy import runtests
from collections import deque

def maxflow(G, s):
    n = 0
    for tuple in G: n = max(n, tuple[0], tuple[1])
    n += 1

    Graph = [[[], False, None] for _ in range(n)]
    for tuple in G:
        Graph[tuple[0]][0].append([tuple[1], tuple[2], tuple[2], 0])
    Graph.append([[], False, None])

    max_flow = 0

    for first in range(n):
        if first == s: continue
        for second in range(first + 1, n):
            if second == s: continue

            Graph[first][0].append([n, float('inf'), float('inf'), 0])
            Graph[second][0].append([n, float('inf'), float('inf'), 0])
            for i in range(n+1):
                for j in range(len(Graph[i][0])):
                    Graph[i][0][j][2] = Graph[i][0][j][1]
                    Graph[i][0][j][3] = 0

            while True:
                for i in range(n+1):
                    Graph[i][1] = False
                    Graph[i][2] = None
                Q = deque()
                Q.append(s)
                Graph[s][1] = True

                while Q:
                    u = Q.popleft()
                    for tab in Graph[u][0]:
                        v = tab[0]
                        if Graph[v][1] == False and tab[2] > 0:
                            Graph[v][1] = True
                            Graph[v][2] = u
                            Q.append(v)
                
                if Graph[n][2] == None:
                    #nie istnieje scieżka powiększająca
                    break

                local_flow = float('inf')
                k = n
                while Graph[k][2] != None:
                    parent = Graph[k][2]
                    for i in range(len(Graph[parent][0])):
                        if Graph[parent][0][i][0] == k:
                            local_flow = min(local_flow, Graph[parent][0][i][2])
                    k = parent

                k = n
                while Graph[k][2] != None:
                    parent = Graph[k][2]
                    for i in range(len(Graph[parent][0])):
                        if Graph[parent][0][i][0] == k:
                            Graph[parent][0][i][2] -= local_flow
                            Graph[parent][0][i][3] += local_flow
                    k = parent

            sum = 0

            for i in range(len(Graph[first][0])):
                if Graph[first][0][i][0] == n:
                    sum += Graph[first][0][i][3]
                    Graph[first][0].pop(i)
            for i in range(len(Graph[second][0])):
                if Graph[second][0][i][0] == n:
                    sum += Graph[second][0][i][3]
                    Graph[second][0].pop(i)
            
            max_flow = max(max_flow, sum)

    return max_flow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )