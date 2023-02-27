def left(i): return 2*i + 1
def right(i): return 2*i + 2
def parent(i): return (i-1)//2

def heapify(A, n, i):
    l = left(i)
    r = right(i)
    min_ind = i
    if l < n and A[l] < A[min_ind]:
        min_ind = l
    if r < n and A[r] < A[min_ind]:
        min_ind = r
    if min_ind != i:
        A[i], A[min_ind] = A[min_ind], A[i]
        heapify(A, n, min_ind)

def build_heap(A):
    n = len(A)
    for i in range(parent(n-1), -1, -1):
        heapify(A, n, i)

def heap_sort(A):
    n = len(A)
    build_heap(A)
    for i in range(n-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapify(A, i, 0)

A = [43, 4, 32, 1, 23]
heap_sort(A)
print(A)