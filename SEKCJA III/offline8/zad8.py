#Kacper Słoniec

#Opis algorytmu:
#Obliczamy czas budowy wszystkich możliwych autostrad. Czasy te sortujemy. A następnie szukamy grafu spójnego z minimalną różnicą czasów (metodą brute force).

from collections import deque
from zad8testy import runtests

def time(A, B):
    length = ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5
    if int(length) == length: return length
    else: return int(length) + 1

def spojne(n, Tab, start, stop):
    G = [[] for _ in range(n)]
    for i in range(start, stop+1):
        G[Tab[i][1]].append(Tab[i][2])
        G[Tab[i][2]].append(Tab[i][1])
    
    Q = deque()
    visited = 0
    V = [False for _ in range(len(G))]

    V[0] = True
    visited += 1
    Q.append(0)

    while Q:
        u = Q.popleft()
        for v in G[u]:
            if V[v] == False:
                V[v] = True
                visited += 1
                Q.append(v)
    
    if visited == n:
        return True
    else:
        return False

def highway(A):
    n = len(A)

    Times = []
    for i in range(n-1):
        for j in range(i+1, n):
            Times.append((time(A[i], A[j]), i, j))

    Times.sort(key = lambda tup: tup[0])
    r = len(Times)

    minimum = float('inf')
    for start in range(r):
        for end in range(start+n-2, r):
            if spojne(n, Times, start, end):
                minimum = min(minimum, Times[end][0] - Times[start][0])
    
    return minimum

#A =[(10,10),(15,25),(20,20),(30,40)]
#print(highway(A))
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )