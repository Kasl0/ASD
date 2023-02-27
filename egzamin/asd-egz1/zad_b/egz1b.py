# Kacper Słoniec

# Złożoność obliczeniowa: O(n)

# Opis algorytmu:

# Pole x klasy Node to 3-elementowa tablica, zawierająca po koleji:
# poziom na którym znajduje się wierzchołek, wskaźnik na rodzica (parent), informację czy wierzchołek jest potrzebny czy nie (czy możemy go usunąć)

# Kroki:
# 1) Zaczynamy od wyliczenia wysokości całego drzewa przechodząc po każdym wierzchołku,
# przy okazji aktualizujemy zawartość pola x każdego Node'a. -> O(n)
# 2) Tworzymy tablicę Levels i uzupełniamy ją o informację o szerokości drzewa dla każdego z poziomów -> O(n)
# 3) Obliczamy maksymalną szerokość drzewa, szukając max'a w tablicy Levels -> O(n)
# 4) Obliczamy najwyższy poziom drzewa, na którym szerokość jest równa maksymalnej szerokości drzewa -> O(n)
# 5) Usuwamy krawędzie do dzieci wierzchołków o wysokości height, a liście drzewa o wysokości mniejszej niż height
# dodajemy do kolejki To_remove. Dodatkowo oznaczamy wierzchołki, których nie możemy usunąć, idąc od wierzchołka
# nieusuwalnego w stronę korzenia, przez parent'y. Przez dany wierzchołek możemy przejść tylko raz, bo zostanie on oznaczony
# i następnym razem drogę zablokuje stosowny if, dlatego złożoność O(n) -> O(n)
# 6) Usuwamy odnogi wierzchołków zapisanych w kolejce, wykorzystując informację, który może być usunięty, a który nie.
# Złożoność O(n) z tego samego powodu co wyżej - nie przejdziemy 2 razy przez ten sam wierzchołek -> O(n)


from egz1btesty import runtests
from collections import deque

class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def wideentall( T ):
  #1) Liczymy wysokość całego drzewa i aktualizujemy zawartość pola x - O(n)
  max_height = 0
  T.x = [0, None, True]
  Q = deque()
  Q.append(T)

  while Q:
    A = Q.popleft()
    max_height = max(max_height, A.x[0])

    if A.left != None:
      A.left.x = [A.x[0] + 1, A, False]
      Q.append(A.left)

    if A.right != None:
      A.right.x = [A.x[0] + 1, A, False]
      Q.append(A.right)
  
  max_height += 1

  #2) Uzupełniamy tablicę Levels - O(n)

  Levels = [0 for _ in range(max_height)]

  Q.append(T)

  while Q:
    A = Q.popleft()
    Levels[A.x[0]] += 1

    if A.left != None:
      Q.append(A.left)

    if A.right != None:
      Q.append(A.right)
  
  #3) Obliczamy max_width - O(n)
  
  max_width = max(Levels)

  #4) Obliczamy height - O(n)

  for i in range(max_height-1,-1,-1):
    if Levels[i] == max_width:
      height = i
      break

  #5) Usuwamy część I - O(n)
  removed = 0

  Q.append(T)
  To_remove = deque()

  while Q:
    A = Q.popleft()

    if A.x[0] == height: #nie dodajemy dzieci

      if A.left != None:
        A.left = None
        removed += 1

      if A.right != None:
        A.right = None
        removed += 1

      A.x[2] = True
      while A.x[1] != None:
        A = A.x[1]
        if A.x[2] == True:
          break
        A.x[2] = True
      
    else: #dodajemy dzieci

      if A.left != None:
        Q.append(A.left)

      if A.right != None:
        Q.append(A.right)

      if A.left == None and A.right == None: #Dodajemy wierzchołek do kolejki, żeby usunąć odnogę
        To_remove.append(A)
        
  #6) Usuwamy odnogi wierzchołków zapisanych w kolejce - O(n)
  while To_remove:
    A = To_remove.popleft()
    if A.x[2] == None:
      continue

    while A.x[1] != None:
      A.x[2] = None
      A = A.x[1]

      if A.x[2] == True:
        removed += 1
        break

      if A.x[2] == None:
        break

  return(removed)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = True )