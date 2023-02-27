from random import randint

def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(1,n):
            if array[j-1] > array[j]: array[j-1], array[j] = array[j], array[j-1]
    return array

def bucket_sort(A, min, maks, n_buckets):
    buckets = [[] for _ in range(n_buckets)]
    jump = (maks - min) / n_buckets
    for a in A:
        m = 0
        while (min + jump*m) < a: m += 1
        if m == 0: m += 1
        buckets[m-1].append(a)

    k = 0
    for bucket in buckets:
        bubble_sort(bucket)
        for el in bucket:
            A[k] = el
            k += 1

B = [randint(10,100)/10 for _ in range(20)]
print(B)
bucket_sort(B, 1, 10, 20)
print(B)