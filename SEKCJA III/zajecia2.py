from queue import PriorityQueue

# 1) Najkrótsze ścieżki po krawędziach o malejących wagach e{1,...,|E|}

def dijkstra(G, s, t):
    n = len(G)
    T = [False for _ in range(n)]
    D = [float('inf') for _ in range(n)]
    P = [float('inf') for _ in range(n)]
    D[s] = 0
    q = PriorityQueue()
    for i in range(n):
        q.put((D[i], i))
    while not q.empty():
        h, u = q.get()
        T[u] = True
    for i in range(len(G[u])):
        if D[G[u][i]] > D[u] + G[u][i] and G[u][i] < P[u]:
            D[G[u][i]] = D[u] + G[u][i]
            P[G[u][i]] = G[u][i]

# 2) Domknięcie przechodnie (reprezentacja macierzowa) - ang. transitive closure

def flag_warshall(graph):
    n = len(graph)
    for _ in range(n):
        for k in range(n):
            for x in range(n):
                for y in range(n):
                    if x != y: graph[x][y] = graph[x][y] or (graph[x][k] or graph[k][y])
    return graph

# 3) Wymiana walut

# 4) Optymalny korzeń drzewa.

# 5) Stacja benzynowa.