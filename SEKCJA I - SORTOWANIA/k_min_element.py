from random import randint

#Chcemy obliczyć element, który po posortowaniu byłby pod indeksem k
#Złożoność: O(n)

def select(A, p, k, r):
    if p == r: return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k: return A[q]
        elif q < k: return select(A, q+1, k, r)
        else: return select(A, p, k, q-1)

def quick_sort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quick_sort(A, p, q-1)
        quick_sort(A, q+1, r)

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

k = randint(0, len(B)-1)
print(k)
k_value = select(B, 0, k, len(B)-1)
print(k_value)