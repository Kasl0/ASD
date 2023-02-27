#Kacper Słoniec
#Algorytm polega na stworzeniu dwóch list zawierających dane przedziały.
#Pierwszą listę(startsSorted) sortujemy według wartości początków przedziałów, a drugą(endsSorted) według końcówek.
#Następnie "naprawiamy" listy: startsSorted, tak aby dla przedziałów zaczynających się od tej samej wartości, pierwsze występowały największe przedziały z najmniejszym indeksem;
#endsSorted, tak aby dla przedziałów kończących się na tą samą wartość, ostatnie występowały największe przedziały z najmniejszym indeksem.
#Wynikiem jest wartość maksymalna różnicy między indeksami pozycji przedziału o danym indeksie w stworzonych i posortowanych dwóch listach.

from zad2testy import runtests

def quick_sort(A, p, r, col):
    while p < r:
        q = partition(A, p, r, col)
        quick_sort(A, p, q-1, col)
        p = q + 1

def partition(A, p, r, col):
    x = A[r][1][col]
    i = p-1
    for j in range(p, r):
        if A[j][1][col] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

def fix(T, start, end):
    maxValue = T[start][1][1]
    maxValueIndex = start
    maxValueOrginalIndex = T[start][0]
    for i in range(start+1, end+1):
        if T[i][1][1] > maxValue or (T[i][1][1] == maxValue and T[i][0] < maxValueOrginalIndex):
            maxValue = T[i][1][1]
            maxValueIndex = i
            maxValueOrginalIndex = T[i][0]

    T[start], T[maxValueIndex] = T[maxValueIndex], T[start]

def fix_reverse(T, start, end):
    minValue = T[start][1][0]
    minValueIndex = start
    minValueOrginalIndex = T[start][0]
    for i in range(start+1, end+1):
        if T[i][1][0] < minValue or (T[i][1][0] == minValue and T[i][0] < minValueOrginalIndex):
            minValue = T[i][1][0]
            minValueIndex = i
            minValueOrginalIndex = T[i][0]

    T[end], T[minValueIndex] = T[minValueIndex], T[end]

def depth(L):
    n = len(L)
    startsSorted = [[i, L[i]] for i in range(n)]
    endsSorted = startsSorted.copy()
    quick_sort(startsSorted, 0, n-1, 0)
    quick_sort(endsSorted, 0, n-1, 1)

    for i in range(n-1):
        if startsSorted[i][1][0] == startsSorted[i+1][1][0]:
            start = i
            while startsSorted[start][1][0] == startsSorted[i+1][1][0]:
                i += 1

            fix(startsSorted, start, i)

    for i in range(n-1):
        if endsSorted[i][1][1] == endsSorted[i+1][1][1]:
            start = i
            while i+1 < n and endsSorted[start][1][1] == endsSorted[i+1][1][1]:
                i += 1

            fix_reverse(endsSorted, start, i)

    indexDiference = [0 for _ in range(n)]
    for i in range(n):
        indexDiference[endsSorted[i][0]] += i
        indexDiference[startsSorted[i][0]] -= i

    return max(indexDiference)

runtests( depth )
