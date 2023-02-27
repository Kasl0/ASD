# 1) Czy w danym DAG jest ścieżką Hamiltona?

def hamilton(G):
    n = len(G)
    T = [False for _ in range(n)]
    L = []
    def dfs_visit(G, T, L, n):
        T[n] = True
        for i in range(len(G[n])):
            if not T[G[n][i]]:
                dfs_visit(G, T, L, G[n][i])
        L.append(n)
    for i in range(n):
        if not T[i]:
            dfs_visit(G, T, L, i)
    L.reverse()
    for i in range(1,n):
        if[i-1] not in G[L[i]]:
            return False
    return True

# 2) Czy w grafie skierowanym istnieje dobry początek?

def dp(G):
    n = len(G)
    visited = [False for _ in range(n)]
    time = 0
    v = 0
    for i in range(n):
        if not visited[n]:
            DFS_visit(G, visited, i)
    G2 = reverse_graph(G)

def DFS_visit(G, visited, u):
    nonlocal time
    time += 1
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            DFS_visit(G, visited, v)
    v.time = time

# 3) MST i najkrótsze ścieżki:
# Dijkstra - R^+, zachłanny
# Bellman-Fod - dynamiczny
# Floyd - Warshall - każdy z każdym, dynamiczny

# 4) Ścieżka o najmniejszym iloczynie wag: