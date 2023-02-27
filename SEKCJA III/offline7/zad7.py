#Kacper Słoniec

#Opis algorytmu:
#Jest to zmodyfikowany algorytm DFS.
#Podróżujemy w głąb odwiedzając rekurencyjnie kolejne miasta, przechodząc przez bramy tak jak możemy (zaczynając od miasta 0, przechodząc przez bramę północną).
#Jeśli dojdziemy do ostatniego miasta, które w dodatku ma możliwość dojścia do miasta 0, to zwracamy listę zawierającą historię naszych wizyt.
#W przeciwnym wypadku zwracamy None. I tak rekurencyjnie szukamy cyklu Hamiltona.

#Złożoność obliczeniowa: wykładnicza

from zad7testy import runtests

def DFStravel(G, Visited, from_city, to_city, History):
    Visited[to_city] = True
    History.append(to_city)

    if from_city in G[to_city][0]: gate = 1
    else: gate = 0

    if 0 in G[to_city][gate] and len(G) == len(History): return(History)

    for city in G[to_city][gate]:
        if not Visited[city]:
            returned = DFStravel(G, Visited.copy(), to_city, city, History.copy())
            if returned != None: return returned
    
    return None

def droga(G):
    Visited = [False for _ in G]
    History = []
    
    Visited[0] = True
    History.append(0)

    for city in G[0][0]:
        returned = DFStravel(G, Visited.copy(), 0, city, History.copy())
        if returned != None: return returned

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )