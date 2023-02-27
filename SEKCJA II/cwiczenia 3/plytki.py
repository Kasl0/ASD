def plytki(T):
    last_plytka = T[0]-2
    wynik = 0
    for i in range(len(T)):
        if T[i] > last_plytka:
            last_plytka = T[i]+1
            wynik+=1
    return wynik
