#Kacper Słoniec

#Opis algorytmu:
#Jest to zmodyfikowany algorytm BFS.
#Szukamy najkrótszej ścieżki z 's' do 't', przy okazji zapisując w pamięci "kluczowe krawędzie", których usunięcie powoduje przerwanie ścieżki.
#Gdy nie ma żadnego połączenia z 's' do 't' zwracamy None.
#Gdy istnieją >=2 najkrótsze ścieżki, mające różne "kluczowe krawędzie", zwracamy None.
#Gdy istnieje dowolna ilość najkrótszych ścieżek mających tą samą "kluczową krawędź", zwracamy tą krawędź.

#Złożoność obliczeniowa: Θ(n)

from zad6testy import runtests
from collections import deque

def longer(G, s, t):
    v_count = len(G)
    Distance = [-1 for _ in range(v_count)]
    Edge = [0 for _ in range(v_count)]
    NewEdge = [False for _ in range(v_count)]
    
    Q = deque()
    Distance[s] = 0
    NewEdge[s] = True
    Q.append(s)
    
    while Q:
        u = Q.popleft()

        if u == t:
            return Edge[u]

        for v in G[u]:

            if Distance[v] == -1:
                if NewEdge[u]:
                    Edge[v] = (u, v)
                else:
                    Edge[v] = Edge[u]
                    
                Distance[v] = Distance[u] + 1
                Q.append(v)

            elif Distance[v] == Distance[u] + 1 and Edge[v] != Edge[u]:
                Edge[v] = (u, v)
                NewEdge[v] = True
                if v == t:
                    return None
    
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )