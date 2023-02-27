from collections import deque

def BFS(G, s):
    #G = (V,E)
    Q = deque()
    for v in V: v.visted = False

    s.d = 0
    s.visited = False
    s.parent = None
    Q.put(s)

    while Q:
        u = Q.popleft()
        for v: #sąsiedzi u
            if not v.visited:
                v.visited = True
                v.d = u.d + 1
                v.parent = u
                Q.put(v)