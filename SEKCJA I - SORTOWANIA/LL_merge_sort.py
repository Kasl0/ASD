from random import randint

class Node:
    def __init__(self, v=-1):
        self.val = v
        self.next = None

def merge(L1,L2):
    head = Node()
    tail = head

    while (L1.next is not None) and (L2.next is not None):

        if L1.next.val < L2.next.val:
            tail.next = L1.next
            L1.next = L1.next.next
        else:
            tail.next = L2.next
            L2.next = L2.next.next

        tail = tail.next

    if L1.next is not None:
        tail.next = L1.next
    else:
        tail.next = L2.next

    while tail.next is not None:
        tail = tail.next
    return head, tail

def n_series(lst):
    head = Node()
    head.next = lst.next
    tail = head.next
    lst.next = lst.next.next
    while (lst.next != None) and (lst.next.val >= tail.val):
        tail.next = lst.next
        lst.next = lst.next.next
        tail = tail.next
    tail.next = None
    return head

def merge_sort(lst):
    while True:
        n = 0
        head = Node()
        tail = head
        while lst.next is not None:
            s1 = n_series(lst)
            n += 1
            if lst.next is None:
                tail.next = s1.next
            else:
                s2 = n_series(lst)
                n += 1
                m_head, m_tail = merge(s1,s2)
                tail.next = m_head.next
                tail = m_tail
        lst.next = head.next
        if (n <= 2): break

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
merge_sort(l1)
wypisz(l1)