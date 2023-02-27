from time import time


def DFS(G):
    #G = (V,E)
    for v in V:
        v.visited = False
        v.parent = None
    time = 0
    for u in V:
        if not u.visited:
            DFSVisit(G, u)

def DFSVisit(G, u):
    nonlocal time
    time += 1
    u.visited = True
    for v: #v - sąsiad u
        if not v.visited:
            v.parent = u
            DFSVisit(G, v)
    time += 1