from random import randint

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

"""def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        p = q + 1"""

"""def quick_sort(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q-p < r-q:
            quick_sort(A, p, q-1)
            p = q + 1
        else:
            quick_sort(A, q+1, r)
            r = q - 1"""

#quick_sort iterative
"""def quick_sort(A):
    n = len(A)
    S = [(-1,-1) for _ in range(n)]
    ptr = 0
    S[0] = (0, n-1)
    while ptr >= 0:
        p, r = S[ptr]
        ptr -= 1
        q = partition(A, p, r)
        if p < q-1:
            ptr += 1
            S[ptr] = (p, q-1)
        if q+1 < r:
            ptr += 1
            S[ptr] = (q+1, r)"""

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

B = [randint(1,100) for _ in range(10)]
print(B)
quick_sort(B, 0, len(B)-1)
print(B)