#Kacper Słoniec

#Opis algorytmu:
#Na początku sprawdzamy czy lista jest 1-chaotyczna.
#Jeśli tak, to sortujemy listę sortowaniem bąbelkowym w złożoności O(n).
#W innym przypadku stosujemy zmodyfikowany algorytm na heap sort.
#Zaczynamy od stworzenia k+1 elementowej tablicy, na której budujemy kopiec z k+1 pierwszych node'ów z linked listy.
#Kopiec ten jest specjalnym kopcem zawierającym node'y o najmniejszej wartości na szczycie. Każdy węzeł (poza samym szczytem) ma rodzica o niższej wartości.
#Po stworzeniu kopca na szczycie znajduje się najmniejszy element kopca, czyli node listy o najmniejszej wartości. Tworzymy z niego pierwszy node nowej, posortowanej listy.
#Szczyt kopca zamieniamy na kolejny node z orginalnej link listy. Naprawiamy kopiec.
#Na szczycie znajdziemy node o drugiej najmniejszej wartości w liście. Dołączamy go do poprzedniego node'a o mniejszej wartości.
#Powtarzając te kroki w pętli, aż do wyczerpania node'ów z orginalnej listy, tworzymy nową posortowaną listę.
#Ostatnie elementy dołączamy z kopca, a ten się zmniejsza.
#Na koniec zwracamy wskaźnik na pierwszy element nowej, posortowanej listy.

#Złożoność czasowa dla k = Θ(1) -> O(n)
#Złożoność czasowa dla k = Θ(log n) -> O(n*log(log n))
#Złożoność czasowa dla k = Θ(n) -> O(n*log(n))

from zad1testy import Node, runtests

def bubble_sort(head):
    f = head
    prev = None

    while f.next != None:
        if f.next.val < f.val:
            if prev == None:
                head = f.next
                f.next = f.next.next
                head.next = f
            else:
                prev.next = f.next
                f.next = f.next.next
                prev.next.next = f
        prev = f
        f = f.next

    return head

def heapify(A, n, i):
    l = 2*i + 1
    r = 2*i + 2
    min_ind = i
    if l < n and A[l].val < A[min_ind].val:
        min_ind = l
    if r < n and A[r].val < A[min_ind].val:
        min_ind = r
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify(A, n, min_ind)

def SortH(p, k):
    if k == 1:
        return bubble_sort(p)

    A = [None for _ in range(k+1)]
    for i in range(k+1):
        A[i] = p
        p = p.next
        if p == None:
            k = i
            break

    #Build heap:
    for i in range((k-1)//2, -1, -1):
        heapify(A, k+1, i)

    head = A[0]
    tail = head

    while p != None:
        A[0] = p
        heapify(A, k+1, 0)
        p = p.next

        tail.next = A[0]
        tail = tail.next

    for i in range(k, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)
        tail.next = A[0]
        tail = tail.next

    tail.next = None

    return head

runtests( SortH ) 
