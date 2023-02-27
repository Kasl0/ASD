from random import randint

class Heap:
    def __init__(self, n):
        self.T = [0 for _ in range(n)]
        self.size = 0

def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

"""def heapify(H, n, i):
    l = left(i)
    r = right(i)
    max_ind = i
    if l < n and H.T[l] > H.TA[max_ind]:
        max_ind = l
    if r < n and H.T[r] > H.T[max_ind]:
        max_ind = r
    if max_ind != i:
        H.T[i], H.T[max_ind] = H.T[max_ind], H.T[i]
        heapify(H.T, n, max_ind)"""

"""def build_heap(H):
    n = len(H.T)
    for i in range(parent(n-1), -1, -1):
        heapify(H, n, i)"""

"""def heap_sort(H):
    n = len(H.T)
    build_heap(H)
    for i in range(n-1, 0, -1):
        H.T[0], H.T[i] = H.T[i], H.T[0]
        heapify(H, i, 0)"""

def heapify_from_down(H, i):
    if i == 0:
        return
    p = parent(i)
    if H.T[p] < H.T[i]:
        H.T[p], H.T[i] = H.T[i], H.T[p]
        heapify_from_down(H, p)

def insert(H, e):
    if len(H.T) == H.size:
        return

    H.T[H.size] = e
    H.size += 1

    i = H.size - 1
    heapify_from_down(H, i)

A = Heap(10)
for _ in range(10):
    insert(A, randint(1,100))
print(A.T, A.size)