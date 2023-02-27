#Kacper Słoniec

#Opis algorytmu:
# Wyliczamy n - liczba napsiów w wejściowej tablicy T oraz max_word_len - długość najdłuższego słowa w tej tablicy.
# W między czasie tworzymy i uzupełniamy tablicę Val, która dla każdego wyrazu z T będzie przechowywać krotność każdej litery alfabetu.
# Tablicę Val sortujemy radix sortem (z pomocą counting sort'a) w czasie ϴ(n).
# Dzięki przeprowadzonemu sortowaniu, takie same elementy tablicy Val(czyli takie same tablice z krotnością liter) znajdują się obok siebie.
# Co równoważnie znaczy, że aby znaleźć maksymalną popularność anagramową, wystarczy znaleść długość najdłuższego ciągu takich samych elementów w Val.
# Robimy to w czasie liniowym, zliczając długości ciągów elementów o tej samej wartości.

#Złożoność czasowa: ϴ(N)
#Złożoność pamięciowa: ϴ(N)

from kol1btesty import runtests

def radix_sort(A, n, max_count):
    for kol in range(25,-1,-1):
        counting_sort(A, n, kol, max_count)

def counting_sort(A, n, kol, max_count):
    C = [0] * max_count
    B = [0] * n
    for i in range(n): C[A[i][kol]] += 1
    for i in range(1, max_count): C[i] = C[i] + C[i-1]
    for i in range(n-1, -1, -1):
        l = A[i][kol]
        B[C[l]-1] = A[i]
        C[l] -= 1
    for i in range(n):
        A[i] = B[i]

def f(T):
    n = len(T)
    max_word_len = 0
    Val = [[0 for _ in range(26)] for _ in range(n)]

    for i in range(n):
        word_len = len(T[i])
        max_word_len = max(max_word_len, word_len)

        for j in range(word_len):
            Val[i][ord(T[i][j])-97] += 1

    radix_sort(Val, n, max_word_len)
    
    max_strike = 0
    current_strike = 1
    for i in range(1, n):
        if Val[i-1] == Val[i]:
            current_strike += 1
        else:
            max_strike = max(max_strike, current_strike)
            current_strike = 1

    max_strike = max(max_strike, current_strike)
    return max_strike

#Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
