#Kacper Słoniec

#Opis algorytmu:
#Wykonujemy podwójnie algorytm Dijkstry. Po raz pierwszy dla lotniska s, obliczając drogi do każdego innego lotniska.
#Drugi raz dla wierzchołka t. Algorytm Dijkstry ma złożoność O(m*log n).
#Gdy mamy już "obliczone" tablice ze wszystkimi odległościami, sprawdzamy każdy z każdym - złożoność O(n^2)
#i szukamy najmniejszej sumy kosztu: dotarcia z s do i, przelotu z i do j, dotarcia z j do t.

#Złożoność: O(n^2)

from kol3btesty import runtests
from queue import PriorityQueue

def airports( G, A, s, t ):
    n = len(G)
    Q = PriorityQueue()

    #Dijkstra dla s:

    DistanceFromS = [float('inf') for _ in range(n)]
    DistanceFromS[s] = 0
    Q.put((0, s))

    while not Q.empty():
        distance, airport = Q.get()
        if DistanceFromS[airport] != distance:
            continue
        for connection in G[airport]:
            next_airport, next_distance = connection
            if DistanceFromS[next_airport] > DistanceFromS[airport] + next_distance:
                DistanceFromS[next_airport] = DistanceFromS[airport] + next_distance
                Q.put((DistanceFromS[next_airport], next_airport))

    #Dijkstra dla t:

    DistanceFromT = [float('inf') for _ in range(n)]
    DistanceFromT[t] = 0
    Q.put((0, t))

    while not Q.empty():
        distance, airport = Q.get()
        if DistanceFromT[airport] != distance:
            continue
        for connection in G[airport]:
            next_airport, next_distance = connection
            if DistanceFromT[next_airport] > DistanceFromT[airport] + next_distance:
                DistanceFromT[next_airport] = DistanceFromT[airport] + next_distance
                Q.put((DistanceFromT[next_airport], next_airport))
    
    #Sprawdzamy każdy z każdym:
    minDistance = DistanceFromS[t]
    
    for i in range(n):
        DistanceFromS[i] += A[i]
    for i in range(n):
        DistanceFromT[i] += A[i]
        
    return min(DistanceFromS[t] - A[t], min(DistanceFromS) + min(DistanceFromT))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )