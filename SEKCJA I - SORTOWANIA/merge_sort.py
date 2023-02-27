from random import randint

def merge_sort(A, p, r):
    if p == r:
        return
    
    q = (p+r)//2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)

    B = [None for _ in range(r-p+1)]
    i = p
    j = q+1
    k = 0
    while i <= q and j <= r:
        if A[i] < A[j]:
            B[k] = A[i]
            i += 1
        else:
            B[k] = A[j]
            j += 1
        k += 1

    while i <= q:
        B[k] = A[i]
        i += 1
        k += 1

    while j <= r:
        B[k] = A[j]
        j += 1
        k += 1
    
    for l in range(r-p+1):
        A[p+l] = B[l]

B = [randint(1,100) for _ in range(10)]
print(B)
merge_sort(B, 0, len(B)-1)
print(B)