from random import randint

def radix_sort(A, kol):
    while(kol > 0):
        counting_sort(A, kol-1)
        kol -= 1

def counting_sort(A, kol):
    n = len(A)
    C = [0] * 26
    B = [0] * n
    for x in range(n):
        C[ord(A[x][kol])-97] += 1
    for i in range(1, 26): C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        l = ord(A[i][kol]) - 97
        B[C[l]-1] = A[i]
        C[l] -= 1
    for i in range(n):
        A[i] = B[i]

n = 20
B = [None for _ in range(n)]
for i in range(n):
    slowo = ""
    k = randint(1,9)
    for j in range(k):
        slowo = slowo + chr(randint(97,122))
    B[i] = slowo
print(B)

k = 0
l = 1
while k < n:
    for j in range(k, n):
        if len(B[j]) == l:
            B[j], B[k] = B[k], B[j]
            k += 1
    l += 1
print(B)

#radix_sort(B, k)
#print(B)