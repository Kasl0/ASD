def ciezarowka(T,L):
    p = L
    i = 1
    wynik = []
    wynik.append(0)
    while(p<len(T)):
        while(T[i]<p):
            i+=1
        wynik.append(i-1)
        p += T[i]
    return wynik