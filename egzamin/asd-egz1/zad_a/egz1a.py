# Kacper Słoniec

# Złożoność obliczeniowa: O(n log n)

# Opis algorytmu:
# Sortujemy tablicę S w kolejności malejących wartości.
# Każdego dnia wydobywamy największą możliwą wartość śniegu - Dla dnia pierwszego S[0], dla drugiego S[1] - 1, dla trzeciego S[2] - 2, ... itd.

# Uzasadnienie poprawności:
# Wiemy, że wydąbędziemy śnieg z obszarów o największej jego ilości, nie wiemy tylko w jakiej kolejności.
# Czyli w d dni wydąbędziemy równowartość sumy d największych wartości w S, odjąwszy śnieg stopiony.
# Ilość śniegu stopionego na d obszarach w d dni będzie stałą wyrażoną przed liczbę d.
# Żadnego obszaru mającego jedną z d największych wartości NIE rozjedziemy, bo śnieg będziemy wydobywać w kolejności położenia obszarów.
# Wartość wydobytego śniegu nie zależy od kolejności wydobycia, jeśli nie rozjedziemy śniegu który chcemy zebrać.
# Dlatego stosujemy kolejność, taką żeby nic nie rozjechać.
# Kolejność nie ma znaczenia dla wyniku => algorytm jest poprawny.

from egz1atesty import runtests

def snow( S ):
    S.sort(reverse = True)

    collected = 0
    day = 0

    while S[day] - day > 0:
        collected += (S[day] - day)
        day += 1

    return collected

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
