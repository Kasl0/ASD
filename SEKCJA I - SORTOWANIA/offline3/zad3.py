#Kacper Słoniec
#Tablicę dzielimy na N kubełków. Każdy kubełek sortujemy bucket_sortem. Ostatecznie łączymy wszystkie kubełki w całość.

#Złożoność czasowa: Θ = n
#Złożoność pamięciowa: Θ = n

from zad3testy import runtests

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

def SortTab(T, P):
    n = len(T)
    buckets = [[] for _ in range(n-1)]
    for t in T:
        if t == n: buckets[n-2].append(t)
        else: buckets[int(t)-1].append(t)

    k = 0
    for i in range(n-1):
        if len(buckets[i]) == 0: continue
        bucket_sort(buckets[i], i+1, i+2, len(buckets[i]))
        for el in buckets[i]:
            T[k] = el
            k += 1
    
    return T

runtests( SortTab )