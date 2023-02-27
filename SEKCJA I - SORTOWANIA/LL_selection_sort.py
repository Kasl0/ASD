from random import randint

class Node:
    def __init__(self, v=-1):
        self.val = v
        self.next = None

def insert(lista, n):
    while lista.next and lista.next.val < n.val:
        lista = lista.next
    n.next = lista.next
    lista.next = n

def delete_max(lista):
    prev = lista
    maks = lista.next.val
    lista = lista.next
    while lista.next is not None:
        if lista.next.val > maks:
            maks = lista.next.val
            prev = lista
        lista = lista.next
    temp = prev.next
    prev.next = prev.next.next
    temp.next = None
    return temp

def selection_sort_list(lista):
    sorted = Node(-1)
    while lista.next is not None:
        temp = delete_max(lista)
        temp.next = sorted.next
        sorted.next = temp
    lista.next = sorted.next

def stworz(n):
    head = Node()
    f = head
    for _ in range(n):
        f.next = Node(randint(1,100))
        f = f.next
    return head

def wypisz(f):
    while f != None:
        print(f.val, end = ' -> ')
        f = f.next
    print(f)

l1 = stworz(8)
wypisz(l1)
selection_sort_list(l1)
wypisz(l1)