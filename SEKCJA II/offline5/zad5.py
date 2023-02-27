#Kacper Słoniec

#Opis algorytmu:
#W rozwiązaniu używamy kolejki priorytetowej.
#Za każdym razem wybieramy przystanek z największą ilością paliwa.
#Przystanek może być za nami, lub przed nami w zasięgu naszegego paliwa w baku.
#Przystanek dodajemy do listy z przystankami, którą na końcu sortujemy.

#Złożoność obliczeniowa: O(nlogn)

from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    Stops = [0]
    fuel = T[0]
    index = 0

    q = PriorityQueue()
    for i in range(1, fuel + 1):
        q.put((-T[i], i))

    while index + fuel < len(T)-1:

        val, i = q.get()
        val *= -1
        Stops.append(i)

        if index + fuel + val >= len(T)-1:
            break

        for j in range(index + fuel + 1, index + fuel + val + 1):
            q.put((-T[j], j))

        if i > index:
            fuel -= (i - index)
            index = i
        fuel += val
    
    return sorted(Stops)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )