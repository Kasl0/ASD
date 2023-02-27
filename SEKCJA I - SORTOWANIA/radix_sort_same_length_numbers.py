from random import randint

def radix_sort(A, kol):
    while(kol > 0):
        counting_sort(A, kol-1, 10)
        kol -= 1

def counting_sort(A, kol, k):
    n = len(A)
    C = [0] * k
    B = [0] * n
    for x in range(n): C[n_digit(A[x], kol)] += 1
    for i in range(1, k): C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        l = n_digit(A[i], kol)
        B[C[l]-1] = A[i]
        C[l] -= 1
    for i in range(n):
        A[i] = B[i]

def n_digit(number, n):
    return int(str(number)[n])

def length(number):
    return len(str(number))

n = 30
B = [randint(1,999) for _ in range(n)]
print(B)

k = 0
l = 1
while k < n:
    for j in range(k, n):
        if length(B[j]) == l:
            B[j], B[k] = B[k], B[j]
            k += 1
    l += 1
print(B)

#radix_sort(B, 3)
